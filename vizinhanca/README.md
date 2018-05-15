## Vizinhança

Em Kohonen, podemos utilizar vários tipos de topologia para delimitar a nossa vizinhança de neurônios. Vamos detalhar as topologias nas próximas seções.

### Vizinhança Unidimensional

À fins didáticos, vamos dar uma olhada na topologia Unidimensional (assim como nome já fala, de somente uma dimensão) como segue na imagem abaixo:

<p align="center">
 Mapa Unidimensional de Kohonen p. 170. Fausett (1994)
</p>

<p align="center">
 <img align="center" src="https://github.com/MuriloChaves/Kohonen_Fausett/blob/master/vizinhanca/imagens/vizinhanca_unidimensional.gif">
</p>

Pode-se notar que, temos praticamente dois vetores: um vetor com neurônios; e outro vetor com as entradas, que são conectados com os todos neurônios, um pouco complicado de entender de antemão.

Vamos por parte... 

Ao desmembrar o problema e tentarmos compreender as partes isoladamente, podemos analisar um vetor qualquer (mesmo não sendo de objetos neurônios). 

Primeiro: vamos declarar um vetor "fictício de neurônios".

```python
mapa_neuronios = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Podemos chegar a conclusão que teríamos 10 neurônios, mais como funcionaria a vizinhança? 

Para isso, definimos uma variável <i>R</i> com o valor que desejamos delimitar o 'raio' da vizinhança. Assim temos:

```
0, 1, 2, {3, (4, [5], 6), 7}, 8, 9
```

\[ \] R = 0 <br/>
\( \) R = 1 <br/>
\{ \} R = 2 <br/>
. <br/>
. <br/>
. <br/>

Quando temos o R = 0, indicamos que estamos trabalhando sem definir vizinhança, e assim entrando em uma outra conversa chamada de 'o vencedor leva tudo', ou seja, somente retornará o neurônio x.

```
R = 0

### Vizinhos do nó:  0 ###
 [0]

### Vizinhos do nó:  1 ###
 [1]

### Vizinhos do nó:  2 ###
 [2]

### Vizinhos do nó:  3 ###
 [3]

### Vizinhos do nó:  4 ###
 [4]

### Vizinhos do nó:  5 ###
 [5]

### Vizinhos do nó:  6 ###
 [6]

### Vizinhos do nó:  7 ###
 [7]

### Vizinhos do nó:  8 ###
 [8]

### Vizinhos do nó:  9 ###
 [9]
```

Quando começamos a retornar os vizinhos delimitados por R, podemos notar que as coisas começam a ficar um pouco mais interessantes.

```
R = 1

### Vizinhos do nó:  0 ###
 [1]

### Vizinhos do nó:  1 ###
 [0, 2]

### Vizinhos do nó:  2 ###
 [1, 3]

### Vizinhos do nó:  3 ###
 [2, 4]

### Vizinhos do nó:  4 ###
 [3, 5]

### Vizinhos do nó:  5 ###
 [4, 6]

### Vizinhos do nó:  6 ###
 [5, 7]

### Vizinhos do nó:  7 ###
 [6, 8]

### Vizinhos do nó:  8 ###
 [7, 9]

### Vizinhos do nó:  9 ###
 [8]

```

Assim como podemos notar, na demonstração, somente é retornado os vizinhos em 1.

```
R = 2

### Vizinhos do nó:  0 ###
 [1, 2]

### Vizinhos do nó:  1 ###
 [0, 2, 3]

### Vizinhos do nó:  2 ###
 [0, 1, 3, 4]

### Vizinhos do nó:  3 ###
 [1, 2, 4, 5]

### Vizinhos do nó:  4 ###
 [2, 3, 5, 6]

### Vizinhos do nó:  5 ###
 [3, 4, 6, 7]

### Vizinhos do nó:  6 ###
 [4, 5, 7, 8]

### Vizinhos do nó:  7 ###
 [5, 6, 8, 9]

### Vizinhos do nó:  8 ###
 [6, 7, 9]

### Vizinhos do nó:  9 ###
 [7, 8]
```

Aqui já vemos ao retornarmos dois vizinhos.

O código está disponível.
