import pywhatkit as kit
import cv2

Handwritten = input("Enter your text to convert into handwritting:")
kit.text_to_handwriting(Handwritten,save_to="pythoncoding.png")
img=cv2.imread("pythoncoding.png")
cv2.imshow("Python coding",img)
cv2.waitkey(0)
cv2.destrouAllWindows()
