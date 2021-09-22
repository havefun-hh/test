import re
import numpy as np
import random


a = np.array(range(10))
print(a)

b = re.compile(r'^[a-z0-9]*$')
s = 'woiv23va.fae'
print(b.match(s))

