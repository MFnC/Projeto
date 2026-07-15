from ..Subclasses_Figura.FiguraDoisPontos import FiguraDoisPontos

class Pentagono(FiguraDoisPontos):
    def desenhar(self, canvas, dash=None):
        cx = (self.x1 + self.x2) / 2
        cy = (self.y1 + self.y2) / 2
        rx = (self.x2 - self.x1) / 2
        ry = (self.y2 - self.y1) / 2
        pontos = [
            cx, cy - ry,
            cx + rx * 0.9511, cy - ry * 0.3090,
            cx + rx * 0.5878, cy + ry * 0.8090,
            cx - rx * 0.5878, cy + ry * 0.8090,
            cx - rx * 0.9511, cy - ry * 0.3090
        ]
        canvas.create_polygon(pontos, outline=self.cor_borda, fill=self.cor_preenchimento, dash=dash)