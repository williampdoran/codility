
def sockMerchant2(n, ar):
    counts = [0] * (100+1)
    for i, sock in enumerate(ar):
        counts[ar[i]] +=1
    odds = 0
    for count in counts:
        if count % 2 == 1:
            odds += 1
    return (n - odds)//2

def sockMerchant(n, arr):
    counts = {}
    pairs = 0
    for sock in arr:
        counts[sock] = counts.get(sock, 0) + 1
        if counts[sock] %2 == 0:
            pairs += 1
    return pairs

n= 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

assert 3 == sockMerchant(n, ar)