# controlador_estilo.py
from tkinter import colorchooser

class ControladorEstiloMixin:
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