filename=open('Egxample2.txt')
for items in filename:
    items=items.strip()
    if items.startswith('From '):
        items=items.upper()
        items=items.split()
        for item in items:
            if item.startswith('From ') or item.endswith('THU'):
                if item.startswith('From ') or item.endswith('CWEN@IUPUI.EDU'):
                    print(items,'firststage')
quit()