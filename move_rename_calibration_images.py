#!/usr/bin/env python2.7

"""
@author: Mitchell Scott
@contact: miscott@uw.edu
"""

import argparse
import glob
import cv2

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Move and rename images \
                        for calibration")
    parser.add_argument("images", help="Base Path to calibration images")
    parser.add_argument("save_path", help="Path to save calibration images")
    parser.add_argument("--encoding", help="Encoding of the images",
                        default="jpg")
    parser.add_argument("--save_encoding", help="Encoding of the images",
                        default="jpg")
    args = parser.parse_args()

    img_path = args.images
    save_path = args.save_path
    if (img_path[-1] != "/"):
        img_path += "/"
    if (save_path[-1] != "/"):
        save_path += "/"
    images = glob.glob(img_path + "*." + args.encoding)
    for i, fname in enumerate(images):
        img = cv2.imread(fname)
        new_fname = save_path + "img" + str(i) + "." + args.save_encoding
        cv2.imwrite(new_fname, img)
