'''
Nested for loop 
use cases:--> When for each iteration of the loop we need to
              repeat some action a given number of items

syntax:---> for <var1> in <iter1>:
                #optional code
                for <var2> in <iter2>:
                    #code
                #optional code
'''
#Example

# for i in range(4):
#     for j in range(2):
#         print(i,j)

# print(list(range(1)))
# print(range(5))

# Example 2

# for i in range(2,5):
#     for j in range(3,5):
#         print("Loops")


# Example 3
products = {
    "product1":{
        "brand":"A",
        "price":100
    },
    "product2":{
        "brand":"B",
        "price":200
    },
    "product3":{
        "brand":"C",
        "price":200
    }
}

for product,data in products.items():
    # print("product-name", product)
    for category,value in data.items():
        print(category.capitalize(), ":", value)
    print()

    # for 
