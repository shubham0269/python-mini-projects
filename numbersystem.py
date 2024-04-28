

# ====================================== number printing ==============================================


print("choose the order:\n (1) : increasing \n (2) : decresing")
order = int(input("press: "))
if order == 1:
    print("enter your choice:\n (1) : rowise \n (2) : column")
    choice = int(input("press: "))
    
    if choice == 1:
        start = int(input("enter the starting point: "))
        end = int(input("enter the ending point: "))
        update = int(input("enter the update point: "))
        for i in range(start, end + 1, update):
            print(i, end=" ")
            
    elif choice == 2:
        start = int(input("enter the starting point: "))
        end = int(input("enter the ending point: "))
        update = int(input("enter the update point: "))
        for i in range(start, end + 1, update):
            print(i)
    else:
        print("not a valid input")

elif order == 2:
    print("enter your choice:\n (1) : rowise \n (2) : column")
    choice = int(input("press: "))
    
    if choice == 1:
        start = int(input("enter the starting point: "))
        end = int(input("enter the ending point: "))
        update = int(input("enter the update point: "))
        numbers = list(range(start, -(end - 1), -update))      
        for i in numbers:
            print(i, end=" ")
            
    elif choice == 2:
        start = int(input("enter the starting point: "))
        end = int(input("enter the ending point: "))
        update = int(input("enter the update point: "))
        numbers = list(range(start, -(end - 1), -update))
        
        
        for i in numbers:
            print(i)
            
    else:
        print("not a valid input")
else:
    print("syntax error")

















# print("Choose the order:\n (1): Increasing \n (2): Decreasing")
# order = int(input("Press: "))


# if order not in [1, 2]:
#     print("Not a valid order")
#     exit() 

# print("Enter your choice:\n (1): Row-wise \n (2): Column")
# choice = int(input("Press: "))


# if choice not in [1, 2]:
#     print("Not a valid input")
#     exit()


# start = int(input("Enter the starting point: "))
# end = int(input("Enter the ending point: "))
# update = int(input("Enter the update point: "))


# if order == 1 and update <= 0:
#     print("Update point must be positive for increasing order")
#     exit()
# elif order == 2 and update >= 0:
#     print("Update point must be negative for decreasing order")
#     exit()


# if order == 1:  
#     if start > end:
#         print("Starting point should be less than ending point for increasing order")
#     else:
#         if choice == 1:
#             for i in range(start, end + 1, update):
#                 print(i, end=" ")
#         elif choice == 2:
#             for i in range(start, end + 1, update):
#                 print(i)
            
# elif order == 2: 
#     if start < end:
#         print("Starting point should be greater than ending point for decreasing order")
#     else:
#         if choice == 1:
#             numbers = list(range(start, -(end - 1), -update))
#             for i in numbers:
#                 print(i, end=" ")
#         elif choice == 2:
#             numbers = list(range(start, -(end - 1), -update))
#             for i in numbers:
#                 print(i)
