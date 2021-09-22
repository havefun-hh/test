
GEN = 2000
LEN = 500

def add(a, b):
    res = a + b
    return res

def plus(a, b):
    res = a * b
    return res

if __name__ == '__main__':
    print(GEN)
    a = 1
    b = 2
    res1 = add(a, b)
    res2 = plus(a, b)
