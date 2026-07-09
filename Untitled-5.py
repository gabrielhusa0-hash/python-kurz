import cv2
import numpy as np

# Načtení zabudovaného policejního detektoru obličeje, který ti funguje
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

kamera = cv2.VideoCapture(0)

print("SKENER PRSTŮ BĚŽÍ! Ukončíš ho klávesou 'q'.")

while True:
    uspech, snimek = kamera.read()
    if not uspech:
        break

    snimek = cv2.flip(snimek, 1)
    vyska, sirka, _ = snimek.shape
    sedy = cv2.cvtColor(snimek, cv2.COLOR_BGR2GRAY)

    # 1. DETEKCE OBLIČEJE (Ať ti zůstane to, co ti fungovalo)
    obliceje = face_cascade.detectMultiScale(sedy, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))
    for (x, y, w, h) in obliceje:
        cv2.rectangle(snimek, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(snimek, "TARGET ACQUIRED", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # 2. CHYTRÁ DETEKCE PRSTŮ POMOCÍ KONTUR (Nepotřebuje MediaPipe!)
    # Převedeme obraz na černobílý podle kůže, abychom našli ruku
    blur = cv2.GaussianBlur(sedy, (35, 35), 0)
    _, threshed = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    kontury, _ = cv2.findContours(threshed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(kontury) > 0:
        # Najdeme největší objekt v záběru (předpokládáme, že je to ruka)
        nejvetsi_kontura = max(kontury, key=cv2.contourArea)
        
        # Najdeme špičky prstů (nejvzdálenější body)
        hull = cv2.convexHull(nejvetsi_kontura, returnPoints=False)
        if len(hull) > 4:
            defekty = cv2.convexityDefects(nejvetsi_kontura, hull)
            
            if defekty is not None:
                body_prstu = []
                for i in range(defekty.shape[0]):
                    s, e, f, d = defekty[i, 0]
                    start = tuple(nejvetsi_kontura[s][0])
                    end = tuple(nejvetsi_kontura[e][0])
                    far = tuple(nejvetsi_kontura[f][0])
                    
                    # Filtrujeme body, které vypadají jako špičky prstů
                    if d > 10000:
                        body_prstu.append(start)

                # Seřadíme body zleva doprava, abychom věděli, který prst je který
                body_prstu = sorted(list(set(body_prstu)), key=lambda x: x[0])
                
                nazvy_prstu = ["Palec", "Ukazovacek", "Prostrednik", "Prstenicek", "Malicek"]
                
                # Opatříme každý nalezený bod prstu správným názvem
                for idx, bod in enumerate(body_prstu[:5]):
                    if idx < len(nazvy_prstu):
                        # Vykreslíme barevný puntík na prst
                        cv2.circle(snimek, bod, 8, (0, 0, 255), cv2.FILLED)
                        # Vykreslíme název prstu v češtině
                        cv2.putText(snimek, nazvy_prstu[idx], (bod[0] - 20, bod[1] - 20),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

    cv2.imshow("Skener prstu", snimek)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

kamera.release()
cv2.destroyAllWindows()