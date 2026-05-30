import os
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split, cross_val_score, KFold, GridSearchCV
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.preprocessing import StandardScaler


np.random.seed(42)

# Unified file paths
MODEL_DIR = "output/models/PCA_SVR"
RESULT_DIR = "output/results/PCA_SVR"
os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs(RESULT_DIR, exist_ok=True)

# Data file paths
file_name = "m5spec"  # m5spec/mp5spec/mp6spec for select
SPECTRA_FILE = f'output/preprocessed_spectra/{file_name}tra/SG/processed_spectra.xlsx'
PROPERTY_FILE = 'docs/propvals.xlsx'

# Target components and corresponding wavelength regions
component_wavelength_regions = {
    'Moisture': [(1766, 1846), (1320, 1464), (2016, 2074)],
    'Lipids': [(2246, 2308), (2332, 2350), (1844, 1846)],
    'Protein': [(2112, 2160), (1200, 1206), (1740, 1780)],
    'Starch': [(1198, 1202), (2110, 2166), (1464, 1480)]
}

def main():
    # Load dataset
    df_spectra = pd.read_excel(SPECTRA_FILE, sheet_name='Sheet1')
    df_properties = pd.read_excel(PROPERTY_FILE, sheet_name='Sheet1')
    wavelengths = df_spectra.columns[1:].astype(float).values

    metric_records = []

    for component, regions in component_wavelength_regions.items():
        print(f"\nProcessing Component: {component}")
        selected_indices = []

        # Select wavelengths within defined regions
        for lower, upper in regions:
            wavelength_mask = (wavelengths >= lower) & (wavelengths <= upper)
            selected_indices.extend(np.where(wavelength_mask)[0])

        if not selected_indices:
            print(f"Warning: No valid wavelengths found for {component}")
            continue

        # Prepare feature and label
        X = df_spectra.iloc[:, 1:].iloc[:, selected_indices].values
        y = df_properties[component].values

        # Data standardization
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        # Split training and test set
        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=0.2, random_state=42
        )

        # Hyperparameter tuning with Grid Search
        print(f"Training SVR model for {component}")
        param_grid = {
            'C': [0.1, 1, 10, 100],
            'gamma': ['scale', 'auto', 0.1, 0.01],
            'epsilon': [0.1, 0.2, 0.3]
        }
        grid_search = GridSearchCV(
            estimator=SVR(kernel='rbf'),
            param_grid=param_grid,
            cv=5,
            scoring='r2',
            n_jobs=-1
        )
        grid_search.fit(X_train, y_train)
        best_model = grid_search.best_estimator_
        print(f"Best Parameters: {grid_search.best_params_}")

        # Model prediction
        y_pred = best_model.predict(X_test)

        # Calculate evaluation metrics
        corr_coef = np.corrcoef(y_test, y_pred)[0, 1]
        r2 = r2_score(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))

        print(f"R: {corr_coef:.4f}")
        print(f"R²: {r2:.4f}")
        print(f"MAE: {mae:.4f}")
        print(f"RMSE: {rmse:.4f}")

        metric_records.append([component, corr_coef, r2, mae, rmse])

        # 5-fold cross validation
        kf = KFold(n_splits=5, shuffle=True, random_state=42)
        cv_r2_scores = cross_val_score(best_model, X_scaled, y, cv=kf, scoring='r2')
        print(f"Cross Validation R²: {cv_r2_scores.mean():.4f} ± {cv_r2_scores.std():.4f}")

        # Plot prediction scatter diagram
        plt.figure(figsize=(8, 6))
        plt.scatter(y_test, y_pred, alpha=0.5)
        plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
        plt.xlabel('Actual Value')
        plt.ylabel('Predicted Value')
        plt.title(f'{component} Content - SVR Model Prediction Result')
        plt.savefig(f"{RESULT_DIR}/{component}_svr_scatter.png", dpi=300, bbox_inches='tight')
        plt.close()

        # Save model, scaler and selected wavelength indices
        joblib.dump(best_model, f"{MODEL_DIR}/{component}_svr.joblib")
        joblib.dump(scaler, f"{MODEL_DIR}/{component}_scaler.joblib")
        joblib.dump(selected_indices, f"{MODEL_DIR}/{component}_wavelength_indices.joblib")

    # Export all metrics to Excel
    df_metrics = pd.DataFrame(
        metric_records,
        columns=['Component', 'Correlation Coefficient (R)', 'R²', 'MAE', 'RMSE']
    )
    df_metrics.to_excel(f"{RESULT_DIR}/svr_metrics.xlsx", index=False)
    print("\nAll models and evaluation results saved successfully.")
    print(f"Metrics file: {RESULT_DIR}/svr_metrics.xlsx")

if __name__ == "__main__":
    main()
