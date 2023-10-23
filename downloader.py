from slicer import Slicer
from main import Main

s = Slicer()
m = Main()

class Downloader():
    def extractor(self):

        terminy, godzina = m.urlParser()

        lista_godzina = [] # lista na Nd 8:00 - 11:00 (3g.)
        lista_godzina2 = [] # lista na 8:00 - 11:00
        lista_terminy = [] # lista na daty
        lista = [] # lista na ostateczny wynik

        licznik = 0 # licznik do inkrementacji dla pętli for


        for element in terminy:
            lista_terminy.append(element.text)

        for element in godzina:
            lista_godzina.append(element.text)

        for x in lista_godzina:
            time = s.time(x)
            lista_godzina2.append(time)

        """
        for x in range(len(lista_godzina2)):
            lista.append(lista_terminy[licznik])
            lista.append(lista_godzina2[licznik])
            licznik += 1
        """

        data_dict = {}

        for x in range(len(lista_godzina2)):
            termin = lista_terminy[x]
            godzina = lista_godzina2[x]

            if termin in data_dict:
                data_dict[termin].append(godzina)
            else:
                data_dict[termin] = [godzina]

        return data_dict

