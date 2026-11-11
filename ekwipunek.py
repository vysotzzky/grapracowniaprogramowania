from dataclasses import dataclass, replace


@dataclass
class Przedmiot:
    waga: int
    wartosc: int
    ilosc: int = 1


Ekwipunek = dict[str, Przedmiot]
MAKSYMALNY_UDZWIG = 25  # kg

# Waga i wartość w katalogu dotyczą jednej sztuki.
SKLEP = {
    "miecz": Przedmiot(waga=5, wartosc=25),
    "mikstura": Przedmiot(waga=1, wartosc=10),
    "tarcza": Przedmiot(waga=7, wartosc=20),
    "zbroja": Przedmiot(waga=12, wartosc=40),
}


def laczna_waga(ekwipunek: Ekwipunek) -> int:
    return sum(przedmiot.waga * przedmiot.ilosc for przedmiot in ekwipunek.values())


def pokaz_przedmioty(ekwipunek: Ekwipunek, zloto: int) -> None:
    print(f"\nZłoto: {zloto} | Udźwig: {laczna_waga(ekwipunek)}/{MAKSYMALNY_UDZWIG} kg")
    if not ekwipunek:
        print("Ekwipunek jest pusty.")

    for nazwa, przedmiot in ekwipunek.items():
        print(
            f"- {nazwa}: {przedmiot.ilosc} szt. "
            f"({przedmiot.waga} kg, {przedmiot.wartosc} złota za sztukę)"
        )


def pobierz_nazwe(komunikat: str) -> str:
    return input(komunikat).strip().casefold()


def pobierz_dodatnia_liczbe(komunikat: str) -> int:
    while True:
        try:
            liczba = int(input(komunikat))
        except ValueError:
            print("Wpisz dodatnią liczbę całkowitą.")
            continue

        if liczba > 0:
            return liczba
        print("Wpisz dodatnią liczbę całkowitą.")


def dodaj_sztuke(ekwipunek: Ekwipunek, nazwa: str, wzor: Przedmiot) -> bool:
    przedmiot = ekwipunek.get(nazwa)
    waga_sztuki = przedmiot.waga if przedmiot else wzor.waga
    wolny_udzwig = MAKSYMALNY_UDZWIG - laczna_waga(ekwipunek)
    if waga_sztuki > wolny_udzwig:
        print(f"Brak miejsca. Pozostały udźwig: {wolny_udzwig} kg.")
        return False

    if przedmiot:
        przedmiot.ilosc += 1
    else:
        ekwipunek[nazwa] = replace(wzor, ilosc=1)
    return True


def usun_sztuke(ekwipunek: Ekwipunek, nazwa: str) -> None:
    przedmiot = ekwipunek[nazwa]
    przedmiot.ilosc -= 1
    if przedmiot.ilosc == 0:
        del ekwipunek[nazwa]


def dodaj_znalezisko(ekwipunek: Ekwipunek) -> None:
    nazwa = pobierz_nazwe("Nazwa znalezionego przedmiotu: ")
    if not nazwa:
        print("Podaj nazwę przedmiotu.")
        return

    wzor = ekwipunek.get(nazwa) or SKLEP.get(nazwa)
    if wzor is None:
        waga = pobierz_dodatnia_liczbe("Waga jednej sztuki w kg: ")
        wartosc = pobierz_dodatnia_liczbe("Wartość jednej sztuki w złocie: ")
        wzor = Przedmiot(waga, wartosc)

    if dodaj_sztuke(ekwipunek, nazwa, wzor):
        print(f"Dodano 1 szt.: {nazwa}.")


def kup_przedmiot(ekwipunek: Ekwipunek, zloto: int) -> int:
    print(f"\nSklep | Złoto: {zloto}")
    for nazwa, przedmiot in SKLEP.items():
        print(f"- {nazwa}: {przedmiot.wartosc} złota, {przedmiot.waga} kg")

    nazwa = pobierz_nazwe("Co chcesz kupić? ")
    towar = SKLEP.get(nazwa)
    if towar is None:
        print("Tego przedmiotu nie ma w sklepie.")
        return zloto
    if zloto < towar.wartosc:
        print("Masz za mało złota.")
        return zloto
    if not dodaj_sztuke(ekwipunek, nazwa, towar):
        return zloto

    print(f"Kupiono 1 szt.: {nazwa} za {towar.wartosc} złota.")
    return zloto - towar.wartosc


def sprzedaj_przedmiot(ekwipunek: Ekwipunek, zloto: int) -> int:
    if not ekwipunek:
        print("Ekwipunek jest pusty.")
        return zloto

    print("\nCeny sprzedaży za sztukę:")
    for nazwa, przedmiot in ekwipunek.items():
        print(f"- {nazwa}: {cena_sprzedazy(przedmiot)} złota")

    nazwa = pobierz_nazwe("Co chcesz sprzedać? ")
    przedmiot = ekwipunek.get(nazwa)
    if przedmiot is None:
        print("Nie masz tego przedmiotu.")
        return zloto

    cena = cena_sprzedazy(przedmiot)
    usun_sztuke(ekwipunek, nazwa)
    print(f"Sprzedano 1 szt.: {nazwa} za {cena} złota.")
    return zloto + cena


def cena_sprzedazy(przedmiot: Przedmiot) -> int:
    return max(1, przedmiot.wartosc // 2)


def dodaj_przedmiot(ekwipunek: Ekwipunek, zloto: int) -> int:
    while True:
        print("\n1. Dodaj znalezisko\n2. Kup w sklepie\n3. Sprzedaj przedmiot\n4. Wróć")
        wybor = input("Wybierz opcję: ").strip()

        if wybor == "1":
            dodaj_znalezisko(ekwipunek)
        elif wybor == "2":
            zloto = kup_przedmiot(ekwipunek, zloto)
        elif wybor == "3":
            zloto = sprzedaj_przedmiot(ekwipunek, zloto)
        elif wybor == "4":
            return zloto
        else:
            print("Wybierz opcję od 1 do 4.")


def uzyj_przedmiotu(ekwipunek: Ekwipunek) -> None:
    nazwa = pobierz_nazwe("Którego przedmiotu chcesz użyć? ")
    if nazwa not in ekwipunek:
        print("Nie masz tego przedmiotu.")
        return

    usun_sztuke(ekwipunek, nazwa)
    print(f"Użyto 1 szt.: {nazwa}.")


def sprawdz_przedmiot(ekwipunek: Ekwipunek) -> None:
    nazwa = pobierz_nazwe("Jaki przedmiot sprawdzić? ")
    przedmiot = ekwipunek.get(nazwa)
    if przedmiot is None:
        print("Nie masz tego przedmiotu.")
    else:
        print(f"Masz {przedmiot.ilosc} szt.: {nazwa}.")


def zakoncz_gre() -> None:
    print("Do zobaczenia!")


def main() -> None:
    ekwipunek = {
        "miecz": replace(SKLEP["miecz"]),
        "mikstura": replace(SKLEP["mikstura"], ilosc=3),
    }
    zloto = 50

    while True:
        print("\n=== Ekwipunek bohatera ===")
        print("1. Pokaż przedmioty")
        print("2. Dodaj przedmiot / sklep")
        print("3. Użyj przedmiotu")
        print("4. Sprawdź przedmiot")
        print("5. Wyjdź")
        wybor = input("Wybierz opcję: ").strip()

        if wybor == "1":
            pokaz_przedmioty(ekwipunek, zloto)
        elif wybor == "2":
            zloto = dodaj_przedmiot(ekwipunek, zloto)
        elif wybor == "3":
            uzyj_przedmiotu(ekwipunek)
        elif wybor == "4":
            sprawdz_przedmiot(ekwipunek)
        elif wybor == "5":
            zakoncz_gre()
            break
        else:
            print("Wybierz opcję od 1 do 5.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print()
        zakoncz_gre()
