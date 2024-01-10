import requests
from os import system
from time import sleep
from bs4 import BeautifulSoup

from Modulos.FormData import params, form_data
from Modulos.Cabecalho import cabecalho


class Facebook:
    def __init__(self) -> None:
        self.ptcl = "https"
        self.host = "mbasic.facebook.com"
        self.url_root = f"{self.ptcl}://{self.host}/"
        self.host_post = "login/device-based/regular/login/"
        # self.header = cabecalho()
        self.cookies = None
        self._session = requests.Session()
        self._session.headers = cabecalho()

    def login(self, email: str, passwd: str) -> None:
        _params = params()
        _data = form_data(email, passwd)
        try:
            self.site = self._session.get(self.url_root)
            tags = BeautifulSoup(self.site.text, "html.parser")

            # Obter os valores direto no html
            _data['lsd'] = tags.find("input", attrs={'name': 'lsd'})['value']
            _data['jazoest'] = tags.find("input", attrs={'name': 'jazoest'})['value']
            _data['m_ts'] = tags.find("input", attrs={'name': 'm_ts'})['value']
            _data['li'] = tags.find("input", attrs={'name': 'li'})['value']
            sleep(3)
        
        except requests.exceptions.RequestException as e:
            print(f'\033[31mFalha na conexão! Erro: {e}\033[m')
        
        else:
            self.site = self._session.post(url=self.url_root+self.host_post, params=_params, data=_data)
        
        with open("index.html", "wt") as file:
            file.write(self.site.text)
    
    def verificar(self):
        page = self.site
        informations = BeautifulSoup(page.text, "html.parser")
        if informations.find("div", attrs={'id': 'login_error'}):
            return False
        else:
            return True

    def perfil(self) -> dict:
        """ 
        1-Nome do usuário
        2-Data de nascimento
        3-Gênero
        4-Localização
        5-Lista de Amigos
        6-Informações de contactos
        7-Informaçôes educacionais
         """
        # Solicitar a pagina Sobre/About
        self.site = self._session.get(url=self.url_root+"profile.php?v=info")
        soup = BeautifulSoup(self.site.text, "html.parser")
        nome = soup.find("strong", attrs={'class': 'cd'}).get_text()
        print(f"Nome: {nome}")

        data_nascimento = soup.find_all(class_=lambda x: x and 'dy' in x.split())

        # Agora, 'elementos' contém a lista de elementos correspondentes ao seletor XPath
        for elemento in data_nascimento:
            print(elemento.text)
        # print(f"1- Data => {data_nascimento}")
        

        with open("index.html", "wt") as file:
            file.write(self.site.text)


system("clear")

print("==" * 25)
facebook = Facebook()
facebook.login("955509058", "Senhafoda")
if facebook.verificar():
    print("\033[32mLogado com susseco!\033[m")
else:
    print("\033[31m!Erro ao logar!\033[m")
print("==" * 25)
facebook.perfil()