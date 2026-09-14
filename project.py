import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np

# Inicializace kamery a detektoru ruky (stačí 1 ruka)
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)

canvas = None
xp, yp = 0, 0

print("Spouštím KRESLENÍ PRSTEM... Pro ukončení stiskni 'q'.")

while cap.isOpened():
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    h, w, c = img.shape
    if canvas is None:
        canvas = np.zeros((h, w, 3), dtype=np.uint8)

    # Detekce ruky a jejích bodů
    hands, img = detector.findHands(img, draw=True) # draw=True vykreslí kostru ruky jako na videu

    if hands:
        hand = hands[0]
        lmList = hand["lmList"] 
        
        # Bod 8 je špička ukazováčku
        x8, y8 = lmList[8][0], lmList[8][1]

        # Zjistím, které prsty jsou nahoře (vrátí pole např. [0, 1, 0, 0, 0] pro ukazováček)
        fingers = detector.fingersUp(hand)

        # REŽIM KRESLENÍ: Pouze ukazováček je nahoře (index 1 v poli fingers)
        if fingers[1] == 1 and fingers[2] == 0:
            cv2.circle(img, (x8, y8), 10, (0, 255, 0), cv2.FILLED)
            if xp == 0 and yp == 0:
                xp, yp = x8, y8
            
            # Kreslíme čáru
            cv2.line(canvas, (xp, yp), (x8, y8), (0, 255, 0), 5)
            xp, yp = x8, y8
            
        # REŽIM MAZÁNÍ: Ukazováček i prostředníček jsou nahoře
        elif fingers[1] == 1 and fingers[2] == 1:
            cv2.circle(img, (x8, y8), 25, (0, 0, 255), cv2.FILLED)
            if xp == 0 and yp == 0:
                xp, yp = x8, y8
            
            # Mažeme (kreslíme černou)
            cv2.line(canvas, (xp, yp), (x8, y8), (0, 0, 0), 50)
            xp, yp = x8, y8
        else:
            xp, yp = 0, 0
    else:
        xp, yp = 0, 0

    # Spojení obrazu kamery a kreslení
    img_gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, img_inv = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY_INV)
    img_inv = cv2.cvtColor(img_inv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, img_inv)
    combined = cv2.bitwise_or(img, canvas)

    # Malinký decentní nápis v rohu, žádná obří grafika přes půl obrazovky
    cv2.putText(combined, "Kresleni prstem", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
    cv2.imshow("Finger Drawing", combined)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()