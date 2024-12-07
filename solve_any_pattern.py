'''
Basic syntax:--
for row in range():
    for col in range():
        print("*", end="")
'''

# Q1
'''
    j=0
i=0 * * * * *
i=1 * * * * *
i=2 * * * * *
i=3 * * * * *
i=4 * * * * *
'''
# n = 5
# for i in range(n):
#     for j in range(n):
#         print("*", end=" ")
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
#     for j in range(i,n):
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

# for i in range(n):
#     for j in range(i,n):
#         print(" ", end=" ")
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

# n = 5

# for i in range(n):
#     for j in range(i+1):
#         print(" ", end=" ")
    
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

# for i in range(n):
#     for j in range(i,n):
#         print(" ", end=" ")
#     for j in range(i):
#         print("*", end=" ")
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
n = 5
for i in range(n):

    for j in range(i+1):
        print(" ", end=" ")
    
    for j in range(i,n-1):
        print("*", end=" ")
    
    for j in range(i,n):
        print("*", end=" ")
    
    print()  # print() is used to print the new line
