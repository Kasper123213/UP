import cv2
import time

#program działa podobnie do programu Kamera1, więc opisane zostały tu tylko funkcje nie zawarte w pliku poprzednim

cap = cv2.VideoCapture(0)

photoIndex = 1

while True:
    #zmienna określa, czy ma być zrobione zdjęcie
    aboutToPhoto = False
    # Przechwytujemy dwa obrazy a nie jeden, żeby mieć możliwość analizy różnic między nimi
    ret, frame = cap.read()
    time.sleep(0.001)
    ret1, frame2 = cap.read()

    if not ret or not ret1:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Koniec Programu")
        break

    #sunkcja odejmuje od siebie dwie macierze reprezentujące dwie klatki przechwycone przez kamerę
    diff = cv2.absdiff(frame, frame2)
    #zmienna diff zawierająca macierz różnic kolorów między klatkami konwertujemy na odcienie szarości
    #można było pominąć ten krok i zostawić różnice dla macierzy zawierającej kolory w systemie RGB
    # jednak powodowało to duży ubytek na płunności wyświetlanego na żywo obrazu
    diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)



    ############################# Ten kod dopisaliśmy w domu #################################################qq

    # zmienna określa czułość na wykrywanie ruchu, eliminuje to drgania kamery lub mimowolne drgania ciała
    threshold = 80

    # #wszystkie piksele o wartości 90-255 zostają usatawione na 255. zapewnia to jednolity
    _, diff = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)

    #Sprawdzamy czy któreś piksele wykazały istotne zmiany
    for arr in diff:
        if any(arr) > 0:
            aboutToPhoto = True
            break

    ##########################################################################################################


    if aboutToPhoto:
        print("Zrobiono zdjęcie")
        time.sleep(0.5)
        fileNameP = "zapisany_obraz" + str(photoIndex) + ".jpg"
        cv2.imwrite(fileNameP, frame)
        photoIndex += 1

    cv2.imshow('Kamera', frame)

cap.release()
cv2.destroyAllWindows()
