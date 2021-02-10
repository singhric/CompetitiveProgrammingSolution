for t in range(int(input())):
    p = int(input())
    division = []
    while p%2==0:
        div = p/2
        print(div)
        division.append(div)
    # print(division)
    # 2i-1 (1 ≤ i ≤ 12)
    # for i in range(1,13):
    #     price = 2**(i-1)
    #     print(price)