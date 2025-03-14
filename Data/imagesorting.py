import os
import pandas as pd

def match_images_to_data(image_base_folder, data_csv_path, output_csv_path, filtered_csv_path):
    """ Matches images to electricity consumption data and filters missing images """
    df = pd.read_csv(data_csv_path)
    all_image_paths = {}
    detected_countries = {}

    print("\n Scanning image directories...\n")

    for root, _, files in os.walk(image_base_folder):
        parts = root.split(os.sep)
        country_folder = next((part for part in parts if part.lower() in df["Country"].str.lower().unique()), None)
        if not country_folder:
            continue

        lower_country_name = country_folder.lower()
        detected_countries[lower_country_name] = country_folder

        for file in files:
            if file.startswith("NOAA_VIIRS") and file.endswith(".jpg"):
                if lower_country_name not in all_image_paths:
                    all_image_paths[lower_country_name] = {}
                all_image_paths[lower_country_name][file] = os.path.join(root, file)

    print("\n Image scanning complete!\n")

    image_paths = []
    image_exists = []

    for _, row in df.iterrows():
        original_country = row["Country"].strip()
        lower_country = original_country.lower()
        image_name = f"NOAA_VIIRS_Y{row['Year']}_M{row['Month_Num']}.jpg"

        if lower_country in all_image_paths and image_name in all_image_paths[lower_country]:
            full_path = all_image_paths[lower_country][image_name]
        else:
            full_path = None

        image_paths.append(full_path if full_path else f"NOT FOUND: {image_name}")
        image_exists.append(bool(full_path))

    df["Image_Filename"] = image_paths
    df["Image_Exists"] = image_exists
    df.to_csv(output_csv_path, index=False)

    df_filtered = df[df["Image_Exists"] == True]
    df_filtered.to_csv(filtered_csv_path, index=False)

    print(f"\n Final CSV saved at: {filtered_csv_path}")
    return df_filtered
