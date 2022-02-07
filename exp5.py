def getsize(filename):
    file=open(filename,'r')
    filedata=file.readlines()
    count=0
    lines=''
    for line in filedata:
        count+=1
        lines+=line
    print(f'Number of lines: {count}')
    return 0