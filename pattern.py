

###########----- question 1 -----###########
# row=int(input("Enter your row number: "))
# b=0
# for i in range(row,0,-1):
#     for j in range(1,i+1):
#         print("5",end=" ")
        
#     print("\r")

###########----- question 1 -----###########

row=int(input("Enter your row number: "))

for i in range(row,0,-1):
    for j in range(i):
        print(j,end=" ")
        
    print("\r")

    





