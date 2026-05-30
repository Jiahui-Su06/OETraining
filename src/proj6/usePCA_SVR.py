import os
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error


# UNIFIED PATHS (MATCH YOUR PCA_SVR TRAINING CODE)
MODEL_DIR = "output/models/PCA_SVR"
SAVE_DIR = "output/results/PCA_SVR"
os.makedirs(SAVE_DIR, exist_ok=True)

COMPONENTS = ['Moisture', 'Lipids', 'Protein', 'Starch']


# ===================== LOAD ALL MODELS =====================
def load_all_models():
    models = {}
    scalers = {}
    selected_indices = {}

    for comp in COMPONENTS:
        try:
            models[comp] = joblib.load(f"{MODEL_DIR}/{comp}_svr.joblib")
            scalers[comp] = joblib.load(f"{MODEL_DIR}/{comp}_scaler.joblib")
            selected_indices[comp] = joblib.load(f"{MODEL_DIR}/{comp}_wavelength_indices.joblib")
            print(f"Loaded {comp} model successfully")
        except Exception as e:
            print(f"ERROR loading {comp}: {str(e)}")
            return None, None, None
    return models, scalers, selected_indices


# ===================== PREDICT & EVALUATE =====================
def predict_components(spectra_data, actual_df, models, scalers, wavelength_indices):
    predictions = {}
    metrics = {}

    for comp in models:
        idx = wavelength_indices[comp]
        X_selected = spectra_data[:, idx]
        X_scaled = scalers[comp].transform(X_selected)
        
        y_pred = models[comp].predict(X_scaled)
        predictions[comp] = y_pred

        if comp in actual_df.columns:
            y_true = actual_df[comp]
            r2 = r2_score(y_true, y_pred)
            mae = mean_absolute_error(y_true, y_pred)
            rmse = np.sqrt(mean_squared_error(y_true, y_pred))
            metrics[comp] = {"R2": r2, "MAE": mae, "RMSE": rmse}

    return pd.DataFrame(predictions), metrics


# ===================== PLOT PREDICTION RESULTS =====================
def plot_predictions(pred_df, actual_df, save_path):
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    axes = axes.flatten()

    for i, comp in enumerate(COMPONENTS):
        ax = axes[i]
        y_pred = pred_df[comp]
        y_true = actual_df[comp]

        ax.scatter(y_true, y_pred, alpha=0.5)
        ax.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], 'r--', lw=2)
        ax.set_title(f"{comp} Content - SVR Test Set Prediction")
        ax.set_xlabel("Actual Value")
        ax.set_ylabel("Predicted Value")

        r2 = r2_score(y_true, y_pred)
        mae = mean_absolute_error(y_true, y_pred)
        rmse = np.sqrt(mean_squared_error(y_true, y_pred))
        stats = f"R² = {r2:.4f}\nMAE = {mae:.4f}\nRMSE = {rmse:.4f}"
        ax.text(0.05, 0.95, stats, transform=ax.transAxes, verticalalignment="top",
                bbox=dict(boxstyle="round", facecolor="white", alpha=0.8))

    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()


# ===================== MAIN FUNCTION =====================
def main():
    models, scalers, indices = load_all_models()
    if not models:
        return

    try:
        # Load test data
        test_spectra = pd.read_excel("docs/test.xlsx")
        test_actual = pd.read_excel("docs/test_actual.xlsx")
        spectra_data = test_spectra.iloc[:, 1:].values
        print(f"Loaded test data: {spectra_data.shape[0]} samples")

        # Predict
        pred_df, metrics = predict_components(spectra_data, test_actual, models, scalers, indices)

        # Print metrics
        print("\n===== Test Set Evaluation Metrics =====")
        for comp, m in metrics.items():
            print(f"\n{comp}:")
            print(f"R2: {m['R2']:.4f}")
            print(f"MAE: {m['MAE']:.4f}")
            print(f"RMSE: {m['RMSE']:.4f}")

        # Save predictions
        pred_df.to_excel(f"{SAVE_DIR}/test_set_predictions.xlsx", index=False)
        print(f"\nPredictions saved to: {SAVE_DIR}/test_set_predictions.xlsx")

        # Plot
        plot_path = f"{SAVE_DIR}/test_set_comparison_plot.png"
        plot_predictions(pred_df, test_actual, plot_path)
        print(f"Plot saved to: {plot_path}")

    except Exception as e:
        print(f"ERROR: {str(e)}")


if __name__ == "__main__":
    main()
