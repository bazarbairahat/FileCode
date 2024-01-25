import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Инициализация детектора руки
hands = mp_hands.Hands()

# Инициализация видеопотока с веб-камеры
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    # Конвертация изображения в формат RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Поиск руки и пальцев на кадре
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Отобразить скелет руки и ключевые точки пальцев на изображении
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Извлечь координаты кончиков пальцев
            finger_tips = {
                "thumb": hand_landmarks.landmark[4],
                "index": hand_landmarks.landmark[8],
                "middle": hand_landmarks.landmark[12],
                "ring": hand_landmarks.landmark[16],
                "pinky": hand_landmarks.landmark[20]
            }

            # Распознавание пальцев
            recognized_fingers = []
            for finger, landmark in finger_tips.items():
                if landmark.y < hand_landmarks.landmark[0].y:  # Проверка, что палец находится выше запястья
                    recognized_fingers.append(finger)

            # Вывести результат распознавания
            recognized_fingers_str = ", ".join(recognized_fingers)
            cv2.putText(frame, recognized_fingers_str, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Finger Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
