lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
list2 = []
for var in lst1:
    if isinstance(var, str):
        list2.append(var)

print(list2)


####
lst2 = [var for var in lst1 if isinstance(var, str)]
print(lst2)