import os, shutil
import re

menu = """
        1. List all files in the folder
        2. Search file match ext
        3. Search file name match regex
        4. Copy file to another location
        """
list_file = []
def list_all(src):
    print("List all files in folder:")
    list= os.listdir(src)
    for i in list:
        print(i)
    return list

def extension(list, ext):
    for i in list:
        if ext in i:
            print(i)
        else:
            list_file.remove(i)
    list = list_file

def regex(list, reg):
    for i in list:
        if re.match(reg,i):
            print(i)
        else:
            list_file.remove(i)
    list = list_file

while True:
    print(menu)
    s = int(input("Please select: "))
    if (s == 1):
        src = input("Location: ")
        list_file = list_all(src)
        list = list_all(src)
    elif (s == 2):
        ext = input("extension: ")
        extension(list, ext)

    elif (s == 3):
        reg = input("regex: ")
        regex(list, reg)

    elif (s == 4):
        dst = input('Location: ')
        for i in list_file:
            shutil.copy(src + '/'+i, dst + '/' +i)
        print("Success")
    else:
        break

