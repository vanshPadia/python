'''selection_sort'''
def sort(num):
    n =len(num)

    for i in range(0,n):
        min = i
        for j in range(i,n):
            if num[j]> min[i]:
                min[i] ,num[j],num[j],min[i]
    return sort
sort(num=[1,3,5,6,2,7,9,8])
print(sort)