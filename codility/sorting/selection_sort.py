
N = [2,3,6,7,4,9,0,2]

def selection_sort(A):
    n = len(A)
    for i in range(0, n):
        min_index = i
        for j in range(i + 1, n):
            if A[j] < A[min_index]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]
    return A

def counting_sort(A, k):
    n = len(A)
    counts = [0] * (k +1)
    for i in range(0, n):
        counts[A[i]] += 1
    p = 0
    for i in range(0, k+1):
        for j in range(counts[i]):
            A[p] = i
            p += 1
    return A

def merge(l, r):
    result = [0] * (len(r) + len(l))
    j, k = 0, 0
    for i in range(0, len(result)):
        if j == len(l):
            result[i] = r[k]
            k += 1
        elif k == len(r):
            result[i] = l[j]
            j += 1
        elif l[j] > r[k]:
            result[i] = r[k]
            k += 1
        else:
            result[i] = l[j]
            j += 1
    return result

def merge_sort(A):
    n = len(A)
    if n <= 1:
        return A
    mid = (0 + n)//2
    left = A[:mid]
    right = A[mid:]
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    return merge(sorted_left, sorted_right)

def insertion_sort(A):
    for index in range(1, len(A)):
        current_value = A[index]
        current_index = index
        while current_index > 0 and A[current_index -1] > current_value:
            A[current_index] =A[current_index -1]
            current_index = current_index -1
        A[current_index] = current_value
    return A

def partition(A, low, high):
    i = low - 1
    pivot = A[high]
    for j in range(low, high):
        if A[j] <= pivot:
            i = i +1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[high] = A[high], A[i+1]
    return (i + 1)


def qs(A, low, high):
    if len(A) == 1:
        return A
    if low < high:
        pivot = partition(A, low, high)
        qs(A, low, pivot -1)
        qs(A, pivot +1, high)

def quick_sort(A):
    low, high = 0, len(N) -1
    qs(A, low,high)
    return A


# print(selection_sort(N))
# print(counting_sort(N, 10))

# print(merge([1,2,3], [2,4,5]))
# print(merge_sort(N))
# print(insertion_sort(N))
print(quick_sort(N))