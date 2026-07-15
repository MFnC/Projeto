from ..Figura import Figura

class Circulo(Figura):
    def __init__(self, x, y, cor_borda, cor_preenchimento):
        super().__init__(cor_borda, cor_preenchimento)
        self.centro_x = x
        self.centro_y = y
        self.raio = 0

    def atualizar(self, x, y):
        self.raio = ((self.centro_x - x) ** 2 + (self.centro_y - y) ** 2) ** 0.5

    def desenhar(self, canvas, dash=None):
        canvas.create_oval(self.centro_x - self.raio, self.centro_y - self.raio,
                           self.centro_x + self.raio, self.centro_y + self.raio,
                           outline=self.cor_borda, fill=self.cor_preenchimento, dash=dash)

    def incompleta(self):
        return self.raio == 0