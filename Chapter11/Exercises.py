#Chapter 11 Exercises
import random
import time

fin = open('words.txt')
def reading_text(f):

    dic = dict()
    for d in f:
        dic[str(d.split())] = random.randint(0,1000)

    time_start = time.time()
    if 'lollipop' in dic:
        print(dic['lollipop'])
    time_end = time.time()
    print("time diff is ", time_end - time_start)

    return dic


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


def set_default(d):
    """ THis function is doing the same with invert_dict
      but this time we will be using setdefault built-in function"""
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)

    return inverse


print(set_default({'a':1, 'b':2, 'c':1}))

cache = {}


def ack(m, n):
    """This function is an example of Chapter 6 Ackermann function. We used Dictionary to save values """
    if m == 0:
        return n+1
    if n == 0:
        return ack(m-1, 1)
    if (m, n) in cache:
        return cache[m, n]
    else:
        cache[m, n] = ack(m - 1, ack(m, n - 1))
        return cache[m, n]


def has_duplicets(list):
    """With a given list, we check that it has any duplicated item in it."""
    new_list = []
    for i in range(len(list)):
        if list[i] not in new_list:
            new_list.append(list[i])
    if new_list == list:
        return True
    else:
        return False

def has_duplicets2(list):
    "With a given list, we check if has any duplicated item in it."

    dic = {}
    for i in list:
        if i in dic:
            return True
        dic[i] = True
    return False

print(has_duplicets2([1,2,3,4,1]))

def has_duplicates3(list):
    """ In this method we will be using set function to compare two lists"""
    return (len(list)) > len(set(list))


print(has_duplicates3([1,2,3,4,1]))


def rotate_pairs(f):
    """Rotating words from the dic """
    dic = {}
    for key in f:
        dic[str(key.split())] = str(key[::-1].split())

    for d in dic:
        if dic.get(d) in dic:
            print(dic[d])


#print(rotate_pairs(fin))









