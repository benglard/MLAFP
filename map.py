from func import Function

print map(Function("""
s = arg0 + arg1 + arg2
d = s / 3.0
print int(d)
result = d * 5
"""), range(10), range(10, 20), range(20, 30))

print map(Function("""
def test(x): # not needed, but cool
    return x * 2
result = test(arg0)
"""), range(10))

print map(Function("""
last = arg0[-1]
result = arg0 + range(last + 1, last + 6)
"""), (range(x, x+5) for x in xrange(10)))

def closure_test(x=5):
    print map(Function("""
x = kwargs['x']
result = arg0 + x
""", locals()), range(10))

closure_test()