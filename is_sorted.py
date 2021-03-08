


#@author: chansa
#brute force method

items = [1, 1,2,3,3,5,7,7,8,9,9]


def brute_force_search(item,itemlist):
    
    for i in range(0, len(itemlist)-1):
        if (itemlist[i]) > itemlist[i+1]:
            return False
    return True
    print(items)

print(brute_force_search(90,items))

