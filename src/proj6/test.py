import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib.patches import Patch


file_name = "m5spec"  # m5spec/mp5spec/mp6spec for select
df_spectra = pd.read_excel(
    f'output/preprocessed_spectra/{file_name}tra/SG/processed_spectra.xlsx',
    sheet_name='Sheet1'
)
df_propvals = pd.read_excel(
    'docs/propvals.xlsx',
    sheet_name='Sheet1'
)
os.makedirs('output/correlation_analysis', exist_ok=True)
WL = np.array(df_spectra.columns[1:], dtype=float)
components = [
    'Moisture',
    'Lipids',
    'Protein',
    'Starch'
]
colors = [
    '#FF0000', 
    '#00FF00', 
    '#0000FF', 
    '#FFFF00'
]


for idx, (component, color) in enumerate(zip(components, colors)):
    y = df_propvals[component].values
    corrs = []
    for i in range(1, df_spectra.shape[1]):
        x = df_spectra.iloc[:, i].values
        x_mean = np.mean(x)
        y_mean = np.mean(y)
        numerator = np.sum((x-x_mean)*(y-y_mean))
        denominator = np.sqrt(np.sum((x-x_mean)**2))*np.sqrt(np.sum((y-y_mean)**2))
        r = numerator / denominator if denominator != 0 else 0
        corrs.append(r)
    corrs = np.array(corrs)

    plt.figure()
    plt.plot(WL, corrs, color='b', label='Correlation Coefficient')
    plt.axhline(y=0, color='r', linestyle='--', alpha=0.3)
    plt.xlabel('Wavelength (nm)', fontsize=14)
    plt.ylabel('Correlation Coefficient', fontsize=14)
    plt.title(
        f'{component} Content vs. Wavelength',
        fontsize=16
    )
    plt.grid(True, alpha=0.3)

    top3_indices = np.argsort(np.abs(corrs))[-3:]
    legend_patches = []
    used_ranges = []
    for j, i in enumerate(top3_indices):
        # Check for overlaps and slightly offset if overlapped
        left = max(0, i-2)
        right = min(len(WL)-1, i+2)
        # Check for overlap with already used intervals
        y_offset = 0
        for used_left, used_right, used_offset in used_ranges:
            if not (WL[right] < used_left or WL[left] > used_right):
                y_offset += 0.05  # y offset 0.05
        plt.axvspan(
            WL[left], WL[right],
            color=color, alpha=0.3
        )
        used_ranges.append((WL[left], WL[right], y_offset))
        legend_patches.append(Patch(
            facecolor=color, edgecolor='k', alpha=0.3,
            label=f'{component} Band{j+1}: {WL[i]:.1f}nm, Correlation Coefficient: {corrs[i]:.3f}'
        ))

    plt.legend(
        handles=[plt.Line2D([0], [0], color='b', label='Correlation Coefficient')]+legend_patches,
        fontsize=12, loc='best'
    )
    plt.tight_layout()
    plt.savefig(f'output/correlation_analysis/{component}_correlation_top3band_legend.png', dpi=500)
    plt.close()
