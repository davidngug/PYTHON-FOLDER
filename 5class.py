filename=open('Egxample2.txt')
for items in filename:
    items=items.strip()
    if items.startswith('From '):
        items=items.upper()
        items=items.split()
        for item in items:
            if item.startswith('From ') or item.endswith('THU'):
                print(items,'first stage')
                if item.startswith('From ') or item.endswith('2008'):
                    print(items,'Second stage')
quit()