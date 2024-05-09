```python

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

    
cur_dir = os.getcwd()
img_path = "./archive02/garbage_classification/"
label_list = os.listdir(img_path) 
    

img_path_list = list()
img_list = list()

for _ in label_list:
    img_path_list.append(img_path + _)

for _ in label_list:
    img_list.append(os.listdir(img_path + _))


### 함수 실행 코드 ###
train_img, test_img = load_lmg(img_path_list, img_list)


```
