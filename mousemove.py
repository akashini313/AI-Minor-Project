import numpy as np
import cv2
a=np.ones([300,300,3],dtype='uint8')*255
wname='Shapes'
cv2.namedWindow(wname)
def shape(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(a,(x,y),(x+10,y+10),(0,0,0),-5)
    if event==cv2.EVENT_MOUSEMOVE:
        cv2.rectangle(a,(x,y),(x+10,y+10),(0,0,0),-5)
cv2.setMouseCallback(wname,shape)

while True:
    cv2.imshow(wname,a)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
    elif key==ord('c'):
        a[:,:]=255
cv2.destroyAllWindows()
