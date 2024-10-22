x = ['kofo', 'joy', 'peace', 'favour']

y = ['kofo', 'joy', 'peace', 'favour']
print(x is y)

a = 5
b = 5
print(a is b)
print(a == b)

a = 1000
b = 1000
print(id(a))
print(id(b))
print(id(a) == id(b))
a = 5
print(id(a))
a = 8
print(id(a))
print(a is a)

a = 10
b = '10'
print(a is b)
print(a is not b)
