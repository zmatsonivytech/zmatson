
integer = input("Enter a nonnegative integer")
factorial = 1
if int(integer) == 1:
    print("factorial of 1 is 1")
elif int(integer) < 1:
    print("Error, please enter a nonnegative integer")
elif int(integer) >= 1:
    for integer in range(1, int(integer)+1):
        factorial = factorial * integer
    print(factorial)

