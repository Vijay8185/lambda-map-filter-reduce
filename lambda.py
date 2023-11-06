# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# lambda function
s = lambda num:num*num
print(s(7))

con = lambda nme:nme.upper()
print(con('vijay'))

do = lambda x,y,z:x+y+z
print(do(10,20,30))

do = lambda x,y,z:(x+y,y+z)
print(do(10,20,30))

# lambda with positional argument:
add = lambda n:n+100
print(add(10))

# lambda with keyword argument:
my_fun = lambda child1,child2,child3:(child1,child2,child3)
print(my_fun('Amit','Sumit','Vineet'))

# lambda with default argument:
add_numbers = lambda a,b:a-b
print(add_numbers(2,3)

# if else with lambda
grade = lambda A,B: A if num A>70 else B
print(grade(80))

#

value = lambda p,n:p if num '+ve' else n
print(value(-70))

#

min = lambda a, b, c : f"{a} is smaller" if(a < b & b < c) \
     else f"{b} is smaller"  if (b < c) else f"{c} is smaller"
print(min(40, 30, 10))
























      )






























