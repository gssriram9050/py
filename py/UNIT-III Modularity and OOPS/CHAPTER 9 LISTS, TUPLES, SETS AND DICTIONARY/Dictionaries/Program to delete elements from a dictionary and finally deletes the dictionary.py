Dict={'Roll No':12001,'SName':'Meena','Mark1':98,'Mark2':86}
print("Dictionary elements before deletion :\n",Dict)
del Dict['Mark1']#Deleting a particular element
print("Dictionary elements after deletion of a element :\n",Dict)
Dict.clear()#Deleting all elements
print("Dictionary after deletion of all elements :\n",Dict)
del Dict
print(Dict)#Deleting entire dictionary
