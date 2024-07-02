def lonelyinteger(a):
    result = 0
    for number in a:
        result ^= number
    return result


# Input handling
if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    print(lonelyinteger(a))
