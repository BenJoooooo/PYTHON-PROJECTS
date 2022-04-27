print("Enter student's name (LN,FN, MI): ")
name = input()

print("Enter student's grade in: ")
math = input("Math: ")
science = input("Science: ")
english = input("English: ")

math = float(math)
science = float(science)
english = float(english)

total = [math, science, english]
average =  (sum(total) / len(total))
print("Average grade of " + name + " is ", average)