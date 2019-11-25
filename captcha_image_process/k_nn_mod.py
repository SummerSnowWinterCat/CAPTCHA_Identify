import numpy
import os
import time
import re
import captcha_image_process.image_process as process
import math
import matplotlib.pyplot as plot


def init_binarization_images(train_path, binarization_path, vector_path):
    vector_data = []
    train_data = process.get_training_data_path(train_data_path=train_path)
    for train in range(len(train_data)):
        print(train_data[train])
        vector, label = process.create_binarization_image_vector(image_file_path=train_data[train],
                                                                 save_file_path=binarization_path, block_size=10)
        vector_data_path = process.save_vector_file(data=vector, file_name=str(label), save_file_path=vector_path)
        vector_data.append(vector_data_path)
        print('vector_create No.{}'.format(train))
    return 0


def euclidean_distance(test_data, train_data):
    _result = numpy.sqrt(numpy.sum(numpy.square(test_data - train_data)))
    return _result


def load_test_vector(image_file_path, block_size, save_file_path):
    if len(os.listdir(image_file_path)) > 0:
        for dir in os.listdir(image_file_path):
            print(dir)
            if re.search(r'\.(png|jpeg|jpg)$', dir) is None:
                print('Error No test images')
                return -1
            else:
                print('ok')
    else:
        return -1

    # test_data, test_label = process.create_binarization_image_vector(
    #     image_file_path=image_file_path,
    #    block_size=block_size,
    #    save_file_path=save_file_path)

    return  # test_data, test_label


def data_check(data, data_label):
    if len(data) == len(data_label):
        print('unfreeze complete')
        return True
    else:
        return False


def k_search(k, result):
    return sorted(result, key=lambda x: x[1])[k][0]
