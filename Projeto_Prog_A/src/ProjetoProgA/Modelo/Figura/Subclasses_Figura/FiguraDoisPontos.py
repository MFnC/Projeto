from Modelo.Figura.Figura  import Figura

# Subclasse FiguraDoisPontos de Figura 

class FiguraDoisPontos(Figura):
    def __init__(self, x, y, cor_borda, cor_preenchimento):
        super().__init__(cor_borda, cor_preenchimento)
        self.x1 = x
        self.y1 = y
        self.x2 = x
        self.y2 = y

    def atualizar(self, x, y):
        self.x2 = x
        self.y2 = y

    def incompleta(self):
        return (self.x1, self.y1) == (self.x2, self.y2)

#FiguraDoisPontos é uma classe que herda de Figura e fornece a 
# estrutura comum para figuras definidas por um ponto inicial e um ponto final, 
# como linha e retângulo.