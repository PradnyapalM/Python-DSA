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
# l = [8,100,20,40,3,7]
# x = 10
# def get_smaller(l,x):
#     samller = []
#     for i in l:
#         if i<x:
#             samller.append(i)
#     return samller
# print(get_smaller(l,x)) # Output: [8, 20, 3,]

# Q4 Find the even odd of the in the list  Using list Comprehension

# def even_odd(l):
#     even = [e for e in l if e%2==0]
#     odd = [o for o in l if o%2!=0]
#     return even, odd
# l = [10,41,30,25,80]
# even, odd = even_odd(l)
# print("Even: ", even)
# print("Odd: ", odd) # Output: [10, 30, 80] 

# Q5. Find mazimum element of the list
# l = [40]

# def max_no(l):
#     x=0
#     for i in l:
#         if i>x: 
#             x=i
#     return x

# print("Max_no", max_no(l))

# Simple solution

# def getMax(l):
#     for x in l:
#         for y in l:
#             if y > x:
#                 break
#         else:
#             return x
#     return None
# l = [10,20,5,50]
# print(getMax(l))

#Efficient Solution

# def getMax(l):
#     if not l:
#         return None
#     else:
#         res = l[0]
#         for i in range(1,len(l)):
#             if l[i] > res:
#                 res = l[i]
#         return res
                
# l = [10,20,5,50]
# print(getMax(l))

#Q6. Check the list is sorted or not
# 
# my method
# def ifSort(l):
#     if sorted(l)==l:
#         return True
#     else:
#         return False
    
# l = [10,50,30,40]
# print(ifSort(l))  # True

#Traversal using Loop Best solution Big O(n)
# def ifSort(l):
#     for i in range(len(l)-1):
#         if l[i] > l[i+1]:
#             return False
#     return True
        
# l = [20,20,21,30,40]
# print(ifSort(l))  # True

# Q7 Find the only Odd imp

def onlyOdd(l):
    res = None
    for x in l:
        count = l.count(x)
        if count%2!=0:
            res = x
            break
    return res
l = [10,10,20,30,30]        
print(onlyOdd(l))