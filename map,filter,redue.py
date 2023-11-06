# This is a sample Python script.
from functools import reduce


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# map
v = [10,20,30,40,50]
add = lambda num:num+50
print(list(map(add,v)))

t = ['aseet','ram','krishna','arjun']
title = lambda name:name.title()
print(list(map(title,t)))

m = [1,2,3,4,5,6,7]
multiply = lambda num:num*10
print(list(map(multiply,m)))

# filter
o = [65,28,58,77,89,95,30]
print(list(filter(lambda n:n%2==1,o)))

marks = [89,76,90,45,65]
print(list(filter(lambda n:n>70,marks)))

d = [-3,4,-7,9,-10]
print(list(filter(lambda n:n>0,d)))

# reduce
nums = [19,34,76,23,89,101,655]
print(reduce(lambda x,y:max(x,y),nums))
print(reduce(lambda x,y:x+y,nums))
print(reduce(lambda x,y:min(x,y),nums))

# map vs filter vs reduce

# map:
# The map() function iterates through all items in the given iterable and
# executes the function we passed as an argument on each of them.
# syntax: map(function, iterable(s))
# The map() function returns the map_object type.
# If you'd like the map() function to return a list instead,
# you can just cast it when calling the function:
# result = list(map(function, iterable(s)))
# It is a builtin function.

# filter:
# Similar to map(), filter() takes a function object and an iterable and creates a
# new list.
# As the name suggests, filter() forms a new list that contains only elements that
# satisfy a certain condition, i.e. the function we passed returns True.
# syntax: filter(function, iterable(s))
# If you'd like the filter() function to return a list instead,
# you can just cast it when calling the function:
# result = list(filter(function, iterable(s)))
# It is a builtin function as well.

# reduce:
# reduce() works differently than map() and filter().
# It does not return a new list based on the function and iterable we've passed.
# Instead, it returns a single value.
# syntax: reduce(function, sequence[, initial])
# Also, in Python 3 reduce() isn't a built-in function anymore,
# and it can be found in the functools module.








