import numpy as np
import pandas as pd

from scipy.signal import savgol_filter


# Exponential Smoothing
def ES(series, alpha=0.3): # alpha smaller is better
    data = series.values
    smoothed = [data[0]]
    for i in range(1, len(data)):
        smoothed_val = alpha*data[i] + (1-alpha)*smoothed[i-1]
        smoothed.append(smoothed_val)
    return pd.Series(smoothed, index=series.index)


# Standard Normal Variate
def SNV(spectrum):
    mean = np.mean(spectrum)
    std = np.std(spectrum)
    return (spectrum-mean)/std if std != 0 else spectrum-mean


# Savitzky-Golay Filter
SG = savgol_filter
