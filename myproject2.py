
import cv2
import mediapipe as mp
import numpy as np
import time

# 1. Inicializace MediaPipe pro detekci ruky
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

# Styl pro tenké čáry mezi klouby prstů
connection_spec = mp_draw.DrawingSpec(color=(255, 255, 255), thickness=2, circle_radius=2)

# 2. Nastavení webkamery
cap = cv2.VideoCapture(0)

canvas = None
xp, yp = 0, 0
prev_time = 0

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # Zrcadlové otočení obrazu, aby se dobře kreslilo
    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape

    # Vytvoření černého plátna na kreslení
    if canvas is None:
        canvas = np.zeros_like(frame)

    # Převod na RGB pro MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    drawing = False

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            
            # Barevné kuličky na klouby prstů
            for id, lm in enumerate(hand_landmarks.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                
                if id in [1, 2, 3, 4]:        # Palec
                    color = (0, 165, 255)
                elif id in [5, 6, 7, 8]:      # Ukazováček
                    color = (0, 0, 255)
                elif id in [9, 10, 11, 12]:    # Prostředníček
                    color = (0, 255, 0)
                elif id in [13, 14, 15, 16]:   # Prsteníček
                    color = (255, 0, 0)
                else:                         # Malíček
                    color = (255, 0, 255)
                
                cv2.circle(frame, (cx, cy), 6, color, cv2.FILLED)
            
            # Kreslení spojovacích čar ruky
            mp_draw.draw_landmarks(
                frame, 
                hand_landmarks, 
                mp_hands.HAND_CONNECTIONS,
                landmark_drawing_spec=None,
                connection_drawing_spec=connection_spec
            )

            # Pozice špičky ukazováčku (bod 8) a kloubu pod ním (bod 6)
            lm_list = hand_landmarks.landmark
            x1, y1 = int(lm_list[8].x * w), int(lm_list[8].y * h)

            # PODMÍNKA PRO KRESLENÍ: Ukazováček nahoře, prostředníček dole
            if lm_list[8].y < lm_list[6].y and lm_list[12].y > lm_list[10].y:
                drawing = True
                if xp == 0 and yp == 0:
                    xp, yp = x1, y1

                # Kreslení zelené lajny
                cv2.line(canvas, (xp, yp), (x1, y1), (0, 255, 0), 5)
                xp, yp = x1, y1
            else:
                xp, yp = 0, 0

    # Spojení obrazu z kamery a kreslení z plátna
    img_gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, img_inv = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY_INV)
    img_inv = cv2.cvtColor(img_inv, cv2.COLOR_GRAY2BGR)
    frame_bg = cv2.bitwise_and(frame, img_inv)
    combined = cv2.bitwise_or(frame_bg, canvas)

    # FPS info
    cur_time = time.time()
    fps = int(1 / (cur_time - prev_time)) if (cur_time - prev_time) > 0 else 0
    prev_time = cur_time

    cv2.putText(combined, f"FPS: {fps}", (10, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 0), 3)

    if drawing:
        cv2.putText(combined, "Kresleni...", (10, 100), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

    cv2.namedWindow("Kresleni Ukazovackem", cv2.WINDOW_NORMAL)
    cv2.imshow("Kresleni Ukazovackem", combined)

    if cv2.waitKey(1) & 0xFF == 27:  # Esc ukončí program
        break

cap.release()
cv2.destroyAllWindows()