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