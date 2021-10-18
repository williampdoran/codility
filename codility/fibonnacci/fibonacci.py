def fibonacci(n):
    if(n <=1):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n-2)

print(fibonacci(5))

def fibonnacci_dyn(n):
    fib = [0]* (n+2)
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i -2]
    return fib[n]

print(fibonacci(50))
print(fibonnacci_dyn(50))