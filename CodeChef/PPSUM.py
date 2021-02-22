def sumNum(D, N):
    for d in range(D):
        sum = 0
        for i in range(1, N+1):
            sum = sum + i
        N = sum
    return sum
for t in range(int(input())):
    D, N = map(int,input().split())
    print(sumNum(D, N))