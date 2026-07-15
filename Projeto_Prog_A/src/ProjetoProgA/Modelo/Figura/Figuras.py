# Essa classe guarda todas as fuguras criadas

class Figuras:

    def __init__(self):
        self.figuras = []

    def adicionar(self, figura):
        self.figuras.append(figura)

    def obter_figuras(self):
        return self.figuras