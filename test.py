#01、环境搭建与检测

import cv2 as cv
import numpy as np

print("--------------Hi,python--------------")

src = cv.imread("D:/Python_instance/pythonface/6.jpg")
#打开一个窗口
#cv2.namedWindow(<窗口名>,x)
#x=cv2.WINDOW_AUTOSIZE-----默认大小，不能改动
#x=cv2.WINDOW_NORMAL
#或cv2.WINDOW_FREERATIO-----可以改动窗口大小
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
# 简而言之如果有正数x输入则 等待x ms，如果在此期间有按键按下，则立即结束并返回按下按键的ASCII码，否则返回-1
# 如果x=0，那么无限等待下去，直到有按键按下
cv.waitKey(0)
cv.destroyAllWindows()
