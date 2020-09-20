import sys
from PyQt5.QtGui import QPixmap, QIcon, QFont, QImage, QPalette, QBrush, QTransform
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QWidget
from PyQt5 import QtCore
from project_combine import *
from voice_test import *
from recog_place import *
filename = "D:\\project\\ui\\"
coordinate = [30, 100]
dest_coord = [[313,39], [432,51], [310,168], [306,204], [303,313], [238,397], [219,469], [208,508], [193,556], [175,597], [111,787], [34,785]]

class MainWindow(QMainWindow):

    def __init__(self):
        load_model()
        voice_set()
        setWalkingPathLoaction()
        super(MainWindow, self).__init__()
        self.resize(640,1000) # smart phone size 960
        '''palette = QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("D:\\Project\\ui\\background.jpg")))        
        self.setPalette(palette)'''
        self.setStyleSheet("background-color:#2D4080;")
        self.title = "Indoor Navigation"
        self.setWindowTitle(self.title)
        
        #title label
        self.label1 = QLabel(self)
        pixmap = QPixmap(filename+'cover\\title.png')
        self.label1.setPixmap(pixmap)
        self.label1.resize(pixmap.width(),pixmap.height())
        self.label1.move(195,130)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setStyleSheet("border:none; background:transparent")
        
        #map
        self.label2 = QLabel(self)
        pixmap = QPixmap(filename+'building_map.jpg')
        self.label2.setPixmap(pixmap)
        self.label2.resize(pixmap.width(),pixmap.height())
        self.label2.move(15,110)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setStyleSheet("border:none; background:transparent")
        self.label2.setVisible(False)
        
        #destination        
        self.label3 = QLabel(self)
        pixmap = QPixmap(filename+'des.png')
        self.label3.setPixmap(pixmap)
        self.label3.resize(316,58)
        self.label3.move(162,550) 
        self.label3.setStyleSheet("border:none; background:transparent")
        self.label3.setVisible(False)
        #departure
        self.label4 = QLabel(self)
        pixmap = QPixmap(filename+'depa.png')
        self.label4.setPixmap(pixmap)
        self.label4.resize(316,58)
        self.label4.move(162,640)
        self.label4.setStyleSheet("border:none; background:transparent")
        self.label4.setVisible(False)
        
        #video
        self.label6 = QLabel(self)
        t = QTransform()
        t.rotate(90)
        pixmap1 = QPixmap(filename+'building_map_4.jpg')
        pixmap1 = pixmap1.transformed(t)
        self.label6.resize(pixmap1.width(),pixmap1.height())
        self.label6.setScaledContents(True)
        self.label6.move(30,100)
        self.label6.setAlignment(QtCore.Qt.AlignCenter)
        self.label6.setPixmap(pixmap1)
        self.label6.setStyleSheet("border:none; background:transparent")
        self.label6.setVisible(False)
        
        # destination text
        self.label7 = QLabel(self)
        self.label7.setStyleSheet("border:none; background:transparent")
        self.label7.resize(100,24)
        self.label7.move(300,567)
        self.label7.setVisible(False)
        
        # departure text
        self.label8 = QLabel(self)
        self.label8.setStyleSheet("border:none; background:transparent")
        self.label8.resize(100,24)
        self.label8.move(300,657)
        self.label8.setVisible(False)
        
        # cover picture
        self.label9 = QLabel(self)
        pixmap = QPixmap(filename+'cover\\pic.png')
        self.label9.setPixmap(pixmap)
        self.label9.resize(pixmap.width(),pixmap.height())
        self.label9.move(195,290)
        self.label9.setAlignment(QtCore.Qt.AlignCenter)
        self.label9.setStyleSheet("border:none; background:transparent")
        
        # cover slogan
        self.label10 = QLabel(self)
        pixmap = QPixmap(filename+'cover\\Start Your Indoor Discovery.png')
        self.label10.setPixmap(pixmap)
        self.label10.resize(pixmap.width(),pixmap.height())
        self.label10.move(185,570)
        self.label10.setStyleSheet("border:none; background:transparent")
        
        # walk
        self.label12 = QLabel(self)
        pixmap = QPixmap(filename+'walk1.png')
        self.label12.setPixmap(pixmap)
        self.label12.resize(pixmap.width(),pixmap.height())
        self.label12.setStyleSheet("border:none; background:transparent")
        self.label12.setVisible(False)
        
        # introduction
        self.label13 = QLabel(self)
        pixmap = QPixmap(filename+'dest_icon.png')
        self.label13.setPixmap(pixmap)
        self.label13.resize(pixmap.width(),pixmap.height())
        self.label13.setStyleSheet("border:none; background:transparent")
        self.label13.setVisible(False)
        
        #error message
        self.label5 = QLabel(self)
        self.label5.setAlignment(QtCore.Qt.AlignCenter)
        self.label5.resize(298,37)
        self.label5.move(171,480)
        self.label5.setStyleSheet("border:none; background:transparent")
        self.label5.setVisible(False)
        
        
        self.button1 = QPushButton(self)#RESET
        self.button1.setIcon(QIcon(filename+'reset.png'))
        self.button1.setIconSize(QtCore.QSize(40,40))  # 建立名字
        self.button1.setStyleSheet("border:none")
        self.button1.resize(40,40)
        self.button1.move(10,15)  # 移動位置
        self.button1.clicked.connect(self.button1Clicked)
        self.button1.setVisible(False)

        self.button2 = QPushButton(self) #語音
        self.button2.setIcon(QIcon(filename+'record.png'))
        self.button2.setIconSize(QtCore.QSize(85,85))
        self.button2.resize(85,85)
        self.button2.setStyleSheet("border:none")
        self.button2.move(460,805)  # 移動位置
        self.button2.clicked.connect(self.button2Clicked)
        self.button2.setVisible(False)

        self.button3 = QPushButton(self) #camera
        self.button3.setIcon(QIcon(filename+'camera.png'))
        self.button3.setIconSize(QtCore.QSize(70,70))
        self.button3.resize(70,70)
        self.button3.setStyleSheet("border:none")
        self.button3.move(110,820)  # 移動位置
        self.button3.clicked.connect(self.button3Clicked)
        self.button3.setVisible(False)

        self.button4 = QPushButton(self) # START
        self.button4.setIcon(QIcon(filename+'group_start.png'))
        self.button4.setIconSize(QtCore.QSize(100,100))
        self.button4.resize(100,100)
        self.button4.setStyleSheet("border:none")
        self.button4.move(270,800)  # 移動位置
        self.button4.clicked.connect(self.button4Clicked)
        self.button4.setVisible(False)
        
        self.button5 = QPushButton(self) # home
        self.button5.setIcon(QIcon(filename+'home.png'))
        self.button5.setIconSize(QtCore.QSize(40,40))  # 建立名字
        self.button5.setStyleSheet("border:none")
        self.button5.resize(40,40)
        self.button5.move(590,15)  # 移動位置
        self.button5.clicked.connect(self.button5Clicked)
        self.button5.setVisible(False)
        
        self.button6 = QPushButton(self) # get start
        self.button6.setIcon(QIcon(filename+'cover\\start button.png'))
        self.button6.setIconSize(QtCore.QSize(200,76))  # 建立名字
        self.button6.setStyleSheet("border:none; background:transparent")
        self.button6.resize(200,76)
        self.button6.move(220,670)  # 移動位置
        self.button6.clicked.connect(self.button6Clicked)
        
        self.button7 = QPushButton(self) # question
        self.button7.setIcon(QIcon(filename+'cover\\question.png'))
        self.button7.setIconSize(QtCore.QSize(60,60))  # 建立名字
        self.button7.setStyleSheet("border:none; background:transparent")
        self.button7.resize(60,60)
        self.button7.move(80,850)  # 移動位置
        self.button7.clicked.connect(self.button7Clicked)
        
        self.button8 = QPushButton(self) # find
        self.button8.setIcon(QIcon(filename+'cover\\find.png'))
        self.button8.setIconSize(QtCore.QSize(60,60))  # 建立名字
        self.button8.setStyleSheet("border:none; background:transparent")
        self.button8.resize(60,60)
        self.button8.move(500,850)  # 移動位置
        self.button8.clicked.connect(self.button8Clicked)
        
        # introduction
        self.label11 = QLabel(self)
        self.label11.resize(394,539)
        self.label11.setStyleSheet("border:none; background:transparent")
        self.label11.setVisible(False)
        
        self.button9 = QPushButton(self) # close introduction
        self.button9.setIcon(QIcon(filename+'cover\\x.png'))
        self.button9.setIconSize(QtCore.QSize(22,23))  # 建立名字
        self.button9.setStyleSheet("border:none; background:transparent")
        self.button9.resize(22,23)
        self.button9.move(475,120)  # 移動位置
        self.button9.clicked.connect(self.button9Clicked)
        self.button9.setVisible(False)

    def button1Clicked(self): # reset
        print('click reset')
        self.button1.setStyleSheet('border: 2px solid gray; background:transparent')
        cv2.waitKey(30)
        self.button1.setStyleSheet('border:none; background:transparent')
        var.isreset = 1
        reset()
        self.label2.setVisible(True)
        self.label3.setVisible(True)
        self.label4.setVisible(True)
        self.label6.setVisible(False)
        self.label7.setVisible(False)
        self.label8.setVisible(False)
        self.label12.setVisible(False)
        self.label13.setVisible(False)
        self.button2.setVisible(True)
        self.button3.setVisible(True)
        self.button4.setVisible(True)
        # map圖像改回來
        pixmap = QPixmap('D:\\project\\ui\\building_map.jpg')
        self.label2.setPixmap(pixmap)        
        
    def button2Clicked(self): # 語音
        print('click voice')
        self.button2.setStyleSheet('border: 2px solid gray; background:transparent')
        cv2.waitKey(30)
        self.button2.setStyleSheet('border:none; background:transparent')
        var.isreset = 0
        #voice_output('請說出目的地')
        voice_detect_destination()
        pixmap = QPixmap('D:\\Project\\ui\\' + place[var.destination_index] + '.png')
        self.label7.setPixmap(pixmap)
        self.label7.setVisible(True)
    
    def button3Clicked(self): # camera
        print('click camera')
        self.button3.setStyleSheet('border: 2px solid gray; background:transparent')
        cv2.waitKey(30)
        self.button3.setStyleSheet('border:none; background:transparent')
        var.isreset = 0
        capture = cv2.VideoCapture("D:/project/4202_start.mp4") #"D:/project/4202_start.mp4"
        c = 1
        time_F = 10
        
        while(capture.isOpened()):
            # 顯示影片
            ret, frame = capture.read()  
            rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
            convertToQtFormat = QPixmap.fromImage(convertToQtFormat)
            self.label2.setPixmap(convertToQtFormat)
            
            if c % time_F == 0:
                check_start_place(frame)
            c = c + 1
            if ret == False or len(var.start_place) > 5:
                print('start: ', len(var.start_place))
                break
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if var.isreset >= 1:
                break
        if var.preindex != -1:
            pixmap = QPixmap('D:\\Project\\ui\\' + place[var.preindex] + '.png')
            self.label8.setPixmap(pixmap)
            self.label8.setVisible(True)
        capture.release()
        # 影片圖像改回來
        pixmap = QPixmap('D:\\project\\ui\\building_map.jpg')
        self.label2.setPixmap(pixmap)

    def button4Clicked(self): # start navigate
        print('start navigation')
        var.isreset = 0

        # 尚未設置出發地與目的地
        if var.preindex == -1 and var.destination_index == -1:
            pixmap = QPixmap(filename+'warning1.png')
            self.label5.setPixmap(pixmap)
            self.label5.setVisible(True)
            cv2.waitKey(1000)
            self.label5.setVisible(False)
        # 尚未設置出發地
        elif var.preindex == -1:
            pixmap = QPixmap(filename+'warning2.png')
            self.label5.setPixmap(pixmap)
            self.label5.setVisible(True)
            cv2.waitKey(1000)
            self.label5.setVisible(False)
        # 尚未設置目的地
        elif var.destination_index == -1:
            pixmap = QPixmap(filename+'warning3.png')
            self.label5.setPixmap(pixmap)
            self.label5.setVisible(True)
            cv2.waitKey(1000)
            self.label5.setVisible(False)
        # 皆設置完成
        else:
            self.label2.setVisible(False)
            self.label3.setVisible(False)
            self.label4.setVisible(False)
            self.label6.setVisible(True)
            self.label7.setVisible(False)
            self.label8.setVisible(False)
            self.label12.setVisible(True)
            self.label13.setVisible(True)
            self.button2.setVisible(False)
            self.button3.setVisible(False)
            self.button4.setVisible(False)
            
            self.label13.move(dest_coord[var.destination_index][0] + coordinate[0], dest_coord[var.destination_index][1] + coordinate[1])
            capture = cv2.VideoCapture("D:/project/4202_current.mp4") #"D:/project/4202_current.mp4"
            c = 1
            time_F = 60
        
            while(capture.isOpened()):
                ret, frame = capture.read()
                cv2.namedWindow('video',0);
                cv2.resizeWindow('video', 580, 900);
                cv2.imshow('video', frame)
                '''
                # 顯示影片
                ret, frame = capture.read()            
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
                convertToQtFormat = QPixmap.fromImage(convertToQtFormat)
                self.label6.setPixmap(convertToQtFormat)'''
                if c % time_F == 0:
                    check_current_place(frame)
                    map_show()
                    self.label12.move(580 - var.centerx + coordinate[0], var.centery + coordinate[1])
                    '''img = cv2.imread("D:\\project\\ui\\d_" + place[var.destination_index] +".jpg")
                    cv2.circle(img,(var.centerx, var.centery),3,(0,0,0), -1)
                    rgbImage = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], rgbImage.shape[1]*rgbImage.shape[2], QImage.Format_RGB888)
                    convertToQtFormat = QPixmap.fromImage(convertToQtFormat)
                    self.label2.setPixmap(convertToQtFormat)'''
                    
                c = c + frame_correction
                if ret == False:
                    break
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                if var.isreset >= 1:
                    break
                if var.preindex == var.destination_index:
                    pixmap = QPixmap(filename+'departure.png')
                    self.label5.setPixmap(pixmap)
                    self.label5.setVisible(True)
                    cv2.waitKey(1000)
                    self.label5.setVisible(False)
                    break
            capture.release()
            reset()
            cv2.destroyAllWindows()
            if var.isreset == 0: # 正常跑完
                self.label2.setVisible(True)
                self.label3.setVisible(True)
                self.label4.setVisible(True)
                self.label6.setVisible(False)
                self.label12.setVisible(False)
                self.label13.setVisible(False)
                self.button2.setVisible(True)
                self.button3.setVisible(True)
                self.button4.setVisible(True)
        
    def button5Clicked(self): # home
        print('click home')
        self.button5.setStyleSheet('border: 2px solid gray; background:transparent')
        cv2.waitKey(30)
        self.button5.setStyleSheet('border:none; background:transparent')
        var.isreset = 2
        self.label1.setVisible(True)
        self.label2.setVisible(False)
        self.label3.setVisible(False)
        self.label4.setVisible(False)
        #self.label5.setVisible(False)
        self.label6.setVisible(False)
        self.label7.setVisible(False)
        self.label8.setVisible(False)
        self.label9.setVisible(True)
        self.label10.setVisible(True)
        self.label11.setVisible(False)
        self.label12.setVisible(False)
        self.label13.setVisible(False)
        self.button1.setVisible(False)
        self.button2.setVisible(False)
        self.button3.setVisible(False)
        self.button4.setVisible(False)
        self.button5.setVisible(False)
        self.button6.setVisible(True)
        self.button7.setVisible(True)
        self.button8.setVisible(True)
        
    def button6Clicked(self): # get start
        print('click get start')
        reset()
        self.label1.setVisible(False)
        self.label2.setVisible(True)
        self.label3.setVisible(True)
        self.label4.setVisible(True)
        self.label9.setVisible(False)
        self.label10.setVisible(False)
        self.label11.setVisible(False)
        self.button1.setVisible(True)
        self.button2.setVisible(True)
        self.button3.setVisible(True)
        self.button4.setVisible(True)
        self.button5.setVisible(True)
        self.button6.setVisible(False)
        self.button7.setVisible(False)
        self.button8.setVisible(False)
        self.button9.setVisible(False)
    
    def button7Clicked(self): # question
        print('click question')
        self.button7.setStyleSheet('border: 2px solid gray; background:transparent')
        cv2.waitKey(30)
        self.button7.setStyleSheet('border:none; background:transparent')
        self.label11.setVisible(True)
        pixmap = QPixmap(filename+'cover\\intro.png')
        self.label11.setPixmap(pixmap)
        self.label11.resize(pixmap.width(),pixmap.height())
        i = 959
        while i >= 100:
            self.label11.move(123, i)
            i = i-5
            cv2.waitKey(5)
        self.button9.setVisible(True)
            
    def button8Clicked(self): # find
        print('click find')
        self.button8.setStyleSheet('border: 2px solid gray; background:transparent')
        cv2.waitKey(30)
        self.button8.setStyleSheet('border:none; background:transparent')
        self.label11.setVisible(True)
        pixmap = QPixmap(filename+'cover\\sum.png')
        self.label11.setPixmap(pixmap)
        self.label11.resize(pixmap.width(),pixmap.height())
        i = 959
        while i >= 100:
            self.label11.move(123, i)
            i = i-5
            cv2.waitKey(5)
        self.button9.setVisible(True)
        
    def button9Clicked(self): # close introduction
        self.button9.setStyleSheet('border: 2px solid gray; background:transparent')
        cv2.waitKey(30)
        self.button9.setStyleSheet('border:none; background:transparent')
        self.label11.setVisible(False)
        self.button9.setVisible(False)



app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())