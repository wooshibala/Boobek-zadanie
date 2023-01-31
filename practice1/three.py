lst_1 = [12, 71, -33, 0, 86]

# using while loop
lst_2 = []
i = 0
while i < len(lst_1):
    lst_2.append(lst_1[i] * 10 + 5)
    i += 1

# using for loop
lst_3 = [x * 10 + 5 for x in lst_1]

print("List 2 (using while):", lst_2)
print("List 3 (using for):", lst_3)
