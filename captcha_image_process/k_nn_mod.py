import numpy
import os
import time
import re
import captcha_image_process.image_process as process

# 二值图
_image_binarization_path = '../captcha_binarization_images/'
# vector file path
_vector_file_path = '../train_data/'
# 缩小像素 10*10
_block_size = 10

if __name__ == '__main__':
    for path in os.listdir(_image_binarization_path):
        if re.search(r'\.(png|jpeg|jpg)$', path) is None:
            continue
        else:
            data, label = process.create_image_vector(image_file_path=_image_binarization_path + path,
                                                      block_size=_block_size,
                                                      save_file_path='../captcha_binarization_images/')
            process.save_vector_file(data=data, file_name=label,save_file_path=_vector_file_path)
