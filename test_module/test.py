import captcha_image_process.image_process as i_process
from PIL import Image
import numpy
import os
import test_module.test_array as a
import random

if __name__ == '__main__':
    data,size=i_process.image_binarization_with_255_to_one(image_file_path='../captcha_binarization_images/7.png')
