"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store
"""

def MaxAmountOfWater(height):
    """
    Return the maximum amount of water a container can store
    """
    # the maximun amonut of water
    max_water = 0
    # index of length in left
    left = 0
    # index of length in right
    right = len(height) - 1
    # while left not height at the end
    while left < len(height)-1:
        if left <= right:
            # the amount of the water is the area of ​​a rectangle 
            # that have length is the smallest length between left and right
            # and width is the distance between left and right
            area = min(height[left], height[right]) * (right - left)
            # find max amount of water
            max_water = max(max_water, area)
            # index of length in the right sub
            right -=1
        else:
            left +=1
            right = len(height) - 1
                
    return max_water
# input string in format [num1,num2,...]
string_list = input("height = ")
# convert the string to list of integer
height = list(map(int,string_list[1:-1].split(",")))
# return the maxumun of water
print(MaxAmountOfWater(height))
