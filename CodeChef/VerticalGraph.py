n = int(input("Amount of N: ")) 
inputs = [] 
for x in range(n): 
    inputs.append(input("Input: "))
print(max(inputs))

for x in range(n):
    for z in int(inputs[x]):
        print("*", end=' ')
    print("\n")
print(inputs)