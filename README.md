# MLAFP

Multiline anonymous functions in Python!

Easy Example
```
from func import Function
f = Function("""
print 1, 5
""")
f()
```

Medium Example
```
from func import Function
print map(Function("""
s = arg0 + arg1 + arg2
d = s / 3.0
print int(d)
result = d * 5
"""), range(10), range(10, 20), range(20, 30))
```

Hard Example (closures)
```
def closure_test(x=5):
    print map(Function("""
x = kwargs['x']
result = arg0 + x
""", locals()), range(10))
closure_test()
```