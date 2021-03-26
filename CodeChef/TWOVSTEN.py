for t in range(int(input())):
    n = input()
    count = 0
    if n[-1]=='0' or n[-1]=='5':
        while n!=0:
            if int(n)%10==0:
                break
            n = int(n)*2
            count = count + 1
        print (count)
    else:
        print("-1")
        


