from collections import OrderedDict


check_list = [1,8,5,7,10,9,3,2,4,4,4]
n = 6

#Option 1: For loop
check_list.sort()
new_list = []
for i in range(len(check_list)):
    if check_list[i] not in new_list:
        new_list.append(check_list[i])
print new_list[n-1]


#Option 2: collections module
print list(OrderedDict.fromkeys(check_list))[n-1]

#option 3: Using set
print list(set(check_list))[n-1]
