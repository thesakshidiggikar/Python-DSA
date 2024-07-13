def flippingBits(n):
    return ~n & 0xFFFFFFFF


if __name__ == "__main__":
    q = int(input().strip())
    for _ in range(q):
        n = int(input().strip())
        print(flippingBits(n))
if __name__ == "__main__":
    q = int(input().strip())
    for _ in range(q):
        n = int(input().strip())
        print(flippingBits(n))
