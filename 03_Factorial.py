a = int(input('Enter Number: '))


def fact(num):
    ans = 1
    for i in range(1, a + 1):
        ans = ans*i
    print('Factorial of ',a,' is ',ans)

if a < 0:
    print('Please Enter Valid Number.')
elif a == 0:
    print('Factorial of 0 is 1')
else:
    fact(a)

# Way - 2

import math

print(math.factorial(a))