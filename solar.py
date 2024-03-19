import cv2
img = cv2.imread("C:/Users/lenovo/OneDrive/Desktop/New folder/solar system.jpg")
cv2.putText(img,"SUN",(15,210),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
cv2.putText(img,"mercury",(125,210),cv2.FONT_HERSHEY_COMPLEX,0.2,(255,255,255),1)
cv2.putText(img,"Venus",(175,210),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255),1)
cv2.putText(img,"Earth",(215,210),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255),1)
cv2.putText(img,"Marsh",(265,210),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255),1)
cv2.putText(img,"Jupiter",(320,210),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
cv2.putText(img,"Saturn",(395,210),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
cv2.putText(img,"uranus",(470,210),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255),1)
cv2.putText(img,"Neptune",(530,210),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255),1)

cv2.imshow("test",img)
cv2.waitKey(0)