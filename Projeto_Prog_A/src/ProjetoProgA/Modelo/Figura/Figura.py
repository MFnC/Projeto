from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self, cor_borda, cor_preenchimento):
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento

    @abstractmethod
    def atualizar(self, x, y):
        pass

    @abstractmethod
    def desenhar(self, canvas):
        pass

    @abstractmethod
    def incompleta(self):
        pass


