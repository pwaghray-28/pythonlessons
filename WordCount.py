def wordcount():
    filename = input("Enter the file name")
    wordcount = 0
    f = open(filename,'r')
    for line in f:
        words = line.split()
        wordcount = wordcount+len(words)
    print(wordcount)
wordcount()