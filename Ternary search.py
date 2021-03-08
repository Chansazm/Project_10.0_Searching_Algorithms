
"""
Created on Wed Sep 11 23:24:35 2019

@author: chansa
"""
items = [1, 1,2,3,3,5,7,7,8,9,9]

def ternary(item_list, left, right, y): 
    if (right >= left): 
        first_middle = left + (right - left)//3
        second_middle = first_middle + (right - left)//3
   
        # y present at the first middle 
        if item_list[first_middle] == y: 
            return first_middle 
   
        # y is present at the second middle 
        if item_list[second_middle] == y: 
            return second_middle 
   
         #continue looking for y recursively
        if item_list[first_middle] > y: 
            return ternary(item_list, left, first_middle-1, y) 
   
         
        if item_list[second_middle] < y: 
            return ternary(item_list, second_middle+1, right, y) 
   
        
        return ternary(item_list, first_middle+1, second_middle-1, y) 
    print(items)
     
    # We reach here when element is not present in the item_list
    return print("Not in the list")

#we search for 2 from 0 to 10 in items
print(ternary(items, 0,10,2))

#we search for 3 from 0 to 10 in items
print(ternary(items, 0,10,4))


