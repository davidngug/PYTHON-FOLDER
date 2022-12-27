str='X-DSPAM-Confidence: 0.8475'
print(len(str))
tr=str.find(' ')
tr=int(tr)
print(tr)
r=str[tr:26]
r=float(r)
print(r)
