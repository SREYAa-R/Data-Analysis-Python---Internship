#creating a list
list_01 = [1,2,3,4,5]
print("Original List :", list_01)

#Adding an element to the list
list_01.append(6)

#Removing an elemnt from the list
list_01.remove(3)

#Modifying an element in the list
list_01[1] = 10
print("Updated List :", list_01)

#creating Dictionary
dict_01 = {'Name': 'Sreya', 'Age': 22, 'City': 'Bangalore'}
print("Original Dictionary :", dict_01)

#Adding
dict_01['Gender'] = 'Female'

#Removing
del dict_01['Age']

#Updating
dict_01['City'] = 'Palakkad'
print("Updated Dictionary :", dict_01)

#creating set
set_01 = {1,2,3,4,5}
print("Original set :", set_01)

#Adding
set_01.add(7)

#Removing
set_01.remove(1)

#Modyfying
set_01.discard(1)
set_01.add(8)

print("Updated Set :", set_01)
