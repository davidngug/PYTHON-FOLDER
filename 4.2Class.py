file=open('EGXAMPLE.txt')
count=0
for line in file:
    count=count+1
    line=line.rstrip()# remove this to know difference
    if not ':53632.deriv' in line:
     continue
    print(line,count)
         