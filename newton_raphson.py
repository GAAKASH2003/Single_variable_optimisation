
import sympy as sp

x, y, z1,z2 = sp.symbols('x y z1 z2')
m=x**3-5*x+2
def newton(m,x_old,acc):
    k=m.diff()
    kd=k.diff()    
    equ1 = sp.Eq(m.diff(), z1)
    sequ1 = equ1.subs({x: x_old})
    res1=sp.solve(sequ1, z1)
    if(res1[0]<=acc):
        return x_old 
    equ2 = sp.Eq(kd, z2)
    sequ2 = equ2.subs({x: x_old})
    res2=sp.solve(sequ2, z2)
    x_new=x_old-(res1[0]/res2[0])
    return newton(m,x_new,acc)
# y=newton(m,2,1)    
# print(f"minimum lies in the range of:({y-1},{y+1})")






