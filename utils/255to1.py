import os 
import cv2 

path =r'E:\segnet_unet\segnet\data\dataset\gtFinet'
path_out = r'E:\segnet_unet\segnet\data\dataset\gtFine'

for i in os.listdir(path):
    tt = cv2.imread(path+'/'+i)
    t = tt[:,:,1]
    t[t == 255] = 1
    cv2.imwrite(path_out+'/'+i,t)
