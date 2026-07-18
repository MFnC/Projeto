from tkinter import colorchooser

class ControladorEstiloMixin:
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
            if self.cor_preenchimento == "":
                self.view.atualizar_cor_preenchimento('#2d2d2d')
        else:
            self.view.aplicar_tema_claro()
            if self.cor_preenchimento == "":
                self.view.atualizar_cor_preenchimento('#ffffff')