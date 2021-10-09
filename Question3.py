
row= int(input("enter your number: "))

for i in range(1,row):
    for j in range(i):
        print((i*2-1),end=" ")
    print("\r")
    

i=1

while i<=row:
    j=1
    while j<=i:
        print((i*2-1),end=" ")
        j=j+1
    i=i+1
    print("\r")

