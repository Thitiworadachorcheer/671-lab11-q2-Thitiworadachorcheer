def summation():
    n = int(input())
    
    lst1 = []
    lst2 = []
    
    for ao in range(n):
        lst1.append(int(input()))
    
    for bo in range(n):
        lst2.append(int(input()))
    
    updated_list = []
    for i in range(n):
        updated_list.append(lst1[i] + lst2[i])
    
    return updated_list

def find_min_max(lst):
    return min(lst), max(lst)

updated_list = summation()
print(updated_list)

print(find_min_max(updated_list))
