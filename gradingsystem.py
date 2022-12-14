#GRADING SYSTEMS BY KINYASH RANG OF(0.0-1.0)
x=input('WHAT IS YOUR SCORE?')
x=float(x)

if x>=0.0 and x<=1.0:
    print('YOUR SCORE LIES WITHIN RANGE')
else :
    print('YOUR SCORE DOES NOT LIE WITHIN RANGE\nPLEASE INPUT CORRECT SCORE')
if x>=0.0 and x<0.6:
    print('F')
if x>=0.6 and x<0.7:
    print('D')
if x>=0.7 and x<0.8:
    print('C')
if x>=0.8 and x<0.9:
    print('B')
if x>=0.9 and x<=1.0:
    print('A')
quit()