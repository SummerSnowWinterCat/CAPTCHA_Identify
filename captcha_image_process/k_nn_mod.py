import numpy
import os
import time
import captcha_image_process.image_process as process

# 二值图
_image_binarization_path = '../captcha_binarization_images/'
# 缩小像素 10*10
_block_size = 10


def create_image_vector(image_file_path):
    # 灰度化 并 保存path
    gray_scale_image_path = process.image_save_to_gray_scale(image_file_path=image_file_path,
                                                             save_file_path=_image_binarization_path)
    # 获取pixel数组和尺寸
    data, image_size = process.image_binarization_with_255_to_one(gray_scale_image_path)
    # 处理0 1 转化白与黑
    data = process.image_binarization_change_0_1(data=data)
    # 数组处理返回向量
    vector = process.image_binarization_vector(data=data, split_size=_block_size)

    return vector


if __name__ == '__main__':
    for path in os.listdir(_image_binarization_path):
        print(create_image_vector(_image_binarization_path + path))
