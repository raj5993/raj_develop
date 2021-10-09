

row=int(input("enter you number of row: "))

m=row-2
for i in range(row,-1,-1):
    for j in range(m,0,-1):
        print(end=" ")
    m=m+1
    for j in range(0,i+1):
        print("*",end=" ")
    print(" ")



k=row*2-2

for i in range(0,row):
    for j in range(0,k):
        print(end=" ")
    k=k-1
    for j in range(0,i+1):
        print("*",end=" ")
    print("\r")








