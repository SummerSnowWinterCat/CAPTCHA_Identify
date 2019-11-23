import os
import random
import numpy
import re
import captcha_image_process.image_process as i_process
import captcha_image_process.image_data_process as d_p

# d_p.create_image_char(image_width=60, image_height=60, char=9, count=1000, background='white',
#                      save_file_path='../captcha_train_images/9/')


train_path = '../captcha_train_images/'
binarization_path = '../captcha_binarization_images/'
vector_path = '../train_data/'


def init_binarization_images():
    train_data = i_process.get_training_data_path(train_data_path=train_path)
    for train in range(len(train_data)):
        print(train_data[train])
        i_process.create_image_vector(image_file_path=train_data[train], save_file_path=binarization_path, block_size=6)
        print('vector_create No.'.format(train))
    return 0


if __name__ == '__main__':
    for data_path in os.listdir(binarization_path):
        i_process.create_image_vector(image_file_path=data_path, block_size=6, save_file_path=vector_path)
