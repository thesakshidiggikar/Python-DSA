# def rec(n):
#     if(n==0):  #function calling it self
#         return
#     print(n)
#     rec(n-1)

# rec(5)

# sum of first n natural numbers
def sum(n):
    if (n==0):
        return 0
    return sum(n - 1) + n
cal=sum(5)
print(cal)
