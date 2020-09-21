import math

def squares(a,n):
    l = []
    for i in range(a,n):
        if math.sqrt(float(i)**2+(float(i)-1)**2) == round(math.sqrt(float(i)**2+(float(i)-1)**2)):
            l.append([int(math.sqrt(i**2+(i-1)**2)),i,i-1])
    return l