import pickle
import traceback
import gerenciar_urna
from common import *

FILE_ELEITORES = 'eleitores.pkl'
FILE_CANDIDATOS = 'candidatos.pkl'

def menu():
    return op

def inserir_eleitor(eleitores):
    print(eleitor)

def atualizar_eleitor(eleitores):
        raise Exception('Titulo inexistente')

def inserir_candidato(candidatos):
    print(candidato)

def listar_candidatos(candidatos):
    for candidato in candidatos.values():
        print(candidato)

if __name__ == "__main__":
    eleitores = {} #dicionário a chave será o titulo
    try:
        print("Carregando arquivo de eleitores ...")

        with open(FILE_ELEITORES, 'rb') as arquivo:
            eleitores = pickle.load(arquivo)
    except FileNotFoundError as fnfe:
        print(fnfe)
        print("Arquivo nao encontrado, nenhum eleitor carregado!")

    candidatos = {}  # dicionário a chave será o titulo
    try:
        print("Carregando arquivo de candidatos ...")

        with open(FILE_CANDIDATOS, 'rb') as arquivo:
            candidatos = pickle.load(arquivo)
    except FileNotFoundError as fnfe:
        print(fnfe)
        print("Arquivo nao encontrado, nenhum candidato carregado!")

    opcao = 1
    while opcao in range(1,8):
        try:
            opcao = menu()

            if opcao == 1:
                inserir_eleitor(eleitores)
            elif opcao == 2:
                atualizar_eleitor(eleitores)
            elif opcao == 3:
                inserir_candidato(candidatos)
            elif opcao == 4:
                listar_candidatos(candidatos)
            elif opcao == 5:
                urna = gerenciar_urna.iniciar_urna(eleitores.values(),
                                                   candidatos.values())
            elif opcao == 6:
                gerenciar_urna.votar(urna)
            elif opcao == 7:
                print("Saindo!")
                break
        except Exception as e:
            #traceback.print_exc()
            print(e)