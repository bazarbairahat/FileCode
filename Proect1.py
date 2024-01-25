import cv2
import mediapipe as mp

# Инициализация объекта MediaPipe для распознавания рук
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Инициализация объекта MediaPipe для отображения результатов
mp_drawing = mp.solutions.drawing_utils

# Инициализация видеопотока с камеры (0 - индекс камеры)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # Считывание кадра с камеры
    ret, frame = cap.read()
    if not ret:
        continue

    # Конвертация кадра в цветовое пространство BGR в RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Обработка кадра с помощью MediaPipe
    results = hands.process(rgb_frame)

    # Если руки обнаружены
    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            # Отображение ключевых точек на руках
            mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

    # Отображение кадра с результатами
    cv2.imshow('Hand Tracking', frame)

    # Выход из цикла по нажатию клавиши 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождение ресурсов
cap.release()
cv2.destroyAllWindows()
