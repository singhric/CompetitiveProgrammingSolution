def lapindrome(word):
    left, right = '',''
    if(len(word)%2 == 0):
        left = word[:len(word)//2]
        right = word[len(word)//2:]
    else:
        left = word[:len(word)//2]
        right = word[len(word)//2+1:]
    lst1 = list(left)
    lst2 = list(right)
    lst1.sort()
    lst2.sort()
    left = str(lst1)
    right = str(lst2)
    if left==right:
        return "YES"
    else:
        return "NO"

for t in range(int(input())):
    word = input()
    print(lapindrome(word))