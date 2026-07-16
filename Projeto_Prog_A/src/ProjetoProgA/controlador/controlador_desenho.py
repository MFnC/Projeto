"""
RASCUNHO do Controlador - criado só para permitir testar a View
(visao) integrada ao Modelo de verdade.
"""
from tkinter import colorchooser
from Modelo.Figura.Subclasses_Figura.Rabisco import Rabisco
from Modelo.Figura.Subclasses_Figura.Circulo import Circulo
from Modelo.Figura.Subclasses_FiguraDoisPontos.Linha import Linha
from Modelo.Figura.Subclasses_FiguraDoisPontos.Oval import Oval
from Modelo.Figura.Subclasses_FiguraDoisPontos.Retangulo import Retangulo

 
# Associa o texto do menu a classe correspondente
FABRICA_FIGURAS = {
    'LINHA': Linha,
    'RABISCO': Rabisco,
    'CÍRCULO': Circulo,
    'OVAL': Oval,
    'RETANGULO': Retangulo
}
 
class ControladorDesenho:
 
    def __init__(self, figuras_modelo):
        self.figuras_modelo = figuras_modelo
        self.figura_nova = None
        self.view = None  # setado depois, via definir_view()
 
        self.cor_borda = "#000000"
        self.cor_preenchimento = ""
 
    def definir_view(self, view):
        self.view = view
 
    # Eventos de mouse (encaminhados pela View)
 
    def mouse_pressionado(self, event):
        classe = FABRICA_FIGURAS[self.view.tipo_figura_selecionado()]
        self.figura_nova = classe(event.x, event.y, self.cor_borda, self.cor_preenchimento)
 
    def mouse_movido(self, event):
        if self.figura_nova is None:
            return
        self.figura_nova.atualizar(event.x, event.y)
        self.view.redesenhar(self.figuras_modelo.obter_figuras(), self.figura_nova)
 
    def mouse_solto(self, event):
        if self.figura_nova is None:
            return
        if not self.figura_nova.incompleta():
            self.figuras_modelo.adicionar(self.figura_nova)
        self.figura_nova = None
        self.view.redesenhar(self.figuras_modelo.obter_figuras(), None)
 
    # Eventos de botao (encaminhados pela View)
 
    def borda_clicada(self, event):
        cor = colorchooser.askcolor(initialcolor=self.cor_borda)[1]
        if cor:
            self.cor_borda = cor
            self.view.atualizar_cor_borda(cor)
 
    def preenchimento_clicado(self, event):
        cor_inicial = self.cor_preenchimento if self.cor_preenchimento else "#ffffff"
        cor = colorchooser.askcolor(initialcolor=cor_inicial)[1]
        if cor:
            self.cor_preenchimento = cor
            self.view.atualizar_cor_preenchimento(cor)
 
    def preenchimento_resetado(self, event):
        self.cor_preenchimento = ""
        self.view.resetar_indicador_preenchimento()
 
    def tema_clicado(self):
        if self.view.cor_de_fundo_atual() == '#ffffff':
            self.view.aplicar_tema_escuro()
        else:
            self.view.aplicar_tema_claro()
