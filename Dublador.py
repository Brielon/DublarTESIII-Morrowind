#Dublar Data files/Video/*.bik cutscenes
#       Data files/Sound/Vo/*mp4 audios
# sera criado um ambiente temporario que nos permitira trabalhar na dublagens...nao se preocupe pois o mesmo sera deletado ao final da tranzacao, pesso apenas a conexao com a internet para que possamos proceguir
import venv
from os import system
import subprocess
import datetime
def CriarAmbiente():
    venv.create('./ambienteTemporario',with_pip=True)
def AtivarAmbiente():
    subprocess.run([".\\ambienteTemporario\\Scripts\\activate.bat"])
def BaixarBibliotecasNecessarias():
    bibliotecas = ["pip","install",
                "selenium"] 
    subprocess.run(bibliotecas)

CriarAmbiente()
AtivarAmbiente()
BaixarBibliotecasNecessarias()

#selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

        
def finalizar():
    DesativarAmbiente()
    DeletarAmbiente()


class Arquivo:
    def __init__(self,diretorio):
        self.diretorio = diretorio
        self.carregarMemoria()
        self.trataraudio()
    def trataraudio(self):
        self.extencao = "."+(self.diretorio.split(".")[-1])
        if ".mp3" == self.extencao:
            self.dublarMP3()
        if ".wav" == self.extencao:
            pass
        if ".bik" == self.extencao:
            pass


    def dublarMP3(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-software-rasterizer")
        options.add_argument("--no-sandbox")
        driver = webdriver.chrome(options=options)
        

        driver.close()
    def rewrite(self):
        with open(self.diretorio,"wb") as bin:
            bin.write(self.binario)

    def carregarMemoria(self):
        self.binario = b""
        with open(self.diretorio,"rb") as bin:
            bin.seek(0)
            while True:
                buffer = bin.read(1024)
                if not buffer: 
                    break
                self.binario += buffer

   

def DesativarAmbiente():
    subprocess.run([".\\ambienteTemporario\\Scripts\\deactivate.bat"])

def DeletarAmbiente():
    system("rd /s /q .\\ambienteTemporario")


def buscador(pasta,*args):
    diretorios = []
    outros = []
    comando = ["dir",pasta]
    retorno = subprocess.run(comando,capture_output=True,text=True,shell=True)
    dir = retorno.stdout
    linhas = dir.split("\n")
    for linha in linhas:
        if "<DIR>" in linha:
            diretorios.append(linha)
        else:
            for arg in args:
                if arg in linha:
                    nome = linha.split()[-1]
                    diretorio = pasta+"/"+nome
                    yield diretorio
                    
    for i,linha in enumerate(diretorios):
        diretorios[i]=linha.split()[-1]
    diretorios = diretorios[2:]
    for buscar in diretorios:
        buscar = pasta+"/"+buscar
        for arquivo in buscador(buscar,*args):
            yield arquivo
    
    

    #aqui contem as extencoes

anotacoes = """
CriarAmbiente                   -   testok
AtivarAmbiente                  -   testok 
BaixarBibliotecasNecessarias    -   testok
BuscarArquivosPTraducao         -   testok
DesativarAmbiente               -   testok
DeletarAmbiente                 -   testok
class Arquivo                   -   
buscador                        -   testok
loading                         -   testok
"""
def loading_screen(tamanhoTotal,i,timeInicio):
    timeAtual = datetime.datetime.now()
    porcentagen = int(float(i/tamanhoTotal)*10)
    porcentagenEm100 = int(float(i/tamanhoTotal)*100)
    faltante = 10-porcentagen
    carregado = "#"*porcentagen
    faltante = "-"*faltante
    system("cls")
    print("Carregando:")
    print("[",carregado,faltante,"]",porcentagenEm100,"%")
    print(i,"/",tamanhoTotal)
    tempoGasto = timeAtual-timeInicio
    tempoGasto = int(tempoGasto.total_seconds())
    porcentagenEm100 = 1 if porcentagenEm100==0 else porcentagenEm100
    tempoRestante = ((100/porcentagenEm100)*tempoGasto)-tempoGasto
    print("Inicio:",timeInicio)
    print("Tempo restante:",int(tempoRestante),"s")

if __name__ == "__main__":
    arquivos = []
    tamanhoTotal = 0
    for arquivo in buscador("Data Files",".mp3",".bik"):
        tamanhoTotal+=1
    timeInicio = datetime.datetime.now()
    for i,arquivo in enumerate(buscador("Data Files",".mp3",".bik")):
        loading_screen(tamanhoTotal,i,timeInicio)
        Arquivo(arquivo).rewrite()
    finalizar()
