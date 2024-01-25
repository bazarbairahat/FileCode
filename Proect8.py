import cv2
import mediapipe as mp

# Инициализируем объект для обнаружения пальцев
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Создаем объект для захвата видеопотока с камеры
cap = cv2.VideoCapture(0)

while True:
    # Захватываем кадр с камеры
    ret, frame = cap.read()

    if not ret:
        break

    # Преобразуем изображение в формат RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Обнаруживаем пальцы на изображении
    results = hands.process(frame_rgb)

    # Инициализируем счетчики пальцев
    num_fingers = 0

    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            for i, landmark in enumerate(landmarks.landmark):
                if i in [4, 8, 12, 16, 20]:
                    # Проверяем, находится ли палец ниже некоторого порога (например, по высоте экрана)
                    if landmark.y * frame.shape[0] > 0.7:
                        num_fingers += 1

    # Отображение зеленого или красного цвета в зависимости от количества пальцев
    if num_fingers == 5:
        color = (0, 255, 0)  # Зеленый цвет
    elif num_fingers == 10:
        color = (0, 0, 255)  # Красный цвет
    else:
        color = (0, 0, 0)    # Черный цвет

    # Отображаем цвет на экране
    cv2.rectangle(frame, (0, 0), (frame.shape[1], frame.shape[0]), color, -1)

    # Отображаем кадр с жестом
    cv2.imshow('Gesture Visualization', frame)

    # Выход из программы при нажатии клавиши 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождаем ресурсы и закрываем окна
cap.release()
cv2.destroyAllWindows()
