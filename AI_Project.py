import cv2
from ultralytics import YOLO

# 1. Načtení AI modelu
model = YOLO("yolov8n.pt")

# 2: Spouštení webkamery (pokud bynešla, změní se 0 na 1)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("CHYBA: Nepodařilo se spustit webkameru. ")
    exit()

print("ÚSPĚCH: Multi-tagret PiP Skener aktivován!")

window_name = "Panopticore AI - Tactical HUD"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# 3. Hlavní smačka programu
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    vyska, sirka, _ = frame.shape
    stred_x, stred_y = sirka // 2, vyska // 2

    # Spouštení AI detekce
    results = model(frame, verbose=False)

    found_persons = []
    found_vehicles = []

    # Procházení detekovaných objektů a jejich roztřidění
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            label = model.names[class_id]
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # Nakreslím základní zelený box do hlavního obrazu pro všechno
            zelena = (0, 255, 0)
        cv2.rectangle(frame, (x1, y1), (x2, y2), zelena, 2)
        cv2.putText(frame, label.upper(), (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, zelena, 1)  

        # Uložím si cíle pro detailní výřezy
        if label == "person":
            found_persons.append((x1, y1, x2, y2))
        elif label in ["car", "motorcycle", "bus", "truck"]:
                found_vehicles.append((x1, y1, x2, y2))

    # VELIKOST A NASTAVENÍ MINI- OKEN (ČTVERCŮ)
    pip_w, pip_h = 250, 180 # Šířka a výška těch malých čtverců s detailem
 
    # 4. ČTVEREC PRO ČLOVĚKA (Vlevo nahoře)
    if found_persons:
        px1, py1, px2, py2 = found_persons[0] # Vezmeme prvního člověka
        # Uděláme výřez z originálního obrazu
    crop_p = frame[max(0, py1-20):min(vyska, py2+20), max(0, px1-20):min(sirka, px2+20)]
    if crop_p.size > 0:
        # Roztáhnu výřez na velikosti mini-okna
        pip_person = cv2.resize(crop_p, (pip_w, pip_h))
        # Vlepím ho do hlavního obrazu (pozice: odshora 50px, zleva 20px)
        frame[50:50+pip_h, 20:20+pip_w] = pip_person
        # Červený rámeček kolem mini-okna a popisek
        cv2.rectangle(frame, (20, 50), (20+pip_w, 50+pip_h), (0, 0, 255), 2)
        cv2.putText(frame, "TARGER ZOOM: PERSON", (20,45), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

    # 5. ČTVEREC PRO AUTO (Vpravo nahoře)
    if found_vehicles:
         ax1, ay1, ax2, ay2 = found_vehicles[0] # Vezmu první auto
         crop_a = frame[max(0, ay1-20):min(vyska, ay2+20), max(0, ax1-20):min(sirka, ax2+20)]
         if crop_a.size > 0:
              pip_auto = cv2.resize(crop_a, (pip_w, pip_h))
              # Vlepím ho na pravou stranu (pozice: odshora 50px, zprava sirka-pip_w-20)
              start_x = sirka - pip_w - 20
              frame[50:50+pip_h, start_x:start_x+pip_w] = pip_auto
              # Modrý/Červený rámeček pro auto
              cv2.rectangle(frame, (start_x, 50), (start_x+pip_w, 50+pip_h), (255, 0, 0), 2)
              cv2.putText(frame, "TARGET ZOOM: VEHICLE", (start_x, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

    # Horní stavová lišta HUD
    cv2.putText(frame, "PANOPTICORE MULTI-SCANNER // EXPERIMENTAL SENSOR SUITE // SYSTEM ACTIVE", (20, 25), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)

    # Zaměřovací kříž/kruh uprostřed hlavní obrazovky
    cv2.circle(frame, (stred_x, stred_y), 40, (0, 255, 0), 1)
    cv2.line(frame, (stred_x - 10, stred_y), (stred_x + 10, stred_y), (0, 255, 0), 1)
    cv2.line(frame, (stred_x, stred_y - 10), (stred_x, stred_y + 10), (0, 255, 0), 1)

    # Zobrazení okna
    cv2.imshow(window_name, frame)

   # Vypnutí klávesou 'q' nebo 'Esc' (pauza 30ms pro plynulost a stabilitu)
    klavesa = cv2.waitKey(30) & 0xFF
    if klavesa == ord('q') or klavesa == 27:
        break

cap.release()
cv2.destroyAllWindows()
print("AI Scanner vypnut.") 

