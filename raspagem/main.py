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
        for i, p in enumerate(self.Princiapais_noticias, 1):
            print('')
            print(f'[{i}]{p.get_text()}') 
            link = p.get('href')
            self.link_noticias.append(p)
        escolher_noticia = int(input('escolha a noticia q deseja: '))
        escolhida = self.link_noticias[escolher_noticia].get('href')
        print(escolhida)

    def destaques(self):
        print('Destaques:')
        for no in self.noticias_items:
            print('')
            print(no.get_text())   




def tela_principal():
    while True:
        test1 = Site()
        dec = int(input("[1] Principais notícias\n[2] Destaques\n[3] Sair\n: "))
        if dec == 1:
            test1.principais_noticias()
        elif dec == 2:
            test1.destaques()
        else:
            break

tela_principal()
 

        