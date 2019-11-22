import captcha_image_process.image_process as i_process
from PIL import Image
import numpy
import os
import test_module.test_array as a
import random

if __name__ == '__main__':
    list, size = (i_process.image_binarization_with_255_to_one('../captcha_binarization_images/1.png.png'))
    np_list = i_process.image_binarization_change_0_1(list)

    print(i_process.image_binarization_vector(np_list, 6))
