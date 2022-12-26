user=input('what is the name of the file ?')
user=str(user)
fname=open(user,'r')
fn=fname.read()
count=0
for subject in fn:
    count=count+1
    if subject.startswith('subject'):
        print('the number of subjects is',count)