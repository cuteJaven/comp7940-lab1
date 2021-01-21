from math import sqrt

x = 52633
fac = []
for i in range(1, int(sqrt(x))+1):
    if x % i == 0:
        fac.append(i)
        fac.append(int(x / i))
print(fac)
