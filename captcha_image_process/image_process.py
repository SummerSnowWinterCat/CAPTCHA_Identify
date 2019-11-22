'''
    author:wintercat
    github:summersnowwintercat.github.io/com
    this is a image learn demo
    2019-11-15 S->
'''

from PIL import Image
import time
import random
import numpy
import os


def remake_image(path):
    '''
    this function is block cut and cross cut
    like:
        cross  \ block
        0 1 0   1 0 1
        1 1 1   0 0 0
        0 1 0   1 0 1
    :param path:image file path
    :return: return image file path
    '''
    _image = Image.open(path)
    limit_height = _image.size[1]
    limit_width = _image.size[0]
    all_limit = 0  # image limit size
    _image = _image.convert('1')
    # _image.show()
    # 0 = black
    # 255 = white
    #
    for h in range(_image.size[1]):
        for w in range(_image.size[0]):
            position = (w, h)
            if _image.getpixel(position) == 0:
                cross_count = 0
                block_count = 0
                # print('get_0')
                # print('get position:', w, h)
                # cross check
                # 1 0 1
                # 0 0 0
                # 1 0 1
                # check position about the 0
                # 0 1 0
                # 1 0 1
                # 0 1 0
                # block 1,2,3,4
                # left->right->bottom left->bottom right
                if h + 1 < limit_height and h + 1 > all_limit:
                    up_pixel = _image.getpixel((w, h + 1))
                    if up_pixel == 255:
                        cross_count += 1
                    else:
                        cross_count = cross_count
                if h - 1 < limit_height and h - 1 > all_limit:
                    down_pixel = _image.getpixel((w, h - 1))
                    if down_pixel == 255:
                        cross_count += 1
                    else:
                        cross_count = cross_count
                if w - 1 < limit_width and w - 1 > all_limit:
                    left_pixel = _image.getpixel((w - 1, h))
                    if left_pixel == 255:
                        cross_count += 1
                    else:
                        cross_count = cross_count
                if w + 1 < limit_width and w + 1 > all_limit:
                    right_pixel = _image.getpixel((w + 1, h))
                    if right_pixel == 255:
                        cross_count += 1
                    else:
                        cross_count = cross_count
                    # _image.putpixel((w, h), 255)
                if h + 1 < limit_height and h + 1 > all_limit and w - 1 < limit_width and w - 1 > all_limit:
                    block_01_pixel = _image.getpixel((w - 1, h + 1))
                    if block_01_pixel == 255:
                        block_count += 1
                    else:
                        block_count = block_count
                if h + 1 < limit_height and h + 1 > all_limit and w + 1 < limit_width and w + 1 > all_limit:
                    block_02_pixel = _image.getpixel((w + 1, h + 1))
                    if block_02_pixel == 255:
                        block_count += 1
                    else:
                        block_count = block_count
                if h - 1 < limit_height and h - 1 > all_limit and w - 1 < limit_width and w - 1 > all_limit:
                    block_03_pixel = _image.getpixel((w - 1, h - 1))
                    if block_03_pixel == 255:
                        block_count += 1
                    else:
                        block_count = block_count
                if h - 1 < limit_height and h - 1 > all_limit and w + 1 < limit_width and w + 1 > all_limit:
                    block_04_pixel = _image.getpixel((w + 1, h - 1))
                    if block_04_pixel == 255:
                        block_count += 1
                    else:
                        block_count = block_count
                if block_count > 3 and cross_count >= 3:
                    print('may be this position is a dummy')
                    print('position:', (w, h))
                    _image.putpixel((w, h), 255)

    random_path = str(random.random())
    random_path = '../captcha_image_block_to_decide/' + random_path + '.png'
    _image.save(random_path, 'png')

    return random_path


def edge_search(path, deep_limit):
    '''
    :param path:image file path
    :param deep_limit: this is a edge deep default=5 if u set 0
    :return: return file path
    '''
    if deep_limit == 0:
        deep_limit = 5  # setting
    print('edge_search:' + path)
    print('deep:' + str(deep_limit))
    _image = Image.open(path)
    _image = _image.convert('1')
    for i in range(deep_limit):
        for h in range(_image.size[1]):
            for w in range(_image.size[0]):
                if _image.getpixel((i, h)) == 0:
                    _image.putpixel((i, h), 255)
                if _image.getpixel((w, i)) == 0:
                    _image.putpixel((w, i), 255)
    random_path = str(random.random())
    random_path = '../captcha_image_edge_to_decide/limit' + str(deep_limit) + '_' + random_path + '.png'
    _image.save(random_path, 'png')
    return random_path


def image_binarization_with_zero_and_one(image_path):
    '''
    this function is image binarization function
    :param path: image file path
    :return: pixel list by 0 1 and image size
    '''
    _image = Image.open(image_path)
    _image_size = _image.size
    _array_image = []
    for h in range(0, _image.size[1]):
        temp = []
        for w in range(0, _image.size[0]):
            position = (w, h)
            pixel = _image.getpixel(position)
            if pixel == 255:
                pixel = 1
                temp.append(pixel)
            else:
                pixel = 0
                temp.append(pixel)
        _array_image.append(temp)
    return _array_image, _image_size


def image_binarization(image_file_path, save_path):
    '''
    this function is create a binarization image and save image into the file
    >>open image read pixel remove pixel->>
    >>save image return image file path
    :param image_file_path:this is origin image file path
    :param save_path:this is save image file path
    :return:null  response no any information
    '''
    file_name = image_file_path.split('/')[len(image_file_path.split('/')) - 1]
    _image = Image.open(image_file_path)
    _image_gray = _image.convert('L')
    data_image_gray = _image_gray.load()
    _pixel = []
    for h in range(_image_gray.size[1]):
        for w in range(_image_gray.size[0]):
            if data_image_gray[w, h] < 200:
                data_image_gray[w, h] = 0
            else:
                data_image_gray[w, h] = 255
    save_path = save_path + file_name
    _image_gray.save(save_path)
    return save_path


def image_cut(path, cut_limit):
    '''
    this is image cut function
    :param path:image file path
    :param cut_limit:cut length
    :return: 0
    '''
    save_path = '../captcha_image_remake/' + str(random.random()) + '.png'
    #
    _image = Image.open(path)
    image_count = int(_image.size[0] / cut_limit)
    limit_height = _image.size[1]
    limit_width = _image.size[0]
    _image.crop(())
    _image.save(save_path, 'png')
    return 0


def image_binarization_vector(array_list, split_size):
    '''
    this function is remake array to vector and statistics
    :param array_list:numpy data list
    :param split_size:vertical and horizontal split count
    :return:vector list
    '''
    vsp_list = numpy.vsplit(array_list, split_size)  # vertical resize
    ''' |split_size = vertical count
    [0 0|0 0]
    [0 0|0 0]
    [0 0|0 0]
    [0 0|0 0]
    '''
    hsp_list = []  # horizontal resize
    for vsp in vsp_list:
        hsp_list.append(numpy.hsplit(vsp, split_size))
    '''
    [0 0|0 0]
    [0 0|0 0]
    ---------
    [0 0|0 0]
    [0 0|0 0]
    '''
    result = []
    for hsp in hsp_list:
        hsp_result = []
        for i in hsp:
            sum_number = numpy.sum(i)
            hsp_result.append(sum_number)
            result.append(hsp_result)

    return numpy.vstack(result)
