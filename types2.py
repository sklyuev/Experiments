print type(None)        # <type 'NoneType'>
print type(type(None))  # <type 'type'>
print type(True)        # <type 'bool'>
print type('qwer')      # <type 'str'>
print type([])          # <type 'list'>
print type(())          # <type 'tuple'>
print type({})          # <type 'dict'>
print type({1, 2, 3})   # <type 'set'>

def foo():
    pass

print type(foo)             # <type 'function'>
print type(lambda x: x*x)   # <type 'function'>

class Boo(object):
    pass

print type(Boo())           # <class '__main__.Boo'>
print type((x*x for x in range(5))) # <type 'generator'>

def too():
    for x in range(5):
        yield x

print type(too) # <type 'function'>

fd = open("oop.py")
print type(fd)  # <type 'file'>
