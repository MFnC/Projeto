from abc import ABC, abstractmethod

from Modelo.Figura.Subclasses_Figura import Rabisco, Circulo, Poligono
from Modelo.Figura.Subclasses_FiguraDoisPontos import Linha, Oval, Retangulo

# --- CLASSE BASE DO STATE ---
class Ferramenta_state(ABC):
    def __init__(self, controlador):
        self.ctx = controlador  # Referência ao controlador principal (Contexto)

    @abstractmethod
    def pressionado(self, event): pass

    @abstractmethod
    def movido(self, event): pass

    @abstractmethod
    def movido_livre(self, event): pass

    @abstractmethod
    def solto(self, event): pass

    def duplo_clique(self, event): pass


# --- STATE PARA FORMAS PADRÃO ---
class FormaPadrao_state(Ferramenta_state):
    def __init__(self, controlador, classe_figura):
        super().__init__(controlador)
        self.classe_figura = classe_figura

    def pressionado(self, event):
        self.ctx.figura_nova = self.classe_figura(
            event.x, event.y, self.ctx.cor_borda, self.ctx.cor_preenchimento
        )

    def movido(self, event):
        if self.ctx.figura_nova:
            self.ctx.figura_nova.atualizar(event.x, event.y)
            self.ctx.view.redesenhar(self.ctx.figuras_modelo.obter_figuras(), self.ctx.figura_nova)

    def movido_livre(self, event):
        pass

    def solto(self, event):
        if self.ctx.figura_nova:
            if not self.ctx.figura_nova.incompleta():
                self.ctx.figuras_modelo.adicionar(self.ctx.figura_nova)
            self.ctx.figura_nova = None
            self.ctx.view.redesenhar(self.ctx.figuras_modelo.obter_figuras(), None)


# --- STATE EXCLUSIVO DO POLÍGONO ---
class Poligono_state(Ferramenta_state):
    def pressionado(self, event):
        if self.ctx.figura_nova is None:
            self.ctx.figura_nova = Poligono(
                event.x, event.y, self.ctx.cor_borda, self.ctx.cor_preenchimento
            )
        else:
            self.ctx.figura_nova.adicionar_vertice(event.x, event.y)
        self.ctx.view.redesenhar(self.ctx.figuras_modelo.obter_figuras(), self.ctx.figura_nova)

    def movido(self, event):
        pass

    def movido_livre(self, event):
        if self.ctx.figura_nova:
            self.ctx.figura_nova.atualizar(event.x, event.y)
            self.ctx.view.redesenhar(self.ctx.figuras_modelo.obter_figuras(), self.ctx.figura_nova)

    def solto(self, event):
        pass

    def duplo_clique(self, event):
        if self.ctx.figura_nova is None:
            return

        pontos_filtrados = []
        for p in self.ctx.figura_nova.pontos:
            if not pontos_filtrados or p != pontos_filtrados[-1]:
                pontos_filtrados.append(p)
        self.ctx.figura_nova.pontos = pontos_filtrados

        if len(self.ctx.figura_nova.pontos) >= 3:
            self.ctx.figura_nova.finalizar()
            self.ctx.figuras_modelo.adicionar(self.ctx.figura_nova)
            
        self.ctx.figura_nova = None
        self.ctx.view.redesenhar(self.ctx.figuras_modelo.obter_figuras(), None)


# --- DICIONÁRIO AUXILIAR PARA TROCA DE STATES ---
MAPA_ESTADOS = {
    'LINHA': lambda ctx: FormaPadrao_state(ctx, Linha),
    'RABISCO': lambda ctx: FormaPadrao_state(ctx, Rabisco),
    'CÍRCULO': lambda ctx: FormaPadrao_state(ctx, Circulo),
    'OVAL': lambda ctx: FormaPadrao_state(ctx, Oval),
    'RETANGULO': lambda ctx: FormaPadrao_state(ctx, Retangulo),
    'POLIGONO': lambda ctx: Poligono_state(ctx)
}

# Mantemos isso aqui para a sua Main.py continuar importando sem dar erro
FABRICA_FIGURAS = {k: None for k in MAPA_ESTADOS.keys()}


# --- MIXIN QUE COMPORTA A MÁQUINA DE ESTADOS DO MOUSE ---
class ControladorMouseMixin:
    def atualizar_state(self):
        """Busca a ferramenta selecionada na View e altera o State atual"""
        tipo = self.view.tipo_figura_selecionado()
        if tipo in MAPA_ESTADOS:
            self.state_atual = MAPA_ESTADOS[tipo](self)

    def mouse_pressionado(self, event):
        self.atualizar_state()  # Atualiza o state dinamicamente antes do clique
        self.state_atual.pressionado(event)
 
    def mouse_movido(self, event):
        self.state_atual.movido(event)

    def mouse_movido_livre(self, event):
        self.state_atual.movido_livre(event)
 
    def mouse_solto(self, event):
        self.state_atual.solto(event)

    def finalizar_poligono(self, event):
        self.state_atual.duplo_clique(event)