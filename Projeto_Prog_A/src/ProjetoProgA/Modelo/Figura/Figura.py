# classe base (Superclasse)

class Figura:
    def __init__(self, cor_borda, cor_preenchimento):
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento

    def atualizar(self, x, y):
        raise NotImplementedError

    def desenhar(self, canvas, dash=None):
        raise NotImplementedError

    def incompleta(self):
        raise NotImplementedError
