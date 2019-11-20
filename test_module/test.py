import captcha_image_process.image_process as i_process
from PIL import Image
import numpy
import os

if __name__ == '__main__':
    path = '../test_image/captcha_single_image(32x32)/'
    for i in os.listdir(path):
        i_process.image_binarization(path + i, save_path='../captcha_binarization_images/')
    # i_process.image_binarization(image_file_path='../test_image/test_image_box/4.png',save_path='../captcha_binarization_images/')
