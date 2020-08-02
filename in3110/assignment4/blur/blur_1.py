#!/usr/bin/env python
#importing stuff
import numpy as np
import cv2
import time
#imported separated method for checking input-format
from check_fileformat import format_test, failed_format_test_print

def blur_matrix(image):
    '''Takes an image as input; then returns blurred image without padding'''

    src = np.pad(image, [[1, 1],[1, 1],[0, 0]], mode='edge')
    src = src.astype("uint32")
    dst = np.zeros(image.shape)

    for h in range(1, dst.shape[0]-1):
        for w in range(1, dst.shape[1]-1):
            for c in range(0, dst.shape[2]):
                    dst [h,w,c] = (src [h,w,c] + src[h -1,w,c] + src[h+1,w,c]
                                    + src[h,w -1,c] + src[h,w+1,c]
                                    + src[h -1,w -1,c] + src[h -1,w+1,c]
                                    + src[h+1,w -1,c] + src[h+1,w+1,c]) /9
    dst = dst.astype("uint8")
    return dst

#The method regular blue(input,inpyt) can take a jpg image, run blur_matrix, make an outfil and time it.
#The method seems to be working great and splitting different tasks to different methods makes the
# code more readable, awesome job!

'''Take an image as input and a <string>.jpg as output. '''
def regular_blur(input_img, output_img):
    #checks inputformat
    if format_test(input_img) and not isinstance(imput_img, np.ndarray):
        failed_format_test_print(input_img)
        return
    else:
        #startint calculating the time
        start = time.time()

        #reading in image
        image = cv2.imread(input_img)
        blurred_image = blur_matrix(image)

        cv2.imwrite(output_img, blurred_image)

        #ending the time count and calculating elapsed_time
        end = time.time()
        elapsed_time = end - start
        print ("python time: ", elapsed_time)
