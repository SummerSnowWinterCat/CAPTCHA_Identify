import captcha_image_process.image_process as i_process
from PIL import Image
import numpy
import os

if __name__ == '__main__':
   i_process.image_binarization_with_zero_and_one(image_path='../captcha_binarization_images/2.png.png')