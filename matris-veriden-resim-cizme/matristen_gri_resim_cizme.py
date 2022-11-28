import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

data = np.zeros( (48,48), dtype=np.uint8)

data_file = pd.read_csv('face_data.csv')
satir = data_file.iat[2,2]

satir_int = list(map(int,satir.split()))
# print(satir_int[0])

for i in range(48):
    for j in range(48):
        pix = 48*i + j
        # print(pix)
        data[i,j]= satir_int[pix]



plt.imshow(data, interpolation='nearest')
plt.show()