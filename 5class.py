filename=open('Egxample2.txt')
filname=filename.read()
for items in filname:
    items=items.strip()
    if items.startswith('From '):
        items=items.upper()
        items=items.split()
        print(items)
quit()