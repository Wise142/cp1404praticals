"""
get number_of_gift
get number_of_student

gift_per_student= number_of_gift // number_of_student
left_gift= number_of_gift % number_of_student

display gift_per_number
display left_gift

"""

number_of_gift = int(input("How many gifts :"))
number_of_student = int(input("How many students :"))

gift_per_student = number_of_gift // number_of_student
left_gift = number_of_gift % number_of_student

print("Each student will get", gift_per_student, "gifts")
print("This is how much gift left", left_gift)
