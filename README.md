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

Medium Example (closures)
```
from func import Function
def closure_test(x=5):
    print map(Function("""
x = kwargs['x']
result = arg0 + x
""", locals()), range(10))
closure_test()
```

Hard Example (callbacks)
```
from func import Function
import requests

def get(url, done=None, fail=None):
    rv = requests.get(url)
    if rv.status_code == 200 and done:
        done(rv)
    elif fail:
        fail(rv)

get('http://www.google.com',
    done=Function("""
print 'Success!'
from bs4 import BeautifulSoup as html_parse
html = html_parse(arg0.text)
print len(html.find_all('div'))
"""), 
    fail=Function("""
print arg0.status_code
"""))
```