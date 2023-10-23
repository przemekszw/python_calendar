from bs4 import BeautifulSoup
import requests
#Klasy

class Main():
    def urlParser(self):
        # URL pobieranie strony
        url = "https://planzajec.uek.krakow.pl/index.php?typ=G&id=237971&okres=1"
        response = requests.get(url)

        if response.status_code == 200:
            pass
        else:
            print("Error: ", response.status_code)

        soup = BeautifulSoup(response.content, 'html.parser')

        # DATA WYKŁADU
        terminy = soup.find_all(class_='termin')
        # GODZINA WYKŁADU
        godzina = soup.find_all(class_='dzien')

        return terminy, godzina



