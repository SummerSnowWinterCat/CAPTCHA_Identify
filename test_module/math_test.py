import os
import numpy
import re
import random


def euclidean_distance(x, y):
    _data = 0
    _result = numpy.sqrt(numpy.sum(numpy.square(x - y)))
    return _result


if __name__ == '__main__':
    print('K-NN')
    _test_data = numpy.array([[1, 4, 5, 6], [6, 2, 3, 5]])
    vector_test = numpy.array([[random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)],
                               [random.randint(0, 9), random.randint(0, 9), random.randint(0, 9),
                                random.randint(0, 9)]])

    vector_data = numpy.array([[0, 1, 4, 1], [2, 2, 2, 2]])

    print('Vector Test :{}'.format(vector_test))
    print(euclidean_distance(_test_data, vector_data))
