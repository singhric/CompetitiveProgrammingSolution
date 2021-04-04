def checkHost(num):
    lst = [2010, 2015, 2016, 2017, 2019]
    for i in lst:
        if i == num:
            return True
    return False

for i in range(int(input())):
    num = int(input())
    if checkHost(num):
        print("HOSTED")
    else:
        print("NOT HOSTED")