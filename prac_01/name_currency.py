name = input("Enter your name: ")
while name == "":
    print("Name cannot be blank")
    name = input("Enter your name: ")

salary = float(input("Enter your salary: "))
while salary < 0:
    print("Salary cannot be below 0")
    salary = float(input("Enter your salary: "))

print("NAME:", name.upper())
print("SALARY: $", format(salary, ",.2f"), sep="")