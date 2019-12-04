import os
import random
import numpy
import re
import captcha_image_process.image_process as i_process
import captcha_image_process.image_data_process as d_p
import captcha_image_process.k_nn_mod as knn

# d_p.create_image_char(image_width=60, image_height=60, char=9, count=1000, background='white',
#                      save_file_path='../captcha_train_images/9/')


train_path = '../captcha_train_images/'
binarization_path = '../captcha_binarization_images/'
vector_path = '../train_data/'

if __name__ == '__main__':
    knn.load_test_vector(image_file_path='../test_data/', block_size=10, save_file_path='test_image/test_image_box/')
