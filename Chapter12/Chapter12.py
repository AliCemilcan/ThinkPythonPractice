t = tuple('tuples')
print(t)
print(t[1:5])
## You can always replace the tuple with another one but syntax is important
new_tuple = ('aali',) + t[1:5]
print(new_tuple)

## divmod() methodu bolum ve kalani iki variable halinde return eder( tuple )

kalan, bolum = divmod(13,3)

print(f'kalan {kalan}, bolum {bolum}')


b = [('z',3),('d',1),('x',5)]
a= [('c',0),('d',1),('r',2)]


def has_match(a,b):
    for x,c in zip(a,b):
        if x == c:
             print(x, c)
        else:
            continue
    return False

has_match(a,b)

for index, element in enumerate('ali'):
    print(index, element)

d = {'a':0, 'b':1, 'c':2, 'd':3}

tuple_d  = d.items()
print((tuple_d))

for key, values in tuple_d:
    print(key, values)

new_dic = dict(a)
print(new_dic)
l1 = ["ali","veli"]
l2 = [101,202]
deneme = dict(zip(l1, l2))

print(deneme)


str = "alii"
countaa = str.count('i')
print(countaa)


t = ('a','l','o')
t2 = ('o','l','a')
print(sorted(t) == sorted(t2))
