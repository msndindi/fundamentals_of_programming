# comparison operators

print(10 == 10)
print(10 != 10)
print(10 < 10)
print(10 > 10)
print(10 <= 10)
print(10 >= 10)


ord('a')
print(ord('a'))


"bag" > "apple"
print("bag" > "apple")


# conditional statements
# indenting and : are very important in conditional statements

temperature = 15
if temperature > 25:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature < 10:
    print("It's a nice day")
else:
    print("It's a cold day")
print("Done")


# Ternary operator

# applicants_age = 20
# if applicants_age >= 18:
#     print("Applicant is eligible to vote")
# else:
#     print("Wait until you are 18 years old to vote")


applicants_age = 20
message = "Applicant is eligible to vote" if applicants_age >= 18 else "Wait until you are 18 years old to vote"
print(message)


student_age = 25
message = "You are qualified to apply for tech program" if student_age >= 20 else "Wait until you turn 18 years old to apply for tech program"
print(message)

# logical operators : and, or, not

high_income = True
good_credit = False
student = True

#and operator executes if both conditions are true
#or operator executes if any one of the conditions is true
#not operator executes if the condition is false

# if high_income or good_credit:
#     print("Eligible for loan")
# else:
#     print("Not eligible for loan")


# if not student:
#     print("Eligible for loan")
# else:
#     print("Not eligible for loan")

#You can combine logical operators to create more complex conditions. For example, you can check if a person is eligible for a loan based on their income, credit score, and student status.

if (high_income or good_credit) and not student:
    print("Eligible for loan")
else:
    print("Not eligible for loan")



#and operator
dog_age = 11
dog_home =  "Alta"

message = "Eligible for vaccination" if (dog_age > 10 and dog_home == "Alta") else "Not eligible for vaccination"
print(message)



