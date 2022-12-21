# pip install streamlit==1.13.0
# streamlit run uygulama.py   (pycharm terminalde) streamlit 1.13.0

import streamlit as st
import cv2

st.title("Webcam Streamlit Canlı Yüz Tanıma Uygulaması")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

face_detector = cv2.CascadeClassifier('haarcascades\haarcascade_frontalface_default.xml')

while run:
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    # Bulunan yüzler işaretlenir.
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    FRAME_WINDOW.image(frame)
else:
    st.write('Stopped')
