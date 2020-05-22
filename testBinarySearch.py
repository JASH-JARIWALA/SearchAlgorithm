import numpy as np
import datetime
import math

search = input("Search : ").upper()

loadStart = datetime.datetime.now()
a = np.load('testArray.npy')
loadEnd = datetime.datetime.now()
loadTime = (loadEnd - loadStart).microseconds/1000

executionStart = datetime.datetime.now()
result = []
# #Compare
l1 = search.upper()

low = 0
high = a.__len__()-1
mid = None
while low < high:    
    mid = (low + high) // 2
    l2 = a[mid]    
    if l2[:len(l1)] == search :
        break
    else:        
        if search < a[mid]:
            high = mid - 1
        else:
            low = mid + 1
            
    
l = len(search)
i = mid
while 1:
    s = a[i]
    if s[:l] == search and l>=3:
        result.append(s)
    elif s[:l] == search and len(s)<l+3:
        result.append(s)
    elif s[:l] != search:
        break
    i-=1    

result.reverse()

i = mid+1

while  i < len(a):
    s = a[i]
    if s[:l] == search and l>=3:
        result.append(s)
    elif s[:l] == search and len(s)<l+3:
        result.append(s)
    elif s[:l] != search:
        break
    i+=1




executionEnd = datetime.datetime.now()
executionTime = (executionEnd - executionStart).microseconds/1000

# for r in result:print(r)
print("Number of words found : ", str(len(result)))
print("Search time: ", str(executionTime))
print("Array Load time: ", str(loadTime))
print("Total : ",str(executionTime+loadTime))



# Compare
# l1 = 'A'
# l2 = 'ABC'

# a1 = []
# a2 = []

# l = len(l1) if len(l1)<len(l2) else len(l2)


# for i in range(len(l1)):
#     a1.append(ord(l1[i]))

# for i in range(len(l2)):
#     a2.append(ord(l2[i]))

# high = l1
# if l1 == l2[:len(l1)]:
#     print("Equal")
# else:
#     for i in range(l):
#         if a1[i] >= a2[i]:
#             continue 
#         else:
#             high = l2
#             break
#     print(high)