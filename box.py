from cmath import sqrt

import sympy as sp

acc=0.01

# print(sqrt(dx**2))
def rec(x,y,dx,dy,acc):
    if((dx**2+dy**2)**0.5<1):
        print(x,y)
        return
    mi=999999
    fi=999999
    mx=0
    my=0
    dix=[0,dx,dx,-dx,-dx,dx,-dx,0,0]
    diy=[0,dy,-dy,-dy,dy,0,0,dy,-dy]
    
    for i in range(0,9):       
      fx=x+dix[i]
      fy=y+diy[i]
      
      fun=8*fx**2+4*fx*fy+5*fy**2
      print(fx,fy,fun)
      if(fun<fi):
          mi=i
          fi=fun
          mx=fx
          my=fy
           
    if(mi==0):
        dx=dx/2
        dy=dy/2
    print(mx,my)        
    rec(mx,my,dx,dy,acc)
    
    
rec(0,0,1,1,acc)
           
     
    
      
           
    
    