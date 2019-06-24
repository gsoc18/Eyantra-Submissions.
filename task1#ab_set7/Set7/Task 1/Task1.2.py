#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
**************************************************************************
*                  E-Yantra Robotics Competition
*                  ================================
*  This software is intended to check version compatiability of open source software
*  Theme: ANT BOT
*  MODULE: Task1.2
*  Filename: Task1.2.py
*  Version: 1.0.0  
*  Date: October 31, 2018
*  
*  Author: e-Yantra Project, Department of Computer Science
*  and Engineering, Indian Institute of Technology Bombay.
*  
*  Software released under Creative Commons CC BY-NC-SA
*
*  For legal information refer to:
*        http://creativecommons.org/licenses/by-nc-sa/4.0/legalcode 
*     
*
*  This software is made available on an “AS IS WHERE IS BASIS”. 
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD project under National Mission on Education using 
*  ICT(NMEICT)
*
**************************************************************************
"""

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
    '''
    code for color Image processing to detect the color and shape of the 2 objects at max.
    mentioned in the Task_Description document. Save the resulting images with the shape
    and color detected highlighted by boundary mentioned in the Task_Description document.
    The resulting image should be saved as a jpg. The boundary should be of 25 pixels wide.
    '''

    result_image = cv2.imread(img)

    ''''lower = np.array([0, 0, 0])
    upper = np.array([15, 15, 15])
    shapeMask = cv2.inRange(image, lower, upper)
    cv2.imshow('ColorImage', shapeMask)
    ''''
    cv2.imshow('ColorImage', result_image)
   
    cv2.waitKey(0)


if __name__ == '__main__':
    #aruco_detect("ArUco7.jpg")
    color_detect("Image1.jpg")
