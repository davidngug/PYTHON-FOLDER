file=open('EGXAMPLE.txt')
count=0
for line in file:
    count=count+1
    line=line.rstrip()# remove this to know difference
    if line.startswith('From:'):
        print(count,'from',line)
    if not '53632.deriv' in line:
        print(count,'632 deriv',line)
        continue
        #can refer to skip go to next
