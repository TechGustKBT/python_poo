import pickle
import traceback

from common import *

FILES_ELEITORES = 'eleitores.pkl'

def menu_eleitor():
    print("1 -> Novo Eleitor")
    print("2 -> Atualizar Eleitor")
    print("3 -> Sair")
    op = int(input("Digite a opção [1, 2, 3]"))
    while op not in (1, 2, 3):
        op = int(input("Digite a opção [1, 2, 3"))


def inserir_eleitor(eleitores):
    titulo = int(input("Digite o Título: "))

    if titulo in eleitores:
        raise Exception("Titulo já existente!")

    nome = input("Digite seu nome -> ")
    RG = int(input("Digite o seu RG -> "))
    CPF = int(input("Digite o seu CPF -> "))
    secao = input("Digite a seção -> ")
    zona = input("Digite a zona -> ")

    eleitor = Eleitor(nome, RG, CPF, titulo, secao, zona)
    eleitores[eleitor.get_titulo()] = eleitor

    with open(FILE_ELEITORES, 'wb') as arquivo:
        pickle.dump(eleitores, arquivo)


def atualizar_eleitor(eleitores):
    titulo = int(input("Digite o titulo do eleitor -> "))

    if titulo in eleitores:
        eleitor = eleitores[titulo]
        print(eleitor)
        secao = input("Digite a nova secao -> ")
        zona = input("Digite a nova zona -> ")
        eleitor.secao = secao
        eleitor.zona = zona

        with open(FILE_ELEITORES, 'wb') as arquivo:
            pickle.dump(eleitores, arquivo)

        print('Dados do eleitor atualizados com sucesso!')
        print(eleitor)
    else:
        raise Exception('Titulo inexistente!')

if __name__ == '__main__':
    eleitores = {}
    try:
        print("Carregando arquivo de eleitores ...")

        with open(FILE_ELEITORES, 'rb') as arquivo:
            eleitores = pickle.load(arquivo)
    except FileNotFoundError as fnfe:
        print(fnfe)
        print("Arquivo não encontrado, nenhum eleitor carregado!")

    opcao = 1
    while opcao in (1,2,3):
        try:
            opcao = menu_eleitor()

            if opcao == 1:
                inserir_eleitor(eleitores)
            elif opcao == 2:
                atualizar_eleitor(eleitores)
            elif opcao == 3:
                print("Saindo...")
                break
        except Exception as e:
            print(e)