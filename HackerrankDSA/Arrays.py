def reverseArray(A):
    reverseArray = A[::-1]
    return reverseArray


if __name__=="__main__":
    n = int(input().strip())

# Read the array elements
A = list(map(int, input().strip().split()))
reversed_A = reverseArray(A)


print(" ".join(map(str, reversed_A)))
.
