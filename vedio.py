import cv2
# تم استدعاء مكتبه cv2
# Load the cascade
#  cascade تم تحميل 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# هذا الامر لالتقاط ابعاد الوجه في الفيديو 
cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')
# هنا تم وضع شرط للتحقق
while True:
    # Read the frame
    _, img = cap.read()
   # للقراءة
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # امر لالتقاط ابعاد الوجه في الفيديو 
    # Draw the rectangle around each face

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display
    cv2.imshow('img', img)
    # عرص الصوره الملتقطه من الفيديو
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
        
# Release the VideoCapture object
cap.release()