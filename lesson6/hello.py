# import os, shutil
# oldFile = 'folder/spam'+str('{:0>3}'.format(11)+'.txt')
# newFile = 'folder/spam'+str('{:0>3}'.format(10)+'.txt')
# shutil.move(oldFile, newFile)

# for i in range(1, 10):
#     with open('folder/test00'+str(i)+'.pdf', 'w+') as f:
#         f.write(str(i))
# for i in range(10, 31):
#     with open('folder/spam0'+str(i)+'.txt', 'w+') as f:
#         f.write(str(i))

# import pyinputplus as pyip
# def str_to_bool(string):
#     if string == 'yes':
#         string = True
#     else:
#         string = False
#     return string
# tomato = pyip.inputYesNo('tomato? (y or n): ')
# print(tomato)
# print(type(tomato))
# tomato = str_to_bool(tomato)
# print(type(tomato))

# import re

# reg_match = re.compile(r'[.yaml|.json]$')

# list = ["file.json", "test.txt", "file.yaml", "file.pdf", "thefile.doc"]

# for i in list:
#     if re.search(reg_match, i):
#         print(i)

import yaml

with open('folder/file_json.yaml') as file:
    documents = yaml.full_load(file)

print(type(documents))

for item, doc in documents.items():
    print(item, ":", doc)
