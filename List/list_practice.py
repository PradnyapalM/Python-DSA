# Q1. find even and odd of the list
'''
def eve_odd(l):
    even = []
    odd = []
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd
l = [1,2,3,4,5,6,7,8,9]
even,odd = eve_odd(l)
print("Even no: ", even)
print("Odd_No", odd)
'''

# Q2 Get the smallest elements of the list or compare
'''
def getSmall(l,x):
    res = []
    for i in l:
        if i<x:
            res.append(i)
    return res

l = [1,4,6,2,77,55,33]
x=10
print(getSmall(l,x))
'''

# Slicing

# l = [10,20,30,40,50]
# print(l[0:5:2])
# print(l[:4]) #end-1
# print(l[2:])
# print(l[::-1])
# print(l[-1:-6:-1])

# list comprehensionn
# l = [x for x in range(1,11) if x%2==0]
# print(l)