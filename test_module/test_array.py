import os
import random
import numpy
import captcha_image_process.image_process as i_process
import captcha_image_process.image_data_process as d_p

if __name__ == '__main__':
    d_p.create_image_char(image_width=60, image_height=60, char=0, count=1000, background='white',
                          save_file_path='../captcha_train_images/0/')

