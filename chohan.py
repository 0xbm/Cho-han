#!/usr/bin/env python3

# * Gra Chohan - Bakuchi
# **  rzut koscmi
# **  obstaw czy suma parzysta czy nieparzysta
# **  start z 5000 kredytami
# **  za kazda wygrana dom gry pobiera 10%
# **  konczymy gre jak skoncza sie kredyty
# **  konczymy gre jak gracz chce odejsc od stolu
# **  zakladamy maksymalna wygrana na 20000 kredytow

# dostajemy z bank na start 5000 kredytow
# japonskie cyfry
# poczatek while
# informujemy gracz ile ma kredytow
# stawianie pieniedzy
# musimy sprawdzic czy gracz nie postawil wiecej niz posiada
# gracz wybiera czy parzyste czy nieparzyste
# losowanie wartosci kosci
# wyswietlamy kosci
# sprawdzamy czy gracz wygral
# jezeli wygral to :
#   wygrywa ilosc o ktora sie zalozyl pomniejszona o 10% (oplata dla banku)
#       sprawdzamy czy przekroczyl 20000
#       jezeli tak to wyswietalmy gratulacje
#   jezeli przegra to traci ilosc kredytow o ktore sie zalozyl
#   sprawdzamy czy ma kredyty w portfelu- jezeli nie ma konczymy gre
#   jezeli ma to moze grac dalej
#   koniec glownej petli


# import random

# # Dostajemy z banku na start 5000 kredytów
# kredyt = 5000

# # japońskie cyfry
# JAPONSKIE_CYFRY = {1: "ichi", 2: "ni", 3: "san", 4: "shi", 5: "go", 6: "roku"}
# # WHILE
# while True:

#     # inforujemy gracza ile ma kredytów
#     print("Masz", kredyt, "kredytów", "Ile chcesz postawić?")
#     # stawianie pieniędz
#     while True:
#         stawka = int(input())
#         if stawka > kredyt:
#             # musimy sprawdzić czy gracz nie postawil wiecej niż posiada
#             print("Nie masz tyle kredytów")
#         # elif not stawka.isdecimal():
#         #     print("To nie jest liczba")
#         else:
#             stawka = int(stawka)
#             break

#     # Gracz wybiera czy parzyste czy nieparzyste
#     print("Wybierz parzyste czy nieparzyste")
#     while True:
#         wybor = input()
#         if wybor == "parzyste" or wybor == "nieparzyste":
#             break
#         else:
#             print("Nieprawidłowy wybór")
#     # losowanie wartości kości
#     kostka1 = random.randint(1, 6)
#     kostka2 = random.randint(1, 6)
#     # Wyświetlamy kości
#     print("Wyrzuciłeś", JAPONSKIE_CYFRY[kostka1], "i", JAPONSKIE_CYFRY[kostka2])
#     print("Suma to", kostka1 + kostka2)
#     # sprawdzamy czy wygrał
#     czyParzyste = (kostka1 + kostka2) % 2 == 0
#     if czyParzyste:
#         wygrywa = "parzyste"
#     else:
#         wygrywa = "nieparzyste"
#     # Jeżeli wygrał to
#     if wygrywa == wybor:
#         print("Wygrałeś")
#         # Wygrywa ilość o którą się założył pomniejszoną o 10%
#         kredyt += stawka - int(0.1 * stawka)
#         print("Masz", kredyt, "kredytów")
#         if kredyt >= 20000:
#             # sprawdzamy czy przekroczył 20000
#             # jeżeli tak to wyświetlamy gratulacje
#             print("Gratulacje wygrałeś")
#             break
#     else:
#         # Jeżeli przegra to traci kredyty o które sie założył
#         kredyt = kredyt - stawka
#         print("Przegrałeś")

#         if kredyt <= 0:
#             # sprawdzamy czy ma kredyty w portfelu - jeżeli nie ma kończymy grę
#             print("Przegrałeś, nie masz kredytów")
#             print("dziękujemy za gre!")
#             exit()
#             break
#     print("Czy chcesz grać dalej? (t/n)")
#     # sprawdzamy czy chce grać dalej
#     while True:
#         czyGrać = input()
#         if czyGrać == "t":
#             break
#         elif czyGrać == "n":
#             print("Dziękujemy za grę")
#             exit()
#         else:
#             print("Nieprawidłowy wybór")
#     # jeżeli ma moze grać dalej
#     # koniec głównej pętli

import random
import funkcje as f

# Dostajemy z banku na start 5000 kredytów
kredyt = 5000

# japońskie cyfry
JAPONSKIE_CYFRY = {1: "ichi", 2: "ni", 3: "san", 4: "shi", 5: "go", 6: "roku"}


# WHILE

while True:

    # inforujemy gracza ile ma kredytów
    f.wydruk(f"Masz {kredyt} kredytów. Ile chcesz postawić?")

    # stawianie pieniędzy
    stawka = f.stawiana_stawka(kredyt)

    # Gracz wybiera czy parzyste czy nieparzyste
    wybor = f.wybor_cho_han()

    # losowanie wartości kości
    kostka1, kostka2 = f.rzut_kostkami()

    # Wyświetlamy kości
    f.wyswietl_wynik(JAPONSKIE_CYFRY, kostka1, kostka2)

    # sprawdzamy czy wygrał
    wygrywa = f.ktory_wygrywa(kostka1, kostka2)

    # Jeżeli wygrał to
    if wygrywa == wybor:
        # Wygrywa ilość o którą się założył pomniejszoną o 10%
        kredyt = f.wygrana(kredyt, stawka)
        f.zwyciestwo(kredyt)
    else:
        # Jeżeli przegra to traci kredyty o które sie założył
        kredyt = f.przegrana(kredyt, stawka)

        if kredyt <= 0:
            # sprawdzamy czy ma kredyty w portfelu - jeżeli nie ma kończymy grę
            f.brak_kredytow_koniec_gry()

    # sprawdzamy czy chce grać dalej
    f.czy_grasz_dalej()
