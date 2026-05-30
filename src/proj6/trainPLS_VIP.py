import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.cross_decomposition import PLSRegression
import joblib
import os


np.random.seed(42)

# UNIFIED PATHS
MODEL_DIR = "output/models/PLS_VIP"
RESULT_DIR = "output/results/PLS_VIP"
os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs(RESULT_DIR, exist_ok=True)

# DATA PATHS
file_name = "m5spec"  # m5spec/mp5spec/mp6spec for select
SPECTRA_PATH = f'output/preprocessed_spectra/{file_name}tra/SG/processed_spectra.xlsx'
PROP_PATH = 'docs/propvals.xlsx'

# TARGET COMPONENTS
COMPONENTS = ['Moisture', 'Lipids', 'Protein', 'Starch']


# ===================== VIP CALCULATION FUNCTION =====================
def calculate_vip(model, X):
    t = model.x_scores_
    w = model.x_weights_
    q = model.y_loadings_
    p, h = w.shape
    vips = np.zeros((p,))
    s = np.diag(t.T @ t @ q.T @ q).reshape(h, -1)
    total_s = np.sum(s)
    for i in range(p):
        weight = np.array([(w[i, j] / np.linalg.norm(w[:, j]))**2 for j in range(h)])
        vips[i] = np.sqrt(p * (np.sum(s.T * weight)) / total_s)
    return vips


# ===================== OPTIMIZE PLS COMPONENTS =====================
def optimize_n_components(X, y, max_components=20):
    r2_scores = []
    for n in range(1, max_components + 1):
        pls = PLSRegression(n_components=n)
        scores = cross_val_score(pls, X, y, cv=5, scoring='r2')
        r2_scores.append(scores.mean())
    optimal_n = np.argmax(r2_scores) + 1

    plt.figure(figsize=(10, 6))
    plt.plot(range(1, max_components + 1), r2_scores, 'bo-')
    plt.axvline(x=optimal_n, color='r', linestyle='--')
    plt.xlabel('Number of Components')
    plt.ylabel('R² Score')
    plt.title('PLS Components Optimization')
    plt.grid(True)
    return optimal_n


# ===================== MAIN TRAINING PROCESS =====================
def main():
    df_spectra = pd.read_excel(SPECTRA_PATH, sheet_name='Sheet1')
    df_propvals = pd.read_excel(PROP_PATH, sheet_name='Sheet1')
    wavelengths = np.array(df_spectra.columns[1:], dtype=float)
    results = []

    for comp in COMPONENTS:
        print(f"Processing Component: {comp}")

        # Full spectrum data
        X = df_spectra.iloc[:, 1:].values
        y = df_propvals[comp].values

        # Standardization
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        # Find optimal components
        optimal_n = optimize_n_components(X_scaled, y)
        plt.savefig(f"{RESULT_DIR}/{comp}_pls_components.png", dpi=500, bbox_inches='tight')
        plt.close()
        print(f"Optimal number of components: {optimal_n}")

        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=0.2, random_state=42
        )

        # Train full PLS for VIP calculation
        pls_full = PLSRegression(n_components=optimal_n)
        pls_full.fit(X_train, y_train)

        # Calculate VIP and select important wavelengths (VIP >= 1)
        vip_scores = calculate_vip(pls_full, X_train)
        important_idx = np.where(vip_scores >= 1.0)[0]
        print(f"Important wavelengths (VIP≥1): {len(important_idx)}")

        # Retrain model using only important wavelengths
        X_train_imp = X_train[:, important_idx]
        X_test_imp = X_test[:, important_idx]
        final_n = min(optimal_n, X_train_imp.shape[1])
        pls_final = PLSRegression(n_components=final_n)
        pls_final.fit(X_train_imp, y_train)
        y_pred = pls_final.predict(X_test_imp).ravel()

        # Evaluation metrics
        R = np.corrcoef(y_test, y_pred)[0, 1]
        R2 = r2_score(y_test, y_pred)
        MAE = mean_absolute_error(y_test, y_pred)
        RMSE = np.sqrt(mean_squared_error(y_test, y_pred))

        print(f"R: {R:.4f}")
        print(f"R²: {R2:.4f}")
        print(f"MAE: {MAE:.4f}")
        print(f"RMSE: {RMSE:.4f}")

        results.append([comp, R, R2, MAE, RMSE])

        # 5-fold cross validation
        cv = KFold(n_splits=5, shuffle=True, random_state=42)
        cv_scores = cross_val_score(pls_final, X_scaled[:, important_idx], y, cv=cv, scoring='r2')
        print(f"Cross Validation R²: {cv_scores.mean():.4f} ± {cv_scores.std():.4f}")

        # Prediction scatter plot
        plt.figure(figsize=(8, 6))
        plt.scatter(y_test, y_pred, alpha=0.5)
        plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
        plt.xlabel('Actual Value')
        plt.ylabel('Predicted Value')
        plt.title(f'{comp} Content - PLS (VIP≥1) Prediction')
        plt.savefig(f"{RESULT_DIR}/{comp}_pls_vip_scatter.png", dpi=500, bbox_inches='tight')
        plt.close()

        # VIP score plot
        plt.figure(figsize=(10, 6))
        plt.plot(wavelengths, vip_scores, 'b-')
        plt.axhline(y=1.0, color='r', linestyle='--')
        plt.xlabel('Wavelength (nm)')
        plt.ylabel('VIP Score')
        plt.title(f'{comp} - PLS VIP Scores')
        plt.grid(True)
        plt.savefig(f"{RESULT_DIR}/{comp}_pls_vip.png", dpi=500, bbox_inches='tight')
        plt.close()

        # SAVE MODEL, SCALER, INDICES
        joblib.dump(pls_final, f"{MODEL_DIR}/{comp}_pls_vip.joblib")
        joblib.dump(scaler, f"{MODEL_DIR}/{comp}_pls_vip_scaler.joblib")
        joblib.dump(important_idx, f"{MODEL_DIR}/{comp}_pls_vip_indices.joblib")
        print("Model saved successfully!")

    # Save all metrics to Excel
    df_results = pd.DataFrame(
        results,
        columns=['Component', 'R', 'R²', 'MAE', 'RMSE']
    )
    df_results.to_excel(f"{RESULT_DIR}/pls_vip_metrics.xlsx", index=False)

    print("ALL TASKS COMPLETED!")
    print(f"Models saved to: {MODEL_DIR}")
    print(f"Results saved to: {RESULT_DIR}")

if __name__ == "__main__":
    main()
