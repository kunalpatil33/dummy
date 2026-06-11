x = set()
print(type(x))
x.add(30)
print(x)
x={10,20,30,40,10}
print(x)
x=list(x)
print("xl"[0])

"xl"[2]=90
print("xl")
x=set("xl")
print(x.type(x))

a={1,2,3}
b={3,4,5,}
print(a.union(b))
print(a|b)

print(a.intersection(b))
print(a&b)

print(a.difference(b))
print(b-a)

print(a.symmetric_difference(b))
print(a^b)