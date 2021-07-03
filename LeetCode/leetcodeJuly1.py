def grayCode(n: int):
    if (n <= 0):
        return
    arr = list()
    arr.append("0")
    arr.append("1")
    i = 2
    j = 0
    while(True):
        if i >= 1 << n:
            break
        for j in range(i - 1, -1, -1):
            arr.append(arr[j])
        for j in range(i):
            arr[j] = "0" + arr[j]
        for j in range(i, 2 * i):
            arr[j] = "1" + arr[j]
        i = i << 1
    for i in range(len(arr)):
        arr.append(i)
    arr = [x for x in arr if not isinstance(x, int)]
    lst = []
    for j in arr:
        lst.append(int(j,2))
    print(lst)
grayCode(2)
