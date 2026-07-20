from Modelo.Figura.Figuras import Figuras
from Controlador.controlador_desenho import ControladorDesenho, FABRICA_FIGURAS
from Visao.JanelaPrincipal import JanelaPrincipal

if __name__ == "__main__":
    modelo = Figuras()
    controlador = ControladorDesenho(modelo)

    tipos_de_figura = list(FABRICA_FIGURAS.keys())
    view = JanelaPrincipal(controlador, tipos_de_figura)

    controlador.definir_view(view)

    view.iniciar()