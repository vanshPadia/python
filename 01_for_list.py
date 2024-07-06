print('hello world')
L1 = []  # Initialize an empty list

# Get input from user for number of elements in the list
num = int(input("Enter the number of elements you want to add to the list: "))

# Loop to get numbers and append them to the list
for i in range(num):
    number = int(input(f"Enter number {i + 1}: "))  # Prompt user for each number
    L1.append(number)  # Append each number to the list

print("The list L1 is:", L1)
l2 =L1.sort()

# continou = 'y'
# while (continou == 'y'):
#     find =int(input("enter a number you want to find : "))
#     found = False
#     for x in L1:
#         if x == find:
#             found = True
#             break
#     if found:
#         print ("we find the numder " ,find)
#     else:
#         print("we can not  find the number ",find)

#     continou = input("enter y for continou: ")


    



