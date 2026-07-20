# controlador_arquivo.py
import json
from tkinter import filedialog

from Modelo.Figura.Subclasses_Figura import Rabisco, Circulo, Poligono
from Modelo.Figura.Subclasses_FiguraDoisPontos import Linha, Oval, Retangulo

# Mapeia o nome da classe (texto) para a classe em si. Usado para
# reconstruir os objetos corretos ao carregar um arquivo salvo.
CLASSES_POR_NOME = {
    'Linha': Linha,
    'Rabisco': Rabisco,
    'Circulo': Circulo,
    'Oval': Oval,
    'Retangulo': Retangulo,
    'Poligono': Poligono,
}

def figura_para_dict(figura):
    return {
        "classe": type(figura).__name__,
        "atributos": vars(figura),
    }

def dict_para_figura(dados):
    classe = CLASSES_POR_NOME[dados["classe"]]
    figura = object.__new__(classe)
    figura.__dict__.update(dados["atributos"])
    return figura

class ControladorArquivoMixin:
    def salvar_clicado(self):
        caminho = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("Arquivo JSON", "*.json")],
            title="Salvar desenho como..."
        )
        if not caminho:
            return

        figuras_salvas = [
            figura_para_dict(figura)
            for figura in self.figuras_modelo.obter_figuras()
        ]

        with open(caminho, "w", encoding="utf-8") as arquivo:
            json.dump({"figuras": figuras_salvas}, arquivo, indent=2)

    def abrir_clicado(self):
        caminho = filedialog.askopenfilename(
            filetypes=[("Arquivo JSON", "*.json")],
            title="Abrir desenho..."
        )
        if not caminho:
            return

        with open(caminho, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        figuras_carregadas = [
            dict_para_figura(item) for item in dados.get("figuras", [])
        ]

        self.figuras_modelo.carregar(figuras_carregadas)
        self.figura_nova = None
        self.view.redesenhar(self.figuras_modelo.obter_figuras(), None)