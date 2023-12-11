import os
import cv2
from keras.utils import image_dataset_from_directory
train_img_path = '../videodata/TrainValVideo_frame'
test_img_path ='../videodata/TestVideo_frame'
json_path = '../videodata/train_val_videodatainfo.json'

def get_img_idx(json_path, train_img_path, seq):
    pairs = {}
    matching_img = [file for file in os.listdir(train_img_path) if file.endswith(seq)]
    with open(json_path) as data:
        for file in os.listdir(train_img_path):
            if file.endswith(f'{seq}.jpg'):
                pairs[seq] = file
    return pairs

                
    #for i in range(140200):
    #    if data['sentences'][i]['video_id'] == f'video{id}':
    #        print(data['sentences'][i]['caption']
def encode_img(img_path): #그냥 resize 아닌가
    image_dataset_from_directory(
        img_path,
        labels='train',
        color_mode='rgb',
        batch_size=32,
        image_size=(30, 30),
        shuffle=True,
        interpolation='bilinear',
        validation_split=0.2
    )
def data_gen(captions, img, id):


