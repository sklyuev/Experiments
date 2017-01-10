""" Experiments with traing comma """

a = [1, 2, 3]
print len(a)

a2 = [1, 2, 3, ]
print len(a2)

t = ()
print type(t), len(t)   # <type 'tuple'> 0

t2 = (1,)
print type(t2), len(t2)  # <type 'tuple'> 1

t3 = (1)
print type(t3)  # <type 'int'>

d = {1: '1', }
print len(d)    # 1
