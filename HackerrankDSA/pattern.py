def print_door_mat(N, M):
    # Top portion (upper mat)
    for i in range(N // 2):
        pattern = ".|." * (2 * i + 1)
        print(pattern.center(M, "-"))

    # Middle line (center mat)
    print("WELCOME".center(M, "-"))

    # Bottom portion (lower mat)
    for i in range(N // 2 - 1, -1, -1):
        pattern = ".|." * (2 * i + 1)
        print(pattern.center(M, "-"))


if __name__ == "__main__":
    N, M = map(int, input().split())
    print_door_mat(N, M)
