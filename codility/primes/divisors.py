def divisors(n):
    i = 1
    results = 0
    while(i * i < n):
        if n % i == 0:
            results += 2
        i += 1
    if(i * i == n):
        results += 1
    return results

def isPrime(n):
    i = 2
    while( i * i < n):
        if n % i == 0:
            print(i, n/i)
            return False
        i += 1
    return True

def coins(n):
    coin = [0] * (n+1)
    for i in range(1, n+1):
        coin[i] = divisors(i) % 2
    return coin[1:]

print(divisors(36))

print(isPrime(12345))
print(coins(10))


