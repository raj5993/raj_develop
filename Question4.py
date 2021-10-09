
row=int(input("enter your number: "))

for i in range(1,row):
    for j in range(i):
        print(i,end=" ")
        i=i-1
    print("\r")

