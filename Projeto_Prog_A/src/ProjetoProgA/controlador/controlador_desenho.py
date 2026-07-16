from tkinter import colorchooser

# Importando as classes do modelo que o professor pediu
from Modelo.Figura.Subclasses_Figura.Rabisco import Rabisco
from Modelo.Figura.Subclasses_Figura.Circulo import Circulo
from Modelo.Figura.Subclasses_Figura.Poligono import Poligono
from Modelo.Figura.Subclasses_FiguraDoisPontos.Linha import Linha
from Modelo.Figura.Subclasses_FiguraDoisPontos.Oval import Oval
from Modelo.Figura.Subclasses_FiguraDoisPontos.Retangulo import Retangulo

# Dicionario pra associar o texto que vem da tela com a classe certa
FABRICA_FIGURAS = {
    'LINHA': Linha,
    'RABISCO': Rabisco,
    'CÍRCULO': Circulo,
    'OVAL': Oval,
    'RETANGULO': Retangulo,
    'POLIGONO': Poligono
}

class ControladorDesenho:
 
    def __init__(self, figuras_modelo):
        self.figuras_modelo = figuras_modelo
        self.figura_nova = None
        self.view = None  # vai ser setado depois na Main
 
        self.cor_borda = "#000000"
        self.cor_preenchimento = ""
 
    def definir_view(self, view):
        self.view = view
 
    # --- Cliques e movimentos do mouse no Canvas ---
 
    def mouse_pressionado(self, event):
        tipo_selecionado = self.view.tipo_figura_selecionado()

        # O poligono e chato pq precisa de varios cliques, entao trata separado
        if tipo_selecionado == "POLIGONO":
            if self.figura_nova is None:
                self.figura_nova = Poligono(
                    event.x, event.y, 
                    self.cor_borda, self.cor_preenchimento
                )
            else:
                self.figura_nova.adicionar_vertice(event.x, event.y)
            
            # manda a tela desenhar o poligono em andamento
            self.view.redesenhar(self.figuras_modelo.obter_figuras(), self.figura_nova)
            return

        # Para as outras formas cria normal
        classe = FABRICA_FIGURAS[tipo_selecionado]
        self.figura_nova = classe(event.x, event.y, self.cor_borda, self.cor_preenchimento)
 
    def mouse_movido(self, event):
        # Atualiza a prévia do desenho enquanto o mouse arrasta
        if self.figura_nova is None:
            return
        self.figura_nova.atualizar(event.x, event.y)
        self.view.redesenhar(self.figuras_modelo.obter_figuras(), self.figura_nova)
 
    def mouse_solto(self, event):
        if self.figura_nova is None:
            return
            
        # Ignora se for poligono pq ele so fecha no duplo clique
        if self.view.tipo_figura_selecionado() == "POLIGONO":
            return

        # Se nao estiver vazia, adiciona na lista do modelo
        if not self.figura_nova.incompleta():
            self.figuras_modelo.adicionar(self.figura_nova)
        self.figura_nova = None
        self.view.redesenhar(self.figuras_modelo.obter_figuras(), None)

    def finalizar_poligono(self, event):
        # Duplo clique fecha a forma e salva o poligono
        if self.figura_nova is None:
            return

        if self.view.tipo_figura_selecionado() != "POLIGONO":
            return

        self.figura_nova.finalizar()
        self.figuras_modelo.adicionar(self.figura_nova)
        self.figura_nova = None
        self.view.redesenhar(self.figuras_modelo.obter_figuras(), None)
 
    # --- Cliques nos botoes de cores e tema ---
 
    def borda_clicada(self, event):
        # Abre a caixinha de escolher cor do tkinter
        cor = colorchooser.askcolor(initialcolor=self.cor_borda)[1]
        if cor:
            self.cor_borda = cor
            self.view.atualizar_cor_borda(cor)
 
    def preenchimento_clicado(self, event):
        # Abre o seletor pra cor de preenchimento
        cor_inicial = self.cor_preenchimento if self.cor_preenchimento else "#ffffff"
        cor = colorchooser.askcolor(initialcolor=cor_inicial)[1]
        if cor:
            self.cor_preenchimento = cor
            self.view.atualizar_cor_preenchimento(cor)
 
    def preenchimento_resetado(self, event):
        # Clique direito reseta para sem preenchimento
        self.cor_preenchimento = ""
        self.view.resetar_indicador_preenchimento()
 
    def tema_clicado(self):
        # Altera entre o fundo escuro e o claro
        if self.view.cor_de_fundo_atual() == '#ffffff':
            self.view.aplicar_tema_escuro()
            # Se nao tiver cor de preenchimento, camufla com o fundo do modo escuro
            if self.cor_preenchimento == "":
                self.view.atualizar_cor_preenchimento('#2d2d2d')
        else:
            self.view.aplicar_tema_claro()
            # Camufla com o fundo claro
            if self.cor_preenchimento == "":
                self.view.atualizar_cor_preenchimento('#ffffff')