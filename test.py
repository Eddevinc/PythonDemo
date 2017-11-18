def fib(x):
    return(0 if x ==0 else (1 if x == 1 else fib(x-1)+fib(x-2)))


n = int(input("Enter number of elements to display: "))
for i in range(n):
    print(fib(i), end='')
