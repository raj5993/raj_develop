
row=int(input("enter your number: "))

for i in range(row,0,-1):
    for j in range(i):
        print(j,end=" ")
    print("\r")
    