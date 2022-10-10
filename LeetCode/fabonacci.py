lst = []
t1 = 0
t2  = 1
nextTerm = t1 + t2
lst.append(t1)
lst.append(t2)
for i in range(12):
    lst.append(nextTerm)
    t1 = t2
    t2 = nextTerm
    nextTerm = t1 + t2
print(lst)
t = int(input("Enter the number of Students "))
room = int(input("Enter the number of rooms "))
while(t):
    userInput = int(input("Enter the age: "))
    if userInput in lst:
        print("Even")
    else:
        print("Odd")
