import cv2
import mediapipe as mp
import time

# Initialize mediapipe hand solution
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=2,
                       min_detection_confidence=0.5,
                       min_tracking_confidence=0.5)

# Start webcam
cap = cv2.VideoCapture(0)

# FPS calculation
p_time = 0

# Finger tip landmark indices in Mediapipe
finger_tips = [4, 8, 12, 16, 20]

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            h, w, _ = frame.shape
            landmarks = [(int(lm.x * w), int(lm.y * h)) for lm in hand_landmarks.landmark]

            fingers_status = []

            # Thumb check (different axis depending on left/right)
            if landmarks[finger_tips[0]][0] < landmarks[finger_tips[0] - 1][0]:
                fingers_status.append("Thumb: Open")
            else:
                fingers_status.append("Thumb: Closed")

            # Other 4 fingers
            for tip in finger_tips[1:]:
                if landmarks[tip][1] < landmarks[tip - 2][1]:
                    fingers_status.append(f"Finger {tip}: Open")
                else:
                    fingers_status.append(f"Finger {tip}: Closed")

            # Display finger status on frame
            y0 = 80
            for i, text in enumerate(fingers_status):
                cv2.putText(frame, text, (10, y0 + i*30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

    # Calculate FPS
    c_time = time.time()
    fps = 1 / (c_time - p_time) if (c_time - p_time) > 0 else 0
    p_time = c_time

    cv2.putText(frame, f'FPS: {int(fps)}', (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Hand Recognition + Fingers", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()
