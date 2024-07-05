import math

def binarySearch(A: list, T: int):
    L = 0
    R = len(A)-1
    while L <= R:
        m = math.floor((L+R)/2)
        if A[m] < T:
            L = m+1
        elif A[m] > T:
            R = m-1
        else:
            return m
    return "unsuccesful"

print(binarySearch([1,2,3,4,5,6,7,8,9,10,11,12],8))
print(binarySearch([1,2,3,4,5,6,7,9,10,11,12],8))
