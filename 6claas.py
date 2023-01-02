page=[1,2,3,4,5,6,7,8,9]#isa list
mpage=page.append(2)
xpage=page.pop(5) #5 is index
print(page)

forex={}#isa dict
forex['counter']=1
forex['bima']=89
print(forex)

forex['counter']=forex['counter']+80
print(forex)

print('porn' in forex)#response true or false used by in

counts=dict()#
papers=['elon','mark','ford','bob','elon','ford']
for paper in papers:
    if paper not in counts:
        counts[paper]=1
    else:counts[paper]=counts[paper]+1 
    print(counts)
    
quit()
counts[paper]=counts.get(paper,0)+1# YOU CAN USE THIS FOR (LINE 15-17)


