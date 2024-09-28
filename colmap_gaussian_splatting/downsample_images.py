import os
from PIL import Image
import logging
import argparse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("downsample_images")

def downsample_images(input_dir, output_dir, downsample_factor=2):
    """
    Downsamples all JPEG images in the input directory by the specified factor and saves them to the output directory.

    Args:
        input_dir (str): Path to the directory containing the input JPEG images.
        output_dir (str): Path to the directory where the downsampled images will be saved.
        downsample_factor (int, optional): Factor by which to downsample the images. Defaults to 2.
    """
    if not os.path.isdir(input_dir):
        raise ValueError(f"Input_dir ({input_dir}) is not a directory.")
    
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Loop through all files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".jpg") or filename.endswith(".jpeg"):
            # Construct the input and output file paths
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            # Open the image and downsample it
            with Image.open(input_path) as img:
                new_size = (int(img.width / downsample_factor), int(img.height / downsample_factor))
                downsampled_img = img.resize(new_size, resample=Image.BILINEAR)

                # Save the downsampled image to the output directory
                downsampled_img.save(output_path)

            print(f"Downsampled {filename} and saved to {output_path}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("write_mpeg_dash")

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_dir", required=True, type=str)
    parser.add_argument("-o", "--output_dir", required=True, type=str)
    parser.add_argument("-d", "--downsample_factor", required=False, default=4, type=int)

    args = parser.parse_args()
    logger.info("Downsampling images..")
    downsample_images(args.input_dir, args.output_dir, args.downsample_factor)
    logger.info("Complete")