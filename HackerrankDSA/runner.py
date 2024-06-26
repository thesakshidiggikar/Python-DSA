if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())
    uq_score = list(set(arr))
    uq_score.sort(reverse=True)
    runne = uq_score[1]
    print(runne)
