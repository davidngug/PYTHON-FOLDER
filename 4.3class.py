user=input('what is the name of the file ?')
count=0
try:fname=open(user)
except:print('WRONG FILE NAME')
for subject in fname:
        count=count+1
        if subject.startswith('subject'):
        print('the number of subjects is',count)
quit()