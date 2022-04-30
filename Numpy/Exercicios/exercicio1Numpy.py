# Utilizando a biblioteca numpy siga as instruções abaixo:
# Crie um array 6x6 preenchido com zero
# Preencha o centro desse array com um array 4x4 preenchido com uns
# Preencha o centro desse array com um array 2x2 preenchido com dois
# Gere um segundo array 6x6 com números inteiros aleatórios entre 0 e 2.
# Subtraia o primeiro array pelo segundo

import numpy as np


array = np.zeros([6,6]) #linhas por colunas
print(array,'\n')
array[1:5, 1:5] = array_1 = np.ones([4,4]) #vai selecionar o centro do primeiro array
print(array)
array[2:-2, 2:-2] = np.full(shape=(2,2), fill_value=2)
print(array,'\n')
np.random.seed(0) #vai fazer o aleatório mas não vai ficar mudando em cada execução
array_1 = np.random.randint(low=0, high=3, size=(6,6))
print(array_1)

array_result = array - array_1
print(array_result)



