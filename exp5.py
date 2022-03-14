def getsize(filename):
    file=open(filename,'r')
    filedata=file.readlines()
    newlinecount=0
    num_char=0
    for line in filedata:
        num_char+=len(line)
        if line[-1]=='\n':
            newlinecount+=1
    print(f'Number of lines: {newlinecount+1}')
    print(f"File Size is : {num_char+newlinecount} bytes")
getsize(input())
