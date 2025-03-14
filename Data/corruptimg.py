import pandas as pd
import numpy as np
from PIL import Image
import os

def is_black_image(image_path, threshold=10):
    """Check if an image is black by verifying its maximum pixel value."""
    try:
        img = Image.open(image_path).convert('RGB')
        img_array = np.array(img) / 255.0  # Normalize pixel values
        return np.max(img_array) <= threshold / 255.0
    except Exception as e:
        print(f"Error processing image {image_path}: {str(e)}")
        return True  # Treat unreadable images as black

def filter_black_images(df):
    """Remove rows with black images from the dataframe."""
    valid_rows = []
    
    for _, row in df.iterrows():
        image_path = row['Image_Filename']
        if os.path.exists(image_path) and not is_black_image(image_path):
            valid_rows.append(row)
    
    return pd.DataFrame(valid_rows)


df = pd.read_csv("C:\\Users\\SPEED\\Desktop\\New Microsoft Excel Worksheet.csv")
cleaned_df = filter_black_images(df)
cleaned_df.to_csv('filtered_dataframe.csv', index=False)
