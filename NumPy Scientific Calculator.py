import numpy as np
print("====Numpy Scientific Calculator====")
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
#Convert into NumPy arrays
arr=np.array([num1,num2])
#Basic Operations
print("Addition:",np.add(num1,num2))
print("Subtraction:",np.subtract(num1,num2))
print("Multiplication:",np.multiply(num1,num2))
print("Division:",np.divide(num1,num2))
#Power
print("\nPower")
print(f"{num1}^{num2}=",np.power(num1,num2))
#Square Root
print("\nSquare root")
print("Square Root of first num is:",np.sqrt(num1))
print("Square Root of second num is:",np.sqrt(num2))
#Trignometry
print("\nTrignometry Values:")
print("sin of first num is:",np.sin(num1))
print("cos of first num is:",np.cos(num2))
print("tan of first num is:",np.tan(num1))

#Arrays Operations
print("\nArray Created")
print(arr)
print("Mean:",np.mean(arr))
print("Standard Deviation:",np.std(arr))
print("Maximum:",np.max(arr))
print("Minimum:",np.min(arr))
#Rounded Values
print("\nRounded Values:")
print("Round form",np.round(arr,2))

