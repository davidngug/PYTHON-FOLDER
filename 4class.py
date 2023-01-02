file=open('2class.py','r')
F=file.read()
print(len(F))

f=F[20:500]
f=f.rstrip()
f=f.split('#')
print(f)

for words in f:
    if 'letters' in words:
        print('found')
    else:
        print('not there ')
    if words.endswith('letters') or words.startswith('letters'):#WORKS BUT USED IN-EFFECTIVELY
        print('found it')
    else:print("didnt found it")
    quit()