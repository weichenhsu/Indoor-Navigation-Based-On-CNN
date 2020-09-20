# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 23:37:04 2020

@author: User
"""

import cv2
import time 
from imageai.Prediction.Custom import CustomImagePrediction
import os

execution_path = os.getcwd()

prediction = CustomImagePrediction()
prediction.setModelTypeAsDenseNet()
prediction.setModelPath('dense_old/model_ex-013_acc-0.976341.h5')
prediction.setJsonPath('dense_old/model_class.json')
prediction.loadModel(num_objects=13)

# 開啟影片檔案
cap = cv2.VideoCapture('D:\\User\\Downloads\\65105_current (online-video-cutter.com) (4).mp4')

place = ['ele_r']
correct = 0
wrong = 0

# 以迴圈從影片檔案讀取影格，並顯示出來
while(cap.isOpened()):
    ret, frame = cap.read()
    if not(frame is None):
        cv2.imwrite('tmp.jpg', frame)
    else:
        break
    prediction_image = 'tmp.jpg'
    predictions, probabilities = prediction.predictImage(prediction_image, result_count=1)
    print(predictions[0])
    if predictions[0] == place[0]:
        correct += 1
    else:
        wrong += 1
        
    #cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print('correct: ', correct)
print('wrong: ', wrong)