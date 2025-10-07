# Checkpoint 02 - Python - Jogo da Velha

![Checkpoint](https://img.shields.io/badge/Checkpoint-02-blueviolet)
![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Retro Game](https://img.shields.io/badge/TicTacToe-Play-orange?style=plastic&logo=gamepad&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

# 🎮 Jogo da Velha (Tic Tac Toe) em Python

Este projeto implementa o clássico **Jogo da Velha (Tic Tac Toe)** em Python, utilizando uma matriz 3x3 para representar o tabuleiro.
O jogo é para **dois jogadores**, que se revezam colocando `X` ou `O` até que um deles vença ou ocorra empate.

## ✨ Funcionalidades

✔️ Tabuleiro 3x3 exibido após cada jogada  
✔️ Dois jogadores se alternam (`X` e `O`)  
✔️ Verificação de vitória em linhas, colunas ou diagonais  
✔️ Verificação de empate  
✔️ Checagem de jogadas válidas  
✔️ Opção de sair a qualquer momento digitando `s`

## 🛠️ Pré-requisitos

* [Python 3.10+](https://www.python.org/downloads/) instalado na sua máquina

## 📥 Instalação

Clone este repositório em sua máquina:

```bash
git clone https://github.com/seu-usuario/tic_tac_toe.git
```

Entre na pasta do projeto:

```bash
cd tic_tac_toe
```

## ▶️ Execução

Execute o jogo com:

```bash
python tictactoe.py
```

## 📂 Estrutura do projeto

```
tic_tac_toe/ 
│ 
├── tictactoe.py       # Arquivo principal com o código do jogo 
├── README.md          # Este arquivo de instruções 
└── LICENSE            # Licença MIT
```

## 📝 Exemplo de uso

```
   0   1   2
0    |   |  
  ---+---+---
1    |   |  
  ---+---+---
2    |   |  

Jogador X, escolha a linha (0, 1, 2) ou 's' para sair: 1
Jogador X, escolha a coluna (0, 1, 2) ou 's' para sair: 1

   0   1   2
0    |   |  
  ---+---+---
1    | X |  
  ---+---+---
2    |   |  

Jogador O, escolha a linha (0, 1, 2) ou 's' para sair: 0
Jogador O, escolha a coluna (0, 1, 2) ou 's' para sair: 2

   0   1   2
0    |   | O
  ---+---+---
1    | X |  
  ---+---+---
2    |   |  

Jogador X, escolha a linha (0, 1, 2) ou 's' para sair: s
Jogo encerrado pelo usuário.
```

## 👨‍💻 Autor

`Mario Antonio Oliveira - RM567713`
`Vinicius Augusto Silva - RM566830`
