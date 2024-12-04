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
