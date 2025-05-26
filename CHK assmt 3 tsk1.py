# Assignment 3 chkbe92@gmail.com

print ("'Assignment 3 Task 1' User : chkeb92@gmail.com")
print ("Calculate Factorial Using a Function")


def factorial(n):

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

sample = 5
z = 1
for x in range(1, sample + 1):
    z = z * x

#print('Factorial of 5 is:', z)

number = int(input("Enter a number to calculate its factorial: "))
print(f"Factorial of {number} is: {factorial(number)}")

