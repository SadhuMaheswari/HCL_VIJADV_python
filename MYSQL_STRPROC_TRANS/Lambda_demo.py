def add(x,y):
    return x+y

add=lambda x,y:x+y
print(add(10,10))

m=lambda a,b:a if(a>b) else b

even_odd=lambda num:"num is even" if(num%2==0) else "num is odd"
print(even_odd(5))

def demo(x):
    return lambda a:a*x

d=demo(5)
print(d(11))

rev_string=lambda m:m[::-1]
print(rev_string('mahi'))

def rev_str(s):
    return s[::-1]
print(rev_str('mahi'))

l=[5,60,45,55,90,190,35]
def demo_fun(n):
    if n>=50:
        return True
    else:
        return False
print(demo_fun(60))

def decor(func):
    def inner(name):
        if name=="hcl":
            print("hello hcl")
        else:
            func(name)
        return inner
def wish(name):
    print("hello",name)