#!/usr/bin/env python
import numpy as np
import cv2
import random
from blur.blur_3 import numba_blur

def test_one():
    #random seed makes it so that random array is equal every time
    seed = random.seed(32)
    random_image = np.random.randint(0, 256, size=(100, 100, 3))
    #get highest value from array
    result = np.amax(random_image)
    #blur to make an item in array the average of its neighbours
    blurred_array = numba_blur(random_image)
    #highest value should now be lower than before
    excp = np.amax(blurred_array)
    assert excp < result


if __name__ == '__main__':
    test_one()
