from ..Subclasses_Figura.FiguraDoisPontos import FiguraDoisPontos

class Triangulo(FiguraDoisPontos):
    def desenhar(self, canvas, dash=None):
        cx = (self.x1 + self.x2) / 2
        pontos = [
            cx, self.y1,
            self.x2, self.y2,
            self.x1, self.y2
        ]
        canvas.create_polygon(pontos, outline=self.cor_borda, fill=self.cor_preenchimento, dash=dash)