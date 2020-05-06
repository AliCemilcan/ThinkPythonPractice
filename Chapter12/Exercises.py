# 12-1

def most_frequent2(str):
    """ Takes a string and prints the letter with decreasing order of frequency"""
    t1 = {}
    for a in str:
        t1[a] = t1.get(a, 0) + 1

    for key, element in reversed(t1.items()):
        print(key, element)
    # d = zip(reversed(t1),range(len(t1)))
    # print(d)
    # for key, element in d:
    #     print(element, key)


def most_frequent(s):
    """Sorts the letters in s in reverse order of frequency.

    s: string

    Returns: list of letters
    """
    hist = make_histogram(s)

    t = []
    for x, freq in hist.items():
        t.append((freq, x))

    t.sort(reverse=True)

    res = []
    for freq, x in t:
        res.append(x)

    return res


def make_histogram(s):
    """Make a map from letters to number of times they appear in s.

    s: string

    Returns: map from letter to frequency
    """
    hist = {}
    for x in s:
        hist[x] = hist.get(x, 0) + 1
    return hist


def read_file(filename):
    """Returns the contents of a file as a string."""
    return open(filename).read()


#
# if __name__ == '__main__':
#     s = read_file('words.txt')
#     t = most_frequent2(s)
#     for x in t:
#         print(x)
# write a program that reads a word list from words.txt and prints all the anagrams

# Exercise 12


def word2tuple(word):
    """ Get a string and convert it to a tuple and sort it"""
    new_word = tuple(sorted(word))
    return new_word


def anagrams(word_list):
    """ Get a list of words and assign their tuple`s to dictionary key"""
    dic = dict()
    for words in word_list:
        words = words.strip()
        new_word = word2tuple(words)
        # If not in dictionary, create new open
        dic[new_word] = dic.get(new_word, [])
        # Or append
        dic[new_word].append(words)
    return dic

def print_anagrams(dic):
    """ Gets a dictionary and print the List of tuple key assignments"""
    list2sort = []
    for key in sorted(dic):
        words = dic.get(key)
        if len(words) > 1:
            list2sort.append(words)

    for s in sorted(list2sort, key=len, reverse=True):
        print(s)

    for letter_set in dic:
        # ...
        if len(words) > 1 and len(letter_set) == 8:
            print(words)
    # ...


s = read_file('words.txt')
fin = open("words.txt")

#print(print_anagrams(anagrams(fin)))




