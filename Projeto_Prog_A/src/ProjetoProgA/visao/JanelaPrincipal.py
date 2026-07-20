from tkinter import Tk, Frame, StringVar, Label, Canvas, W, E
from tkinter import ttk

class JanelaPrincipal:
    def __init__(self, controlador, tipos_de_figura):

        self.controlador = controlador

        self.root = Tk()
        self.root.title("Paint")
        self.root.geometry("860x680")
        self.root.configure(bg='#ffffff')

        self._fonte_moderna = ('Segoe UI', 10, 'normal')
        self._construir_estilo()
        self._construir_widgets(tipos_de_figura)
        self._conectar_eventos()

    # Construção da interface

    def _construir_estilo(self):
        self.style = ttk.Style()
        self.style.theme_use('default')

        self.style.configure('TLabel', background='#ffffff', foreground='#333333', font=self._fonte_moderna)
        self.style.configure('TMenubutton', background='#f0f0f0', foreground='#333333', font=self._fonte_moderna,
                             borderwidth=0, padding=6, relief="flat", focuscolor="")
        self.style.configure('TButton', background='#f0f0f0', foreground='#333333', font=self._fonte_moderna,
                             borderwidth=0, padding=6, relief="flat", focuscolor="")

        self.style.map('TMenubutton', background=[('active', '#e4e4e4')], foreground=[('active', '#333333')])
        self.style.map('TButton', background=[('active', '#e4e4e4')], foreground=[('active', '#333333')])

    def _construir_widgets(self, tipos_de_figura):
        self.frame = Frame(self.root, bg='#ffffff')
        paddings = {'padx': 5, 'pady': 10}

        # Alinhamento dos componentes na barra superior usando grid
        label = ttk.Label(self.frame, text='FIGURA:')
        label.grid(column=0, row=0, sticky=W, **paddings)

        self.tipo_figura_var = StringVar(self.root)
        self.tipo_figura_var.set(tipos_de_figura[0])
        self.option_menu = ttk.OptionMenu(self.frame, self.tipo_figura_var,
                                          tipos_de_figura[0], *tipos_de_figura)
        self.option_menu.grid(column=1, row=0, sticky=W, **paddings)

        label_borda = ttk.Label(self.frame, text='BORDA:')
        label_borda.grid(column=2, row=0, sticky=W, padx=(15, 2), pady=10)

        self.indicador_borda = Label(self.frame, bg="#000000", width=3, height=1, relief="sunken", bd=1)
        self.indicador_borda.grid(column=3, row=0, sticky=W, padx=(0, 15), pady=10)

        label_preenchimento = ttk.Label(self.frame, text='PREENCHIMENTO:')
        label_preenchimento.grid(column=4, row=0, sticky=W, padx=(0, 2), pady=10)

        self.indicador_preenchimento = Label(self.frame, bg='#ffffff', width=3, height=1, relief="sunken", bd=1)
        self.indicador_preenchimento.grid(column=5, row=0, sticky=W, padx=(0, 5), pady=10)

        self.frame.columnconfigure(6, weight=1)

        label_tema = ttk.Label(self.frame, text='TEMA:')
        label_tema.grid(column=7, row=0, sticky=E, padx=(15, 2), pady=10)

        self.botao_tema = ttk.Button(self.frame, text="CLARO")
        self.botao_tema.grid(column=8, row=0, sticky=W, pady=10)

        # Botoes de Salvar e Abrir arquivo
        self.botao_salvar = ttk.Button(self.frame, text="SALVAR")
        self.botao_salvar.grid(column=9, row=0, sticky=W, padx=(15, 0), pady=10)

        self.botao_abrir = ttk.Button(self.frame, text="ABRIR")
        self.botao_abrir.grid(column=10, row=0, sticky=W, padx=(5, 0), pady=10)

        self.canvas = Canvas(self.frame, bg='#ffffff', width=680, height=580,
                             highlightthickness=1, highlightbackground='#e0e0e0', bd=0)
        self.canvas.grid(column=0, row=1, columnspan=11, sticky=W, pady=(15, 0))
        self.frame.pack(padx=20, pady=20)

    def _conectar_eventos(self):
        # Eventos de mouse no canvas encaminhados para o Controlador
        self.canvas.bind('<ButtonPress-1>', self.controlador.mouse_pressionado)
        self.canvas.bind('<B1-Motion>', self.controlador.mouse_movido)
        self.canvas.bind('<ButtonRelease-1>', self.controlador.mouse_solto)
        # Duplo-clique: usado para finalizar a construcao de um Poligono
        # (que e formado por varios cliques simples, um por vertice)
        self.canvas.bind('<Double-Button-1>', self.controlador.finalizar_poligono)
        # Movimento livre (sem botao pressionado): usado para a "linha
        # elastica" do Poligono, que acompanha o mouse entre um clique
        # e outro, mostrando onde o proximo vertice vai cair
        self.canvas.bind('<Motion>', self.controlador.mouse_movido_livre)

        # Eventos de botão também encaminhados para o Controlador
        self.indicador_borda.bind("<Button-1>", self.controlador.borda_clicada)
        self.indicador_preenchimento.bind("<Button-1>", self.controlador.preenchimento_clicado)
        self.indicador_preenchimento.bind("<Button-3>", self.controlador.preenchimento_resetado)
        self.botao_tema.configure(command=self.controlador.tema_clicado)
        self.botao_salvar.configure(command=self.controlador.salvar_clicado)
        self.botao_abrir.configure(command=self.controlador.abrir_clicado)

    # Métodos públicos chamados pelo Controlador para atualizar a tela

    def tipo_figura_selecionado(self):
        return self.tipo_figura_var.get()

    def redesenhar(self, figuras, figura_atual):
        self.canvas.delete("all")
        for figura in figuras:
            figura.desenhar(self.canvas)
        if figura_atual is not None:
            figura_atual.desenhar(self.canvas, dash=(4, 2))

    def atualizar_cor_borda(self, cor):
        self.indicador_borda.configure(bg=cor)

    def atualizar_cor_preenchimento(self, cor):
        self.indicador_preenchimento.configure(bg=cor)

    def resetar_indicador_preenchimento(self):
        cor_fundo_canvas = self.canvas.cget('bg')
        self.indicador_preenchimento.configure(bg=cor_fundo_canvas)

    def cor_de_fundo_atual(self):
        return self.canvas.cget('bg')

    def aplicar_tema_escuro(self):
        self.root.configure(bg='#1e1e1e')
        self.frame.configure(bg='#1e1e1e')
        self.canvas.configure(bg='#2d2d2d', highlightbackground='#1e1e1e')

        self.style.configure('TLabel', background='#1e1e1e', foreground='#ffffff')
        self.style.configure('TMenubutton', background='#3a3a3a', foreground='#ffffff', focuscolor="")
        self.style.configure('TButton', background='#3a3a3a', foreground='#ffffff', focuscolor="")

        self.style.map('TMenubutton', background=[('active', '#4a4a4a')], foreground=[('active', '#ffffff')])
        self.style.map('TButton', background=[('active', '#4a4a4a')], foreground=[('active', '#ffffff')])
        self.botao_tema.configure(text="ESCURO")

    def aplicar_tema_claro(self):
        self.root.configure(bg='#ffffff')
        self.frame.configure(bg='#ffffff')
        self.canvas.configure(bg='#ffffff', highlightbackground='#e0e0e0')

        self.style.configure('TLabel', background='#ffffff', foreground='#333333')
        self.style.configure('TMenubutton', background='#f0f0f0', foreground='#333333', focuscolor="")
        self.style.configure('TButton', background='#f0f0f0', foreground='#333333', focuscolor="")

        self.style.map('TMenubutton', background=[('active', '#e4e4e4')], foreground=[('active', '#333333')])
        self.style.map('TButton', background=[('active', '#e4e4e4')], foreground=[('active', '#333333')])
        self.botao_tema.configure(text="CLARO")

    def iniciar(self):
        self.root.mainloop()