import os
import pandas as pd
import matplotlib.pyplot as plt

from core import ES, SNV, SG


file_name = "mp6spec"  # m5spec/mp5spec/mp6spec for select
method = "SG"  # ES/SNV/SG for select

df = pd.read_excel(
    f"docs/{file_name}.xlsx",
    sheet_name='Sheet1',
    index_col=0
)
output_folder = f"output/preprocessed_spectra/{file_name}tra/{method}"
os.makedirs(output_folder, exist_ok=True)
WL = df.columns.astype(float)  # wavelength (nm)


# Parameters
## ES
alpha = 0.24
## SG
window_length = 65  # must be even
polyorder = 3  # usually be 2 or 3
deriv_order = 1

processed_df = pd.DataFrame(index=df.index, columns=df.columns)
for sample_number, row in df.iterrows():
    plt.figure()
    if method == "ES":
        smoothed_row = ES(row, alpha=alpha)
        processed_spectrum = smoothed_row.values
        processed_df.loc[sample_number] = processed_spectrum
    elif method == "SNV":
        processed_spectrum = SNV(row.values)
        processed_df.loc[sample_number] = processed_spectrum
    elif method == "SG":
        processed_spectrum = SG(
            row.values, 
            window_length=window_length,
            polyorder=polyorder,
            deriv=deriv_order
        )
        processed_df.loc[sample_number] = processed_spectrum
    plt.plot(WL, row.values, label='original', color='blue', alpha=0.6)
    plt.plot(WL, processed_spectrum, label='processed', color='red', linewidth=2)
    plt.xlim(1100, 2500)
    plt.title(f"Sample#{sample_number} Spectrum", fontsize=16)
    plt.xlabel("Wavelength (nm)", fontsize=14)
    plt.ylabel("Absorbance", fontsize=14)
    plt.grid(True)
    plt.legend()
    plt.savefig(
        output_folder+f"/sample#{sample_number}.png",
        bbox_inches='tight',
        dpi=500
    )
    plt.close()

plt.figure()
for sample_number, row in processed_df.iterrows():
    plt.plot(WL, row.values, alpha=0.7, linewidth=1)
plt.xlim(1100, 2500)
plt.title("All Smoothed Samples Spectra", fontsize=16)
plt.xlabel('Wavelength (nm)', fontsize=14)
plt.ylabel('Absorbance', fontsize=14)
plt.grid(True)
plt.savefig(
    output_folder+"/all_samples_spectra.png",
    bbox_inches='tight',
    dpi=500
)
plt.close()
