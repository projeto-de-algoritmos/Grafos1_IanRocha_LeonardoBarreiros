# Random Maze

**Disciplina**: FGA0124 - PROJETO DE ALGORITMOS - TA

## Alunos
<hr>

|Matrícula | Aluno |
| -- | -- |
| 15/0135521  | Leonardo dos S. S. Barreiros |
| 16/0124778  | Ian Pereira de Sousa Rocha |
<br>

## Sobre

<hr>
<p align="justify"> Random Maze é um jogo feito em python, utilizando a biblioteca pygame.

<p align="justify"> O jogo é bem simples. O jogador têm de descobrir a saída do labirinto.

<p align="justify"> Da parte do código nós fizemos em programação orientada a objeto, onde temos uma classe principal chamada <strong> Main</strong> em que nela é chamada todas as instâncias dos objetos presentes no jogo, compondo seu construtor.

<p align="justify"> Utilizamos para construir o labirinto um gerador de labirinto com arvore binária, em que para cada celula existente no grid irá verificar a existência de possíveis vizinhos a norte e oeste e assim criando uma conexão, portanto, possibilitando diferentes conexões, formando diferentes labirintos.

<p align="justify"> Ao final de tudo, caso o jogador desista de achar o fim do labirinto através do comando de saída, o jogo irá disponibilizar o menor caminho desde o começo do spawn do jogador colorindo-o.

<p align="justify"> O algorítmo utilizado para realizar o menor caminho é a busca em largura apontando o nó inicial e final, que também mudam de posição conforme é gerado um novo labirinto.

## Requisitos

``` sh
Python 3.7+

```
### Pygame 2.0.1

<p align="justify"> Basta instalar os requisitos mínimos para rodar o projeto através do comando abaixo:

``` sh
    pip install -r requirements.txt
```


