def numberOfSquares(base):  
	base = (base - 2)  
	base = base // 2
	return base * (base + 1) / 2
for t in range(int(input())):
    base = int(input())
    print(int(numberOfSquares(base))) 
