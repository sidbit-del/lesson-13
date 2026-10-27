print("half pyramid pattern of stars")
r=int(input("enter the number of rows:"))

for i in range(r):

    for j in range(i+1):
        print("*",end="")

    print()