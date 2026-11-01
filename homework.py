print("welcome to the best star pyramid pattern ")
 
rows = int(input("Enter number of rows for star pattern: "))
 
for i in range(rows):
    for j in range(i + 1):
        print("* ", end="")
 

print("===== FLOYD'S TRIANGLE =====")
 
rows = int(input("Enter number of rows for Floyd's Triangle: "))
number = 1
 
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(number, end=" ")
        number += 1
 

print("===== DIAMOND NUMBER PATTERN =====")
 
row_size = int(input("Enter number of rows for diamond pattern: "))
 
if row_size % 2 == 0:
    half_rows = row_size // 2
else:
    half_rows = row_size // 2 + 1
 
space = half_rows - 1
 
for i in range(1, half_rows + 1):
    for j in range(1, space + 1):
        print(" ", end="")
 
    space -= 1
    number = 1
 
    for j in range(2 * i - 1):
        print(number, end="")
        number += 1
 
    
space = 1
 
for i in range(1, half_rows):
    for j in range(1, space + 1):
        print(" ", end="")
 
    space += 1
    number = 1
 
    for j in range(1, 2 * (half_rows - i)):
        print(number, end="")
        number += 1
 
    
 
print("Loop designs finished bye bye=====")
print("You created star and triangle and diamond patterns using nested loops")
