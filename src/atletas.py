from abc import ABC

class Atleta(ABC):
    nome : str
    idade : int
    peso : float

    def __init__(self, n : str, i : int, p : float):
        self.nome = n
        self.idade = i
        self.peso = p

    def aquecer(self):
        return f"{self.nome} está aquecendo\n"

    def __str__(self):
        info = f'NOME: {self.nome}, IDADE: {self.idade}, PESO: {self.peso} KG'
        return info

class Corredor(Atleta):
    def correr(self):
        return f"{self.nome} está correndo\n"

class Nadador(Atleta):
    def nadar(self):
        return f"{self.nome} está nadando\n"

class Pedalador(Atleta):
    def pedalar(self):
        return f"{self.nome} está pedalando\n"

class TriAtleta(Corredor, Nadador, Pedalador):
    def realizar_maratona(self):
        info = self.aquecer()
        info += self.correr()
        info += self.nadar()
        info += self.pedalar()

        return info