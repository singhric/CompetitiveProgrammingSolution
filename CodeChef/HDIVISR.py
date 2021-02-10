def printDivisors(n) : 
    i = 1
    while i <= n : 
        if (n % i==0) : 
            if (i<=10):
                TenList.append(i) 
        i = i + 1
TenList = []
n = int(input())
printDivisors(n)
print(max(TenList))