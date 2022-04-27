fruits = ["apple", "banana", "cherry", "kiwi",
"mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
newlist = [y for y in fruits] #no condition
print(newlist)
newlist = [z for z in fruits if 'x' != "mango"]
print(newlist)
#except mango
