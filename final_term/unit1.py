"""
given a strings consisting of words and space, return the length of the last word in the string
A word is a maximal substring consisiting of non-space characters only
"""
# input the string
s = input("s = ")
# print the length of the last word in the string
print(len(s.split()[-1]))