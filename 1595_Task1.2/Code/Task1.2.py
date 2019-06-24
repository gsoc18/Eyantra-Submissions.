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
import csv
#path_to_image = 'C:\Users\New\Desktop\Task1.2\2. Code'

# cd Desktop\Task1.2\2. Code

def aruco_detect(path_to_image):
    '''
    you will need to modify the ArUco library's API using the dictionary in it to the respective
    one from the list above in the aruco_lib.py. This API's line is the only line of code you are
    allowed to modify in aruco_lib.py!!!
    '''
    print ("Note that name of the shapes and color must be lower case and if NO object is to be selected then enter 0")
    s1 = input("Shape 1 : ")
    c1 = input("Color 1 : ")
    s2 = input("Shape 2 : ")
    c2 = input("Color 2 : ")
    color_detect(path_to_image,s1,c1,s2,c2)



def detectShape(cnt):
    shape = 'unknown'
    # calculate perimeter using
    c=cnt
    peri = cv2.arcLength(c, True)
    # apply contour approximation and store the result in vertices
    vertices = cv2.approxPolyDP(c, 0.04 * peri, True)

    # If the shape it triangle, it will have 3 vertices
    if len(vertices) == 3:
        shape = 'triangle'

    # if the shape has 4 vertices, it is either a square or
    # a rectangle
    elif len(vertices) == 4:
        # using the boundingRect method calculate the width and height
        # of enclosing rectange and then calculte aspect ratio

        x, y, width, height = cv2.boundingRect(vertices)
        aspectRatio = float(width) / height

        # a square will have an aspect ratio that is approximately
        # equal to one, otherwise, the shape is a rectangle
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
            shape = "square"
        else:
            shape = "rectangle"

    # if the shape is a pentagon, it will have 5 vertices
    elif len(vertices) == 5:
        shape = "pentagon"

    # otherwise, we assume the shape is a circle
    else:
        shape = "circle"

    # return the name of the shape
    return shape


def color_detect(timg,s1,c1,s2,c2):
    '''
    code for color Image processing to detect the color and shape of the 2 objects at max.
    mentioned in the Task_Description document. Save the resulting images with the shape
    and color detected highlighted by boundary mentioned in the Task_Description document.
    The resulting image should be saved as a jpg. The boundary should be of 25 pixels wide.
    '''
    image = cv2.imread(timg)
    #cv2.imshow("Original", image)

    # convert the color image into grayscale
    grayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Find edges in the image using canny edge detection method
    # Calculate lower threshold and upper threshold using sigma = 0.33
    sigma = 0.33
    v = np.median(grayScale)
    low = int(max(0, (1.0 - sigma) * v))
    high = int(min(255, (1.0 + sigma) * v))

    edged = cv2.Canny(grayScale, low, high)

    # After finding edges we have to find contours
    # Contour is a curve of points with no gaps in the curve
    # It will help us to find location of shapes

    # cv2.RETR_EXTERNAL is passed to find the outermost contours (because we want to outline the shapes)
    # cv2.CHAIN_APPROX_SIMPLE is removing redundant points along a line
    (_, cnts, _) = cv2.findContours(edged,
                                    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    '''
    We are going to use contour approximation method to find vertices of
    geometric shapes. The alogrithm  is also known as Ramer Douglas Peucker alogrithm.
    In OpenCV it is implemented in cv2.approxPolyDP method.abs

    detectShape() function below takes a contour as parameter and
    then returns its shape
     '''




    # Now we will loop over every contour
    # call detectShape() for it and
    # write the name of shape in the center of image

    # loop over the contours
    

    centroid=['','']
    i=0
    for c in cnts:
        # compute the moment of contour
        M = cv2.moments(c)
        # From moment we can calculte area, centroid etc
        # The center or centroid can be calculated as follows

        cX = int(M['m10'] / M['m00'])
        cY = int(M['m01'] / M['m00'])

        s='('+str(cX)+','+str(cY)+')'
        #print(s)
        # call detectShape for contour c
        shape=detectShape(c)

        # Outline the contor
        #color = int(image[cX,cY])
        b,g,r=cv2.split(image)
       
        
        # SINCE THE SHAPES ARE SINGLE COLORED, WE WILL USE THE RGB OF SINGLE POINT --> CENTROID TO DETECT THE COLOR     #------------------------------------------------------------------------------------------------------------------------------
        #	  THESE ARE THE CO-ORDINATES OF GTHE CENTROIDS AND THEIR CORRESPONDING RGB VALUES

        #		(787,563)
        #		49 125 237
        #		[ 49 125 237]
        #		(235,571)
        #		0 183 55
        #		[  0 183  55]
        #		(1091,221)
        #		0 0 254
        #		[  0   0 254]
        #		(648,242)
        #		199 114 68
        #		[199 114  68]
        #		(197,197)
        #		240 240 240
        #		[240 240 240]
        #---------------------------------------------------------------------------------------------------------------------------


        temp=(255,255,255)
        if(shape == s1 or shape == s2):
            if (b[cY][cX]==199 and g[cY][cX]==114 and r[cY][cX]==68) and (c1 == "blue" or c2=="blue"):
                temp=(0,0,255)		# Assigning red contour for blue shape
                cv2.drawContours(image, [c], -1, temp, 25)
                cv2.putText(image, s,(cX, cY), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
                centroid[i]="(" + s + ")"
                i = i + 1
                #print (s)
            if b[cY][cX]==0 and g[cY][cX]==183 and r[cY][cX]==55 and (c1 == "green" or c2=="green"):
                temp=(255,0,0)		# Assigning blue contour for green shape
                cv2.drawContours(image, [c], -1, temp, 25)
                cv2.putText(image, s,(cX, cY), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
                centroid[i]="(" + s + ")"
                i = i + 1
                #print (s)
            if b[cY][cX]==0 and g[cY][cX]==0 and r[cY][cX]==254 and (c1 == "red" or c2=="red"):
                temp=(0,255,0)		# Assigning green contour for red shape
                cv2.drawContours(image, [c], -1, temp, 25)
                cv2.putText(image, s,(cX, cY), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
                centroid[i]="(" + s + ")"
                
                
                i = i + 1
                #print (s)           
           
            # Write the name of shape on the center of shapes
        
    
    img2 = image[0:1280, 0:1280, :]  # separate out the Aruco image from the whole image
    
    det_aruco_list = f1.detect_Aruco(img2)
   
    #print (det_aruco_list)
   
    key = str(det_aruco_list.keys())
    #print (key[len(key) - 3])
    #print (type(det_aruco_list))
    if det_aruco_list:
        img3 = f1.mark_Aruco(img2, det_aruco_list)
        id_aruco_trace = f1.calculate_Robot_State(img3, det_aruco_list)
        #print (id_aruco_trace)
        # show the output image
    #Instead of timg we can pass ArUco1.jpg,ArUco2.jpg   
    row = [ timg,key[len(key) - 3],centroid[0],centroid[1]]
    
    with open('1595_Task1.2.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)

    csvFile.close()

     
    #cv2.imshow("Image", image)
    #Specify the file name to Write
    cv2.imwrite("ArUco5.jpg",image)
       

    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    
 

if __name__ == '__main__':
    #For Generalized Code, we take the Total Images as Input and Save 4 Images in the Same directory for Each Image
    test_case = int(input('Enter total number of Images to be processed.'))

    for i in range(test_case):
        image_name = input("Type Image name and Format")
        aruco_detect(image_name)
    #img = cv2.imread("Image1.jpg")
    #Change Dictionary in aruco_lib for particular images
    # load the image on disk and then display it
    
