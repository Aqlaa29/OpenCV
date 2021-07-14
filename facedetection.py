import cv2
#قمنا با استدعاء مكتبة cv2  

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read the input image
img = cv2.imread('face.jpg')
#استخدمت صوره لرجل من الموقع مفتوح المصدر unsplash

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# التعرف على الوجه 
# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
#هنا حددنا متغيرات لنتمكن من التقاط صوره كامله للتعرف على الوجه
# Display the output
cv2.imshow('img', img)
cv2.waitKey()
#تم قراءة الصوره والتعرف عليها 