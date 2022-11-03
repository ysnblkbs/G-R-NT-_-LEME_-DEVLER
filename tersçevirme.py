import cv2
import numpy as np
from matplotlib import pyplot as plt

foto = cv2.imread("foto/foto.jpg",0)
[w,h] = (np.shape(foto))

ters_foto = np.zeros([w,h], dtype=np.uint8)
enyuksek = (np.max(foto))

for v in range(0,w):
    for u in range(0,h):
        ters_foto[v,u] = enyuksek - foto[v,u]

cv2.imshow("foto",foto)
cv2.imshow("ters",ters_foto)
cv2.waitKey(0)