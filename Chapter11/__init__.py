def histogram(s):
    dic = dict()
    for c in s:
        if c not in dic:
            dic[c] = 1
        else:
            dic[c] += 1
    return dic


h = histogram('alia')
print(h)
print(h.get('d', 10))

def histogram2(s):
    """ In this histogram function we will use .get() to check item in the list or not"""
    dic = dict()
    for c in s:
        if dic.get(c, 0) == 0:
            dic[c] = 1
        else:
            dic[c] += 1
    return dic


c = histogram2('alia')

print(c)

#Looping the Dictionary


def print_hist(h):
    for d in sorted(h):
        print(d, h[d])

print_hist(c)

def reverse_lookup(d,v):
    """ Here we are searching value in a dictionary and if can not find
    send a built-in Lookup error"""
    for k in d:
        if d[k] == v:
            return k
    raise LookupError("Values are not appear in the dictionary")

print(reverse_lookup(h, 2))

def invert_dict(d):
    """Gets a dictionary and for each key of the given dictionary assign it to a value
    if value not in the new dictionary creates a key with that value and assign key as a value
    otherwise append key to already created map"""
    inverse = dict()
    for key in sorted(d):
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

print(invert_dict(h))


#Fibonacci example from chapter 6

def fibonacci_old(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


known = {0:0, 1:1}


def fibonacci(n):
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res


print(fibonacci(4))

print(known)

count = 3

def example1():
    global count
    count = count + 1
    print(count)


example1()
