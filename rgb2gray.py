from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def r2g():
	img=np.asarray(Image.open('qwe.jpg'))
	height,width,channels=img.shape
	img_new=np.zeros((height,width))
	for i in range(0,height):
		for j in range(0,width):
			img_new[i,j]=int(0.3*img[i,j,0]+0.59*img[i,j,1]+0.11*img[i,j,2])
	return img_new
abc=r2g()
im=plt.imshow(abc,cmap='gray')
plt.show()