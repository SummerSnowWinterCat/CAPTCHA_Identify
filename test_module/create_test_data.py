import captcha_image_process.image_data_process as d_process
import os


def create_train_data():
    print("<Create Train Data />")
    for i in range(0, 10):
        d_process.create_image_char(image_height=60, image_width=60, char=i, count=1000, background='white',
                                    save_file_path='../captcha_train_images/{}/'.format(i))
    return 1


def create_train_data_once(number):
    d_process.create_image_char(image_height=60, image_width=60, char=number, count=1, background='white',
                                save_file_path='../captcha_train_images/{}/'.format(number))
    return 1
