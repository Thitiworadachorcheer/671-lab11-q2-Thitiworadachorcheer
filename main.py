def summation (lst1 , lst2):
    one = []
    for i in range (len(lst1)):
        one.append(lst1[i] + lst2[i])
    return one

def find_min_max (two):
    min_lst = min(two)
    max_lst = max(two)
    return min_lst, max_lst

n = int(input())
lst1 = []
for j in range (n):
    lst1.append(int(input()))
lst2 = []
for j in range (n):
    lst2.append(int(input()))

job = summation(lst1 , lst2)
print(job)

print(find_min_max(job))# YOUR CODE HERE
