from ..Subclasses_Figura.FiguraDoisPontos import FiguraDoisPontos

class Linha(FiguraDoisPontos):
    def desenhar(self, canvas, dash=None):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=self.cor_borda, dash=dash)