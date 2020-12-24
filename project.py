import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation  import FuncAnimation
fig,ax=plt.subplots()
point,=plt.plot([],[],'o')
ball,=plt.plot([],[],'o')
ball1,=plt.plot([],[],'>')
ball2,=plt.plot([],[],'<')

x,y=[],[]
h=20
fix=0
fix1=0
R=10
def blade(x0,R,n,alpha):
    x=R*np.cos(alpha)+x0
    y=R*np.sin(alpha)
    return x,y
def blade1(x0,y0,R,n,alpha,t):
    x=R*np.cos(alpha)+x0
    y=R*np.sin(alpha)+y0
    X=x*np.cos(t/4)-y*np.sin(t/4)+x0
    Y=y*np.cos(t/4)+x*np.sin(t/4)

    return X,-Y
def blade2(x0,y0,R,n,t):
    alpha=np.arange(np.pi/2,np.pi*(3/2),0.1)
    b=np.arange(0,np.pi/2,0.01)
    x=R*np.cos(alpha)
    y=R*np.sin(alpha)
    X=x*np.cos(b[t])-y*np.sin(b[t])+x0
    Y=y*np.cos(b[t])+x*np.sin(b[t])+y0
    return -X,-Y
edge=h+10
plt.axis('equal')
ax.set_xlim(-edge,edge)
ax.set_ylim(-edge,edge)
def animate(i):
    ball.set_data(blade(x0=0,R=R,n=1,alpha=np.arange(0,2*np.pi,0.1)))
    x.append(i*0)
    y.append(h+(-i))
    if y[i]<=-R and fix==fix1:
        fix=i
        fix1=fix+1
    if y[i]<=-R:
        y[i]=0
        ball.set_data(blade(x0=0,R=1000,n=1,alpha=np.arange(0,2*np.pi,0.1)))
        ball1.set_data(blade1(x0=10,y0=0,R=R,n=1,alpha=np.arange(np.pi/2,np.pi*(3/2),0.1),t=i))
        ball2.set_data(blade2(x0=10,y0=0,R=R,n=1,t=i-fix))

    point.set_data(x,y)
     
    
ani=FuncAnimation(fig,
                  animate,
                  frames=100,
                  interval=100)


