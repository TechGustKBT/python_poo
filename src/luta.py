from Lutador import *
import random

def golpear(B1 : MMA, B2: MMA):
    golpe = random.randrange(1, 7)

    if golpe == 1:
        B1.gancho(B2)
    elif golpe == 2:
        B1.cruzado(B2)
    elif golpe == 3:
        B1.gancho(B2)
    elif golpe == 4:
        B1.chute_alto(B2)
    elif golpe == 5:
        B1.chave_braco(B2)
    elif golpe == 6:
        B1.superman_punch(B2)

if __name__ == "__main__":

    B1 = MMA("Zé Rafael")
    B2 = MMA("Gustavo Gomez")

    while B1.energia > 0 and B2.energia > 0:
        print(B1)
        print(B2)
        Lutador = random.randrange(1, 3)
        if Lutador == 1:
            golpear(B1, B2)
        else:
            golpear(B2, B1)

    if B1.energia <= 0:
        print(B1.nome, "venceu do", B2.nome, "!!!!")
    else:
        print(B2.nome, "venceu do", B1.nome, "!!!!")





