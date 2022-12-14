#METHOD (1) USES KNOWN LEAST VALUE # METHOD (2) USES ALL UNKNOWN VALUES 
largest_so_far=-1
print(largest_so_far,'largest so far')
for num in (21,200,7008,99,10098,6054,1023,7898):
    if num>largest_so_far:
        largest_so_far=num
    print(largest_so_far,num)
print('largest so far',largest_so_far)
quit()

