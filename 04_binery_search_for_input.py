def search(lst, target):
    l = 0
    u = len(lst) - 1
   

    while l <= u:
        mid = (l + u) // 2

        if lst[mid] == target:
            return [mid]
            break
        elif lst[mid] != target:
            if target < lst[mid]:
                u = mid - 1
            else:
                l = mid + 1
    return -1
    
#list is sorted




my_list = []
num = int(input("Enter the number of elements you want to add to the list: "))

# Loop to get numbers and append them to the list
for i in range(num):
    number = int(input(f"Enter number {i + 1}: "))  # Prompt user for each number
    my_list.append(number)  # Append each number to the list

my_list.sort()
print("The list my_list is:", my_list)

continou = 'y'
while continou == 'y':
    target_value =int(input("enter a number you want to find : "))
    search_result = search(my_list, target_value)

    if search_result != -1:
        print(f"We found {search_result} at index {target_value}")
    else:
        print("not Found")
    break
continou = input("enter y for continou: ")



