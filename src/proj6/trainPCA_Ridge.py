import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import joblib

from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.preprocessing import StandardScaler


np.random.seed(42)

# DATA PATHS
file_name = "m5spec"  # m5spec/mp5spec/mp6spec for select
SPECTRA_PATH = f'output/preprocessed_spectra/{file_name}tra/SG/processed_spectra.xlsx'
PROP_PATH = 'docs/propvals.xlsx'

# SAVE PATHS
MODEL_DIR = "output/models/PCA_Ridge"
RESULT_DIR = "output/results/PCA_Ridge"

os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs(RESULT_DIR, exist_ok=True)

# COMPONENTS
COMPONENTS = ['Moisture', 'Lipids', 'Protein', 'Starch']

# ===================== MAIN =====================
def main():
    df_spectra = pd.read_excel(SPECTRA_PATH, sheet_name='Sheet1')
    df_propvals = pd.read_excel(PROP_PATH, sheet_name='Sheet1')
    wavelengths = np.array(df_spectra.columns[1:], dtype=float)
    results = []

    for component in COMPONENTS:
        print(f"Processing Component: {component}")
        y = df_propvals[component]

        # Correlation Analysis
        print("\nAnalyzing wavelength correlations...")
        correlations = []
        for i in range(1, df_spectra.shape[1]):
            wl = wavelengths[i-1]
            corr = np.corrcoef(df_spectra.iloc[:, i], y)[0, 1]
            correlations.append((wl, corr))

        correlations = np.array(correlations)
        wl_corr = correlations[:, 0]
        corr_vals = correlations[:, 1]

        # Top 10 wavelengths
        top10_idx = np.argsort(np.abs(corr_vals))[-10:]
        top10_wl = wl_corr[top10_idx]
        top10_corr = corr_vals[top10_idx]

        print("Top 10 correlated wavelengths:")
        for j, (w, c) in enumerate(zip(top10_wl, top10_corr), 1):
            print(f"  {j}. {w:.1f} nm | r = {c:.4f}")

        # Save correlation plot
        plt.figure(figsize=(15, 6))
        plt.plot(wl_corr, corr_vals)
        plt.axhline(0, color='red', linestyle='--', alpha=0.4)
        plt.title(f'Correlation between {component} and Wavelengths')
        plt.xlabel('Wavelength (nm)')
        plt.ylabel('Correlation Coefficient')
        plt.grid(True)
        plt.savefig(f"{RESULT_DIR}/{component}_correlation.png", dpi=500, bbox_inches='tight')
        plt.close()

        # Auto-select significant wavelengths (|r| >= 0.3)
        significant_mask = np.abs(corr_vals) >= 0.3
        selected_indices = np.where(significant_mask)[0]

        if len(selected_indices) == 0:
            print(f"No significant wavelengths for {component}, skip modeling.")
            continue

        print(f"\nSelected {len(selected_indices)} significant wavelengths")

        # Prepare data
        X = df_spectra.iloc[:, 1:].iloc[:, selected_indices].values

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=0.2, random_state=42
        )

        # Train Ridge Model
        print("Training Ridge model...")
        model = Ridge(alpha=1.0)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        # Metrics
        R = np.corrcoef(y_test, y_pred)[0, 1]
        R2 = r2_score(y_test, y_pred)
        MAE = mean_absolute_error(y_test, y_pred)
        RMSE = np.sqrt(mean_squared_error(y_test, y_pred))

        print("Metrics:")
        print(f"R: {R:.4f}")
        print(f"R²: {R2:.4f}")
        print(f"MAE: {MAE:.4f}")
        print(f"RMSE: {RMSE:.4f}")

        results.append([component, R, R2, MAE, RMSE])

        # Cross validation
        cv = KFold(n_splits=5, shuffle=True, random_state=42)
        cv_scores = cross_val_score(model, X_scaled, y, cv=cv, scoring='r2')
        print(f"  CV R²: {cv_scores.mean():.4f} ± {cv_scores.std():.4f}")

        # Prediction plot
        plt.figure(figsize=(8, 6))
        plt.scatter(y_test, y_pred, alpha=0.5)
        plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
        plt.xlabel('Actual Value')
        plt.ylabel('Predicted Value')
        plt.title(f'{component} Content - Ridge Prediction')
        plt.savefig(f"{RESULT_DIR}/{component}_ridge_scatter.png", dpi=500, bbox_inches='tight')
        plt.close()

        # SAVE MODEL
        joblib.dump(model, f"{MODEL_DIR}/{component}_ridge.joblib")
        joblib.dump(scaler, f"{MODEL_DIR}/{component}_scaler.joblib")
        joblib.dump(selected_indices, f"{MODEL_DIR}/{component}_wavelength_indices.joblib")

        print("Model saved successfully!")

    # Save all metrics
    df_results = pd.DataFrame(results, columns=['Component', 'R', 'R²', 'MAE', 'RMSE'])
    df_results.to_excel(f"{RESULT_DIR}/ridge_metrics.xlsx", index=False)

    print("\n==================================================")
    print("ALL TASKS COMPLETED!")
    print(f"Correlation figures: {RESULT_DIR}")
    print(f"Models saved: {MODEL_DIR}")
    print(f"Results saved: {RESULT_DIR}")

if __name__ == "__main__":
    main()
