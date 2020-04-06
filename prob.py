a,b,*d={x for x in range(0,12,3)}
d.append(3)
print(type(d))

def add(a,*b):
      print(a)
      print(type(b))
      c=a
      for i in b:
            c=c+i
      print(c)

add(2,4,7,1)
