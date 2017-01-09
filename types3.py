print(type(None))        # <class 'NoneType'>
print(type(type(None)))  # <class 'type'>
print(type(True))        # <class 'bool'>
print(type('qwer'))      # <class 'str'>
print(type([]))          # <class 'list'>
print(type(()))          # <class 'tuple'>
print(type({}))          # <class 'dict'>
print(type({1, 2, 3}))   # <class 'set'>

def foo():
    pass

print(type(foo))             # <class 'function'>
print(type(lambda x: x*x))   # <class 'function'>

class Boo(object):
    pass

print(type(Boo()))           # <class '__main__.Boo'>
print(type((x*x for x in range(5)))) # <class 'generator'>

def too():
    for x in range(5):
        yield x

print(type(too)) # <class 'function'>

fd = open("oop.py")
print(type(fd))  # <class '_io.TextIOWrapper'>
