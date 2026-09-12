def fact(num): 
    if num == 0: 
        return 1
    return num * fact(num -1)
num = int(input("Enter a number to find factorial : "))
print(f"Factorial of {num} is : ", fact(num))