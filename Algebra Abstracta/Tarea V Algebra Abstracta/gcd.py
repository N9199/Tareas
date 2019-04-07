def gcd(a,b):
    if a == 0 and b == 0:
        return 0
    if min(a,b)==0:
        return max(a,b)
    
    if a>b:
        print("\\[",a,":",b,"=",a//b,"\\]")
        print("Resto:$",a%b,"$")
        return gcd(b,a%b)
    else:
        print("\\[",b,":",a,"=",b//a,"\\]")
        print("Resto:$",b%a,"$")
        return gcd(a,b%a)

a,b = input().split()
a=int(a)
b=int(b)
print(gcd(a,b))œ