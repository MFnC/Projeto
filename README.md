# 🎨 Projeto: Aplicação de Desenho Vetorial (Paint)

**Disciplina:** Programação / Orientação a Objetos  
**Ambiente de Desenvolvimento:** Python 3.14+  
**Interface Gráfica:** Tkinter / TTK  

---

## 📋 Visão Geral do Projeto
Este projeto consiste no desenvolvimento de uma aplicação desktop interativa de desenho vetorial, inspirada no software Paint clássico. O objetivo principal é aplicar conceitos de manipulação de interface gráfica (GUI), tratamento de eventos de mouse, renderização de primitivas gráficas e gerenciamento de estados em tempo real.

## 👥 Metodologia de Desenho e Controle de Versão (Git)

O projeto foi planejado e desenvolvido em conjunto pela equipe, utilizando o **Git** para garantir o paralelismo na construção das funcionalidades e manter a integridade do código-fonte. 

A estrutura de ramificações (*branches*) foi organizada da seguinte forma:

*   **`main`:** Ramificação principal que contém apenas as versões consolidadas, testadas e prontas da aplicação.
*   **3 Branches de Desenvolvimento:** Criamos uma *branch* exclusiva para cada integrante do grupo. Isso permitiu que cada pessoa desenvolvesse trechos específicos do código em paralelo (como tratamento de eventos de desenho, design da interface e sistema de temas) sem que o trabalho de um interferisse diretamente no do outro.
*   **Integração:** Após a conclusão e validação das ferramentas de forma isolada, os códigos foram integrados à *main* por meio de processos de mesclagem (*merge*), resolvendo conflitos de forma colaborativa.

> 💡 **Saneamento e Atualização Local:** Para garantir a sincronia de código entre o grupo e evitar conflitos antes de novas implementações, foi adotado o uso de `git restore .` e `git clean -fd` para descarte seguro de arquivos/alterações de teste, seguido de `git pull origin <branch>` para atualização segura das máquinas locais.

---

## 🛠️ Funcionalidades Implementadas (Critérios de Avaliação)

### 1. Primitivas Gráficas e Ferramentas (`FIGURA`)
A aplicação suporta a criação dinâmica de 6 tipos de figuras geométricas e traços livres no canvas:
*   **LINHA:** Renderização de segmentos de reta ligando o clique inicial (`ButtonPress`) ao ponto de liberação (`ButtonRelease`).
*   **RABISCO:** Desenho livre baseado no rastreio contínuo do movimento do mouse, gerando uma sequência de coordenadas interligadas.
*   **CÍRCULO:** Desenho de circunferências perfeitas. O raio é calculado dinamicamente via Teorema de Pitágoras com base no deslocamento do cursor em relação ao centro.
*   **OVAL:** Geração de elipses definidas pelas coordenadas delimitadoras do arrastar do mouse.
*   **RETANGULO:** Criação de quadriláteros baseados nos eixos diagonais informados pelo usuário.
*   **POLÍGONO (Novo!):** Geração de polígonos fechados e dinâmicos com múltiplos vértices.

### 2. Comportamento Avançado do Mouse para Polígonos (Clique-e-Solte)
Diferente das formas tradicionais por arrasto, a ferramenta **Polígono** implementa um fluxo de design profissional de alta precisão:
*   **Adição sem arrastar:** O usuário dá cliques simples e solta o botão imediatamente. A linha elástica guia do segmento o acompanha livremente pelo movimento do mouse na tela (`mouse_movido_livre`).
*   **Duplo clique para finalizar:** O duplo clique (`Double-1`) fecha a forma inteiramente, unindo o último vértice ao inicial e aplicando a cor de preenchimento.
*   **Filtro Inteligente contra Trepidação:** Algoritmo dedicado que analisa e descarta vértices duplicados ou ruídos gerados por cliques acidentais e de alta sensibilidade do mouse no momento de finalização do polígono.

### 3. Manipulação de Cores e Atributos Visuais
*   **Seletor de Cor da Borda:** Abre a janela nativa do sistema (`colorchooser`) e atualiza o indicador visual quadrado com o canal RGB selecionado para o contorno.
*   **Seletor de Cor de Preenchimento:** Permite definir a cor interna para preenchimento de formas fechadas (Círculo, Oval, Retângulo e Polígono).
*   **Mecanismo de Reset:** Um botão dedicado que limpa o preenchimento das figuras, adaptando-se de forma inteligente ao fundo para simular transparência.

### 4. Renderização em Tempo Real (Feedback Visual)
*   **Rascunho Dinâmico:** Durante o evento de arrastar do mouse (`B1-Motion`) ou movimento livre na ferramenta de polígonos, o programa renderiza a figura temporária utilizando um contorno pontilhado (`dash`), permitindo que o usuário visualize o resultado antes de consolidar o objeto na tela.

### 5. Sistema de Temas (Modo Claro / Modo Escuro)
*   Interface totalmente adaptável. Ao alternar o tema, os componentes de interface (`widgets`) e as propriedades de estilo do Canvas mudam de cor dinamicamente para manter o contraste e a usabilidade.

---

## 🔬 Detalhes Técnicos e Arquitetura do Código

### 🏗️ Arquitetura por Mixins (Divisão do Controlador)
Para evitar o crescimento desordenado do arquivo principal `ControladorDesenho` e garantir o princípio de responsabilidade única (SRP), a lógica foi modularizada no Python usando o conceito de **Mixins**:
*   `ControladorEstiloMixin` (`controlador_estilo.py`): Contém estritamente o código para paletas de cores, reset de preenchimentos e troca do tema do sistema.
*   `ControladorMouseMixin` (`controlador_mouse.py`): Reúne a captura dos cliques do mouse, rascunhos em tempo real e a complexa máquina de estados da linha guia do polígono.
*   `ControladorDesenho` (`controlador_desenho.py`): Classe principal que atua como o "cérebro" unificado do MVC, herdando os mixins de estilo e mouse. Fornece o dicionário `FABRICA_FIGURAS` de maneira transparente à `Main.py` sem afetar dependências externas.

### 🛑 Solução de Importações Circulares (`Circular Import`)
Para resolver os problemas clássicos de acoplamento mútuo em tempo de inicialização, as referências de herança das subclasses foram ajustadas:
*   Subclasses de `Figura` (como `Poligono.py` e `Retangulo.py`) foram corrigidas para realizar importações com caminhos absolutos do pacote (`from Modelo.Figura.Figura import Figura`), enquanto a classe base `Figura.py` foi completamente isolada de importações de seus filhos.
*   Os arquivos de pacotes (`__init__.py`) foram limpos para evitar importações cruzadas automáticas indesejadas pelo interpretador.
