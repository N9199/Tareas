import math
l = [2, 3]
def Primes(n):
    #print(n)
    i = 6
    if l[-1] > i:
        i = 6*(l[-1]//6)
    while i < n:
        #print(i)
        b1, b2 = True, True
        for p in l:
            if (i-1)%p == 0:
                b1 = False
            if (i+1)%p == 0:
                b2 = False
            if not b1 and not b2:
                break
        if b1 and l[-1] < i-1:
            l.append(i-1)
        if b2 and l[-1] < i+1:
            l.append(i+1)
        i += 6
def isPrime(n):
    Primes(int(math.sqrt(n)))
    b3 = True
    for p in l:
        if n%p == 0:
            b3 = False
            break
    return b3

def factor(n):
    Primes(n)
    factors = []
    temp = n
    for p in l:
        #print(p,temp)
        if n%p == 0:
            factors.append(p)
            temp//=p
        if temp == 1:
            break
    return factors

number = int(input())
if isPrime(number):
    print(True)
else:
    print(factor(number))
#print(l)
