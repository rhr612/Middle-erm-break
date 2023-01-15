import math

print('Wellcome\n')
print('aX^2+bY+C  (b>a>c)\n'+'Input a-')
a1=input()
print('\nInput b`-')
b1=input()
print('\nInput c-')
c1=input()

print('Your input-  '+'a='+a1+'    b='+b1+'    c='+c1)


a=float(a1)
b=float(b1)
c=float(c1)

#calculation////////////////////////////////////////

root = math.sqrt(b*b-4*a*c)
x1=(-b+root)/(2*a)
x2=(-b-root)/(2*a)
print(root)
print('The Reasult is-\n')
print('X1=  ')
print(x1)
print('\nX2=  ')
print(x2)
