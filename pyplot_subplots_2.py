#example from: https://www.w3schools.com/python/matplotlib_subplot.asp

import numpy as np
import matplotlib.pyplot as plt


x=np.linspace(1,50,200)
y1=np.sin(x)
y2=np.cos(x)
y3=np.arctan(x)
x=np.linspace(1,50,200)


#Signle axis (=subplot)
fig1, ax = plt.subplots()
ax7=plt.plot(y1)
plt.show()


#Multiple axes (=subplots), unpacking method
fig2, (ax1, ax2) = plt.subplots(nrows=1, ncols=2,facecolor="aliceblue")

ax1.semilogy()
ax1.set_title('yuhu')
ax2.set_title('maripuju')
ax1.plot(x, y1,'x'':''m', label='y1') #señal a plotear en ax1
ax1.plot(x,y2, label='y2') #otra señal a plotear en ax1
ax2.plot(x, y3, label='y3')

#Add a horizontal line across the Axes. Note that there´s no need to "plot"
ax2.axhline(y=30,xmin=0,xmax=3,c="blue",linewidth=0.5,zorder=0) #

ax1.legend()
ax2.legend()
plt.show()
    
    
    
    