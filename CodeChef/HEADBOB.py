def checkIndian(string):
    if "I" in string:
        return "INDIAN"
    elif "Y" in string:
        return "NOT INDIAN"
    else:
        return "NOT SURE"

for t in range(int(input())):
    n = int(input())
    string = input()
    print(checkIndian(string))
