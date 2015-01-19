from func import Function

f = Function("""
print 1, 5
""")
f()

f = Function("""
class Test:
    pass

t = Test()
t.x = 5

print 2, t.x
""")
f()

class Test:
    pass

(Function("""
t = arg0
t.x = 5
print 3, t.x
"""))(Test())

(Function("""
t = arg0() # construct class in Function
t.x = 5
print 4, t.x
"""))(Test)

def closure_test():
    x = 5
    (Function("""
print 5, kwargs['lcl']['x']
"""))(lcl=locals())

closure_test()

def closure_test_2():
    x = 5
    (Function("""
print 6, kwargs['x']
""", locals()))()

closure_test_2()