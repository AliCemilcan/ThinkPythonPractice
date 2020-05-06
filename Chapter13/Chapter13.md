# Chapter 13

This Chapter we will be doing exercises in order to understand and practice on the
what  we have learned so far.

## Exercise 13.1
Write a program that reads a file , breaks each line into words, strips and whitespaces and
punctuations from the words, finally convert to lowercase.

```
#Create a txt file and write some stuff. You can call it requirements.txt if you want.
with open('requirements.txt') as notebook:
    notes = notebook.read().split()


def reader(notes):
    new_list = []
    for word in notes:
        if (word in punctuation) or (word in whitespace):
            pass
        else:
            new_list.append(word.lower())
    return new_list
```

## Exerceise 13.2
 Go to project Gutenberg (https://Gutenberg.org) and download you favorite book in the plain text format.
 Read the book , Skip over the header.
 Then count total number of words in the book and how many times it used.
 Print number of different words used in the book.

```
philosophy = "schopenhauer.txt"
julesverne = 'julesverne.txt'

def open_read_book(book):
""" Get the book and start reading from the signal and add everything into a List"""
    liste = []
    flag = False
    signal = '*** START OF'
    for line in book:
        if flag == True:  ## Check the Flag for the beginning of the book
            for word in line.split():
                liste.append(word)
        elif (signal in line) and (flag == False):
            flag = True
        else:
            pass
    return liste
    
    
def clean(word):
""" Get a word and each word clean it with string.punctuation or string.whitespace methods """
    cleansed = ''
    for char in word:
        if ((char in punctuation) or (char in whitespace)):
            pass
        else:
            cleansed += char.lower()
    return cleansed


def histogram(data):
""" return the frequency of occurences of each word in the book"""
    hist = {}
    for word in data:
        hist[word] = hist.get(word, 0) + 1
    return hist


books = [philosophy, julesverne]

def stats():
    for book in books:
        book = open(book, 'r')# Opens the book with a read command
        print("Stats for  %s:" % book.name)
        data = [clean(word) for word in open_read_book(book)]#Get a list from open_read_book method and foreach the each word with a clean() method
        book.close()
        print("Total: %s" % len(data))
        print(" Unique: %s" % len(histogram(data)))
        print(histogram(data))
```