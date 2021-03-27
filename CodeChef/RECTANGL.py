for t in range(int(input())):
    lst = list(map(int, input().split()))
    lst = sorted(lst)
    if lst[0] == lst[1] and lst[2] == lst[3]:
        print("YES")
    else:
        print("NO")