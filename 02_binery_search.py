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




my_list = [1, 3, 5, 7, 9, 11, 13]
target_value = 14


search_result = search(my_list, target_value)

if search_result != -1:
    print(f"We found {search_result} at index {target_value}")
else:
    print("not Found")



# def search(lst, target):
#     l = 0
#     u = len(lst) - 1

#     while l <= u:
#         mid = (l + u) // 2

#         if lst[mid] == target:
#             return mid  # Return the index where target is found
#         elif target < lst[mid]:
#             u = mid - 1
#         else:
#             l = mid + 1

#     return -1  # Return -1 if target is not found

# # Example usage:
# my_list = [1, 3, 5, 7, 9, 11, 13]
# target_value = 2
# search_result = search(my_list, target_value)

# if search_result != -1:
#     print(f"We found {target_value} at index {search_result}")
# else:
#     print(f"{target_value} is not in the list.")
