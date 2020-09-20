import numpy as np
import cv2 
import random
import var
#from voice_test import voice2test_main
img = cv2.imread("D:/project/building_map.jpg")
class_room = []
path = []
nowIndex = 0
last = 0
lastIndex = 0
class Baz1():
    "stores path location"
    def __init__(self, area, x, y):
        self.area = area
        self.x = x
        self.y = y
def setWalkingPathLoaction():    
    path.append(Baz1("4202",([283,258]),([107,108])))
    path.append(Baz1("4201",([230,201,172,146,122,124]),([110,112,114,116,120,148])))
    path.append(Baz1("Oaisle1",([125,126,127,128,129,130]),([179,194,210,224,238,253])))
    path.append(Baz1("Oaisle2",([131,132,133,134]),([268,280,290,303])))
    path.append(Baz1("Oaisle3",([134,135,136,138,140,142,145,147,161,182,214]),([333,341,349,365,399,419,430,442,467,473,480])))
    path.append(Baz1("ele",([251,266]),([487,503])))
    path.append(Baz1("Naisle1",([278,291,301]),([525,549,573])))
    path.append(Baz1("Naisle2",([312,320,329]),([596,616,644])))
    path.append(Baz1("Naisle3",([341,352,362]),([673,699,724])))
    #path.append(Baz1("Ndoor",([628,645,658,669]),([227,233,235,235])))
    path.append(Baz1("Naisle4",([381,408]),([748,759])))
    path.append(Baz1("65104",([444,472,505]),([763,762,762])))
    path.append(Baz1("65105",([532,558]),([762,761])))
    
def map_show():
    global nowIndex
    global last ##last area
    global lastIndex
    if(var.preindex == var.destination_index): #抵達目的地
        return
    if(last != var.preindex):
        if var.direction == 1:
            nowIndex = 0
        else:
            nowIndex = len(path[var.preindex].x) - 1
        last = var.preindex
    else:
        if var.direction == 1:
            if(nowIndex < len(path[var.preindex].x)-1):
                nowIndex = nowIndex + 1
                lastIndex = nowIndex            
            elif(nowIndex == len(path[var.preindex].x)-1) and last == var.preindex:
                #print('last')
                nowIndex = lastIndex
        elif var.direction == -1:
            if nowIndex > 0:
                nowIndex = nowIndex - 1
                lastIndex = nowIndex            
            elif(nowIndex == 0) and last == var.preindex:
                #print('last')
                nowIndex = lastIndex
    var.centerx = int(path[var.preindex].x[nowIndex])
    var.centery = int(path[var.preindex].y[nowIndex])
    #print('nowIndex:______________', nowIndex)
    '''elif(last != var.preindex):
        if var.direction == 1:
            nowIndex = 0
        else:
            nowIndex = len(path[var.preindex].x) - 1
        last = var.preindex'''
        #print(last)
    '''elif (nowIndex == len(path[var.preindex].x)-1) and last != var.preindex:
        nowIndex = 0
        last = var.preindex
    '''
