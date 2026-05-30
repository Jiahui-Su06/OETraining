import os
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error


MODEL_DIR = "output/models/PLS_VIP"
SAVE_DIR = "output/results/PLS_VIP"
os.makedirs(SAVE_DIR, exist_ok=True)

COMPONENTS = ['Moisture', 'Lipids', 'Protein', 'Starch']


# ===================== LOAD MODELS =====================
def load_all_models():
    models = {}
    scalers = {}
    selected_indices = {}

    for comp in COMPONENTS:
        try:
            models[comp] = joblib.load(f"{MODEL_DIR}/{comp}_pls_vip.joblib")
            scalers[comp] = joblib.load(f"{MODEL_DIR}/{comp}_pls_vip_scaler.joblib")
            selected_indices[comp] = joblib.load(f"{MODEL_DIR}/{comp}_pls_vip_indices.joblib")
            print(f"Loaded {comp} model successfully")
        except Exception as e:
            print(f"ERROR loading {comp}: {str(e)}")
            return None, None, None
    return models, scalers, selected_indices


# ===================== PREDICT =====================
def predict_components(spectra_data, actual_df, models, scalers, indices):
    predictions = {}
    metrics = {}

    for comp in models:
        scaler = scalers[comp]
        imp_idx = indices[comp]

        # Correct order: scale first, then select wavelengths
        X_scaled = scaler.transform(spectra_data)
        X_selected = X_scaled[:, imp_idx]

        y_pred = models[comp].predict(X_selected).ravel()
        predictions[comp] = y_pred

        if comp in actual_df.columns:
            y_true = actual_df[comp]
            r2 = r2_score(y_true, y_pred)
            mae = mean_absolute_error(y_true, y_pred)
            rmse = np.sqrt(mean_squared_error(y_true, y_pred))
            metrics[comp] = {"R2": r2, "MAE": mae, "RMSE": rmse}

    return pd.DataFrame(predictions), metrics


# ===================== PLOT =====================
def plot_predictions(pred_df, actual_df, save_path):
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    axes = axes.flatten()

    for i, comp in enumerate(COMPONENTS):
        ax = axes[i]
        y_pred = pred_df[comp]
        y_true = actual_df[comp]

        ax.scatter(y_true, y_pred, alpha=0.5)
        ax.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], 'r--', lw=2)
        ax.set_title(f"{comp} Content - PLS Test Prediction")
        ax.set_xlabel("Actual Value")
        ax.set_ylabel("Predicted Value")

        r2 = r2_score(y_true, y_pred)
        mae = mean_absolute_error(y_true, y_pred)
        rmse = np.sqrt(mean_squared_error(y_true, y_pred))
        txt = f"R² = {r2:.4f}\nMAE = {mae:.4f}\nRMSE = {rmse:.4f}"
        ax.text(0.05, 0.95, txt, transform=ax.transAxes, verticalalignment="top",
                bbox=dict(boxstyle="round", facecolor="white", alpha=0.8))

    plt.tight_layout()
    plt.savefig(save_path, dpi=500, bbox_inches="tight")
    plt.close()


# ===================== MAIN =====================
def main():
    models, scalers, indices = load_all_models()
    if not models:
        return

    try:
        test_spectra = pd.read_excel("docs/test.xlsx")
        test_actual = pd.read_excel("docs/test_actual.xlsx")
        spectra_data = test_spectra.iloc[:, 1:].values
        print(f"Loaded test data: {spectra_data.shape[0]} samples")

        pred_df, metrics = predict_components(spectra_data, test_actual, models, scalers, indices)

        print("\n===== Test Set Metrics =====")
        for comp, m in metrics.items():
            print(f"{comp}: R2={m['R2']:.4f}, MAE={m['MAE']:.4f}, RMSE={m['RMSE']:.4f}")

        pred_df.to_excel(f"{SAVE_DIR}/test_set_predictions.xlsx", index=False)
        plot_predictions(pred_df, test_actual, f"{SAVE_DIR}/test_set_pls_prediction.png")

        print(f"\nAll results saved to: {SAVE_DIR}")
    
    except Exception as e:
        print(f"ERROR: {str(e)}")


if __name__ == "__main__":
    main()
