import re
s='''We God’s creation!
Worried about imperfection. 
Why lot of confusion? 
Which ends up in a tension! 
Unable to pay attention? 
You're the one in control of the situation. 
Find a solution,
Because you have an ambition..
Be with caution.
No more lamentation.
Follow God's instruction,
Lead of life with satisfaction'''

print("The given string is ")
print(s,"\n")

print("Below is the list of words ending in 'tion' ")
print(re.findall(r'\b\w+tion', s), '\n')

print("Below is the list of words starting with 'W or a'")
l = re.findall(r"\b[Wa]\w+", s)
print(l)
print("The number of words starting with 'W and a': ", len(l), '\n')

print("The number of lines in string:", len(s.split('\n')), '\n')

l1 = re.findall(r'\b\w+tion', s)
print("Number of words ending with 'tion':", len(l1))

l3 = s.split()
print("Number of words in the given string :", len(l3))

print("Number of words not ending with 'tion':", len(l3)-len(l1))
