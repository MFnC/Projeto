from ..Subclasses_Figura.FiguraDoisPontos import FiguraDoisPontos

class Retangulo(FiguraDoisPontos):
    def desenhar(self, canvas, dash=None):
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2,
                                outline=self.cor_borda, fill=self.cor_preenchimento, dash=dash)