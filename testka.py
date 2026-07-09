import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector

# 1. NASTAVENÍ KAMERY
kamera = cv2.VideoCapture(0)

# 2. DETEKTOR OBLIČEJE (Zelený zaměřovač)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 3. DETEKTOR RUKOU (Zrychlené nastavení přímo pro tvůj PC, fialový box vypnutý)
detektor_rukou = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)

print("SKENER BEZI! Barevne body na koneccich prstu aktivni. Ukoncis klavesou 'q'.")

while True:
    uspech, snimek = kamera.read()
    if not uspech:
        break

    # Otočení obrazu jako v zrcadle
    snimek = cv2.flip(snimek, 1)

    # 4. DETEKCE RUKOU (draw=False schová ten velký fialový čtverec a čáry)
    ruce, _ = detektor_rukou.findHands(snimek, draw=False)

    if ruce:
        ruka1 = ruce[0]
        lmList = ruka1["lmList"] 

        if lmList:
            # Souřadnice pro konečky prstů (X a Y pozice)
            # OpenCV používá barvy v pořadí BGR (Modrá, Zelená, Červená)

            # PALEC (Bod 4) -> MODRÁ
            x4, y4 = lmList[4][0], lmList[4][1]
            cv2.circle(snimek, (x4, y4), 15, (255, 0, 0), cv2.FILLED)

            # UKAZOVÁČEK (Bod 8) -> ZELENÁ
            x8, y8 = lmList[8][0], lmList[8][1]
            cv2.circle(snimek, (x8, y8), 15, (0, 255, 0), cv2.FILLED)

            # PROSTŘEDNÍČEK (Bod 12) -> ČERVENÁ
            x12, y12 = lmList[12][0], lmList[12][1]
            cv2.circle(snimek, (x12, y12), 15, (0, 0, 255), cv2.FILLED)

            # PRSTENÍČEK (Bod 16) -> ORANŽOVÁ
            x16, y16 = lmList[16][0], lmList[16][1]
            cv2.circle(snimek, (x16, y16), 15, (0, 128, 255), cv2.FILLED)

            # MALÍČEK (Bod 20) -> FIALOVÁ
            x20, y20 = lmList[20][0], lmList[20][1]
            cv2.circle(snimek, (x20, y20), 15, (255, 0, 128), cv2.FILLED)

    # 5. DETEKCE OBLIČEJE (Zelený zaměřovač)
    sedy = cv2.cvtColor(snimek, cv2.COLOR_BGR2GRAY)
    obliceje = face_cascade.detectMultiScale(sedy, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))
    for (x, y, w, h) in obliceje:
        cv2.rectangle(snimek, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(snimek, "TARGET ACQUIRED", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv2.line(snimek, (x + w//2 - 15, y + h//2), (x + w//2 + 15, y + h//2), (0, 255, 0), 2)
        cv2.line(snimek, (x + w//2, y + h//2 - 15), (x + w//2, y + h//2 + 15), (0, 255, 0), 2)

    # ZOBRAZENÍ OKNA
    cv2.imshow("Policejni a Kloubovy Scanner", snimek)

    # Vypnutí pomocí klávesy 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

kamera.release()
cv2.destroyAllWindows()
print("Skener vypnut.")
