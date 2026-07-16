from ..Figura import Figura

class Poligono(Figura):
    def __init__(self, x, y, cor_borda, cor_preenchimento):
        super().__init__(cor_borda, cor_preenchimento)

        # Lista de vértices
        self.pontos = [(x, y)]

        # Posição temporária do mouse
        self.x_temp = x
        self.y_temp = y

        # Indica se o polígono foi finalizado
        self.finalizado = False

    def atualizar(self, x, y):
        self.x_temp = x
        self.y_temp = y

    def adicionar_vertice(self, x, y):
        self.pontos.append((x, y))

    def finalizar(self):
        self.finalizado = True

    def desenhar(self, canvas, dash=None):
        coordenadas = []

        for x, y in self.pontos:
            coordenadas.extend([x, y])

        if self.finalizado:
            canvas.create_polygon(
                coordenadas,
                outline=self.cor_borda,
                fill=self.cor_preenchimento,
                dash=dash
            )
        else:
            # Mostra uma prévia até o mouse
            coords = coordenadas + [self.x_temp, self.y_temp]

            canvas.create_line(
                coords,
                fill=self.cor_borda,
                dash=dash
            )

    def incompleta(self):
        return not self.finalizado