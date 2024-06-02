# String data type

# Literal assignment
first = "Jason"
last = "Jones"

print(type(first))
print(type(first) == str)
print(isinstance(first, str))

# Constructor function
# pizza = str("Pepperoni")
# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

#Concatenation function
# fullname = first + " " + last
# print(fullname)

# fullname += "!"
# print(fullname)

# Casting a number to a string
decade = str(1970)
print(type(decade))
print(decade)

statement = "I love rock music from the " + decade + "s."
print(statement)

# Multiple lines
multiline = '''
Hey, how are you?

I was just checking in.


'''
print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# String Methods

print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)
      
print(len(multiline))
multiline += "                                   "
multiline = "                          " + multiline
print(len(multiline))

# Removing the extra "whitespace" found above
print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))
      



