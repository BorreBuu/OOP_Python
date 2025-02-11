list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
list4 = [2, 3, 4]

print(list1 is list2)
print(list1 is list3)
print(list2 is list3)
print(list1 is list4)

print()

print(list1 == list2)
print(list1 == list3)
print(list2 == list3)
print(list2 == list4)