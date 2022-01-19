def readline(filename):
    from csv import reader
    file=open(filename,'r')
    filedata=reader(file)
    count=0
    lines=''
    for line in filedata:
        count+=1
        lines+=' '+line
    print(count)