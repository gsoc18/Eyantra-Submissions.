# -*- coding: utf-8 -*-
"""
**************************************************************************
*                  E-Yantra Robotics Competition
*                  ================================
*  This software is intended to check version compatiability of open source software
*  Theme: ANT BOT
*  MODULE: Task1.1
*  Filename: Task1.1.py
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

"""
ArUco ID Dictionaries: 4X4 = 4-bit pixel, 4X4_50 = 50 combinations of a 4-bit pixel image
List of Dictionaries in OpenCV's ArUco library:
DICT_4X4_50	 
DICT_4X4_100	 
DICT_4X4_250	 
DICT_4X4_1000	 
DICT_5X5_50	 
DICT_5X5_100	 
DICT_5X5_250	 
DICT_5X5_1000	 
DICT_6X6_50	 
DICT_6X6_100	 
DICT_6X6_250	 
DICT_6X6_1000	 
DICT_7X7_50	 
DICT_7X7_100	 
DICT_7X7_250	 
DICT_7X7_1000	 
DICT_ARUCO_ORIGINAL

Reference: http://hackage.haskell.org/package/opencv-extra-0.2.0.1/docs/OpenCV-Extra-ArUco.html
"""

import numpy
import cv2
import cv2.aruco as aruco
num_pixels = 400
BLUE = [255,255,255]

def aruco_gen(id_aruco, num_pixels):

    #If ID is less than 50, we can generate both images 4X4_50 Combinations and 5X5_250 Combinations.
    #If ID is greater than 50, we cannot generate images with ID greater than 50 for 4X4_50 Dictionary as it does not have enough combinations, so we need to generate only 5X5_250 Dictionary images for ID greater than 50.
    if id_aruco < 50:
        aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
        img1 = aruco.drawMarker(aruco_dict, id_aruco, num_pixels)

        aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_250)
        img3 = aruco.drawMarker(aruco_dict, id_aruco, num_pixels)

        #Following lines Convert the image to RGB Format
        rgbimg1 =  cv2.cvtColor(img1, cv2.COLOR_GRAY2RGB)
        rgbimg3 =  cv2.cvtColor(img3, cv2.COLOR_GRAY2RGB)
        

        #Following lines are used for border of 25 pixel on each side
        rgbimg1 = cv2.copyMakeBorder(rgbimg1,25,25,25,25,cv2.BORDER_CONSTANT,value=BLUE)
        rgbimg3 = cv2.copyMakeBorder(rgbimg3,25,25,25,25,cv2.BORDER_CONSTANT,value=BLUE)
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        text1 = "ArUco ID = " + str(id_aruco)
        text3 = "ArUco ID = " + str(id_aruco)
        

        #Following lines are used to embed Red text on Images
        cv2.putText(rgbimg1, text1, (75, 18), font, 0.5, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.putText(rgbimg3, text3, (75, 18), font, 0.5, (0, 0, 255), 2, cv2.LINE_AA)

        #2 images of 4x4_50 are saved as ArUcoID_1.jpg 
        #2 images of 5x5_250 are saved as ArUcoID_2.jpg
        
        savetext_1_1 = "ArUco" + str(id_aruco) + "_1" + ".jpg"
        savetext_2_1 = "ArUco" + str(id_aruco) + "_2" + ".jpg"
        

        #Save the Images in Directory
        cv2.imwrite(savetext_1_1 ,rgbimg1)
        cv2.imwrite(savetext_2_1 ,rgbimg3)

        #Following code shows the Images
        #cv2.imshow('frame1',rgbimg1)
        #cv2.imshow('frame3',rgbimg3)

        #Following Line Confirms rgbimg1 is RGB Image
        
        #print (rgbimg1.shape)
        #cv2.waitKey(0)
        cv2.imwrite(savetext_2_1 ,rgbimg3)

    # 5X5_250 Dictionary can generate images with ID Greater than 50 upto ID 249 
    elif id_aruco > 50 and id_aruco < 250:

        aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_250)
        img3 = aruco.drawMarker(aruco_dict, id_aruco, num_pixels)

        rgbimg3 =  cv2.cvtColor(img3, cv2.COLOR_GRAY2RGB)

        rgbimg3 = cv2.copyMakeBorder(rgbimg3,25,25,25,25,cv2.BORDER_CONSTANT,value=BLUE)

        font = cv2.FONT_HERSHEY_SIMPLEX

        text3 = "ArUco ID = " + str(id_aruco)

        cv2.putText(rgbimg3, text3, (75, 18), font, 0.5, (0, 0, 255), 2, cv2.LINE_AA)

        savetext_2_1 = "ArUco" + str(id_aruco) + "_2" + ".jpg"

        cv2.imwrite(savetext_2_1 ,rgbimg3)
        
    #If ID is greater than 249, no image can be generated
    elif id_aruco > 249:
         print("Invaild Input")
    
    '''
    code here for saving the Aruco image as a "jpg" by following the steps below:
    1. save the image as a colour RGB image in OpenCV color image format
    2. embed a boundary of 25 pixels on all four sides and three channels of the image
    3. save the image as "ArUcoID.jpg" where ID is the digits of id_aruco i.e. if the ID is 26 the name should be: ArUco26.jpg
    4. APIs which are permitted to be used are:
    a. cvtColor
    b. imwrite
    and other OpenCV APIs.
    5. You are permitted to modify n, C and variables id_aruco and num_pixels
    '''

    #cv2.destroyAllWindows()
    return

if __name__ == "__main__":
    #For Generalized Code, we take the Total IDs as Input and Save 4 Images in the Same directory for Each ID
    test_case = int(input('Enter total number of IDs to be processed.'))

    for i in range(test_case):
        id_aruco = int(input('Enter ID of Image to be generated.'))
        aruco_gen(id_aruco, num_pixels)
      
