import cv2
import numpy as np
from matplotlib import pyplot as plt

foto = cv2.imread("foto/foto.jpg",0)
Hist = np.zeros(256)
[w,h] = np.shape(foto)
for u in range (0,w):
    for v in range (0,h):
        i = foto[u,v]
        Hist[i]=Hist[i]+1
cv2.imshow("foto",foto)
print(Hist)
plt.hist(Hist)
plt.show()