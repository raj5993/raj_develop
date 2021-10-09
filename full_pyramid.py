
n = int(input("Enter the number of rows: "))  
m = (2 * n) - 2  
for i in range(0, n):  
    for j in range(0, m):  
        print(end=" ")  
    m = m - 1  # decrementing m after each loop  
    for j in range(0, i + 1):  
        # printing full Triangle pyramid using stars  
        print("* ", end=' ')  
    print(" ")  

############---------2nd Trianglr---------#############
row=int(input("enter your number of row: "))
k=row*2-2

for i in range(0,row):
    for j in range(0,k):
        print(end=" ")
    k=k-1
    for j in range(0,i+1):
        print("*",end=' ')
    print("\r")