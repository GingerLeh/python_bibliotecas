import numpy as np 
import sys 
import time

lista = list(range(0, 10**6))
len(lista) #tamanho 
nump_32 = np.array(lista, dtype='uint32')
nump_64 = np.array(lista, dtype='uint64')

#nump.shape 
print(sys.getsizeof(nump_32), sys.getsizeof(lista), sys.getsizeof(nump_64))

print(round(8000056/8000112,2))
print(round(4000112/8000056,2))
start = time.time()
stop = time.time()
nump_64.sum()
print(stop - start)


