# Example 1: Checking if a Number is Positive or Negative
num : int = int(input("write any number : "))
if num < 0 :
    print("its a negative number")
else:
    print("its a positive number")

# Example 2: Determining if a Number is Even or Odd
if num % 2 == 0:
    print("its a even number")
else:
    print("its a odd number")

# Example 3: Checking if a Student Passed or Failed

marks : int = int(input("write your marks : "))
if marks > 33 :
    print("its pass")
else:
    print("its fail")