r = [1,2,3,4,5,1,2,3,]
print(r.index(3,3))

print(r.count(3))

if 100 in r:
  print('exist')

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)

s = 'My name is Mike'
to_split = s.split(' ')
print(to_split)

i = [1,2,3,4,5]
j = i
j[0] = 100
print('j=',j)
print('i=',i)

x = [1,2,3,4,5]
y = x.copy()
#同じことができるがcopyを使った方が他の人にわかりやすい
y = x[:]
y[0] = 100
print('y=',y)
print('x=',x)

X = 20
Y = X
Y = 5
print(id(X))
print(id(Y))
print(Y)
print(X)

X = ['a','b']
Y = X
Y[0] = 'p'
print(id(X))
print(id(Y))
print(Y)
print(X)

seat =[]
min = 0
max = 5
min <= len(seat) < max

num_tuple = (10,20)

