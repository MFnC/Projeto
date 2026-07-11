from tkinter import *
from tkinter import ttk
from tkinter import colorchooser

# Salva o clique inicial do mouse para começar a desenhar
def iniciar_figura_nova(event): 
    global figura_nova
    if tipo_figura_var.get() == 'LINHA':
        figura_nova = ("linha", (event.x, event.y, event.x, event.y), cor_borda, cor_preenchimento)
    elif  tipo_figura_var.get() == 'RABISCO': 
        figura_nova = ("rabisco", [(event.x, event.y)], cor_borda, cor_preenchimento)
    elif tipo_figura_var.get() == 'CÍRCULO':
        figura_nova = ('circulo', (event.x, event.y, 0), cor_borda, cor_preenchimento)
    elif tipo_figura_var.get() == 'OVAL':
        figura_nova = ('oval', (event.x, event.y, event.x, event.y), cor_borda, cor_preenchimento)
    elif tipo_figura_var.get() == 'RETANGULO':
        figura_nova = ("retangulo", (event.x, event.y, event.x, event.y), cor_borda, cor_preenchimento)


# Atualiza as coordenadas enquanto o usuário arrasta o mouse
def atualizar_figura_nova(event):
    global figura_nova
    
    if figura_nova is None:
        return
        
    if figura_nova[0] == "rabisco":
        figura_nova[1].append((event.x, event.y))
    elif figura_nova[0] == "linha": 
        figura_nova = ("linha", (figura_nova[1][0], 
                                 figura_nova[1][1], 
                                 event.x, event.y), figura_nova[2], figura_nova[3])
    elif figura_nova[0] == "circulo":
         raio = ((figura_nova[1][0] - event.x)**2 + (figura_nova[1][1] - event.y)**2)**0.5
         figura_nova = ("circulo", (figura_nova[1][0], figura_nova[1][1], raio), figura_nova[2], figura_nova[3])
    elif figura_nova[0] == "oval":
        figura_nova = ("oval", (figura_nova[1][0], figura_nova[1][1], event.x, event.y), figura_nova[2], figura_nova[3])
    elif figura_nova[0] == "retangulo":
        figura_nova = ("retangulo", (figura_nova[1][0],
                                     figura_nova[1][1],
                                     event.x, event.y), figura_nova[2], figura_nova[3])
    desenhar_figuras()
    desenhar_figura_nova()
    

# Salva a figura de vez na lista quando solta o clique
def incluir_figura_nova(event): 
    global figura_nova
    if figura_nova is None:
        return
    if not incompleta(figura_nova): 
        figuras.append(figura_nova) 
    desenhar_figuras()

# Limpa o canvas e redesenha todas as figuras salvas na lista
def desenhar_figuras():
    canvas.delete("all")
    for fig, values, borda, preenchimento in figuras:
        if fig == "linha":
            canvas.create_line(values[0], values[1], values[2], values[3], fill= borda)
        elif fig == "rabisco":
            canvas.create_line(values, fill= borda)
        elif fig == "circulo":
            canvas.create_oval(values[0] - values[2], values[1] - values[2],
                               values[0] + values[2], values[1] + values[2],
                               outline= borda, fill= preenchimento)
        elif fig == "oval":
            canvas.create_oval(values[0], values[1], values[2], values[3],
                               outline= borda, fill= preenchimento)
        elif fig == "retangulo":
            canvas.create_rectangle(values[0], values[1], values[2], values[3],
                                    outline= borda, fill= preenchimento)


# Desenha a figura atual em tempo real usando contorno pontilhado (dash)
def desenhar_figura_nova():
    if figura_nova is None:
        return
    fig, values = figura_nova[0], figura_nova[1]
    if fig == "linha":
        canvas.create_line(values[0], values[1], values[2], values[3], dash=(4, 2))
    elif fig == "rabisco":
        canvas.create_line(values, dash=(4, 2))
    elif fig == "circulo":
        canvas.create_oval(values[0] - values[2], values[1] - values[2],
                           values[0] + values[2], values[1] + values[2], dash=(4, 2))
    elif fig == "oval":
        canvas.create_oval(values[0], values[1], values[2], values[3], dash=(4, 2))
    elif fig == "retangulo":
        canvas.create_rectangle(values[0], values[1], values[2], values[3], dash=(4, 2))

# Validação para saber se a figura tem tamanho maior que zero
def incompleta(figura):
    fig, values = figura[0], figura[1]
    if fig == "linha":
        return (values[0], values[1]) == (values[2], values[3])
    elif fig == "rabisco":
        return len(values) <= 1
    elif fig == "circulo":
        return values[2] == 0
    elif fig == "oval":
        return (values[0], values[1]) == (values[2], values[3])
    elif fig == "retangulo":
        return (values[0], values[1]) == (values[2], values[3])
    
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

figuras = []       
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
option_menu = ttk.OptionMenu(frame, tipo_figura_var, 'LINHA', 'LINHA','RABISCO', 'CÍRCULO', 'OVAL', 'RETANGULO')
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
indicador_preenchimento.bind("<Button-3>", reset_color) # Clique direito do mouse reseta a cor

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

root.mainloop()