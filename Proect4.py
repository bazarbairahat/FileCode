import cv2

# Инициализируем каскадный классификатор для детекции лиц
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Инициализируем видеопоток с помощью OpenCV (здесь можно указать номер вашей веб-камеры)
cap = cv2.VideoCapture(0)

while True:
    # Захватываем кадр с видеопотока
    ret, frame = cap.read()

    # Преобразовываем кадр в черно-белый для детекции лиц
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Детектируем лица на кадре
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Отображаем прямоугольники вокруг обнаруженных лиц
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Отображаем кадр с лицами и жестами
    cv2.imshow('Face Detection', frame)

    # Прерываем цикл, если пользователь нажимает клавишу 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождаем ресурсы и закрываем окна OpenCV
cap.release()
cv2.destroyAllWindows()
