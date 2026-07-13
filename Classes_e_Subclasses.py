# Hierarquia de Figuras

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

# Subclasses de Figura 
class Rabisco(Figura):
    def __init__(self, x, y, cor_borda, cor_preenchimento):
        super().__init__(cor_borda, cor_preenchimento)
        self.pontos = [(x, y)]

    def atualizar(self, x, y):
        self.pontos.append((x, y))

    def desenhar(self, canvas, dash=None):
        canvas.create_line(self.pontos, fill=self.cor_borda, dash=dash)

    def incompleta(self):
        return len(self.pontos) <= 1
    
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


#Subclasses de FiguraDoisPontos 

class Linha(FiguraDoisPontos):
    def desenhar(self, canvas, dash=None):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=self.cor_borda, dash=dash)


class Oval(FiguraDoisPontos):
    def desenhar(self, canvas, dash=None):
        canvas.create_oval(self.x1, self.y1, self.x2, self.y2,
                           outline=self.cor_borda, fill=self.cor_preenchimento, dash=dash)


class Retangulo(FiguraDoisPontos):
    def desenhar(self, canvas, dash=None):
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2,
                                outline=self.cor_borda, fill=self.cor_preenchimento, dash=dash)