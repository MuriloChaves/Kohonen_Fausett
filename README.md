## Mapas auto-organizáveis de Kohonen - baseado em Fausett (1994).

Para acompanhamento e repositório de códigos do capítulo da Fausett sobre Kohonen.

### Algoritmo

Abaixo podemos ver o pseudocódigo tirado da p. 170 adaptado.

```
STEP 0. Iniciar pesos w_ij
        Definir topologia e parâmetros de vizinhança
        Definir os parâmetros da taxa de aprendizagem
        
STEP 1. Enquanto a condição de parada é falso:

          STEP 2. Para cada vetor de entrada x:
          
                    STEP 3. Para cada j:
                              D(j) += (w_ij - x_i) * (w_ij - x_i)
                              
                    STEP 4. Encontrar índice J tal que D(j) é o mínimo
                    
                    STEP 5. Para todas as unidades J especificados em uma vizinhança de J, e para todos os i:
                    
                              w_ij(novo) = w_ij(antigo) + alpha[x_i - w_ij(antigo)]
                              
          STEP 6. Atualizar taxa de aprendizagem
          
        STEP 7. Testar conção de parada
```

### Bibliografia

FAUSETT, Laurene V. <b>Fundamentals of neural networks</b>: Architectures, algorithms, and applications. Upper Saddle River, NJ, USA: Prentice-Hall, Inc., 1994. ISBN 0-13-334186-0. Disponível em: \<<http://www.csbdu.in/csbdu-old/pdf/Fundamentals%20Of%20Neural%20Networks.pdf>\>. Acesso em: 15 maio 2018.
