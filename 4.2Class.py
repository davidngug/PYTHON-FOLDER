file=open('Egxample.txt')
count=0
for line in file:
    count=count+1
    if line.startswith('from: '):
        print(line,count)
        