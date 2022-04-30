from encodings import normalize_encoding
from itertools import count
from xml.dom.minidom import NamedNodeMap
import numpy as np
import pandas
import matplotlib.pyplot as plt 
pd = pandas 

df = pd.read_csv("Assignment03- dataset.csv") 
df.head()
dfNum = df [['Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]']] 


colNam = list(dfNum.columns)
colNam[0]

ncols = 2
nrows = int(np.ceil(len(dfNum.columns) / (1.0*ncols)))

fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(10,10))

counter=0 
for i in range (nrows):
    for j in range(ncols):
        ax = axes[i][j]

        if counter < len (dfNum.columns):
            ax.hist(dfNum[dfNum.columns[counter]], bins=10, label = '{}'.format(dfNum.columns[counter]))
            ax.set_xlabel(colNam[counter])
            ax.set_ylabel("Fequencia")
        else:
            ax.set_axis_off()

        counter =+1 

# plt.show()

# desc = dfNum.describe()
# print(pow(desc.std(),2))
# print(desc)
plt.matshow(df.corr())


f = plt.figure(figsize=(19, 15))
plt.matshow(df.corr(), fignum=f.number)
plt.xticks(range(df.select_dtypes(['number']).shape[1]), df.select_dtypes(['number']).columns, fontsize=14, rotation=45)
plt.yticks(range(df.select_dtypes(['number']).shape[1]), df.select_dtypes(['number']).columns, fontsize=14)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
plt.title('Correlation Matrix', fontsize=16);
plt.show()
