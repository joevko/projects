#!/usr/bin/env python
import numba
#importing stuff
import numpy as np
import cv2
import time
from check_fileformat import format_test, failed_format_test_print

@numba.jit
def blur_jit(src, image):
    ''' Added jit. Rest stays exactly the same as before. '''

    dst = np.zeros(image.shape)
    for h in range(1, dst.shape[0]-1):
        for w in range(1, dst.shape[1]-1):
            for c in range(0,  dst.shape[2]):
                    dst [h,w,c] = (src [h,w,c] + src[h -1,w,c] + src[h+1,w,c]
                                    + src[h,w -1,c] + src[h,w+1,c]
                                    + src[h -1,w -1,c] + src[h -1,w+1,c]
                                    + src[h+1,w -1,c] + src[h+1,w+1,c]) /9
    return dst

#The numba_blur works great as well, have removed the copying-function and made
# the jit-method returnable so that we can use it for other functions.
def numba_blur(input_img, output_img):
    if format_test(input_img) and not isinstance(imput_img, np.ndarray):
        failed_format_test_print(input_img)
        return
    else:
        #reading in image
        image = cv2.imread(input_img)

        src = np.pad(image,((1,1),(1,1),(0,0)),mode='edge')
        src = src.astype("uint32")
        #startint calculating the time
        start = time.time()
        dst = blur_jit(src, image)
        end = time.time()
        dst = dst.astype("uint8")
        cv2.imwrite(output_img, dst)

        #ending the time count and calculating elapsed_time
        elapsed_time = end - start
        print ("numba time: ", elapsed_time)
        return dst
