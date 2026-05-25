import os
import pandas as pd
import matplotlib.pyplot as plt


file_name = "mp6spec"  # m5spec/mp5spec/mp6spec for select
df = pd.read_excel(
    f"docs/{file_name}.xlsx",
    sheet_name='Sheet1',
    index_col=0
)
output_folder = f"output/raw_spectra/{file_name}tra"
os.makedirs(  # make output folder
    output_folder,
    exist_ok=True
)

WL = df.columns.astype(float)  # wavelength (nm)

# plot sample spectrum
plt.figure()
for sample_number, row in df.iterrows():
    plt.plot(WL, row.values, linewidth=2.0)
    plt.title(f'Sample#{sample_number} Spectrum', fontsize=16)
    plt.xlabel('Wavelength (nm)', fontsize=14)
    plt.ylabel('Absorbance', fontsize=14)
    plt.grid(True)
    plt.xlim(1100, 2500)
    plt.ylim(0, 1)
    plt.savefig(
        output_folder+f"/sample#{sample_number}.png",
        bbox_inches="tight",
        dpi=500
    )
    plt.close()

# plot all sample spectra
plt.figure()
for sample_number, row in df.iterrows():
    plt.plot(WL, row.values, alpha=0.5, linewidth=0.8)
plt.title('All Samples Spectra', fontsize=16)
plt.xlabel('Wavelength (nm)', fontsize=14)
plt.ylabel('Absorbance', fontsize=14)
plt.grid(True)
plt.xlim(1100, 2500)
plt.ylim(0, 1)
plt.savefig(
    output_folder+"/all_samples.png",
    bbox_inches='tight',
    dpi=500
)
plt.close()

print("All spectra have been plotted successfully!")
