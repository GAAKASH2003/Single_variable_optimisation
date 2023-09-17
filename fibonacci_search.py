a=0
b=5
acc=0.0000001
m=(2*(b-a)/acc)
print(m)
fi=[1,1]
i=1
while(fi[len(fi)-1]<=m):
    fi.append(fi[len(fi)-1]+fi[len(fi)-2])
fi.pop()    
n=len(fi)-2
print(fi)

def fib(a,b,k):
    l=(fi[n-k+1]/fi[n+1])*(b-a)
    x1=a+l
    x2=b-l
    fx1=x1*x1-4*x1+4
    fx2=x2*x2-4*x2+4
    if(fx1>fx2):
        a=x1
    elif(fx1<=fx2):
        b=x2
    if(k==n):
        print(a,b)
        return
    print(a,b)    
    fib(a,b,k+1)

fib(0,5,2)
    

    

