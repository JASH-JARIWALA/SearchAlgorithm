import numpy as np
import datetime
# from simpleArray import *


# a = [{'w': chr(65+c), 'l': None} for c in range(26)]

# for n1 in range(26):
#     a[n1]['l'] = [{'w': False, 'l': None} for c in range(26)]  ## 26 * 26
#     for n2 in range(26):
#         a[n1]['l'][n2]['l'] = [{'w': False, 'l': None} for c in range(26)]  ## 26 * 26 *26
#         for n3 in range(26):
#             a[n1]['l'][n2]['l'][n3]['l'] = [{'w': False, 'l': None} for c in range(26)]  ## 26 * 26 * 26 * 26



search = input("Search: ").upper()
result = []
c = 0

#Load
loadStart = datetime.datetime.now()
a = np.load('array.npy', allow_pickle=True)
loadEnd = datetime.datetime.now()
loadTime = (loadEnd - loadStart).microseconds/1000


#Execute
executionStart = datetime.datetime.now()

is_length_greater = True if len(search) > 4  else False 
l = 4 if is_length_greater else len(search)
s = a[ord(search[0]) - 65]

# SEARCH for length + 1
for i in range(l-1):
    s = s['l'][ord(search[i+1]) - 65]


# Store
if s['w'] == search: result.append(s['w']) 
if l > 3 and s['l'] != None:
    data = s['l'];
    for found in data:
        # c+=1
        if search in found:
            result.append(found)  
elif s['l'] != None:
    for found in s['l']:
        # c+=1        
        result.append(found['w']) if found['w'] != False else False

#SEARCH for length + 2
if l <= 3:
    for j in range(26):
        # c+=1
        s1 = s['l'][j]
        # print(s1['l'][0])    
    
        # Store
        if l > 2 and s1['l'] != None:
            data = s1['l'];
            for found in data:
                # c+=1
                if search in found:
                    result.append(found) 
        elif s1['l'] != None:
            for found in s1['l']:    
                # c+=1    
                result.append(found['w']) if found['w'] != False else False

executionEnd = datetime.datetime.now()
executionTime = (executionEnd - executionStart).microseconds/1000

# for r in result:print(r)
print("Number of words found : ", str(len(result)))
print("Search time: ", str(executionTime))
print("Array Load time: ", str(loadTime))
print("Total : ",str(executionTime+loadTime))
