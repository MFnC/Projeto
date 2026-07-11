# 🎨 Projeto: Aplicação de Desenho Vetorial (Paint)

**Disciplina:** Programação / Orientação a Objetos  
**Ambiente de Desenvolvimento:** Python 3.14+  
**Interface Gráfica:** Tkinter / TTK  

---

## 📋 Visão Geral do Projeto
Este projeto consiste no desenvolvimento de uma aplicação desktop interativa de desenho vetorial, inspirada no software Paint clássico. O objetivo principal é aplicar conceitos de manipulação de interface gráfica (GUI), tratamento de eventos de mouse, renderização de primitivas gráficas e gerenciamento de estados em tempo real.

---

## 🛠️ Funcionalidades Implementadas (Critérios de Avaliação)

### 1. Primitivas Gráficas e Ferramentas (`FIGURA`)
A aplicação suporta a criação dinâmica de 5 tipos de figuras geométricas e traços livres no canvas:
*   **LINHA:** Renderização de segmentos de reta ligando o clique inicial (`ButtonPress`) ao ponto de liberação (`ButtonRelease`).
*   **RABISCO:** Desenho livre baseado no rastreio contínuo do movimento do mouse, gerando uma sequência de coordenadas interligadas.
*   **CÍRCULO:** Desenho de circunferências perfeitas. O raio é calculado dinamicamente via Teorema de Pitágoras com base no deslocamento do cursor em relação ao centro.
*   **OVAL:** Geração de elipses definidas pelas coordenadas delimitadoras do arrastar do mouse.
*   **RETANGULO:** Criação de quadriláteros baseados nos eixos diagonais informados pelo usuário.

### 2. Manipulação de Cores e Atributos Visuais
*   **Seletor de Cor da Borda:** Abre a janela nativa do sistema (`colorchooser`) e atualiza o indicador visual quadrado com o canal RGB selecionado para o contorno.
*   **Seletor de Cor de Preenchimento:** Permite definir a cor interna para preenchimento de formas fechadas (Círculo, Oval e Retângulo).
*   **Mecanismo de Reset:** Um botão dedicado que limpa o preenchimento das figuras, adaptando-se de forma inteligente ao fundo para simular transparência.

### 3. Renderização em Tempo Real (Feedback Visual)
*   **Rascunho Dinâmico:** Durante o evento de arrastar do mouse (`B1-Motion`), o programa renderiza a figura temporária utilizando um contorno pontilhado (`dash`), permitindo que o usuário visualize o resultado antes de consolidar o objeto na tela.

### 4. Sistema de Temas (Modo Claro / Modo Escuro)
*   Interface totalmente adaptável. Ao alternar o tema, os componentes de interface (`widgets`) e as propriedades de estilo do Canvas mudam de cor dinamicamente para manter o contraste e a usabilidade.

---

## 🔬 Detalhes Técnicos e Arquitetura do Código

*   **Estrutura de Dados das Figuras:** Todos os elementos consolidados no Canvas são armazenados em uma lista global denominada `figuras`. Cada figura é representada por uma estrutura de tuplas:
    ```python
    (tipo_figura, coordenadas, cor_borda, cor_preenchimento)
    ```
    Isso garante o desacoplamento entre os dados lógicos e a renderização visual, facilitando futuras implementações de ações como "Desfazer (Undo)" ou persistência de arquivos.
*   **Tratamento de Exceções e Concorrência de Eventos:** O código conta com travas defensivas (`if figura_nova is None: return`) para mitigar falhas de desempacotamento de dados (`ValueError: not enough values to unpack`) causadas por movimentos excessivamente rápidos do mouse ou interações assíncronas do Tkinter.
*   **Validação de Figuras Incompletas:** Uma função dedicada descarta interações nulas (como cliques simples e estáticos no canvas), impedindo a inserção de objetos de dimensão zero ou vazios na memória da aplicação.
