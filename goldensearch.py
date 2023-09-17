import math
a=0
b=1
acc=0.5
n=(math.log((acc))//math.log(0.618))+1
n=8
def golden_search(a,b,acc,k):
    w1=0
    w2=0
    if(a+0.618*(b-a)>b-0.618*(b-a)):
        w1=b-0.618*(b-a)
        w2=a+0.618*(b-a)
    elif(a+0.618*(b-a)<b-0.618*(b-a)):
        w1=a+0.618*(b-a)
        w2=b-0.618*(b-a)    
   
       
    fx1=(40-90*w1)**2
    fx2=(40-90*w2)**2
    if(fx1>fx2):
        a=w1
    else:
        b=w2
    if(k==n):
        print(90*a+60,90*b+60)
        return
    golden_search(a,b,acc,k+1)
                
golden_search(0,1,acc,0)
    
    
