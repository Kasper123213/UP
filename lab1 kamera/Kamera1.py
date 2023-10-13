import cv2
import time

# otwarcie kamery, arrgument 0 oznacza domyślną kamere systemu
# na zajęciach domyślną kamerą była kamera podłączona przez USB
cap = cv2.VideoCapture(0)

photoIndex = 1
videoIndex = 1
makeGray = False
recordingOn = False

# zdefiniowanie kodeka do kompresji i przechwycenia obrazu video zapisanego  formacie .avi
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# pętla główna programu
while True:
    # Przechwytujemy obraz z kamery do zmiennej frame, zmienna ret zawiera True jeśli obraz został przechwycony poprawnie
    ret, frame = cap.read()

    # Jeśli nie można obsłużyć kamery, wychodzimy z pętli
    if not ret:
        break

    # w ppyrzypadku naciśnięcia 'q' zamykamy program,
    # argument '1' w funkcji waitKey oznacza czas w milisekundach, jaki funkcja będzie czekała na wciśnięcie przycisku
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Koniec Programu")
        break

    # w pyrzypadku naciśnięcia 'c' wyświetlany obraz zostaje wyświetlany w odcieniach szarości,
    # jest również opcja zapisania takiego obrazu klawiszem 'p'
    if cv2.waitKey(1) & 0xFF == ord('c'):
        print("Odcienie szarości")
        time.sleep(0.5)  # dodanie opóżnienia powoduje spadek płynności wyświetlania obrazu na żywo,
        # jednak zmniejsza szanse przypadkowego wielokrotnemu wciśnięciu tego samego przycisku
        makeGray = not makeGray
    if makeGray:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # w pyrzypadku naciśnięcia 'p' zdjęcie zostanie zapisane w miejscu, gdzie znajduje się program główny
    # indeksowanie zdjęć sprawia, że możlwe jest zrobienie dowolnej liczby zdjęć bez problemu z ich nadpisywaniem
    # jednego pliku o nazwie zapisany_obraz.jpg
    if cv2.waitKey(1) & 0xFF == ord('p'):
        print("Zrobiono zdjęcie")
        time.sleep(0.5)
        fileNameP = "zapisany_obraz" + str(photoIndex) + ".jpg"
        cv2.imwrite(fileNameP, frame)
        photoIndex += 1

    # w pyrzypadku naciśnięcia 'r' zmienia sie wartość zmiennej recordingOn na przeciwną
    if cv2.waitKey(1) & 0xFF == ord('r'):
        recordingOn = not recordingOn
        time.sleep(0.5)
        if recordingOn:
            print("Koniec Nagrywania")
            out.release()
        else:
            print("Początek Nagrywania")
            fileNameR = "zapisany_film" + str(videoIndex) + ".avi"
            out = cv2.VideoWriter(fileNameR, fourcc, 20.0, (640, 480))
            videoIndex += 1
    # na podstawie zmiennej recordingOn program decyduje czy zapisać kolejną klatkę filmu czy nie
    if recordingOn:
        out.write(frame)

    # otwieramy okno, wyświetlamy w nim obraz z kamery (frame) i nadajemy nazwe okna "Kamera"
    cv2.imshow('Kamera', frame)

cap.release()
out.release()
cv2.destroyAllWindows()
