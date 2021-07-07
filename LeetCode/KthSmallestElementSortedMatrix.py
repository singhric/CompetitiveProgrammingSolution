def kthSmallest(matrix, k: int):
    lst = []
    # lst = [i for sub in matrix for i in sub]
    for i in matrix:
        for j in i:
            lst.append(j)
    lst.sort()
    print(lst)
    return lst[k-1]


matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
lst = kthSmallest(matrix, k)
print(type(lst))
print(lst)
