#@author: chansa
import sys
items = [12,3,3,5,7,7,8,9,9]

def binary_search_iterative(item, itemlist):
    
    # getting started at both ends of the array
    low = 0
    high = len(itemlist) - 1

    while low <= high:
        # calculate the middle point
        middle_level = (low + high)// 2
        

        # if item is found, return the index
        if itemlist[middle_level] == item:
            return middle_level
        
        # otherwise get the next midpoint
        elif item > itemlist[middle_level]:
            low = middle_level + 1
        else:
            high = middle_level - 1
        print(items)

    if low > high:
        return False

b = sys.getsizeof(items)
print(b)
    

#we search for 2
#rint(binary_search_iterative(2, items))

#we search for 4


#print(binary_search_iterative(4, items))
