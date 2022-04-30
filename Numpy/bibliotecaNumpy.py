#Biblioteca usada para estatística
#help(np.array)
#dir(np)
#dir(array)
# ndim = mostra quantas dimensões tem o array
import numpy as np 

array = np.array([1,2,3,4,5])
# help(type(array.T))

notas = [10,8,4,6]
array = np.array(notas)
print(array.ndim)

notas_s0 = notas.copy()
notas_s1 = [5,6,5,6]
notas_semestres = [notas_s0,notas_s1]

array_2d = np.array(notas_semestres)
print (array_2d)
print (array_2d.ndim)

notas_ano0 = notas_semestres.copy()
notas_ano1 = notas_semestres.copy()
notas_anos = [notas_ano0,notas_ano1]

array_3d = np.array(notas_anos)
print (array_3d)
print (array_3d.ndim)

print(np.zeros([4,2,4]))
print(np.ones([4,2,4]))
print(np.full([4,2,4],100))

print(np.arange(10))

print(np.random.rand(3,2,3))

print (array + 2) # entre outras operações 

# Revisão de listas
# lista = [] colchetes 
lista = ["João", "Ana", "Paulo", "Mateus", "Nasser"]
print(lista[0])
print(lista[-1])
print(lista[1:])
print(lista[:4]) 
# listas não podem ser somadas. Se fizer lista + lista ela concatena e não soma
# listas podem conter vários tipos dentro
lista.remove('Ana')
lista.append('Alessa')
del lista [2]
lista.sort(reverse=True)
lista[::-1] # reverte
lista_copia = lista # o que fizer em uma vai mudar na outra
lista_copia = lista.copy() # se torna independente 






