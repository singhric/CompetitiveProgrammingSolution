def checkVol(n):
    lst = ['A', 'E', 'I', 'O', 'U']
    for i in lst:
        if i == n:
            return 1
    return 0
n = input()
vol = checkVol(n)
if vol == 1:
    print("Vowel")
else:
    print("Consonant")
