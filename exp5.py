def getsize(filename):
    file=open(filename,'r')
    filedata=file.readlines()
    count=0
    newlinecount=0
    num_char=0
    for line in filedata:
        num_char+=len(line)
        if line[-1]=='\n':
            newlinecount+=1
        count+=1
    print(f'Number of lines: {count}')
    print(f"File Size is : {num_char+newlinecount} bytes")
