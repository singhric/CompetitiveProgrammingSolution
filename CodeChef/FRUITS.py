for t in range(int(input())):
    N, M, K = map(int, input().split())
    large = max(N,M)
    small = min(N,M)
    if large != small:
        while K!=0:
            small = small +1
            K = K - 1
            if small == large:
                break
    print(large-small)