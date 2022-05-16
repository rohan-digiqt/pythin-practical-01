a = int(input('Enter First Number: '))
b = int(input('Enter Second Number: '))

if a == b:
    print(a , ' and '  ,b , ' both are equal.')
elif a > b:
    print(a, ' is Maximum.')
else:
    print(b, ' is Maximum.')


# Way - 2

Maximum = max(a,b)
print(Maximum, ' is Maximum.')