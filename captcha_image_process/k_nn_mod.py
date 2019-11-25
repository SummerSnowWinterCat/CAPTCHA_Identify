import numpy
import os
import re
import captcha_image_process.image_process as process


def init_binarization_images(train_path, binarization_path, vector_path):
    '''
    This function is init train file and train data
    :param train_path:train data file path
    :param binarization_path:binarization file path
    :param vector_path:train image data vector path
    :return: 1 no message
    '''
    vector_data = []
    train_data = process.get_training_data_path(train_data_path=train_path)
    for train in range(len(train_data)):
        vector, label = process.create_binarization_image_vector(image_file_path=train_data[train],
                                                                 save_file_path=binarization_path, block_size=10)
        vector_data_path = process.save_vector_file(data=vector, file_name=str(label), save_file_path=vector_path)
        vector_data.append(vector_data_path)
        # print('vector_create No.{}'.format(train))
    return 1


def euclidean_distance(test_data, train_data):
    '''
    This function is euclidean distance match
    :param test_data:test image data --vector
    :param train_data:train image data --vector
    :return:result --distance
    '''
    _result = numpy.sqrt(numpy.sum(numpy.square(test_data - train_data)))
    return _result


def load_test_vector(image_file_path, block_size, save_file_path):
    '''
    This function is load test data file vector
    :param image_file_path:test image file path
    :param block_size:resize vector 60*60->10*10 = 10
    :param save_file_path:test image save file path
    :return:test data and test label
    '''
    _image_file_path = []
    _test_data = []
    _test_label = []
    if len(os.listdir(image_file_path)) > 0:
        for dirs in os.listdir(image_file_path):
            full_path = image_file_path + dirs
            if re.search(r'\.(png|jpeg|jpg)$', full_path) is None:
                continue
            else:
                _image_file_path.append(full_path)
        if len(_image_file_path) > 0:
            for images in _image_file_path:
                test_data, test_label = process.create_binarization_image_vector(
                    image_file_path=images,
                    block_size=block_size,
                    save_file_path=save_file_path)
                _test_data.append(test_data)
                _test_label.append(test_label)
            return _test_data, _test_label
        else:
            return -1
    else:
        return -1


def data_check(data, data_label):
    '''
    This function is check length for data and label
    same or not same
    :param data:data file --list/array
    :param data_label:label file --list/array
    :return:boolean true or false
    '''
    if len(data) == len(data_label):
        print('unfreeze complete')
        return True
    else:
        return False


def k_search(k, result):
    '''
    This function is forecast range for k
    :param k: k is range
    :param result: result data
    :return:forecast data --list/array
    '''
    return sorted(result, key=lambda x: x[1])[k][0]
