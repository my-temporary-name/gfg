def lcmAndGcd(A , B):
    # code here 
    if A<B:
        a=B
        b=A
    else:
        a=A
        b=B
    # print(a,b)
    global x
    x=0
    def gcd(a,b):
        print(a,b)
        if b==0:
            x=a
            print(x)
            return
        
        gcd(b,a%b)
    
    gcd(a,b)
    print("x", x)
    l = a*b
    l=l//x
    arr=list()
    arr.append(x)
    arr.append(l)
    return arr

print(lcmAndGcd(5,10))