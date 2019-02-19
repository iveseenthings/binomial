import math

def nCr(p,q):            #combination of n-elements by k-range, where n=p and k=q
    f = math.factorial
    if p == q:
        return 1
    elif q == 1:
        return p
    elif q > p:
        return 0
    else:
        return ((f(p))//(f(p-q)*f(q)))

a = str(input('insert addent #1 --> '))
b = str(input('insert addent #2 --> '))
n = int(input('insert n -->'))
nvalues = [] #n-values list
kvalues = [] #k-values list
k = 0
k1 = k-1
n1=n+1

print('\n','   Traceback data: ')
print('\n    ', '(',a, '+',b, ')','^',n,'\n')
print('-----------------------')

#n-values calculation
while n1 > 0:
    n1 = n1-1
    print('n: ', n1)
    nvalues.append(n1)

print('-----------------------')
#k-values calculation
while k1 < n:
    k1 = k1+1
    print('k: ', k1)
    kvalues.append(k1)

#print('-----------------------')
#printing n-values and k-values
#print('n values: ', nvalues)
#print('k values: ', kvalues)

print('-----------------------')

#binomial coefficients calculation
i = n+1
l = -1
Bc = []
while i>0 and l<=n+1:
    i=i-1
    l = l+1
    x = nCr(n,kvalues[l])
    Bc.append(x)
    print('binomial coefficient', '(',l+1,')' ' = ', x, '\n')

#print('-----------------------')
#print('binomial coefficient values:\n', Bc)
print('-----------------------')

#generate list of monomials
monomial = []
z=n+1
m=-1
while z>0 and m<=n+1:
    z=z-1
    m=m+1
    mon = str('(') + str(Bc[m]) + str(a) + str('^') + str(nvalues[m])+ str(' * ') + str(b) + str('^') + str(kvalues[m])+str(')')
    print('monomial(',m+1,') =',mon,'\n')
    monomial.append(mon)

#result output
print('\nRESULT:\n')
for o in monomial:
    print(o, end = ' + ')

print('\n\n')
