# Chapter 11 Dictionaries

Dictionary is like a list, however in the List indices must be an *integers*,
in Dictionaries it can be (almost) *any type*.

Dictionaries contains collection of indices which are called **keys**, and a collection
of values.

### dict keyword creates an empty dictionary

` eng2sp = dict()`
`>>> eng2sp
{}`

The {} "*squiggly*" brackets represent an empty dictionary. In order to add an item you use square brackets.

`eng2sp['one'] = 'uno' `

If we see inside, 'one' keyword mapped with 'uno'

`>>> eng2sp
{'one': 'uno'}`

### This output format is also input format, you can create a dictionary with 3 items

`eng2sp = {'one':'uno', 'three':'tres', 'two':'dos'}`

The **len** function returns the number of key - value pairs

`>>> len(eng2sp)
3
`

The **in** operator returns bool. Key is in the Dictionary or not.

`>>> 'one' in eng2sp
True
`

If you want to see the **values**

`>>> values = eng2sp.values()
`
`>>> values
dict_values(['uno', 'tres', 'dos'])
`

### For dictionaries python uses **hashtable** to search key values.

An implementation is a way of programing a computation; some implementations are better than others.  
If you wanna count a how many times each letter count in a given string you can do it with dictionary like;

`def histogram(s):
    dic = dict()
    for c in s:
        if c not in dic:
            dic[c] = 1
        else:
            dic[c] += 1
    return dic`

The for loop traverses the string.
 Each time through the loop, if c is not in the dictionary we create a new item with key c and the initial value 1

### Dictionaries have a get function which takes a key and default value. If key is not in the keys, it returns the default value.

## Reverse Lookup is a searching key with a given value. It can cause some problems since same value can assign more than 1 key

`def reverse_lookup(d,v):
    """ Here we are searching value in a dictionary and if can not find
    send a built-in Lookup error"""
    for k in d:
        if d[k] == v:
            return k
    raise LookupError("Values does not appear in the dictionary)`

## Dictionaries and Lists

Lists can appear as values in a dictionary. For example if we are given a dictionary that maps the letters with their
frequencies. Since there might be different letters with same frequency, you can make a list of those letters

`def invert_dict(d):
    """Gets a dictionary and for each key of the given dictionary assign it to a value.
    if value not in the new dictionary creates a key with that value and assign key as a value
    otherwise append key to the existing map"""
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse`

### As we mentioned earlier Lists can be **values** in the Dictionaries but **cannot be the keys**. It is because keys needs to be hashable.
One of the reason is Lists are *mutable*. If we change the key value, you might have two different entries for the same key.

Here I am replacing old Fibonacci numbers code with new one. Dictionary used and save numbers so it is more effective

`def fibonacci_old(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)`

`
known = {0:0, 1:1}`


`def fibonacci(n):
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res`

## Global Variables
 Defined inside if the _main_ frame which is basically not inside of any function.

`verbose = True`

`def example1():
    if verbose:
        print("Hello")`

Here verbose is a global variable and can be reachable from inside of any function.

If you are changing the value of global variables you need to define it with "global" keyword otherwise it wont be recognized by the compiler/interpreter

`count = 0`

`def example1():
    global count
    count = count + 1`

### However, if the global variable is **mutable, you don't need to use the global keyword as long as you don't re-assign it`s value**

```
known= {0:0, 1:1}

## known is a mutable you don`t need to re-assign it.
def example3():
    known[2] = 2

```

## Exercises

### Exercise 11.1

```
def reader(f):
    """"Write a funtion reads words from words.txt and save it to a dictionary"""
    dic = dict()
    for word in f:
        dic[str(word.split())] = random.randint(1,100000)
    
    time_start = time.time()
    if 'lollipop' in dic:
        print(dic['lollipop'])
    time_end = time.time()
    print("time difference is", time_end - time_start)
    
```
### Exercise 11.2
```
def new_invert_dic(d):
    """We will be using setdefault() to invert dic keys and frequencies"""
    invert_dic = dict()
    for key in d:
        val = p[key]
        invert_dic.setdefault(val, []).append(key)
    return invert_dic
```

### Exercise 11.4
```
def has_duplicets2(list):
    "With a given list, we check if has any duplicated item in it."
    dic = {}
    for i in list:
        if i in dic:
            return True
        dic[i] = True
    return False
```
* or we can use set()*
* 
```
def has_duplicates3(list):
    """ In this method we will be using set function to compare two lists"""
    return (len(list)) > len(set(list))
```

### Exercise 11.4
```
def rotate_pairs(f):
    """Rotating words from the dic and check are there any pairs after rotating the words """
    dic = {}
    for key in f:
        dic[str(key.split())] = str(key[::-1].split())
    for d in dic:
        if dic.get(d) in dic:
            print(dic[d])
```

