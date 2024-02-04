import requests
from bs4 import BeautifulSoup


def wyciagnij_tekst(url):
    # Wysłanie zapytania HTTP do strony internetowej
    response = requests.get(url)

    # Sprawdzenie, czy zapytanie zakończyło się sukcesem
    if response.status_code == 200:
        # Przypisanie zawartości strony do zmiennej
        html_content = response.content

        # Tworzenie obiektu BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Wyszukanie wszystkich znaczników <td> o klasie "ts"
        td_tags = soup.find_all('td', class_='ts')

        # Lista do przechowywania wyciągniętych tekstów
        wyciagniete_teksty = []

        # Iteracja po wszystkich znalezionych znacznikach
        for td_tag in td_tags:
            # Dodanie tekstu do listy wyciągniętych tekstów
            wyciagniete_teksty.append(td_tag.text)

        # Zwrócenie listy wyciągniętych tekstów
        return wyciagniete_teksty
    else:
        # Jeśli zapytanie nie powiedzie się, wyświetlenie komunikatu
        print("Błąd: Nie udało się pobrać strony.")
        return None

def main():
    # Adres URL strony, z której chcesz wyciągnąć tekst
    url = 'https://commands.gg/witcher3/items'
    # url = 'https://commands.gg/witcher3'

    # Wywołanie funkcji wyciagnij_tekst() i przekazanie adresu URL
    wyciagniete_teksty = wyciagnij_tekst(url)

    # Wyświetlenie wyciągniętych tekstów

    with open("items.csv", "w", encoding="utf-8") as f:
        f.write("nazwa,komenda\n")

        if wyciagniete_teksty:
            for tekst in wyciagniete_teksty:
                if not tekst.startswith('additem'):
                    f.write(f"{tekst},")
                else:
                    f.write(f"{tekst}\n")

        for i in range(2,86):
            url = f'https://commands.gg/witcher3/items/{i}'
            wyciagniete_teksty = wyciagnij_tekst(url)

            if wyciagniete_teksty:
                for tekst in wyciagniete_teksty:
                    if not tekst.startswith('additem'):
                        f.write(f"{tekst},")
                    else:
                        f.write(f"{tekst}\n")


if __name__ == '__main__':
    main()
    print("finished")
