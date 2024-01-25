import cv2
import mediapipe as mp
import numpy as np

# Инициализируем MediaPipe Face Detection и Hands Detection
mp_face_detection = mp.solutions.face_detection
mp_hands = mp.solutions.hands

# Инициализируем детекторы лиц и жестов рук
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)
hands_detection = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Открываем веб-камеру
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    # Конвертируем кадр в формат RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Обнаружение лиц
    results = face_detection.process(frame_rgb)
    if results.detections:
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = frame.shape
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
            cv2.rectangle(frame, bbox, (0, 255, 0), 2)

    # Обнаружение жестов рук
    frame_rgb_hands = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
    results_hands = hands_detection.process(frame_rgb_hands)

    if results_hands.multi_hand_landmarks:
        for landmarks in results_hands.multi_hand_landmarks:
            for point in landmarks.landmark:
                x, y = int(point.x * frame.shape[1]), int(point.y * frame.shape[0])
                cv2.circle(frame, (x, y), 5, (255, 0, 0), -1)

    # Отображаем результат
    cv2.imshow('Face and Hands Recognition', frame)

    # Для выхода нажмите 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождаем ресурсы
cap.release()
cv2.destroyAllWindows()
