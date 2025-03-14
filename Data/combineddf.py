import pandas as pd
import os
import glob

def combine_csv_files(data_folder, output_csv):
    """ Combines all CSV files in a folder into one structured DataFrame """
    csv_files = glob.glob(os.path.join(data_folder, "*.csv"))
    print(f"File found {len(csv_files)} CSV files to process.")

    dfs = []
    for file in csv_files:
        print(f"Processing: {file}")
        df = pd.read_csv(file, header=None, names=["Country", "Month", "Electricity_Consumption", "Unit"])
        df = df.drop(columns=["Unit"])

        df[['Month_Num', 'Year']] = df['Month'].str.extract(r'(\d{1,2})/(\d{2})')
        df['Year'] = df['Year'].astype(float).apply(lambda x: int(x) + 2000 if pd.notna(x) else None)
        df = df.dropna(subset=['Year', 'Month_Num'])
        df['Month'] = 'M' + df['Month_Num'].astype(int).astype(str)
        df['Year'] = df['Year'].astype(int)
        df['Formatted_Date'] = df['Month'] + " " + df['Year'].astype(str)
        df['Electricity_Consumption'] = pd.to_numeric(df['Electricity_Consumption'], errors="coerce")

        dfs.append(df)

    combined_df = pd.concat(dfs, ignore_index=True)
    combined_df.to_csv(output_csv, index=False)

    print(f"\nCombined CSV saved at: {output_csv}")
    return combined_df
