# 1TASK 1
num1 = int(input("Enter first number: ")) # num 1 = 15
num2 = int(input("Enter second number: ")) # num 2 = 30

print(f"{num1} == {num2} : {num1 == num2}") # 15== 30 : False
# Explanation for output 1: The "==" sign is used to check for comparism(equality). 
# num1(15) is not equal to num2(30) because 15 is less than 30.
# Hence, the output is False.

print(f"{num1} != {num2} : {num1 != num2}") #15 != 30 : True
# Explanation for output 2: The "!=" sign is used to check for comparism(e i.e not equal). 
# num1(15) is not equal to num2(30) because 15 is less than 30.
# Hence, the output is True.

print(f"{num1} > {num2} : {num1 > num2}") #15 > 30 : False
# Explanation for output 3: The " > " is a comparism operator used to check if a number is greater than the other.
# num1(15) is not greater than num2(30) because 15 is less than 30.
# Hence, the output is False.

print(f"{num1} < {num2} : {num1 < num2}") #15 < 30 : True
# Explanation for output 4: The " < " is a comparism operator used to check if a number is less than the other.
# num1(15) is less than num2(30) because 15 is less than 30.
# Hence, the output is True.


#  Give 3 usecases or scenarios where you can apply the program below.
#1. It can be used for admission process.
#2. It can be used for checking job acceptance status.
#3.  It can be used for population census.


#  Write the code for 1 of the 3 use cases.
# case scenario - Checking for admission status and age requirement.

Candidate_score = int(input("Enter your Jamb score: "))
Age = int(input("Enter your age score: "))
cut_off_mark = 200
Age_requirement = 18

eligibility = (Candidate_score >= 18) and (Age >= 18)
print(f"{Candidate_score} >= {cut_off_mark} : {Candidate_score >= cut_off_mark}")
print(f" You scored {Candidate_score} and your age is {Age}.\nEligibility: {eligibility}\nN.b If your eligibility prints true, you have been admitted. If it is false, you admission has been denied.")




