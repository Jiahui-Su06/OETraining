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

plt.figure(figsize=(14, 8))
thresh_line = plt.axhline(y=0.55, color='r', linestyle='--', alpha=0.5, label='Threshold')
plt.axhline(y=-0.55, color='r', linestyle='--', alpha=0.5)
legend_handles = []
legend_handles.append(thresh_line)

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

    line, = plt.plot(WL, corrs, color=color, label=f'{component}')
    legend_handles.append(line)

    mask = np.abs(corrs) >= 0.55
    diff = np.diff(mask.astype(int))
    starts = np.where(diff == 1)[0] + 1
    if mask[0]: 
        starts = np.insert(starts, 0, 0)
    ends = np.where(diff == -1)[0]
    if mask[-1]: 
        ends = np.append(ends, len(mask)-1)

    regions = [{'start': s, 'end': e, 'max': np.max(np.abs(corrs[s:e+1]))} for s, e in zip(starts, ends)]
    regions.sort(key=lambda x: x['max'], reverse=True)
    
    for i, r in enumerate(regions[:3]):
        plt.axvspan(WL[r['start']], WL[r['end']], facecolor=color, alpha=0.25)
        if i == 0:
            legend_handles.append(Patch(facecolor=color, alpha=0.25, label=f'{component} Significant Band'))

plt.xlabel('Wavelength (nm)', fontsize=20)
plt.ylabel('Correlation Coefficient', fontsize=20)
plt.title('Content vs. Wavelength Correlation Analysis', fontsize=22)
plt.legend(handles=legend_handles, loc='best', ncol=2)
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig('output/correlation_analysis/combined_correlation.png', dpi=500)
plt.close()
