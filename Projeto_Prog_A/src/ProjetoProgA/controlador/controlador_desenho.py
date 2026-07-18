from .controlador_mouse import ControladorMouseMixin, FABRICA_FIGURAS
from .controlador_estilo import ControladorEstiloMixin

class ControladorDesenho(ControladorMouseMixin, ControladorEstiloMixin):
 
    def __init__(self, figuras_modelo):
        self.figuras_modelo = figuras_modelo
        self.figura_nova = None
        self.view = None 
 
        self.cor_borda = "#000000"
        self.cor_preenchimento = ""
        
        # Variável que guarda o State ativo (Ferramenta_state)
        self.state_atual = None
 
    def definir_view(self, view):
        self.view = view
        self.atualizar_state()  # Inicializa o State padrão do sistema