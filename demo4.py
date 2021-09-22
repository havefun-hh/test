import re


a = re.compile(r'^[a-z0-9]*$')
s = 'woiv23va.fae'
print(a.match(s))
