def fib(n):
    if(n<=1):
        return n
    return fib(n-1)+ fib(n-2)
s=int(input("enter the  value"))
print("no.of ways:",fib(s+1))
