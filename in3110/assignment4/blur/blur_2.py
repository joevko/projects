#!/usr/bin/env python
import numpy as np
import cv2
import time
from check_fileformat import format_test, failed_format_test_print

def numpy_blur(input_img, output_img):
    ''' Needs to arguments- similiar as before i.e. one input image
    and one output image '''
    if format_test(input_img) and not isinstance(imput_img, np.ndarray):
        failed_format_test_print(input_img)
        return
    else:
        #measuring runtime
        start = time.time()

        #reading in image
        image = cv2.imread(input_img)
        src = np.pad(image, [[1, 1],[1, 1],[0, 0]], mode='edge')
        src = src.astype("uint32")
        #The method you have made works great, and it does so with the speed
        # we want, great job! Still you can do it slightly more readable.
        #When you have initialized src.astype("uint32") you can initialize dst without
        # copying src, also you can calculate the average, normal blurring, in one sentence
        #like this
        dst =   (src[:-2,:-2,:] + src[:-2,1:-1,:] + src[:-2, 2:,:] +
                src[1:-1,:-2,:] + src[1: -1,1:-1,:] + src[1:-1,2:,:] +
                src[2:,:-2,:] + src[2:,1:-1,:] + src[2:,2:, :])/9

        dst = dst.astype("uint8")

        cv2.imwrite(output_img, dst)

        #ending the time count and calculating elapsed_time
        end = time.time()
        elapsed_time = end - start
        print ("numpy time: ", elapsed_time)
