# Example 4.4 A Kohonen self-organizing map (SOM) to cluster four vectors

from random import random

# let the vectors to be clustered be
# (1, 1, 0, 0); (0, 0, 0, 1); (1, 0, 0, 0); (0, 0, 1, 1).
x = [
    [1, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 0, 1, 1]
]

# the maximum number of clusters to be formed is
m = 2

# supose the learning rate (geometric decrease) is
alpha = .6
# alpha(t+1) = 0.5 alpha(t)

# STEP 0 Initial weights matrix
w = [
    [.2, .8],
    [.6, .4],
    [.5, .7],
    [.9, .3]
]

print('\n### STEP 0. \t Initial weight matrix')
for i in range(len(w)):
    print(w[i])

R = 0
print('\nInitial radius: \nR = ', R)

print('\nInitial learning rate: \na(0) =', alpha)

print('\n\n### STEP 1. \t Begin training')

epochs = 100

for e in range(epochs):
    print('\n\nIteration', e)

    for i in range(len(x[0])):
        aux = x[i]
        
        print('\n\t### Step 2. \t For the vector, ', aux, ', do Steps 3-5')
        
        print('\n\t\t### STEP 3.')
        
        dj = []

        for m in range(len(w[0])):
            print('\t\t\tD(', m+1 ,') =')
            
            D = 0
            
            for j in range(len(aux)):
                print('\t\t\t\t(',w[j][m], '-', aux[j], ') ** 2')
        
                D += (w[j][m] - aux[j]) ** 2
        
            print('\t\t\t\t\t\t = %.2f;' % D)
            dj.append(D)
            #print(dj)
        
        J = (dj.index(min(dj)))
        print('\t\t### STEP 4. \t the input vector is closest to output node', J, 'so \n \t\t\t\t\tJ =', J+1)
        #print(J)

        print('\t\t### STEP 5. \t the weights on the winning unit are updated:')
        for l in range(len(w)):
            aux_ajuste = w[l][J] + alpha * (aux[l] - w[l][J])
            #print(aux_ajuste)
            w[l][J] = aux_ajuste
            
            #w[l][J] = w[l][J] + .6[x[l] - ]
        print('\n\t\t\t\t\t wlJ(new) = wlJ(old) + alpha * (aux[l] - wlJ(antigo))\n')
        print('\t\t\t\t this given the weight matrix')
        for l in range(len(w)):
            print('\t\t\t\t', w[l])

    print('\n\t### Step 6. \t reduce the learning rate:')

    print('\n\t\t\t\t alpha = .5 * (',alpha,') =', .5*alpha)
    alpha = .5 * alpha    
            
        

# RANDOM PESOS
#for i in range(len(x[0])):
#    w.append([])
#    for j in range(m):
#        w[i].append(1)

#for i in range(len(w)):
#    print(w[i])
