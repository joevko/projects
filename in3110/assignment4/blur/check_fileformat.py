#!/usr/bin/env python
def format_test(input_format):
    """ Checks input format agains accepted cv2 module formats
    Args:
        input_format: String containing input filename
    Returns:
        Boolean: True if input_format is NOT valid.
    """
    accepted_cv2_formats = [".bmp", ".dib", ".jpeg", ".jpg", ".jpe", ".jp2" ,
    ".png", ".web", ".pbm", ".pgm", ".ppm", ".pxm", ".pnm", ".pfm", ".sr",
    ".ras",  ".tiff", ".tifm", ".exr", ".hdr", ".pic"]

    if not any(accepted_format in input_format for accepted_format in accepted_cv2_formats):
         return True


def failed_format_test_print( input_format):
    accepted_cv2_formats = [".bmp", ".dib", ".jpeg", ".jpg", ".jpe", ".jp2" ,
    ".png", ".web", ".pbm", ".pgm", ".ppm", ".pxm", ".pnm", ".pfm", ".sr",
    ".ras",  ".tiff", ".tifm", ".exr", ".hdr", ".pic"]

    invalid_format_provided = input_format.split(".")

    print(f"format .{invalid_format_provided[-1]} is not supported by cv2 module.\
    \nPlease provide one of following formats:\n{accepted_cv2_formats}")
