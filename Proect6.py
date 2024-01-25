import cv2
import mediapipe as mp

# Инициализируем объект для работы с руками
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Запускаем видеокамеру
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    # Преобразуем изображение в формат RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Обнаруживаем руки на изображении
    results = hands.process(frame_rgb)

    # Если найдены руки, обрабатываем их
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for landmark in hand_landmarks.landmark:
                # Получаем координаты ключевых точек на руке
                x, y = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0])

                # Рисуем точки на изображении
                cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

    # Отображаем результат на экране
    cv2.imshow("Hand Gestures", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождаем ресурсы
cap.release()
cv2.destroyAllWindows()
