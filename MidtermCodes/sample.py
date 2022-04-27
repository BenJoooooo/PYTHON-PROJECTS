print("Hello World")

name = "Ben"
food = "Rice"
game = "Chess"

sampleText1 = "My name is {} I love {} and playing {}"
sampleText1a = sampleText1.format(name, food, game)
print(sampleText1a)

sampleText2 = "My name is {0} I love {1} and playing {2}"
sampleText2a = sampleText2.format(name, food, game)
print(sampleText2a)

sampletext3 = "My nanme is {newName} I love  {newFood} and playing {newGame}"
sampletext3a = sampletext3.format(newName="Ben", newFood="Pizza", newGame="Basketballl")
print(sampletext3a)

item = "Milk"
cost = 35.50

# Placeholder %
sampletext4 = "The product %s costs %.2f" % (item, cost)
print(sampletext4)

quantity = 5
price = cost * quantity

# Placeholder f String and {}
sampletext5 = f"The product {item} costs {cost * quantity} pesos."
print(sampletext5)
print("The product " + item + "costs " + str(price) + " pesos.")

# Slicing
s = "Hello World!"
print(s[7:12])
print(s[-5:-2])

# Strip - removes any white spaces at the beginnning and end
s = "            Hello, World! "
print(s.strip())

# Length of the String
print(len(s))

# Formatting Functions
print(s.upper())
print(s.lower())

c = "welcome to Python Programming!"
print(c.capitalize())
print(c.title())

# Split
s1 = "Hello, my name is John, I am doing Python"
x = s1.split(" ")
print(x)

# Replace
x = s1.replace("John", "Alec")
print(x)

# Check String
print("Python" in s1)