"""
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. 
If key does not exist in the HashSet, do nothing.
"""

class MyHashSet:
    def __init__(self):
        self.size = 1000
        self.table = [None]*self.size

    def hash_value(self,key):
        return key%self.size
    
    def add(self, key):
        hv = self.hash_value(key)
        if self.table[hv] == None:
            self.table[key] = [key]
        else:
            self.table[hv].append(key)

    def remove(self, key):
        hv = self.hash_value(key)
        if self.table[hv]!=None:
            while key in self.table[hv]:
                self.table[hv].remove[hv]
    
    def contains(self, key):
        hv = self.hash_value(key)
        if self.table[hv]!=None:
            return key in self.table[hv]
        return False
    

# Psuedo code

"""
CLASS MyHashSet:

    FUNCTION __init__():
        size ← 1000
        table ← array of size `size`, filled with null


    FUNCTION hash_value(key):
        RETURN key MODULO size


    FUNCTION add(key):
        hv ← hash_value(key)
        
        IF table[hv] IS null:
            table[hv] ← new list containing [key]
        ELSE IF key NOT IN table[hv]:
            append key to table[hv]


    FUNCTION remove(key):
        hv ← hash_value(key)
        
        IF table[hv] IS NOT null:
            WHILE key EXISTS in table[hv]:
                remove key from table[hv]


    FUNCTION contains(key):
        hv ← hash_value(key)
        
        IF table[hv] IS NOT null:
            RETURN (key IN table[hv])
        
        RETURN false

"""