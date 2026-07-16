from tkinter import *
from tkinter import ttk
from tkinter import colorchooser

# Importa a classe base Figura (Superclasse)
from Modelo.Figura import Figura

# Importa as subclasses de Figura
from Modelo.Figura.Subclasses_Figura import (
    FiguraDoisPontos,
    Rabisco,
    Circulo,
    Poligono
)

# Importa as subclasses de FiguraDoisPontos
from Modelo.Figura.Subclasses_FiguraDoisPontos import (
    Linha,
    Oval,
    Retangulo
)

# Associa o texto do menu à classe correspondente
FABRICA_FIGURAS = {
    'LINHA': Linha,
    'RABISCO': Rabisco,
    'CÍRCULO': Circulo,
    'OVAL': Oval,
    'RETANGULO': Retangulo,
    'POLIGONO': Poligono
}


# Eventos do Canvas

def iniciar_figura_nova(event):
    global figura_nova

    if tipo_figura_var.get() == "POLIGONO":

        if figura_nova is None:

            figura_nova = Poligono(
                event.x,
                event.y,
                cor_borda,
                cor_preenchimento
            )

        else:

            figura_nova.adicionar_vertice(
                event.x,
                event.y
            )

        desenhar_figuras()
        desenhar_figura_nova()
        return

    classe = FABRICA_FIGURAS[tipo_figura_var.get()]
    figura_nova = classe(
        event.x,
        event.y,
        cor_borda,
        cor_preenchimento
    )


def atualizar_figura_nova(event):
    global figura_nova
    if figura_nova is None:
        return
    figura_nova.atualizar(event.x, event.y)
    desenhar_figuras()
    desenhar_figura_nova()

def incluir_figura_nova(event):

    global figura_nova

    if figura_nova is None:
        return

    if tipo_figura_var.get() == "POLIGONO":
        return

    if not figura_nova.incompleta():

        figuras.adicionar(figura_nova)

    figura_nova = None

    desenhar_figuras()

def desenhar_figuras():
    canvas.delete("all")
    for figura in figuras.obter_figuras():
        figura.desenhar(canvas)

def desenhar_figura_nova():
    if figura_nova is None:
        return
    figura_nova.desenhar(canvas, dash=(4, 2))

def finalizar_poligono(event):

    global figura_nova

    if figura_nova is None:
        return

    if tipo_figura_var.get() != "POLIGONO":
        return

    figura_nova.finalizar()

    figuras.adicionar(figura_nova)

    figura_nova = None

    desenhar_figuras()


# Altera as cores da borda e preenchimento:
cor_borda = "#000000"
cor_preenchimento = ""

def PintarBorda(event):
    global cor_borda
    cor = colorchooser.askcolor(initialcolor=cor_borda)[1]
    if cor:
        cor_borda = cor
        indicador_borda.configure(bg=cor_borda)

def PintarPreenchimento(event):
    global cor_preenchimento

    cor_inicial = cor_preenchimento if cor_preenchimento else "#ffffff"
    cor = colorchooser.askcolor(initialcolor=cor_inicial)[1]
    if cor:
        cor_preenchimento = cor
        indicador_preenchimento.configure(bg=cor_preenchimento)

def reset_color(event):
    global cor_preenchimento
    cor_preenchimento = ""

    cor_fundo_canvas = canvas.cget('bg')
    indicador_preenchimento.configure(bg=cor_fundo_canvas)


# Função para alternar entre Modo Claro e Modo Escuro
def alternar_tema():
    if canvas.cget('bg') == '#ffffff':
        # --- Configurações do Modo Escuro ---
        root.configure(bg='#1e1e1e')
        frame.configure(bg='#1e1e1e')
        canvas.configure(bg='#2d2d2d', highlightbackground='#1e1e1e')

        style.configure('TLabel', background='#1e1e1e', foreground='#ffffff')
        style.configure('TMenubutton', background='#3a3a3a', foreground='#ffffff', focuscolor="")
        style.configure('TButton', background='#3a3a3a', foreground='#ffffff', focuscolor="")

        style.map('TMenubutton', background=[('active', '#4a4a4a')], foreground=[('active', '#ffffff')])
        style.map('TButton', background=[('active', '#4a4a4a')], foreground=[('active', '#ffffff')])
        botao_tema.configure(text="ESCURO")


        if cor_preenchimento == "":
            indicador_preenchimento.configure(bg='#2d2d2d')

    else:
        # --- Configurações do Modo Claro ---
        root.configure(bg='#ffffff')
        frame.configure(bg='#ffffff')
        canvas.configure(bg='#ffffff', highlightbackground='#e0e0e0')

        style.configure('TLabel', background='#ffffff', foreground='#333333')
        style.configure('TMenubutton', background='#f0f0f0', foreground='#333333', focuscolor="")
        style.configure('TButton', background='#f0f0f0', foreground='#333333', focuscolor="")

        style.map('TMenubutton', background=[('active', '#e4e4e4')], foreground=[('active', '#333333')])
        style.map('TButton', background=[('active', '#e4e4e4')], foreground=[('active', '#333333')])
        botao_tema.configure(text="CLARO")

        # Se estiver sem preenchimento, camufla com a cor do canvas claro
        if cor_preenchimento == "":
            indicador_preenchimento.configure(bg='#ffffff')


#******* MAIN *******#

# Importa a classe Dessenho
from Modelo.Figura.Figuras import Figuras 
figuras  = Figuras () 
figura_nova = None

root = Tk()
root.title("Paint")
root.geometry("740x680")
root.configure(bg='#ffffff')

FONTE_MODERNA = ('Segoe UI', 10, 'normal')

style = ttk.Style()
style.theme_use('default')

style.configure('TLabel', background='#ffffff', foreground='#333333', font=FONTE_MODERNA)
style.configure('TMenubutton', background='#f0f0f0', foreground='#333333', font=FONTE_MODERNA, borderwidth=0, padding=6, relief="flat", focuscolor="")
style.configure('TButton', background='#f0f0f0', foreground='#333333', font=FONTE_MODERNA, borderwidth=0, padding=6, relief="flat", focuscolor="")

style.map('TMenubutton', background=[('active', '#e4e4e4')], foreground=[('active', '#333333')])
style.map('TButton', background=[('active', '#e4e4e4')], foreground=[('active', '#333333')])

frame = Frame(root, bg='#ffffff')
paddings = {'padx': 5, 'pady': 10}

# Alinhamento dos componentes na barra superior usando grid
label = ttk.Label(frame, text='FIGURA:')
label.grid(column=0, row=0, sticky=W, **paddings)

tipo_figura_var = StringVar(root)
option_menu = ttk.OptionMenu(frame, tipo_figura_var, 'LINHA', 'LINHA', 'RABISCO', 'CÍRCULO', 'OVAL', 'RETANGULO', 'POLIGONO')
option_menu.grid(column=1, row=0, sticky=W, **paddings)

# --- SELETORES DE COR DA IMAGEM ---
label_borda = ttk.Label(frame, text='BORDA:')
label_borda.grid(column=2, row=0, sticky=W, padx=(15, 2), pady=10)

# Caixinha indicadora para Cor da Borda
indicador_borda = Label(frame, bg=cor_borda, width=3, height=1, relief="sunken", bd=1)
indicador_borda.grid(column=3, row=0, sticky=W, padx=(0, 15), pady=10)
indicador_borda.bind("<Button-1>", PintarBorda)

label_preenchimento = ttk.Label(frame, text='PREENCHIMENTO:')
label_preenchimento.grid(column=4, row=0, sticky=W, padx=(0, 2), pady=10)

# Caixinha indicadora para Cor de Preenchimento (Inicia branca, mimetizando o fundo do canvas claro)
indicador_preenchimento = Label(frame, bg='#ffffff', width=3, height=1, relief="sunken", bd=1)
indicador_preenchimento.grid(column=5, row=0, sticky=W, padx=(0, 5), pady=10)
indicador_preenchimento.bind("<Button-1>", PintarPreenchimento)
indicador_preenchimento.bind("<Button-3>", reset_color)  # Clique direito do mouse reseta a cor

# Espaçador para empurrar o tema para o canto direito
frame.columnconfigure(6, weight=1)

label_tema = ttk.Label(frame, text='TEMA:')
label_tema.grid(column=7, row=0, sticky=E, padx=(15, 2), pady=10)

botao_tema = ttk.Button(frame, text="CLARO", command=alternar_tema)
botao_tema.grid(column=8, row=0, sticky=W, pady=10)

# Área de desenho
canvas = Canvas(frame, bg='#ffffff', width=680, height=580, highlightthickness=1, highlightbackground='#e0e0e0', bd=0)
canvas.grid(column=0, row=1, columnspan=9, sticky=W, pady=(15, 0))
frame.pack(padx=20, pady=20)

canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)
canvas.bind("<Double-Button-1>", finalizar_poligono)

root.mainloop()
