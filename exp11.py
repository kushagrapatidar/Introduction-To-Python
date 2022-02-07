def readcharacters(filename):
    file=open(filename,'r')
    filedata=file.readlines()
    characters=[]
    for line in filedata:
        for char in line:
            characters.append(char)
    print(characters)