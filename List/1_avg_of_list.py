l = [10,20,30,40]
avg = 0
sum = 0

no_of_items = len(l)
print(no_of_items)

for i in l:
    sum = sum + i
print("Total_value", sum)
avg = sum/no_of_items
print("Average_of_the_list_is: ", avg)
