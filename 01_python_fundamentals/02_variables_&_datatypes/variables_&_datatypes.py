''' 
Variables is like a container that holds data.
'''
age = 25
name = "Alice"
price = 99.99

print(age)
print(name)
print(price)

a = 1
e = 3.2
b = True
c = "Harry"
d = complex(8, 2)

print(type(a))
print(type(e))
print(type(b))
print(type(c))
print(type(d))


'''
Datatypes specifies the type of value a variable holds. 
This is required in programming to do various operations without causing an error.

WE CAN CHECK THE TYPE OF VARIABLE USING TYPE() FUNCTION
ex:type(students) output: <class 'int'>
'''

# Integer DataType
students = 50
print(students)

# Float DataType
temprature = 98.6
print(temprature)

# String DataType
greeting = "Good Morning"
print(greeting)

# Boolean Datatype
is_raining = True
print(is_raining)

# List 
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]  
print(type(list1))
print(list1)

# Tuples
# Tuples are same as list but they are immutable
tuple1 = (("parrot", "sparrow"),("Lion", "Tiger"))
print(type(tuple1))
print(tuple1)

# Dict
dict1 = {"name" : "Sakshi", "age" : 26, "canVote" : True}
print(type(dict1))
print(dict1)


