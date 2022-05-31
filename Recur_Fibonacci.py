
# Take a upper limit and print the Fibonacci series upto that series using "Recursion" method
# Fibonacci series : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...

n = int(input('\nEnter the limit of series : '))

def fibo(n):
    if n<0:
        return "Invalid Input"
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

for i in range(n):
    print('{}'.format(fibo(i)))