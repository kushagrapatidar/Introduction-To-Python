def readline(filename):
    from csv import reader
    file=open(filename,'r')
    filedata=reader(file)
    count=0
    for row in filedata:
        count+=1
    print(count)