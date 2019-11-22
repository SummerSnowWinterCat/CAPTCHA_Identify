import captcha_image_process.image_process as i_process
from PIL import Image
import numpy
import os
import test_module.test_array as a
import random

if __name__ == '__main__':
    # print('set a array')
    array_w = 60
    array_h = 60
    # print('array({}x{})'.format(array_w, array_h))
    all_arraylist = []
    for h in range(0, array_h):
        set_h = []
        for w in range(0, array_w):
            set_h.append(random.randint(0, 1))
        all_arraylist.append(set_h)

    arraylist = numpy.array(all_arraylist)
    print(arraylist)
    print('===================')
    print('===================')
    print(a.array_split_for_image_size(arraylist, 6))
