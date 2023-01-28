from os import system
import random
from time import sleep


def wydruk(zmienna):
    system("cls")
    print("#####################CHO-HAN#####################")
    print(str(zmienna))
    print("################################################")


def stawiana_stawka(kredyt):
    while True:
        stawka = int(input())
        if stawka > kredyt:
            # musimy sprawdzić czy gracz nie postawil wiecej niż posiada
            wydruk(f"Nie masz tyle kredytów")
        else:
            stawka = int(stawka)
            break
    return stawka


def wybor_cho_han():
    while True:
        wydruk(f"Wybierz parzyste czy nieparzyste")
        wybor = input()
        if wybor == "parzyste" or wybor == "nieparzyste":
            break
        else:
            print("Nieprawidłowy wybór")
    return wybor


def rzut_kostkami():
    kostka1 = random.randint(1, 6)
    kostka2 = random.randint(1, 6)
    return kostka1, kostka2


def wyswietl_wynik(JAPONSKIE_CYFRY, kostka1, kostka2):
    print("Wyrzuciłeś", JAPONSKIE_CYFRY[kostka1], "i", JAPONSKIE_CYFRY[kostka2])
    print("Suma to", kostka1 + kostka2)


def ktory_wygrywa(kostka1, kostka2):
    czyParzyste = (kostka1 + kostka2) % 2 == 0
    if czyParzyste:
        wygrywa = "parzyste"
    else:
        wygrywa = "nieparzyste"
    return wygrywa


def zwyciestwo(kredyt):
    if kredyt >= 20000:
        wydruk(f"Gratulacje wygrałeś")
        exit()


def wygrana(kredyt, stawka):
    kredyt += stawka - int(0.1 * stawka)
    wydruk(f"Wygrałeś \n Masz {kredyt} kredytów")
    sleep(4)
    return kredyt


def przegrana(kredyt, stawka):
    kredyt = kredyt - stawka
    wydruk("Przegrałeś")
    sleep(4)
    return kredyt


def brak_kredytow_koniec_gry():
    wydruk("Przegrałeś, nie masz kredytów \n dziękujemy za gre!")
    exit()


def czy_grasz_dalej():
    wydruk(f"Czy chcesz grać dalej? (t/n)")
    while True:
        czyGrać = input()
        if czyGrać == "t":
            break
        elif czyGrać == "n":
            print("Dziękujemy za grę")
            exit()
        else:
            print("Nieprawidłowy wybór")
