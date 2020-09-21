import math
l = [2, 3]
dp = 1000*[-1]
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
        if p >= n:
            break
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

def yprimes(n,k):
    Primes(2*(k**n)+1)
    a = []
    for i in range(1,k):
        if isPrime(2*(i**n)+1):
            a.append(i)
    return a

def arithmderiv(n):
    if dp[n] != -1:
        return dp[n]
    if n == 0 or n == 1:
        return 0
    if isPrime(n):
        return 1
    temp = factor(n)
    dp[n] = arithmderiv(temp[0])*(int(n/temp[0]))+arithmderiv(int(n/temp[0]))*temp[0]
    return dp[n]

#print(yprimes(2,1000))

#number = int(input())
#if isPrime(number):
    #print(True)
#else:
    #print(factor(number))
#print(l)
c = 0
for i in range(100):
    if arithmderiv(arithmderiv(i)) == 1:
        c += i
print(c)