shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)

# Use of continue and break
for item in shopping_list:
    if item == "spam":
        continue

    print("Buy " + item)

print()
for item in shopping_list:
    if item == "spam":
        break

    print("Buy " + item)

print()

# to know the postion of the item
item_to_find = "spam"
found_at = None     #change in oder to execute line 36

# for index in range(6):
for index in range(len(shopping_list)):
    if shopping_list[index] ==item_to_find:
        found_at = index
        break

if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))

print()
#same answer but another approach

item_to_find = "spam"
found_at = None     #change in oder to execute line 36

# for index in range(6):
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))