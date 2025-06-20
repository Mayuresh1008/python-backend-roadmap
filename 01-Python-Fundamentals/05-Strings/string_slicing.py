names = "Harry,Shubham"
print(names[0:5]) # prints characters from index 0 to 4 

fruit = "Mongo"
len1 = len(fruit)
print(len1)

# Slicing
print(fruit[0:4]) # prints the string from 0 to 3 index
print(fruit[1:4]) # prints the string from 1 to 3 index
print(fruit[:3])  # prints the string from 0 to 2 index even if we don't write starting index in the slice
print(fruit[:]) # if we don't mention both the starting and ending index then it prints the whole string

# Negative slicing
""" 
Python negotiate with negative slicing like this:
pirnt(fruit[0:len(fruit)-2])
Means the negative value we provide while slicing it gets subtracted from the actual len of the string and we get the output.
And we can also find the ending character buy just counting string index from the end point which is -1
it works like this _,_,_,_,_,-3,-2,-1
"""
print(fruit[0:-3])
print(fruit[0:len(fruit)-2])
print(fruit[-3:-1])
