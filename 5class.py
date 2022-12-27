filename=open('Egxample2.txt')
count=0
for items in filename:
    items=items.strip()
    if items.startswith('From '):
        items=items.upper()
        items=items.split()
        for item in items:
            if item.endswith('17:18:23'):
                count=count+1
                items=str(items)
                itemz=items.split(':')    
                print(itemz,'Second stage',count)
quit()