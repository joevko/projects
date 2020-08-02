#!/usr/bin/env python
import argparse
from blur.blur_1 import regular_blur
from blur.blur_2 import numpy_blur
from blur.blur_3 import numba_blur
#import cv2
'''Take a <your_image>.jpg and a <your_requested_outputfile>.jpg as input'''
'''Takes also a selected method by typing -p, -np or -n as a third argument'''
#I didnt quit get the argument choices, regular_blur, numpy_blur, numba_blur to work
#so I implementet this jusing a add_mutually_exclusive_group from the argparse library
#Writing from terminal it is crucial to NOT use " " around input arguments.
parser = argparse.ArgumentParser(description = "User interface for image blur")
parser.add_argument("input_img", help = "Input image")
parser.add_argument("output_img", help = "Output image")
#mutually exclusice group, lets user have access
#to only one method at a time
group = parser.add_mutually_exclusive_group()
group.add_argument("-p", "--python", help="Blurring image using python",\
                    action="store_true")
group.add_argument("-np", "--numpy", help="Blurring image using numpy",\
                    action="store_true")
group.add_argument("-n", "--numba", help="Blurring image using numba",\
                    action="store_true")
args = parser.parse_args()


if args.python:
    regular_blur(args.input_img, args.output_img)
elif args.numpy:
    numpy_blur(args.input_img, args.output_img)
elif args.numba:
    numba_blur(args.input_img, args.output_img)
else:
    print("Did not choose a method to use")
