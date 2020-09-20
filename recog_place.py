import cv2
from imageai.Prediction.Custom import CustomImagePrediction
import os
import numpy
import var
from project_combine import *

model_path = ['dense_old/model_ex-013_acc-0.976341.h5', 'dense_new/model_ex-007_acc-0.999647.h5']
json_path = ['dense_old/model_class.json', 'dense_new/model_class.json']
place = ['4202', '4201', 'OldA1', 'OldA2', 'OldA3', 'ele', '65101', '65101&2', '65102', 'NewA4', '65104', '65105', 'newD']
frame_correction = 1
change = 0
model_index = 0
area_count = 0
prediction = CustomImagePrediction()
    
def reset():
    global model_index, change, area_count
    model_index = 0
    var.start_place = []
    var.preindex = -1
    var.direction = 0
    var.destination_index = -1
    change = 0
    area_count = 0

def change_model():
    global model_index
    print('change model')
    if(model_index == 0):
        model_index = 1
    else:
        model_index = 0
    prediction.setModelTypeAsDenseNet()
    prediction.setModelPath(model_path[model_index])
    prediction.setJsonPath(json_path[model_index])
    prediction.loadModel(num_objects=13)  

def load_model():
    #execution_path = os.getcwd()
    prediction.setModelTypeAsDenseNet()
    prediction.setModelPath(model_path[model_index])
    prediction.setJsonPath(json_path[model_index])
    prediction.loadModel(num_objects=13)  
    

def check_start_place(frame):
    cv2.imwrite('tmp.jpg', frame)
    prediction_image = 'tmp.jpg'
    predictions, probabilities = prediction.predictImage(prediction_image, result_count=1) 
    #print("prediction_image")            
    # 印出結果
    print(predictions[0], ' : ', probabilities[0])
            
    if probabilities[0] > 65:
        x = predictions[0].split("_")
        var.start_place.append(x)
        if len(var.start_place) > 5:
            print(var.start_place)
            tmp = numpy.zeros(shape=(len(place)))
            tmp_d = numpy.zeros(shape=(2))
            for i in range(len(var.start_place)): # 找出判斷最準確的起始地點
                for j in range(len(place)):
                    if(var.start_place[i][0] == place[j]):
                        tmp[j] = tmp[j] + 1
                        if var.start_place[i][1] == 'l' or var.start_place[i][1] == 'f':
                            tmp_d[1] = tmp_d[1] + 1
                        else:
                            tmp_d[0] = tmp_d[0] + 1
                        break
            var.preindex = tmp.argmax(axis = 0)          
            if tmp_d[0] > tmp_d[1]: # 行進方向
                var.direction = -1
            else:
                var.direction = 1
    
def check_current_place(frame):
    global change, area_count
    cv2.imwrite('tmp.jpg', frame)
    prediction_image = 'tmp.jpg'
    predictions, probabilities = prediction.predictImage(prediction_image, result_count=1)
    frame_correction = 1         
    # 印出結果
    print(predictions[0], ' : ', probabilities[0])
    area_count += 1
    #if probabilities[0] > 50:
    if change >= 3:
        print('change: ', change)
        change = -100
        change_model()
    x = predictions[0].split("_")
    for i in range(len(place)): # 找出目前判斷index
        if(x[0] == place[i]):
            index = i
            break
    if predictions[0] == '4201_f':
        index = 2
    print('preindex: ', var.preindex, ' index: ', index)
    if index != var.preindex: # 目前位置有改變
        if index - var.preindex == var.direction: # or index - var.preindex == 2*var.direction:
            print('pre:' + str(var.preindex) + ' now: ' + str(index))
            var.preindex = index
            area_count = 1
    print('area count: _______', area_count)
    if area_count > len(path[var.preindex].x):
        area_count = 1
        var.preindex = var.preindex + var.direction
    # 判斷方向
    if var.preindex == 5 and var.direction == 1:
        change = change + 1
    if var.preindex == 6 and var.direction == -1:
        change = change + 1
