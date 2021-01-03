# fibonacci series by fun

def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

n = int(input("enter no"))
for i in range(1, n+1):
    x = fib(i)
    print(x, end=" ")


# this fuc is returning value and save them
def fib(n):
    d={}
    if n in d:
        return d[n]
    if n <= 2:
        return 1
    d[n] = fib(n - 1) + fib(n - 2)
    return d[n]

a = fib(50)
print('\n',a)
# print(fib(15))
# print(fib(50))
