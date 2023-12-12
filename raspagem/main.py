from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.cnnbrasil.com.br/')
soup = BeautifulSoup(page.text, 'html.parser')

noticias = soup.find(class_='three__highlights__list row')
noticias2 = soup.find(class_='block block--headlines')


class Site:


    def __init__(self):
        self.Princiapais_noticias = noticias.find_all('a')
        self.noticias_items = noticias2.find_all('h3')
        self.link_noticias = ['0']


    def principais_noticias(self):
        #for t in self.Princiapais_noticias:
            #link = t.get('href')
            #self.link_noticias.append(link)
        print('Principais noticias:')
        for p in self.Princiapais_noticias:
            print('')
            print(p.get_text()) 
            link = p.get('href')
            self.link_noticias.append(link)

    def destaques(self):
        print('Destaques:')
        for no in self.noticias_items:
            print('')
            print(no.get_text())   


while True:
    test1 = Site()
    dec = int(input("Para ver as principais nóticias Digite [1] para ver os Destaques [2] e para sair [3]: "))
    if dec == 1:
        test1.principais_noticias()
    elif dec == 2:
        test1.destaques()
    else:
        break
        

