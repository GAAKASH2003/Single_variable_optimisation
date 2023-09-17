

ig=2
d=0.5

li=[2]
def bound(x,d):
    dl=d
    fun="(x**2+54/x)"
    num=eval(fun)
    numf=eval("((x+d)**2+54/(x+d))")
    numi=eval("((x-d)**2+54/(x-d))")
    
    if(numi>=num and num>=numf):
        dl=abs(dl)      
    elif(numi<=num and num<=numf):
        dl=-abs(dl)
    else:
        print("another guess")
        return
    k=0
    prev=num
    t=x+(2**k)*dl
    li.append(t)
    while(eval("t**2+54/t")<prev):
        k=k+1
        prev=eval("t**2+54/t")
        p=li[k]
        t=p+(2**k)*dl
        li.append(t)
    
    print(li[k-1])    
    print(li[k+1])    
    return         

print(bound(1,0.5))
print(li)
