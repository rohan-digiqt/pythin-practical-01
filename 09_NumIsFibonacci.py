a = int(input('Enter Number: '))

n1, n2 = 0, 1

count = 0


if a <= 0:
   print("Please enter a positive integer")
elif a == 1:
   print("Fibonacci sequence upto",a,":")
   print(n1)
else:
   while count < a:
       nth = n1 + n2

       n1 = n2
       n2 = nth
       count += 1
       if nth == a:
           print(a,' is a fibonacci series number')
       else:
           print(a,' is not a fibonacci series number')
           break