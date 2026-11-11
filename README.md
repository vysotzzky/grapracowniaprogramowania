# Ekwipunek bohatera

Konsolowy program w Pythonie. Bohater zaczyna z mieczem, trzema miksturami i 50 sztukami złota.

## Uruchomienie

Wymagany jest Python 3.9 lub nowszy. Program korzysta z biblioteki standardowej.

```bash
python ekwipunek.py
```

Na Windowsie można też użyć `py ekwipunek.py`.

## Obsługa

1. **Pokaż przedmioty** wyświetla ilość, wagę i wartość przedmiotów oraz saldo złota i aktualne obciążenie.
2. **Dodaj przedmiot / sklep** pozwala dodać znalezisko, kupić przedmiot lub sprzedać go. Wagę i wartość nieznanego znaleziska wpisuje się jako dodatnie liczby całkowite. Kolejna sztuka przedmiotu ma te same parametry.
3. **Użyj przedmiotu** zużywa jedną sztukę. Po zużyciu ostatniej sztuki danego przedmiotu program usuwa jego wpis z ekwipunku.
4. **Sprawdź przedmiot** pokazuje, czy bohater ma podany przedmiot i ile sztuk posiada.
5. **Wyjdź** zamyka program.

Bohater może udźwignąć do 25 kg. Do obciążenia wlicza się wagę wszystkich sztuk przedmiotów. Złoto jest przechowywane jako osobne saldo. Przy kupnie program sprawdza cenę i dostępny udźwig. Sprzedaż daje połowę wartości przedmiotu, zaokrągloną w dół do pełnej sztuki złota, z minimum jednej sztuki złota.
