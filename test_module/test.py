import captcha_image_process.image_process as i_process
from PIL import Image
import numpy
import os
import test_module.test_array as a
import random

if __name__ == '__main__':
    i_process.image_to_gray_scale_file_path('../test_image/captcha_single_image(32x32)/',
                                            save_file_path='../captcha_binarization_images/')
