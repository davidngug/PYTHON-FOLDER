filename=open('Egxample2.txt')
for items in filename:
    items=items.strip()
    if items.startswith('From '):
        items=items.upper()
        items=items.split()
        print(items)
quit()