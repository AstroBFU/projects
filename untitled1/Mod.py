import numpy as np
h=3
R=0.3
D=R*2
P_OBJECT= 8900
g=9.8
k=0.02
S=np.pi*R**2
mg=2.5
Ep=mg*g*h
F=P_OBJECT*S*k/2
L=Ep/F
z=0
if L>D:
    z=0
if L>R and L<D:
    z=1
if L<R:
    z=2

print(L,D,z)