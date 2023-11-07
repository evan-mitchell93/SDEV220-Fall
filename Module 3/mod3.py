"""
SDEV 220: Module 3
Evan Mitchell
11/6/2023

Tuples,Lists,Dictionaries,Functions,Classes
Final Projects
"""

#Tuples
my_tuple = (2,4)
#accessing values


my_string = ("hello",)


#duplication
tpl = (2,6) * 3


#unpacking
tpl = ("Hello","SDEV")
str1,str2 = tpl


#swapping
x = 3
y = 2
temp = x
x = y
y = temp

#Python way
x,y = (y,x)

#Lists
my_list = [7,4,1,3,9,0]
print(type(my_list))
my_second = ["Hello"]
print(type(my_second))

#from string
s = "Hello SDEV".split()
print(",".join(s))

#slice [start:stop:step]
print(my_list[0:4:2])

#adding to a list
s.append(220)
s.insert(1,"Class")


#remove from a list
del s[1]
s.remove(220)

#sorting
print(my_list)
my_list.sort(reverse=True)
print(my_list)


my_dogs = ['Golden','Lab','German','Husky']
my_sizes = ['L','L','L']
my_ages = [3,1,5,7]

z = zip(my_dogs,my_sizes,my_ages)
print(list(z))
for dog, size, age in zip(my_dogs,my_sizes,my_ages):
    print(dog,size,age)


#Dictionaries
my_dict = {
    "first name":"Evan",
    "age": 30
}

my_dict2 = dict(name="patrick",age=26)


#adding and removing
my_dict["state"] = "IN"
my_dict["state"] = "MI"


#Sets
my_set = set((1,2,3,1))


my_second_set = {"H","E","X"}

my_set.add(5)

my_set.remove(1)


for x in my_set:
    print(x)

def my_function():
    return("Hello")

str1 = my_function()


def my_add(x,y):
    return(x + y)

def my_range(high = 10,low = 1):
    print("RANGE FUNCTION")
    for i in range(low,high):
        print(i)

def sum_of_some(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print("Sums: ",sum_of_some(1,2,3,4,5,6,7,8,9,0,15))

#Keyword arguments
def key_args(**kwargs):
    for key,value in kwargs.items():
        print(key,value)

key_args(name="Evan",school="Ivy Tech",role="Instructor")


def say_hello():
    print("Hello")
    return

def run_another(func):
    func()

run_another(say_hello)

def multi(n):
    return lambda x : x * n

three = multi(3)
print(three(8))

#Lambda functions
x = lambda a : a + 10
print(x(5))

y = lambda a :[print(i) for i in a]

y([1,2,3,4,5])


class disc:
    def __init__(self,name,speed):
        self.disc_name = name
        self.disc_speed = speed
    def say_speed(self):
        print(self.disc_speed)

d1 = disc("Luna",3)
print(d1.say_speed())