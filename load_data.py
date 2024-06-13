import os
import cv2 as cv
import numpy as np

def load_lmg(img_path_list, img_list):
    train_img = list()
    test_img = list()

    for path_num in range(len(img_path_list)):
        for img_num in range(0, int(len(img_list[path_num]) * 0.8)): ### split 0.8 ###
            ### label ###
            label = path_num
            ### img extract and preprocessing ###
            train = cv.imread(img_path_list[path_num] + "/" + img_list[path_num][img_num])
            train = cv.resize(train, (64, 64))
            train = cv.cvtColor(train, cv.COLOR_BGR2RGB)
            ### / 255.0 normalization
            train_img.append([np.array(train) / 255.0, np.array(label)])

    for path_num in range(len(img_path_list)):
        for img_num in range(int(len(img_list[path_num]) * 0.8) + 1, len(img_list[path_num])): ### split 0.2 ###
            ### label ###
            label = path_num
            ### img extract and preprocessing ###
            test = cv.imread(img_path_list[path_num] + "/" + img_list[path_num][img_num])
            test = cv.resize(test, (64, 64))
            test = cv.cvtColor(test, cv.COLOR_BGR2RGB)
            ### / 255.0 normalization
            test_img.append([np.array(test) / 255.0, np.array(label)])

    
    return train_img, test_img

#### Data 불러오기 ####
cur_dir = os.getcwd()

# garbage data -----------------------------------------
# 경로 설정
garbage_path = "./data/garbage"
garbage_label_list = os.listdir(garbage_path)

garbage_img_path_list = list()
garbage_img_list = list()

for _ in garbage_label_list:
    garbage_img_path_list.append(garbage_path + _)
for _ in garbage_label_list:
    garbage_img_list.append(os.listdir(garbage_path + _))

# 함수 실행
garbage_train_img, garbage_test_img = load_lmg(garbage_img_path_list, garbage_img_list)

# clothes data ------------------------------------------
# 경로 설정
clothes_path = "./data/clothes"
clothes_label_list = os.listdir(clothes_path)  

clothes_img_path_list = list()
clothes_img_list = list()

for _ in clothes_label_list:
    clothes_img_path_list.append(clothes_path + _)

for _ in garbage_label_list:
    clothes_img_list.append(os.listdir(clothes_path + _))

# 함수 실행
clothes_train_img, clothes_test_img = load_lmg(clothes_img_path_list, clothes_img_list)