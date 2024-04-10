import os
import logging
from argparse import ArgumentParser
import shutil
import cv2
import os
from copy import deepcopy

# This Python script is based on the shell converter script provided in the MipNerF 360 repository.
parser = ArgumentParser("Colmap converter")
parser.add_argument("--no_gpu", action='store_true')

parser.add_argument("--images_path", "-s", required=True, type=str)
parser.add_argument("--output_path", type=str)
parser.add_argument("--direction", default="clockwise", type=str)
args = parser.parse_args()

if not os.path.isdir(args.images_path):
    logging.error("images_path is not a directory")
if len(os.listdir(args.images_path)) == 0:
    logging.error("images_path is empty")
if args.direction == "clockwise":
    logging.info("Rotating clockwise")
    rot_dir = cv2.ROTATE_90_CLOCKWISE
elif args.direction == "counterclockwise":
    logging.info("Rotating counterclockwise")
    rot_dir = cv2.ROTATE_90_COUNTERCLOCKWISE
else:
    logging.warn("Unrecognized rotation direction. Rotating clockwise by default...")
    rot_dir = cv2.ROTATE_90_CLOCKWISE

# If output_path is not specified, overwrite the original images
if args.output_path:
    images_dir = deepcopy(args.output_path)
else:
    images_dir = deepcopy(args.images_path)

# Rotate images to correct orientation before undistortion
for filename in os.listdir(args.images_path):
    logging.info(f"Rotating {filename}")
    img = cv2.imread(os.path.join(args.images_path, filename))
    rotated_img = cv2.rotate(img, rot_dir)
    cv2.imwrite(os.path.join(images_dir, filename), rotated_img)

logging.info("Done.")
