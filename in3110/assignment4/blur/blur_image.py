#!/usr/bin/env python
import argparse
import blur_1
import blur_2
import blur_3
import cv2

def blur_image(input_filename, output_filename = None):
    '''This function blurres an image using blur_1, provided input_filename. It
    takes in one or two arguments- output_filename is optional. If output_filename
    argument is not provided, then the function s

    Args:
        input_filename (str): The first parameter.
        output_filename (str): The second parameter.

    Returns:
        numpy array "image"
    '''

    image = cv2.imread(input_filename)
    blurred = blur_1.blur_matrix(image)

    if output_filename is not None:
        cv2.imwrite(output_filename, blurred)

    return blurred
