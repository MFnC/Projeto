# controlador_mouse.py
from Modelo.Figura.Subclasses_Figura import Rabisco, Circulo, Poligono
from Modelo.Figura.Subclasses_FiguraDoisPontos import Linha, Oval, Retangulo

# Dicionario pra associar o texto que vem da tela com a classe certa
FABRICA_FIGURAS = {
    'LINHA': Linha,
    'RABISCO': Rabisco,
    'CÍRCULO': Circulo,
    'OVAL': Oval,
    'RETANGULO': Retangulo,
    'POLIGONO': Poligono
}

class ControladorMouseMixin:
    def mouse_pressionado(self, event):
        tipo_selecionado = self.view.tipo_figura_selecionado()

        # O poligono precisa de cliques simples alternados para adicionar vértices
        if tipo_selecionado == "POLIGONO":
            if self.figura_nova is None:
                self.figura_nova = Poligono(
                    event.x, event.y, 
                    self.cor_borda, self.cor_preenchimento
                )
            else:
                self.figura_nova.adicionar_vertice(event.x, event.y)
            
            # Manda a tela desenhar o poligono em andamento
            self.view.redesenhar(self.figuras_modelo.obter_figuras(), self.figura_nova)
            return

        # Para as outras formas cria normal
        classe = FABRICA_FIGURAS[tipo_selecionado]
        self.figura_nova = classe(event.x, event.y, self.cor_borda, self.cor_preenchimento)
 
    def mouse_movido(self, event):
        # Atualiza a prévia das outras figuras enquanto arrasta o mouse pressionado
        if self.figura_nova is None:
            return
        if self.view.tipo_figura_selecionado() == "POLIGONO":
            return
        self.figura_nova.atualizar(event.x, event.y)
        self.view.redesenhar(self.figuras_modelo.obter_figuras(), self.figura_nova)

    def mouse_movido_livre(self, event):
        # Desenha e estica a linha elástica temporária seguindo o mouse livremente
        if self.figura_nova is None:
            return
        if self.view.tipo_figura_selecionado() == "POLIGONO":
            self.figura_nova.atualizar(event.x, event.y)
            self.view.redesenhar(self.figuras_modelo.obter_figuras(), self.figura_nova)
 
    def mouse_solto(self, event):
        if self.figura_nova is None:
            return
            
        # IMPORTANTE: Ignora se for poligono para permitir o desenho com cliques soltos!
        if self.view.tipo_figura_selecionado() == "POLIGONO":
            return

        # Se nao estiver vazia, adiciona na lista do modelo
        if not self.figura_nova.incompleta():
            self.figuras_modelo.adicionar(self.figura_nova)
        self.figura_nova = None
        self.view.redesenhar(self.figuras_modelo.obter_figuras(), None)

    def finalizar_poligono(self, event):
        # Duplo clique fecha a forma e salva o poligono de forma limpa
        if self.figura_nova is None:
            return

        if self.view.tipo_figura_selecionado() != "POLIGONO":
            return

        # Filtra os pontos repetidos ou idênticos provocados pela sensibilidade do clique duplo
        pontos_filtrados = []
        for p in self.figura_nova.pontos:
            if not pontos_filtrados or p != pontos_filtrados[-1]:
                pontos_filtrados.append(p)
        
        self.figura_nova.pontos = pontos_filtrados

        # Só finaliza se tiver o mínimo de pontos válidos para fechar uma área
        if len(self.figura_nova.pontos) >= 3:
            self.figura_nova.finalizar()
            self.figuras_modelo.adicionar(self.figura_nova)
            
        self.figura_nova = None
        self.view.redesenhar(self.figuras_modelo.obter_figuras(), None)