import numpy as np
import datetime

search = input("Search : ").upper()

loadStart = datetime.datetime.now()
a = np.load('testArray.npy')
loadEnd = datetime.datetime.now()
loadTime = (loadEnd - loadStart).microseconds/1000

executionStart = datetime.datetime.now()
result = []

# #Compare
l1 = search.upper()
# l2 = 'Z'

a1 = []
a2 = []

for i in range(len(l1)):
    a1.append(ord(l1[i]))



found = None

min = 0
max = a.__len__()
mid = 0
while 1:    
    mid = int((min + max)/2)    
    l2 = a[mid]    
    for i in range(len(l2)):
        a2.append(ord(l2[i]))


    if l1 == l2[:len(l1)]:
        print("Equal")
        break
    else:        
        if l1 > l2:
            min = mid
        else:
            max = mid
    

i = mid
while 1:
    s = a[i]
    if s[:len(search)] == search :
        result.append(s) if len(s) <= len(search)+2 else False
        i-=1
    else:
        break

result.reverse()

i = mid+1

while  i < len(a):
    s = a[i]
    if s[:len(search)] == search :
        result.append(s) if len(s) <= len(search)+2 else False
        i+=1
    else:
        break




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

# max = l1
# if l1 == l2[:len(l1)]:
#     print("Equal")
# else:
#     for i in range(l):
#         if a1[i] >= a2[i]:
#             continue 
#         else:
#             max = l2
#             break
#     print(max)