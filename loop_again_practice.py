# Nested For Loop

# for i in range(4):
#     for j in range(2):
#         print(i,j)

# for i in range(2,5):
#     for j in range(3,5):
#         print("Loops")

# Q1
'''
    j=0
i=0 * * * * *
i=1 * * * * *
i=2 * * * * *
i=3 * * * * *
i=4 * * * * *
'''

# n=5
# for i in range(n):
#     for j in range(n):
#         print("*", end="")
#     print()

# Q2 Increasing Triangle Pattern
'''
*
* *
* * *
* * * *
* * * * *
'''

# n = 5

# for i in range(n):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()


# Q3 Decreasing Triangle Pattern
'''
* * * * *
* * * *
* * *
* *
*
'''

# n = 5

# for i in range(n):
#     for j in range(n-i):
#         print("*", end=" ")
#     print()

# Q4 Right Sided Triangle
'''
     *
    **
   ***
  ****
 *****
'''
# n = 5

# #lets first print the space
# for i in range(n):
#     for j in range(i,n):
#         print(" ", end=" ")
# # lets print the star
#     for j in range(i+1):
#         print("*", end=" ")
    
#     print()

# Q5 Right Sided  Downword Triangle
'''
 * * * * *
   * * * *
     * * *
       * *
         *
'''

# n=5
# # lets try to print space
# for i  in range(5):
#     for j in range(i+1):
#         print(" ", end=" ")
# #lets try to print star

#     for j in range(i,n):
#         print("*", end=" ")
    
#     print()

# Q6. Hill Pattern

'''
    *
   ***
  *****
 *******
*********
'''

# n = 5

# # 1 lets try to print space

# for i in range(n):
#     for j in range(i,n):
#         print(" ", end=" ")
    
# # 2 lets print left triangle star
#     for j in range(i):
#         print("*", end=" ")

# # 3 lets print right triangle star
#     for j in range(i+1):
#         print("*", end=" ")

#     print()

# Q7. Reverse Hill Pattern
'''
        * * * * * * 
         * * * * * 
          * * * * 
           * * * 
            * * 
             * 
'''

# n = 5
# # 1 increasing space

# for i in range(n):
#     for j in range(i+1):
#         print(" ", end=" ")

# # print left decreasing triangle

#     for j in range(i,n-1):
#         print("*", end=" ")

# # print Right decreasing triangle

#     for j in range(i,n):
#         print("*", end=" ")
 
#     print()


# Q6. Hill Pattern

'''
    *
   ***
  *****
 *******
*********
* * * * * * 
 * * * * * 
  * * * * 
   * * * 
     * * 
     *
'''
