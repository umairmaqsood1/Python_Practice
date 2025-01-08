num=int(input("Enter the Number:  "))
sum_of_digits=sum(int(digit)**len(str(num)) for digit in str(num))
if num==sum_of_digits:
    print("f{num} : Is ArmStrong")
else:
    print("f{num} Is not ArmStrong")