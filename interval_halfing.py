a=1
b=4
x=1

def fun(a,b,xm,acc):
  l=b-a     
  x1=a+(l)/4
  x2=b-(l)/4
  fx1=x1**2+16/x1
  fx2=x2**2+16/x2
  fxm=xm**2+16/xm
  if(fx1<fxm):
      b=xm
      xm=x1
  elif(fx2<fxm):
      a=xm
      xm=x2
  if((b-a)<=acc):
      print(a,b)
      return         
  fun(a,b,xm,acc)  

fun(1,4,2.5,0.5)
