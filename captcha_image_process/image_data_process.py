import os
import time
import random
from captcha.image import ImageCaptcha
from PIL import Image


def create_random_int_data(data_count, data_length):
    '''
    This is a function to create random int data
    :param data_count:create 0~data_count images
    :return:random data
    '''
    print('Will Create {} Random Data'.format(data_count))
    random_data = []
    for create_number in range(data_count):
        max_length = len(random_data)
        random_str = ''
        for random_length in range(data_length):
            random_str += str(random.randint(0, 9))
        # random_str = str(random_int_01) + str(random_int_02) + str(random_int_03) + str(random_int_04)
        if len(random_data) == 0:
            random_data.append(random_str)
        else:
            # cut the set /2
            # 二分
            if int(random_data[int(max_length / 2)]) > int(random_str):
                for i in range(int(max_length / 2), max_length):
                    if int(random_data[i]) is int(random_str):
                        break
                random_data.append(random_str)
            else:
                for i in range(0, int(max_length / 2)):
                    if int(random_data[i]) is int(random_str):
                        break
                random_data.append(random_str)

    print('End Data [{}]'.format(len(random_data)))
    return random_data


def create_image(random_data, image_file_path, image_width, image_height):
    '''
    This function is to create a image
    :param random_data:4 int str data
    :param image_file_path: save image path
    :param image_height image height
    :param image_width image_width
    :return:data length to creates
    '''
    # default
    if image_width == 0 and image_height == 0:
        img = ImageCaptcha(width=120, height=60)
    else:
        img = ImageCaptcha(width=image_width, height=image_height)
    print('Image Create is start!')
    for data in range(len(random_data)):
        img.create_captcha_image(random_data[data], color=random_color(), background='white').save(
            image_file_path + '{}_{}.png'.format(random_data[data], time.strftime('%Z%Y%m%d%H%M%S', time.localtime())))
        time.sleep(0.1)
        print('No.{}->{}.png'.format(data + 1, random_data[data]))
    return print('+Complete to create {} images+'.format(len(random_data)))


def create_image_char(image_width, image_height, char, count, background, save_file_path):
    '''
    This function is create char  captcha image
    :param image_width:image width
    :param image_height:   image height
    :param char:Str char
    :param count:Int count
    :param background:Str (White)(Black)(Red)...colors
    :param save_file_path:save image file path
    :return:file path list
    '''
    if image_width == 0 and image_height == 0:
        img = ImageCaptcha(width=120, height=60)
    else:
        img = ImageCaptcha(width=image_width, height=image_height)
    print('Image Create Char is start!')
    _path = []
    for i in range(0, count):
        file_path = save_file_path + '{}_{}_{}.png'.format(str(char),
                                                           str(time.strftime('%Z%Y%m%d%H%M%S', time.localtime())),
                                                           str(random.randint(0, 100)))
        img.create_captcha_image(chars=str(char), color=random_color(), background=background).save(file_path)

        _path.append(file_path)
        time.sleep(0.1)
        print('Save {}'.format(file_path))
    return _path


def random_color():
    '''
    This function is random to create a rgb number
    :return:random rgb (255,255,255)
    '''
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
