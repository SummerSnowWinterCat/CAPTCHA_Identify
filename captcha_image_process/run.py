from captcha_image_process import image_data_process, image_process, k_nn_mod
import os

train_path = '../captcha_train_images/'
binarization_path = '../captcha_binarization_images/'
vector_path = '../train_data/'
test_image_file_path = '../test_data/'
test_image_save_path = '../test_image/test_image_box/'
block_size = 10
result = []
k = 3
if __name__ == '__main__':
    # step.01
    # init binarization image
    k_nn_mod.init_binarization_images(train_path=train_path, binarization_path=binarization_path,
                                      vector_path=vector_path)
    # step.02
    # get test data
    test_data, test_label = k_nn_mod.load_test_vector(image_file_path=test_image_file_path, block_size=block_size,
                                                      save_file_path=test_image_save_path)
    # step.03
    # unfreeze train data
    vector_data, vector_label = image_process.vector_file_unfreeze(train_data_path=vector_path)

    # step.04 check data
    # get result
    if k_nn_mod.data_check(data=vector_data, data_label=vector_label):
        for data in range(len(vector_data)):
            print('load..>>{}'.format(data))
            result.append(
                [vector_label[data], k_nn_mod.euclidean_distance(test_data=test_data, train_data=vector_data[data])])
        for k in k_nn_mod.k_search(k, result):
            print('This test data is :[ {} ]'.format(k))
    else:
        print('error[!] ,Step.03')
