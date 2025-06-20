names = "Harry,Shubham"
print(names[0:5]) # prints characters from index 0 to 4 

fruit = "Mongo"
len1 = len(fruit)
print(len1)

# Slicing
print(fruit[0:4]) # prints the string from 0 to 3 index
# it includes 0 but not 4
print(fruit[1:4]) # prints the string from 1 to 3 index
# it includes 1 but not 4
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

# Example
pie = "ApplePie"
print(pie[:5])
print(pie[5:])
print(pie[2:6])
print(pie[-8:])

# Few more examples
word = "Python"
print(word[1])
print(word[-1])

text = "Hello, World!"
print(text[0:5])
print(text[7:])

# adding third slicing will skip the number of letter
print(text[::3]) # prints every third character skiping inbetween characters 
# String starts with "H" further skips 2 character and prints the third one which is "l" same process will be followed further
print(text[::1]) # print the whole string no change
# H, e, l, l, o, ",", , W, o, r, l, d, !
# above print will just print: Hl r!
# the third slicing can also be used for reversing the string buy entering the negative index value and the skiping charcters process can also be followed in the reverse method also
print(text[::-1]) # prints the whole string reverse
print(text[::-3]) # prints every third chracter of by skiping two in reverse order