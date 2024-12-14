# Q1 find avegare
# l = [10,20,30,40]
# avg = 0
# sum = 0

# no_of_items = len(l)
# print(no_of_items)

# for i in l:
#     sum = sum + i
# print("Total_value", sum)
# avg = sum/no_of_items
# print("Average_of_the_list_is: ", avg)

# Q2 Find list of even and odd in the list
# even = []
# odd = []

# def eve_odd(l):
#     for x in l:
#         if x % 2 == 0:
#             even.append(x)
#         else:
#             odd.append(x)
#     return even,odd # It returns multiple of tuple values

# # print(eve_odd(l))

# l = [10,41,30,25,80]
# even, odd = eve_odd(l) # Handling tuple values
# print("Even: ", even)
# print("Odd: ", odd)

# Q3 Get smaller element from the list
l = [8,100,20,40,3,7]
x = 10
def get_smaller(l,x):
    samller = []
    for i in l:
        if i<x:
            samller.append(i)
    return samller
print(get_smaller(l,x)) # Output: [8, 20, 3,]
