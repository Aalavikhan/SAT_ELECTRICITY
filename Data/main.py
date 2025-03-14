from conversion import convert_tif_to_jpeg
from combineddf import combine_csv_files
from imagesorting import match_images_to_data

# Define paths
input_root = "D:\\testtifimg" # Path to the folder containing TIF images
output_root = "D:\\All_new_jpeg" # Path to the folder where converted JPEG images will be saved
data_folder = "D:\\__ALL-CSV__" # Path to the folder containing CSV files
combined_csv_path = "../../combined_electricity_data2.csv" # Path to save the combined CSV file
image_base_folder = output_root # Path to the folder containing JPEG images
final_output_csv = "../../filtered_electricity_data2.csv" # Path to save the final CSV file 
filtered_output_csv = "../../filteredFinal_electricity_data2.csv" # Path to save the filtered CSV file

def main():
    """ Main function to execute all processing steps """
    print("\n Starting Full Processing Pipeline...\n")

    # Step 1: Convert images
    # convert_tif_to_jpeg(input_root, output_root)

    # Step 2: Combine electricity CSV files
    print("\n Combining Electricity Data CSV Files...\n")
    combined_df = combine_csv_files(data_folder, combined_csv_path)
    print("\n Electricity Data CSV Files Combined!\n")

    # Step 3: Match images with electricity data
    print("\n Matching Images to Electricity Data...\n")
    final_df = match_images_to_data(image_base_folder, combined_csv_path, final_output_csv, filtered_output_csv)

    print("\n All processes completed successfully!\n")

if __name__ == "__main__":
    main()
