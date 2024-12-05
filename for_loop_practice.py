#syntax How to Write for Loop

#v1. for <var> in <iterable_or_sequuence>:
#     #code

# Q1 Wap to print all integers between 1 to 1000

# for i in range(1,1001):
#     print(i)

#v2. FOR loops and Range Functions()
#range():- sequence of integers

# for i in range(4): # (stop-1)
#     print(i) # 0,1,2,3

# aleternative solution 
# for i in 0,1,2,3:
#     print(i)

'''
syntax
for <var> in range(stop):
    #code

Range function has 3 parameters i.e start, stop, step
'''


#v3. range() in context Purpose and Advantages
'''
The Advantage of the range tyoe over a regular list or tuple
is that a range object will always take the same small amount of memory.

'''
#Q2. Wap that shows the diffrence between range function vs list or tuple.

# import sys
# seq = [i for i in range(1,1000)]
# print(sys.getsizeof(seq))#8845

# range_seq = range(1,1000)
# print(sys.getsizeof(range_seq)) # 48

#Note:- You can generate custom sequence of integers

#v4. range with one parameter()
# range(5)
# print(list(range(0,5))) # [0,1,2,3,4]

# range(8)
# print(list(range(0,8))) # [0, 1, 2, 3, 4, 5, 6, 7]

# range(0)
# print(list(range(0,0))) # []

# print(range(-5))
# print(list(range(0,-5))) # []

#v5 Intermediate Example

#Q3. Wap to add sequnce with integers of 2

# for i in range(5):
#     print(i + 2)

# Q4. Wap to use a loop variable to modify the value of another variable
# or  WAP to sum of 0 to 10

# total_sum = 0
# for i in range(11):
#     total_sum = total_sum + i

# print(total_sum)

#Q5. Wap to concatenate to connect or join severals strings that currently
# on a list string with message

# words = ["for", "loops", "are", "powerfull" ]
# message = ""
# for i in words:
#     message = message + i
# print(message)

# solution 2

# message = ""
# for i in range(len(words)):
#     if i < len(words)-1:
#         message = message + words[i] + ""
#     else:
#         message = message + words[i]
# print(message)

#v6 Adavanced Examples
# Q6. Wap to iterate the list of values using len() function
# nums = [2,3,4,5,6]
# print(len(nums))# is 5
# for i in range(len(nums)):
#     print(nums[i])

#Q.7 Increment list value by 2
# nums = [2,3,4,5,6]
# print(len(nums))
# for i in range(len(nums)):
#     print("This is i", i)
#     print("This is nums[i]", nums[i])
#     nums[i] = nums[i] + 2
# print(nums)

#Q8. Wap to check even or odd in the list
# nums = [2,3,4,5,6]
# for i in range(len(nums)):
#     if nums[i]%2==0:
#         print("The no is even", nums[i])
#     else:
#         print("The no is Odd", nums[i])

#Q9. Wap to check the string is a pallindrom or not
# word = "hannah"
# is_pal = True

# for i in range(len(word)):
#     if word[i]!= word[len(word)-i-1]:
#         is_pal = False
# print(is_pal)

#v7. range() with two parameter
'''
syntax:- range(start, stop)
[start, start+1, start+2.....stop-1]

'''
# for num in range(2,6):
#     print(num)#2,3,4,5

# or
# for num in 2,3,4,5:
#     print(num)

#v7.1. range() with two parameter Basics
# print(range(1,15))
# print(list(range(1,15))) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# print(list(range(5,10))) # [5, 6, 7, 8, 9]
# print(list(range(10,5))) # []
# print(list(range(5,5))) # []
# print(list(range(0,4))) # [0, 1, 2, 3]

#v7.2. range() with two parameter Intermediate

#Q10.Wap to multiply  no from 1 to 10

# product = 1
# for i in range(1,11):
#     product = product * i

# print(product)

#Q11. Wap to print the part of substring 
# word = "LOOPS"

# for i in range(2, len(word)):
#     print(word[i], end="")

#Q12. Wap to find out average upper half of Data
# total = 0
# couter = 0
# data = [5,3,5,4,9,4,2,7,8]
# print(len(data))
# for i in range(len(data)//2,len(data)):
#     total += data[i]
#     couter = couter + 1
# print(total)
# print(total//couter)

#v7.3. range() with two parameter Advanced

# Q12. Wap to print all the substring of length 
#excluding first and last characters.

# word = "abcd"
#op--> bc
# for i in range(1,len(word)-1):
#     print(word[i],end="")#bc

# ex 2 length of 2

# word = "programming"
# for i in range(1,len(word)-2):
#     print(word[i:i+2])#rogr

#v7.4. range() with three parameter
'''
syantax:- range(start, stop, step)
start, start+step...<max_valid>
'''
# for j in range(2,10,2):
#     print(j) #2 4 6 8 10

# or 

# for j in 2,4,6,8,10:
#     print(j)

#v7.4. range() with three parameter  Basic
# print(list(range(5,20,6))) # [5, 11, 17]
# print(list(range(2,10,3))) # [2, 5, 8]
# print(list(range(10,2,-1))) # [10, 9, 8, 7, 6, 5, 4, 3]

#v7.5 range() with three parameter Intermediate

# Q.13 Wap to print every other character in a string capitalized

# word = "Hello Word"

# for i in range(0,len(word),2):
#     print(word[i].capitalize(), end="")

# Q14. WAP to print first sequence of odd numbers of +ve
# numbers that are smaller than 50

# odd_num = []
# n = 51
# for i in range(1,n,2):
#     odd_num.append(i)
# print(odd_num)

# Q.15 WAP to get list first 10 of multiples of 5
# mul_of_five=[] 
# n = 10
# for i in range(5,5*n+1,5):
#     mul_of_five.append(i)

# print(mul_of_five)

#v7.5 range() with Negative Parameter
'''
range(stop)
if stop<0---->[]
'''
# print(list(range(-5))) # []

'''
range(start, stop)
if start<0--> start. start+1...0, stop-1
'''
# print(list(range(-2,2))) # [-2, -1, 0, 1]

'''
Note:- if stop parameter is -ve so will get []
'''
# print(list(range(2,-5))) # []

'''
if  start<0
    stop<0    ===>[start,....stop-1]
    start<0
'''

'''
if range(start, stop, step)
if start>stop
    step<0     ===>[start,start-step...,<last_valid>]
'''
# print(list(range(7,1,-2)))

# v8. Iterating over Iterables
'''
Goal:- Run the body of the for loop once
       for every element in the iterable

      syntax: - for <var> in <iteragble>:
                    code
'''

# for num in [1,2,3,4,5]:
#     print(num)

# for num in (1,2,4,5):
#     print(num)

# for num in {1,4,5,7}:
#     print(num)

# for key in {"a":1, "b":2, "c":3}:
#     print(key)

# data = {"a":1, "b":2, "c":3}
# for value in data:
#     print(data[value])

#Q16. Wap to remove duplicate characters in the string
# word = "aaabbbccccdddddeeeefff"
# new_word = ""
# for char in word:
#     if char not in new_word:
#         new_word = new_word + char
# print(new_word)

#Q16. Wap to iterate all the keys from the dictionaries

'''
chemical_elements = {
    "H": "Hydrogen",
    "He": "Helium",
    "Li": "Lithium",
}
'''

# for key in chemical_elements.keys():
#     print(key)

#Q17. Wap to iterate all the values from the dictionaries

# for value in chemical_elements.values():
#     print(value)

#Q17. Wap to iterate all the keys and values from the dictionaries

# for key, value in chemical_elements.items():
#     print(key, value)

#v8.1 For Loop and the enumrate function()

'''
Purpose:- To automaticall keep track of counter while
          iterating over an iterable
          [counter + item]
'''
# example for normal code(count the no of elements in the list)
# x = ["a","b","c","d"]
# count = 0
# for i in x:
#     print("No of items is ", i)
#     count = count + 1
# print("No of elements in the list is ",count)


# Using enumrate function()

# print(enumerate(x))
# print(list(enumerate(x)))

#v8.2 enumrate function() and for loops

'''
syntax:- for<var1>,<var2> in enumerate(<iterable>):
                code
        <var1>--->counter
        <var2>--->items
'''
# x = ["a", "b", "c", "d"]
# print(list(enumerate(x)))

# for index, items in enumerate(x):
#     print("for index is", index, "for item is", items)

#Q18. Wap to check the list of values is even if yes then must multiply that value by 2
# x = [1,4,6,3,6,8,4,9,4,5]
# print("Given_list", x)
# for index, num in enumerate(x):
#     if num % 2 == 0:
#         x[index]=num*2
# print("new_list", x)

# without enumerate()
# for num in range(len(x)):
#     if x[num]%2==0:
#         x[num] = x[num]*2

# print("new_list", x)

#Q19. Wap to check the count of cities using enumrate function A->B->C->D

# cities = ["A","B", "C", "D"]

# for count, city in enumerate(cities):
#     if count == len(cities):
#         print("Total no of cities is", city)
#     else:
#         print(city,"->", end="")

# v.9 For loop with sorted and reversed() function
'''
Purpose:- Return a sorted copy of iterable to use it in
          the for loop.
syntax:- sorted<iterable>


'''
# example for sorted function if we dont use

# a = [6,3,1,5,9,4,6,5]
# print("Original list is", a)
# for num in a:
#     print(num, end="")

# if we use sorted function
# print(sorted(a))

'''
sorted in for loop
Syntax:-->  for <var> in sorted(<iterable>):
                   # code
    it will return newq sorted copy of iterable
    and it dosent modify the original iterable
    reverse = True --- To make it decending order
'''
# a = [5,9,2,4,2,1]

# for item in sorted(a, reverse=True):
#     print(item, end=" ")

'''
reversed() in python
Goal:- To iterate over an iterable in order without mutating it.
'''

