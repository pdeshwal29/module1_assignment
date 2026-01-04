num= int(input("enter a number: "))

def fact(num):
    factorial=1
    while num>1:
        factorial *= num
        num -=1

    return factorial

print(f"Factorial of {num} is {fact(num)}")