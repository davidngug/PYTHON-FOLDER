file=open('2class.py','r')
F=file.read()
print(len(F))
f=F[20:500]
print(f)
for words in f:
    if words.endswith(' letters') :
        print('found it')