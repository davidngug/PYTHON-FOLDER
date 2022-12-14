#use of BOOLEAN VARIABLE(found=False)
#BOOLEAN VARIABLE CAN EITHER BE TRUE OR FALSE
#AVERAGE STOPS AT LOOP 4
count=0
counts=0
found=False
for i in [54,98,65,84,78]:
    count=count+1
    counts=(counts+i)
    print('numbers:',i,'loops:',count)
    if counts>=300:
        found=True
        print(found)
        break
av=counts/count
print('average',av)
quit()