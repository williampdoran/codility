def caterpillar(A, sum):
    n = len(A)
    front = 0
    running_total = 0
    for back in range(0, n):
        while (front < n and running_total + A[front] <= sum):
            running_total += A[front]
            front += 1
        if running_total == sum:
            return A[back:front]
        running_total -= A[back]

print(caterpillar([6,2,7,4,1,3,6], 12))

def triangles(A):
    A.sort()
    n = len(A)
    result = 0
    for x in range(n):
        z = x + 2
        for y in range(x + 1, n):
            print(x,y,z, result)
            # print(A[x],A[y],A[z])
            while( z < n and A[x] + A[y] > A[z]):
                z += 1
            result += z -y -1
    return result

print(triangles([10,2,5,1,8,12]))