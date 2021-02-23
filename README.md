# Random Maze

**Disciplina**: FGA0124 - PROJETO DE ALGORITMOS - TA

## Alunos

|Matrícula | Aluno |
| -- | -- |
| 15/0135521  | Leonardo dos S. S. Barreiros |
| 16/0124778  | Ian Pereira de Sousa Rocha |

## Sobre

<p align="justify"> Random Maze é um jogo feito em python, utilizando a biblioteca pygame.

<p align="justify"> O jogo é bem simples. O jogador têm de descobrir a saída do labirinto.

<p align="justify"> Da parte do código nós fizemos em programação orientada a objeto. O programa principal é a <strong>Main.py</strong>

<p align="justify"> Para a construção do labirinto fizemos aplicação de busca em profundidade, em que para cada celula existente no grid irá verificar a existência de possíveis vizinhos e assim criando de forma aleatória as paredes, portanto, possibilitando diferentes labirintos a cada execução.

<p align="justify"> Não há um tratamento para quando o jogador vença ou desista de achar a saida. Basta apenas fechar o jogo no botão 'X' que a execução será finalizada.

## Requisitos

``` sh
Python 3.7+

```
### Pygame 2.0.1

<p align="justify"> Basta instalar os requisitos mínimos para rodar o projeto através do comando abaixo:

``` sh
    pip install -r requirements.txt
```

Ao final para rodar o jogo basta rodar o seguinte comando:

``` sh
    python ./src/Main.py
```

Então o jogo irá iniciar.

Para movimentar o jogador use as <strong> Setas </strong> do teclado.
