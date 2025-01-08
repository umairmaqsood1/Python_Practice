num=int(input("Enter the number to check for Prime"))
if num>1:
    for i in range(2,int(num** 0.5)+1):

        if num % i ==0:
            print("The number is not Prime")
            break
        else:
            print("The number is Prime")
else:
    print("The number is not Prime")
