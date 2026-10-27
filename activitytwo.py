print("floyd's triangle")
r=int(input("enter the number of rows:"))

for i in range(1,r):

    for j in range(1,i+1):
     print(i,end="",)
     i+=1

    print()