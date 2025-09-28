total = 0
count = 0

age = int(input("Enter age (-1 to stop): "))
while age != -1:
    total += age
    count += 1
    age = int(input("Enter age (-1 to stop): "))

if count > 0:
    average = total / count
    print("Total of ages:", total)
    print("Average age:", average)
else:
    print("No ages were entered.")
