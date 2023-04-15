import cv2
from cvzone.FaceDetectionModule import FaceDetector

cap = cv2.VideoCapture(0)

detector = FaceDetector(minDetectionCon=0.75)

while True:
        # capture image
        success, img = cap.read()
        img, bboxs = detector.findFaces(img,draw=True)

        if bboxs:
                for i,bbox in enumerate(bboxs):
                        x,y,w,h = bbox['bbox']
                        if x < 0: x = 0
                        if y < 0: y = 0

                        imgCrop = img[y:y+h,x:x+w]
                        imgBlur = cv2.blur(imgCrop,(35,35))
                        img[y:y + h, x:x + w] = imgBlur
                        # cv2.imshow(f'kesilen resim {i}',imgCrop)

        # display and wait 1ms
        cv2.imshow('webcam', img)
        cv2.waitKey(1)