l = eval(input("Enter list elements: "))

unique_list = []

for item in l:
    if item not in unique_list:
        unique_list.append(item)

print("The original list", l)
print("List after removing duplicates", unique_list)
