import captcha_image_process.image_process as i_process
from PIL import Image
import numpy

if __name__ == '__main__':
    i_process.image_binarization(image_file_path='../test_image/test_image_box/4.png',save_path='../captcha_binarization_images/')