from string import punctuation, whitespace


with open('requirements.txt') as notebook:
    notes = notebook.read().split()


def reader(notes):
    new_list = []
    for word in notes.split:
        if (word in punctuation) or (word in whitespace):
            pass
        else:
            new_list.append(word.lower())
    return new_list



philosophy = "schopenhauer.txt"
julesverne = 'julesverne.txt'

with open(philosophy) as book1:
    philosophy_book = book1.read().split()


## Exercise 13.2


def clean(word):
    cleansed = ''
    for char in word:
        if ((char in punctuation) or (char in whitespace)):
            pass
        else:
            cleansed += char.lower()
    return cleansed


def open_read_book(book):
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


def histogram(data):
    hist = {}
    for word in data:
        hist[word] = hist.get(word, 0) + 1
    return hist


books = [philosophy, julesverne]


def stats():
    for book in books:
        book = open(book, 'r')
        print("Stats for  %s:" % book.name)
        data = [clean(word) for word in open_read_book(book)]
        book.close()
        print("Total: %s" % len(data))
        print(" Unique: %s" % len(histogram(data)))
        new_dic = histogram(data)
        top_20 = []
        for key in new_dic:
            top_20.append(key)
        top_20.sort(reverse=True)
        for i in range(0, 20):
            print(top_20[i])

##Modify the program and print only the words that are not in the word.txt file

with open('words.txt', 'r') as wordtext:
    word_book = wordtext.read().split() #word_book turns as a List


book__philosophy = open(philosophy, 'r')
book_list = set([clean(word) for word in open_read_book(book__philosophy)]) # This is list from a book



def only_unique_words(wordlist, booklist):
        for b in booklist:
            if b not in wordlist:
                print(b)

only_unique_words(word_book, book_list)





