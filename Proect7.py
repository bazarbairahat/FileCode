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
            # Проверяем, поднята ли ладонь (вы можете настроить условия для других жестов)
            if hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y < hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y:
                # Рисуем квадрат на экране
                cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), -1)

    # Отображаем результат на экране
    cv2.imshow("Hand Gestures", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождаем ресурсы
cap.release()
cv2.destroyAllWindows()
