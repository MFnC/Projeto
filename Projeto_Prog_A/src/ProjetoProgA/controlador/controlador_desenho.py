# controlador_desenho.py
from .controlador_mouse import ControladorMouseMixin, FABRICA_FIGURAS  # <--- IMPORTADO AQUI
from .controlador_estilo import ControladorEstiloMixin

class ControladorDesenho(ControladorMouseMixin, ControladorEstiloMixin):
 
    def __init__(self, figuras_modelo):
        self.figuras_modelo = figuras_modelo
        self.figura_nova = None
        self.view = None  # vai ser setado depois na Main
 
        self.cor_borda = "#000000"
        self.cor_preenchimento = ""
 
    def definir_view(self, view):
        self.view = view