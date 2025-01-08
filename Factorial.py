
def factorial(n) :
     return 1 if n==0 else n*factorial(n-1)
num = int(input("Enter the number to know Factorial"))
print(f"factorial:{factorial(num)}")