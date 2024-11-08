# Jogo de Adivinhação - Python e Flask 🎮

Bem-vindo ao meu repositório do **Jogo de Adivinhação**, desenvolvido em Python com **Flask**, **HTML** e **CSS**. O objetivo deste projeto foi criar um jogo interativo onde o usuário deve tentar adivinhar o número escolhido aleatoriamente pelo computador, que varia de 1 a 100. 

## Sobre o Projeto 💻

Neste projeto, implementei um jogo simples, mas divertido, com a seguinte funcionalidade:

- **Jogo de Adivinhação**: O computador escolhe um número aleatório entre 1 e 100, e o usuário tenta adivinhar qual é esse número.
- **Visualização na Web**: Utilizando o Flask, criei uma interface web para que o jogo pudesse ser jogado diretamente no navegador.
- **Design Responsivo**: O layout da interface foi feito com HTML e CSS, garantindo uma boa experiência de usuário.

### Tecnologias Utilizadas 🔧

- **Python**: Para a lógica do jogo e servidor web com Flask.
- **Flask**: Framework web para desenvolver a interface e controlar o fluxo do jogo na web.
- **HTML/CSS**: Para estruturar e estilizar a página da web.
- **Jogo de Adivinhação**: Lógica que gera um número aleatório e interage com o usuário.

## Funcionalidade do Jogo 🎯

O jogo tem as seguintes características:

- O computador escolhe um número aleatório de 1 a 100.
- O jogador deve tentar adivinhar qual é esse número.
- O jogo vai dando dicas ao jogador, indicando se o palpite é maior ou menor que o número correto.

## Estrutura do Repositório 🗂️

Este repositório contém:

- **`app.py`**: O código Python que configura o servidor Flask e contém a lógica do jogo.
- **`static/`**: Contém os arquivos de estilo CSS utilizados para a interface.
- **`templates/`**: Contém os arquivos HTML responsáveis pela estrutura da página.
- **`README.md`**: Este arquivo com as informações sobre o projeto.
  
### Como Rodar o Projeto 🚀

1. Clone o repositório para sua máquina:
    ```bash
    git clone https://github.com/seu-usuario/jogo-adivinhacao.git
    ```

2. Navegue até a pasta do projeto:
    ```bash
    cd jogo-adivinhacao
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Execute o servidor Flask:
    ```bash
    python app.py
    ```

5. Acesse o jogo em seu navegador em `http://127.0.0.1:5000/`.


