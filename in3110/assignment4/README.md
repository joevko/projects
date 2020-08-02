Assignment 4 is about blurring and image.
File blur.py uses argparse to provide a command line user interface
File blur_1.py blurres an image by pure python
File blur_2.py blurres an image by numpy
File blur_3.py blurres an image by numba

Install the blur package (named blur) like this:
pip3 install . --user

Run f.e. like this :
python blur.py beatles.jpg blurred.jpg -b regular_blur
Here your input image is the beatles.jpg picture, it is then saved as 'blurred.jpg',
flag "-b" (blur) with regular_blur - which is blur_1.py

To run the user interface:
python blur.py --help

Unfortunately test_blur.py is not finished.
