import Dublador
def testeTraducao():
    print(">>>>>>>>>>>>>>",Dublador.traducao("my god is big"))
#criando ambiente ok
#ativando o mesmo ok 
#instalando bibliotecas ok 

#testeTraducao() ok
def testeBuscadorarquivos():
    lista_arquivos = []
    for diretorio in Dublador.buscador("Data Files",".mp3",".bik"):
        print(diretorio)

   
   # for arquivo in buscador(".\\Data\ Files\\","mp3","bik")
    #    print(arquivo.nome)
#testeBuscadorarquivos() 
#dasativando e deletando ambiente ok 
def testeArquivo():
    Dublador.Arquivo("testAudio/Atk_AM005.mp3").rewrite()
testeArquivo()
Dublador.finalizar()
