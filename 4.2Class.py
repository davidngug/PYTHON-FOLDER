file=open('Egxample.txt','r')
fil=file.read()
print(len(fil))
count=0
for line in fil:
    count=count+1
    if fil.startswith(' by'):
        print('found')
        continue