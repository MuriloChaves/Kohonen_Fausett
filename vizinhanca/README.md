## Vizinhança

Em Kohonen, podemos utilizar vários tipos de topologia para delimitar a nossa vizinhança de neurônios. Vamos detalhar as topologias nas próximas seções.

### Vizinhança Unidimensional

[vizinhos_unidimensional.py](./codigos/vizinhos_unidimensional.py)

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
