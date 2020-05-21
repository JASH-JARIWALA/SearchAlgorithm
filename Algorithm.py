import numpy as np
a = [{'w': False, 'l': None} for c in range(26)]

# Create
for n1 in range(26):
    a[n1]['l'] = [{'w': False, 'l': None} for c in range(26)]  ## 26 * 26
    for n2 in range(26):
        a[n1]['l'][n2]['l'] = [{'w': False, 'l': None} for c in range(26)]  ## 26 * 26 *26
        for n3 in range(26):
            a[n1]['l'][n2]['l'][n3]['l'] = [{'w': False, 'l': None} for c in range(26)]  ## 26 * 26 * 26 * 26



# Read
file = open('words_alpha.txt','r')
c = 0;
for index in range(370104):    
    search =  file.readline().strip().upper() 
    # c = c+1
    # print(c) 
    is_length_greater = True if len(search) > 4  else False 
    l = 4 if is_length_greater else len(search)
    s = a[ord(search[0]) - 65]

    for i in range(l-1):
        s = s['l'][ord(search[i+1]) - 65]

    if is_length_greater:
        if s['l'] == None:
            s['l'] = [search]             
        else:
            array = s['l']
            array.append(search)
        # print(s['l'])
        # print("size: ", end="")
        # print(len(s['l']), end=",")
    else:
        s['w'] = search
        # print (s['w'])
    # print(a[0]['l'][1]['l'][2]['w'])

np.save('array', a)




    