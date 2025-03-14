from PIL import Image
import os

def convert_tif_to_jpeg(input_root, output_root):
    """ Converts all .tif images to .jpg while preserving folder structure """
    os.makedirs(output_root, exist_ok=True)

    for root, _, files in os.walk(input_root):
        for file in files:
            if file.lower().endswith((".tif", ".tiff")):
                input_path = os.path.join(root, file)
                relative_path = os.path.relpath(root, input_root)
                output_folder = os.path.join(output_root, relative_path)

                os.makedirs(output_folder, exist_ok=True)
                output_path = os.path.join(output_folder, os.path.splitext(file)[0] + ".jpg")

                try:
                    with Image.open(input_path) as img:
                        img = img.convert("RGB")
                        img.save(output_path, "JPEG", quality=95)
                    print(f"Converted: {input_path} → {output_path}")
                except Exception as e:
                    print(f"Failed to convert {input_path}: {e}")

    print("\n TIF to JPEG Conversion Completed!\n")
