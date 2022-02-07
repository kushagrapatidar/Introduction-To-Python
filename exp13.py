def even_length_words(string):
    words=[]
    string=string.split()
    string=str.split(".")
    string=string.split(",")
    for word in string:
        if len(word)%2==0:
            words.append(word)
    [print(word) for word in words]