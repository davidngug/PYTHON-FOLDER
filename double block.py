#you can use either POSITIVE OR NEGATIVE DIGITS IN LINE 2
x=3
y=x-4
if x%2==0:
    print('even')
    print('route 1')
else:
    print('odd')
    if x<y:
        print('x is less than y')
    elif x>y:
        print('x is greater than y')
    else:
        print('x is equal to y')
    print('route 2')
if x>0 and x<10**78:
    print ('positive digit ')
else:
    print('negative digit')
quit()