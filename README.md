# 🏥 Sistema de Cadastro de Pacientes

Um projeto simples em **Python** utilizando a biblioteca **Tkinter** para gerenciamento de dados hospitalares/clínicos. Ideal para estudar a manipulação de interfaces gráficas e widgets complexos.

## 📋 Funcionalidades

- **Formulário de Entrada:** Coleta de dados como Nome, CPF, Data de Nascimento e Contatos.
- **Validação:** Sistema que impede o cadastro se houver campos vazios.
- **Navegação por Abas:** Organização entre a tela de cadastro e a tela de listagem.
- **Tabela de Dados:** Exibição dos pacientes em uma grade organizada (Treeview).

## 🛠️ Tecnologias Utilizadas

* **Python**: Linguagem base.
* **Tkinter**: Biblioteca padrão para GUI (Interface Gráfica do Usuário).
* **ttk**: Extensão do Tkinter para widgets modernos (Notebook e Treeview).

## 📂 Estrutura de Estudo

Para entender o código, foque nestes pontos:
1.  **`janela = Tk()`**: Criação da base do aplicativo.
2.  **`ttk.Notebook`**: Criação das abas "Pacientes" e "Cadastrados".
3.  **`entry.get()`**: Método usado para capturar o texto digitado pelo usuário.
4.  **`tabela.insert`**: Como os dados saem dos campos e entram na lista visual.
