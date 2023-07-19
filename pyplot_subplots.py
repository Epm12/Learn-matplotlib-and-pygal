import matplotlib.pyplot as plt	#importing pyplot module from matplotlib
import numpy as np 				#matplotlib dependant package

x=np.linspace(0,2*np.pi,200)
y=np.sin(x)

fig, ax = plt.subplots()
ax.plot(x,y)
plt.show()
