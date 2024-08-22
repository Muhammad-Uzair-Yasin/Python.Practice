# Print num from 1 to 10
for x in range(1,11):
    print(x , end = "")
    
# Printing Even num from 1 to 10
for x in range(2,11,2):
    print()
    print(x)

# printing any number table
num : int = int(input("write a time which table do you want : "))
for i in range(1,11):
    print(f"{num} * {i} = {num * i}")