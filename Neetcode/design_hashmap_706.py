"""
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
"""

#aolutin 1 using array O(1)

# class MyHashMap:

#     def __init__(self):
#         self.map = [-1]*1000

#     def put(self,key,value):
#         self.map[key] = value

#     def get(self, key):
#         return self.map[key]
    
#     def remove(self, key):
#         self.map[key]=-1

# solution 2 using linked list O(n/k)

class ListNode:
    def __init__(self,key=-1,val=-1,next=None):
        self.key = key
        self.value = val
        self.next = next

class HashMap:
    def __init__(self):
        self.map = [ListNode() for i in range(1000)]

    def hash(self, key):
        return key%len(self.map)
    
    def put(self,key,value):
        cur = self.map[self.hash(key)]

        while cur.next:
            if cur.next.key==key:
                cur.next.value = value
                return
            cur = cur.next
        cur.next = ListNode(key,value)

    def get(self, key):
        cur = self.map[self.hash(key)].next

        while cur:
            if cur.key==key:
                return cur.value
            cur=cur.next
        return -1
    
    def remove(self, key):
        cur = self.map[self.hash(key)]

        while cur.next:
            if cur.next.key==key:
                cur.next=cur.next.next
                return
            cur = cur.next
        

# Psuedo code

"""
CLASS ListNode:
    FUNCTION __init__(key = -1, value = -1, next = null):
        self.key ← key
        self.value ← value
        self.next ← next


CLASS HashMap:
    FUNCTION __init__():
        Create an array `map` of size 1000
        Each element in map is a dummy ListNode

    FUNCTION hash(key):
        RETURN key MODULO size of map


    FUNCTION put(key, value):
        index ← hash(key)
        cur ← map[index]

        WHILE cur.next IS NOT null:
            IF cur.next.key EQUALS key:
                cur.next.value ← value   // Update existing value
                RETURN
            cur ← cur.next

        cur.next ← new ListNode(key, value)  // Add new node


    FUNCTION get(key):
        index ← hash(key)
        cur ← map[index].next   // Skip dummy node

        WHILE cur IS NOT null:
            IF cur.key EQUALS key:
                RETURN cur.value
            cur ← cur.next

        RETURN -1   // Key not found


    FUNCTION remove(key):
        index ← hash(key)
        cur ← map[index]   // Start at dummy node

        WHILE cur.next IS NOT null:
            IF cur.next.key EQUALS key:
                cur.next ← cur.next.next   // Remove node
                RETURN
            cur ← cur.next

"""

