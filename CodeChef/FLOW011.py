def grossSalary(salary):
    if salary < 1500:
        return salary * 2
    else:
        hra = 500
        da = salary * 0.98
        return salary + da + hra

for t in range(int(input())):
    salary = int(input())
    print(grossSalary(salary))