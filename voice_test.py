# 語音辨識
import speech_recognition
import time
import os
import pyaudio
import wave    
# 語音合成
import pyttsx3
# 字串相似度 
import difflib
import var

global engine

def Voice_To_Text():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source: 
        print("請開始說話:")                               # print 一個提示 提醒你可以講話了
        r.adjust_for_ambient_noise(source)     # 函數調整麥克風的噪音:
        audio = r.listen(source)
    try:
        Text = r.recognize_google(audio, language="zh-TW")     

    except r.UnknowValueError:
        Text = "無法翻譯"
    except sr.RequestError as e:
        Text = "無法翻譯{0}".format(e)
              # 兩個 except 是當語音辨識不出來的時候 防呆用的 
    return Text

def is_number(s):
    try:
        float(s)
        return True
    except:
        return False

def Number_To_Chinese(text):
    model = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']
    result = ''
    for i in range(len(text)):
        result += model[int(text[i])]
    return result

def string_similar(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()

def voice_set():
    global engine
    # 語音合成初始化
    engine = pyttsx3.init()
    engine.setProperty('voice', "com.apple.speech.synthesis.voice.mei-jia")
    # 語速控制
    rate = engine.getProperty('rate')
    #print(rate)
    engine.setProperty('rate', rate-20)

    # 音量控制
    volume = engine.getProperty('volume')
    #print(volume)
    engine.setProperty('volume', volume-0.25)
    
def voice_detect_destination():
    place = ['4202', '4201', 'OldA1', 'OldA2', 'OldA3', 'ele', '65101', '65101&2', '65102', 'NewA4', '65104', '65105', 'newD']
    # 讀取目的地
    text = Voice_To_Text()
    print('語音輸入:', text)
    # 辨認目的地位置
    temp = 0
    for i in range(len(place)):
        x = string_similar(place[i], text)
        if x == 1:
            var.destination_index = i
            break
        elif x >= temp:
            var.destination_index = i
            temp = x
    print(place[var.destination_index], ' index: ', var.destination_index)

def voice_output(sentence):
    global engine
    engine.say(sentence)
    engine.runAndWait()
