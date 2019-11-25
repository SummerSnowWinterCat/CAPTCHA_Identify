from captcha_image_process import image_data_process, image_process, k_nn_mod
import os

train_path = '../captcha_train_images/'  # sample or train image (origin)
binarization_path = '../captcha_binarization_images/'  # image binarization file path
vector_path = '../train_data/'  # train data file path (vector file)
test_image_file_path = '../test_data/'  # test data file path
test_image_save_path = '../test_image/test_image_box/'  # test data binarization file path
block_size = 10  # block size is resize image binarization like 60*60->10*10 = 10
k = 3  # this is forecast range
forecast_num = []  # forecast result
if __name__ == '__main__':
    # step.01
    # init binarization image
    print('<<<init>>>')
    k_nn_mod.init_binarization_images(train_path=train_path, binarization_path=binarization_path,
                                      vector_path=vector_path)
    # step.02
    # get test data
    print('<<<load test data>>>')
    test_data, test_label = k_nn_mod.load_test_vector(image_file_path=test_image_file_path, block_size=block_size,
                                                      save_file_path=test_image_save_path)
    # step.03
    # unfreeze train data
    print('<<<load train data>>>')
    vector_data, vector_label = image_process.vector_file_unfreeze(train_data_path=vector_path)

    # step.04 check data
    # get result
    if k_nn_mod.data_check(data=vector_data, data_label=vector_label) and k_nn_mod.data_check(data=test_data,
                                                                                              data_label=test_label):

        for test in range(len(test_data)):
            result = []
            for data in range(len(vector_data)):
                print('load..>>{}'.format(data))
                result.append(
                    [vector_label[data],
                     k_nn_mod.euclidean_distance(test_data=test_data[test], train_data=vector_data[data])])
            forecast_num.append(k_nn_mod.k_search(k=k, result=result))
        print('forecast:', forecast_num)
    else:
        print('error[!] ,Step.03')
