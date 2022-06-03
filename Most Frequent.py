# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 16:55:37 2022

@author: Sandra
"""

word = str(input("PLEASE ENTER A STRING: "))
def most_frequent(word):
    result = {}
    for i in word:
        keys = result.keys()
        if i not in keys:
            result[i]=1
        else:
            result[i]+= 1
    return result

output = most_frequent(word)

sorted_values = sorted(output.values()) # Sort the values
sorted_dict = {}

for i in sorted_values:
    for k in output.keys():
        if output[k] == i:
            sorted_dict[k] = output[k]
            break

print(sorted_dict)



   








































