import re
import os

list =[]
for i in os.listdir("folder"):

    if i.startswith("spam"):
        m = re.match(r"([a-zA-Z]+)(\d+)",i)
        list.append(int(m.group(2)))

list.sort()
x = 1
for i in list:
    if x == i:
        x += 1
    else:
        oldFile = 'folder/spam'+str('{:0>3}'.format(i)+'.txt')
        newFile = 'folder/spam'+str('{:0>3}'.format(x)+'.txt')

        x += 1
        os.replace(oldFile, newFile)



