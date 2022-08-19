from cmath import sqrt 
import sys
a = float(input('Enter 1st coefficient: '))
if a == 0:
    print("1st coefficient can't be zero. Program exits.")
    sys.exit()

b = float(input('Enter 2nd coefficient: '))
c = float(input('Enter 3rd coefficient: '))

D = b**2 - 4*a*c
if D>0:
    root1 = (-b+sqrt(D))/(2*a)
    root2 = (-b-sqrt(D))/(2*a)
    print('There are two real roots:',"{:.3f}".format(root1.real),'and',"{:.3f}".format(root2.real))

elif D==0:
    root = -b/(2*a)
    print('There is only one real roots:',"{:.3f}".format(root))

elif D<0:
    root1 = (-b/(2*a)) + ((sqrt(D))/(2*a))
    root2 = (-b/(2*a)) - ((sqrt(D))/(2*a))
    print('There are two complex roots:',"{:.3f}".format(root1),'and',"{:.3f}".format(root2))
