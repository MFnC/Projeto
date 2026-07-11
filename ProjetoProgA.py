from tkinter import *
from tkinter import ttk
from tkinter import colorchooser

# Quando mouse é pressionado
def iniciar_figura_nova(event): 
    global figura_nova 
    if tipo_figura_var.get() == 'Linha':
        figura_nova = ("linha", (event.x, event.y, event.x, event.y), cor_borda, cor_preenchimento)
    elif  tipo_figura_var.get() == 'Rabisco': 
        figura_nova = ("rabisco", [(event.x, event.y)], cor_borda, cor_preenchimento)
    elif tipo_figura_var.get() == 'Círculo':
        figura_nova = ('circulo', (event.x, event.y, 0), cor_borda, cor_preenchimento)
    elif tipo_figura_var.get() == 'Retangulo':
        figura_nova = ("retangulo", (event.x, event.y, event.x, event.y), cor_borda, cor_preenchimento)

# Quando mouse é movido com o botão pressionado
def atualizar_figura_nova(event):
    global figura_nova
    if figura_nova[0] == "rabisco":
        figura_nova[1].append((event.x, event.y))
    elif figura_nova[0] == "linha": 
        figura_nova = ("linha", (figura_nova[1][0], figura_nova[1][1], 
                                 event.x, event.y),
                                 figura_nova[2], figura_nova[3])
    elif figura_nova[0] == "circulo":
         raio = ((figura_nova[1][0] - event.x)**2 + (figura_nova[1][1] - event.y)**2)**0.5
         figura_nova = ("circulo", (figura_nova[1][0], figura_nova[1][1], raio), 
                        figura_nova[2], figura_nova[3])
    elif figura_nova[0] == "retangulo":
        figura_nova = ("retangulo", (figura_nova[1][0], figura_nova[1][1],
                                     event.x, event.y), 
                                     figura_nova[2],figura_nova[3])
    desenhar_figuras()
    desenhar_figura_nova()
    
# Quando mouse é solto
def incluir_figura_nova(event): 
    if not incompleta(figura_nova): 
        figuras.append(figura_nova) 
    desenhar_figuras()

def desenhar_figuras():
    canvas.delete("all")
    for fig, values, borda, preenchimento in figuras:
        if fig == "linha":
            canvas.create_line(values[0], 
                               values[1], 
                               values[2], 
                               values[3],
                               fill=  borda)
        elif fig == "rabisco":
            canvas.create_line(values, fill= borda)
        elif fig == "circulo":
            canvas.create_oval(values[0] - values[2], 
                               values[1] - values[2],
                               values[0] + values[2], 
                               values[1] + values[2],
                               outline=borda,
                               fill=preenchimento)
        elif fig == "retangulo":
            canvas.create_rectangle(values[0], values[1], 
                                    values[2], values[3],
                                    outline=borda, 
                                    fill=preenchimento)

def desenhar_figura_nova():
    fig, values, borda, preenchimento = figura_nova
    if fig == "linha":
        canvas.create_line(values[0], values[1], 
                           values[2], values[3], 
                           dash=(4, 2))
    elif fig == "rabisco":
        canvas.create_line(values, dash=(4, 2))
    elif fig == "circulo":
        canvas.create_oval(values[0] - values[2], 
                           values[1] - values[2],
                           values[0] + values[2], 
                           values[1] + values[2], 
                           dash=(4, 2))
    elif fig == "retangulo":
        canvas.create_rectangle(values[0], values[1], 
                                values[2], values[3], 
                                dash=(4, 2))

def incompleta(figura):
    fig, values, borda, preenchimento = figura
    if fig == "linha":
        return (values[0], values[1]) == (values[2], values[3])
    elif fig == "rabisco":
        return len(values) <= 1
    elif fig == "circulo":
        return values[2] == 0
    elif fig == "retangulo":
        return (values[0], values[1]) == (values[2], values[3])

# Altera as cores da borda e preenchimento:

cor_borda = "Black"
cor_preenchimento = ""
def PintarBorda():
    global cor_borda
    cor = colorchooser.askcolor()[1]
    if cor:
        cor_borda = cor

def PintarPreenchimento():
    global cor_preenchimento
    cor = colorchooser.askcolor()[1]
    if cor:
        cor_preenchimento = cor

def reset_color():
    global cor_preenchimento
    cor_preenchimento = ""


#*** MAIN ***#
figuras = []       # Todas as figuras desenhadas
figura_nova = None # Figura que está sendo desenhada, mas ainda não foi incluída em figuras
root = Tk()
frame = Frame(root)

# Widgets arranjados com Layout grid dentro de frame
paddings = {'padx': 5, 'pady': 5} 

# label
label = ttk.Label(frame,  text='Paint:')
label.grid(column=0, row=0, sticky=W, **paddings)

# option menu
tipo_figura_var = StringVar(root) # Guarda o tipo de figura selecionado no option menu (linha, rabisco, círculo ou retângulo)
option_menu = ttk.OptionMenu(frame, tipo_figura_var,
                             'Linha', 'Linha', 'Rabisco', 'Círculo', 'Retangulo')
option_menu.grid(column=1, row=0, sticky=W, **paddings)

# clors menu
botao = Menubutton(root, text="Cores")
menu = Menu(botao, tearoff=0)
menu.add_command(label= 'Borda', command= PintarBorda)
menu.add_command(label= 'Preenchimento', command= PintarPreenchimento)
menu.add_command(label= 'Rsetar Preenchimento', command= reset_color)
botao ["menu"] = menu
botao.pack()


# Área de desenho
canvas = Canvas(frame, bg='white', width=600, height=600)
canvas.grid(column=0, row=1, columnspan=2, sticky=W, **paddings)
frame.pack()

# Eventos de mouse associados ao canvas - com seus callbacks
canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)
root.mainloop()