from atletas import *

if __name__ == "__main__":
    c1  = Corredor("Rony", 29, 65)
    print(c1)
    print(c1.aquecer())
    print(c1.correr())

    n1 = Nadador("Marcos Rocha", 35, 68)
    print(n1)
    print(n1.aquecer())
    print(n1.nadar())

    p1 = Pedalador("Raphael Veiga", 29, 77)
    print(p1)
    print(p1.aquecer())
    print(p1.pedalar())

    t1 = TriAtleta("Weverton", 36, 89)
    print(t1)
    print(t1.realizar_maratona())
    print(TriAtleta.__mro__)