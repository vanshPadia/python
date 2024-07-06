def sort(arry):
    n = len(arry)
    
    for j in range(n):
        for i in range(0, n-j-1):
            if arry[i] > arry[i+1]:
            
                # temp = arry[i+1]
                # arry[i+1]=arry[i]
                # arry[i]=temp
            
                #arry[i], arry[i+1] = arry[i+1], arry[i]
                arry[i] = arry[i] ^ arry[i+1]
                arry[i+1] = arry[i] ^ arry[i+1]
                arry[i] = arry[i] ^ arry[i+1]
    
    return arry

my_arry = [1, 3, 56, 2, 6, 23, 67]
sorted_arry = sort(my_arry)
print(sorted_arry)


# def swap(a,b):
    # c =b
    # b =a
    # a =c
    # return a,b
# 
# a =1
# b =2
# a,b = swap(a,b)
# print(a,b)