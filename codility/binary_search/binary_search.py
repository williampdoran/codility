def binary_search(A, elem):
    start= 0
    end = len(A) -1
    result = -1
    while(start <= end):
        mid = (start + end)//2
        if(A[mid] <= elem):
            start = mid +1
            result = mid
        else:
            end = mid -1
    return result

print(binary_search([1,2,3,4,5,6], 5))
print(binary_search([1,2,3,4,5,6], 7))