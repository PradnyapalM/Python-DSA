#Check the two string/arr has anagram or not 
# ex jar==raj

# def has_anagram(s,t):
#     s = sorted(s)
#     t = sorted(t)
#     if s==t:
#         return True
#     return False
 
# s= "jar"
# t="raj"

# print(has_anagram(s,t))

def has_anagram(s,t):
   count = {}

   for x in s:
      count[x] = count.get(x,0)+1

   for x in t:
      if x not in count or count[x]==0:
         return False
      count[x]=count[x]-1
   return True
      
   
s= "bar"
t="raj"

print(has_anagram(s,t))


