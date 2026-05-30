import os
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy.signal import savgol_filter


# Exponential Smoothing
def ES(series, alpha=0.3):
    return series.ewm(alpha=alpha, adjust=False).mean()
# def ES(series, alpha=0.3): # alpha smaller is better
#     data = series.values
#     smoothed = [data[0]]
#     for i in range(1, len(data)):
#         smoothed_val = alpha*data[i] + (1-alpha)*smoothed[i-1]
#         smoothed.append(smoothed_val)
#     return pd.Series(smoothed, index=series.index)


# Standard Normal Variate
def SNV(spectrum):
    mean = np.mean(spectrum)
    std = np.std(spectrum)
    return (spectrum-mean)/std if std != 0 else spectrum-mean


# Savitzky-Golay Filter
SG = savgol_filter


def calcSNR(signal, noise):
    signal_power = np.mean(signal**2)
    noise_power = np.mean(noise**2)
    return 10*np.log10(signal_power/noise_power) if noise_power != 0 else float('inf')


def calcSM(signal):
    # calculate smoothness
    return np.sum(np.diff(signal)**2)


def calcFP(original, processed):
    # Calculate feature preservation
    return np.corrcoef(original, processed)[0, 1]


def evaluatePreprocess(df):
    results = {
        'ES':  {'SNR': [], 'SM': [], 'FP': [], 'Time': []},
        'SNV': {'SNR': [], 'SM': [], 'FP': [], 'Time': []},
        'SG':  {'SNR': [], 'SM': [], 'FP': [], 'Time': []}
    }
    
    for sample_number, row in df.iterrows():
        original_data = row.values
        
        # ES
        start_time = time.time()
        ES_data = ES(row, alpha=0.24)
        results['ES']['Time'].append(time.time()-start_time)
        results['ES']['SNR'].append(calcSNR(ES_data, original_data-ES_data))
        results['ES']['SM'].append(calcSM(ES_data))
        results['ES']['FP'].append(calcFP(original_data, ES_data))
        
        # SNV
        start_time = time.time()
        SNV_data = SNV(original_data)
        results['SNV']['Time'].append(time.time()-start_time)
        results['SNV']['SNR'].append(calcSNR(SNV_data, original_data-SNV_data))
        results['SNV']['SM'].append(calcSM(SNV_data))
        results['SNV']['FP'].append(calcFP(original_data, SNV_data))
        
        # SG
        start_time = time.time()
        SG_data = SG(original_data, window_length=65, polyorder=3, deriv=1)
        results['SG']['Time'].append(time.time()-start_time)
        results['SG']['SNR'].append(calcSNR(SG_data, original_data-SG_data))
        results['SG']['SM'].append(calcSM(SG_data))
        results['SG']['FP'].append(calcFP(original_data, SG_data))
    
    # calculate mean results
    summary = {}
    for method in results:
        summary[method] = {
            'Mean SNR (dB)': np.mean(results[method]['SNR']),
            'Mean Smoothness': np.mean(results[method]['SM']),
            'Mean Feature Preservation': np.mean(results[method]['FP']),
            'Mean Processing Time (s)': np.mean(results[method]['Time'])
        }
    
    metrics = ['Mean SNR (dB)',
               'Mean Smoothness',
               'Mean Feature Preservation',
               'Mean Processing Time (s)']
    methods = list(summary.keys())
    
    plt.figure()
    for i, metric in enumerate(metrics, 1):
        plt.subplot(2, 2, i)
        values = [summary[method][metric] for method in methods]
        plt.bar(methods, values)
        plt.title(metric)
    plt.tight_layout()
    
    output_folder = "output/preprocessed_spectra/preprocess_evaluation"
    os.makedirs(output_folder, exist_ok=True)
    plt.savefig(
        output_folder+'/preprocess_evaluation.png',
        dpi=500
    )
    plt.close()
    
    summary_df = pd.DataFrame(summary).T
    summary_df.to_csv(output_folder+'/preprocess_evaluation_metrics.csv')
    
    print("\nPreproc. Methods Performance:")
    for method in summary:
        print(f"\n{method}:")
        for metric, value in summary[method].items():
            print(f"{metric}: {value:.6f}")
    
    return summary
