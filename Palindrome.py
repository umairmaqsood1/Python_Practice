string=input("Enter the String to check for Palindrome:")
if string==string[::-1]:
    print("The String is palindrome")
else:
    print("The given String is not Palindrome")