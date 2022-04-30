from cProfile import label
from ctypes.wintypes import PFLOAT
from imp import lock_held
import numpy as np 
import matplotlib.pyplot as plt

meses = np.array(['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set'])
temperaturas = np.array ([25,26,23,20,18,17,16,18,20])

plt.title('Ano 1900')
plt.bar(meses,temperaturas, label = 'temperatura') # (x,y) colocar o ; no final é como o show.-> plt.plot plota em linhas padrao
plt.legend()
plt.yticks([0,10,20,30])
plt.xlabel('Meses')
plt.ylabel('Temperatura')
plt.grid(axis='y')
# plt.show()
plt.savefig('primeira_aula_matlib.jpeg')