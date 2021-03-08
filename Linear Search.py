#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 14:22:38 2019

@author: chansa
"""
items = [1,5,9,3,2,1,9,8,3,7]

def linear_search(item, itemlist):
    for i in range(0,len(items)):
        if item == itemlist[i]:
            itemlist[i] = 0
        #printing out happens here if item is found
       
    print (itemlist)
    return None
    

#Lets search for 7 in items
print(linear_search(7, items))




