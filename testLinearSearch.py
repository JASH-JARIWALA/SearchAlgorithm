import numpy as np
import datetime

# a = []
# file = open('words_alpha.txt','r')
# c = 0;
# for index in range(370104):    
#     search =  file.readline().strip().upper()
#     a.append(search)

# np.save('testArray', sorted(a))

search = input("Search : ").upper()

loadStart = datetime.datetime.now()
a = np.load('testArray.npy')
loadEnd = datetime.datetime.now()
loadTime = (loadEnd - loadStart).microseconds/1000

executionStart = datetime.datetime.now()
result = []

l = len(search)
c = 0
for s in a:
    # c+=1
    if s[:l] == search and len(search) >= 3:
        result.append(s)
    elif s[:l] == search and len(s)<l+3:
        result.append(s)

executionEnd = datetime.datetime.now()
executionTime = (executionEnd - executionStart).microseconds/1000

# for r in result:print(r)
print("Number of words found : ", str(len(result)))
print("Search time: ", str(executionTime))
print("Array Load time: ", str(loadTime))
print("Total : ",str(executionTime+loadTime))

