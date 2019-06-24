#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import cv2
import cv2.aruco as aruco
import aruco_lib as f1

#path_to_image = 'C:\Users\New\Desktop\Task1.2\2. Code'

# cd Desktop\Task1.2\2. Code

def aruco_detect(path_to_image):
    '''
    you will need to modify the ArUco library's API using the dictionary in it to the respective
    one from the list above in the aruco_lib.py. This API's line is the only line of code you are
    allowed to modify in aruco_lib.py!!!
    '''

    img = cv2.imread(path_to_image)  # give the name of the image with the complete path
    id_aruco_trace = 0
    det_aruco_list = {}
    
    
    img2 = img[0:450, 0:450, :]  # separate out the Aruco image from the whole image
    
    det_aruco_list = f1.detect_Aruco(img2)
    if det_aruco_list:
        img3 = f1.mark_Aruco(img2, det_aruco_list)
        id_aruco_trace = f1.calculate_Robot_State(img3, det_aruco_list)
        print (id_aruco_trace)
        cv2.imshow('image', img2)
        cv2.waitKey(0)
    cv2.destroyAllWindows()


def color_detect(img):
    result_image = cv2.imread(img)
    cv2.imshow('ColorImage', result_image)
    cv2.waitKey(0)


if __name__ == '__main__':
    aruco_detect("Image5.jpg")
    #color_detect("ArUco217.jpg")
