import random

def simula_dados():
    print("************************")
    print("***Simulador de dados***")
    print("************************")

    dados = [4,6,8,10,12,20]
    numeros = []
    indice = 0

    for n in dados:
        dado = dados[indice]
        numeros.append(dados.index(dado))
        indice += 1

    print(numeros)

    #numeros = [0,1,2,3,4,5]
    print("Dados: (0) d4 (1) d6 (2) d8 (3) d10 (4) d12 (5) d20")
    numero_dado = int(input("Qual dado você deseja jogar?"))

    if numeros.count(numero_dado):
        quantidade_de_vezes = int(input("Quantas vezes você deseja jogar o dado?"))

        dado_escolhido = dados[numero_dado]

        print("Dado escolhido: d{}".format(dado_escolhido))

        rola_dado(dado_escolhido, quantidade_de_vezes)

    else:
        print("Numero inválido, iniciando novamente!")
        simula_dados()

    print("iniciando novamente!")
    simula_dados()

def rola_dado(dado, quantidade):
    valor = random.randrange(1, dado) * quantidade
    print(valor)

if (__name__ == "__main__"):
    simula_dados()