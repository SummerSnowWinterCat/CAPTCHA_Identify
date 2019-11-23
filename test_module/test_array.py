import os
import random
import numpy
import re
import captcha_image_process.image_process as i_process
import captcha_image_process.image_data_process as d_p
import matplotlib.pyplot as plot

# d_p.create_image_char(image_width=60, image_height=60, char=9, count=1000, background='white',
#                      save_file_path='../captcha_train_images/9/')


train_path = '../captcha_train_images/'
binarization_path = '../captcha_binarization_images/'
vector_path = '../train_data/'


def init_binarization_images():
    vector_data = []
    train_data = i_process.get_training_data_path(train_data_path=train_path)
    for train in range(len(train_data)):
        print(train_data[train])
        vector, label = i_process.create_binarization_image_vector(image_file_path=train_data[train],
                                                                   save_file_path=binarization_path, block_size=10)
        vector_data_path = i_process.save_vector_file(data=vector, file_name=str(label), save_file_path=vector_path)
        vector_data.append(vector_data_path)
        print('vector_create No.{}'.format(train))
    return 0


if __name__ == '__main__':
    # init_binarization_images()
    test_data, test_label = i_process.create_binarization_image_vector(image_file_path='../test_data/unknown.png',
                                                                       block_size=10,
                                                                       save_file_path='../test_image/test_image_box/')
    # sample data
    vector_data, vector_label = i_process.vector_file_unfreeze(train_data_path=vector_path)
    if len(vector_data) == len(vector_label):
        print('unfreeze complete')
    for data in range(len(vector_data)):
        result = (test_data - vector_data[data])
        result = numpy.sum(result)
        plot.scatter(x=result, y=vector_label[data], alpha=0.8, s=30)

    plot.show()
