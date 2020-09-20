import numpy as np
import cv2 
img = cv2.imread("D:\\florrie\Project\\all\\building_map.jpg")
'''
def draw_rec(event,x,y,flags,param):
    global x1,y1
    if event == cv2.EVENT_LBUTTONDOWN:
        x1, y1 = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        cv2.rectangle(img,(x1,y1),(x,y),(0,255,255),0)
        cv2.imwrite("D:\\florrie\Project\\all\\building_map.jpg",img)
        print((x1,y1),(x,y))
    
    cv2.imshow('image',img)
'''
def draw_spot(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),2,( 0,0,255),-1)
        cv2.imwrite("D:\\florrie\Project\\all\\route.jpg",img)
        print(x,y)
    cv2.imshow('image',img)
def main():
    global count
    count = 0
    cv2.imshow('image',img)
    cv2.setMouseCallback('image',draw_spot)

    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()