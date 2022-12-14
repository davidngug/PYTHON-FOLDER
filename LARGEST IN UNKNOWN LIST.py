largest_so_far=None
print('largest so far',largest_so_far)
for i in(21,200,7008,99,10098,6054,1023,7898):
    if largest_so_far is None or i >largest_so_far:
        largest_so_far=i
    print('Loop:',i,largest_so_far)
print('Largest So Far',largest_so_far)
quit()





#TO FIND SMALLEST, CHANGE TO SMALLEST CONVERTE LINE 4 ,greater than(>) TO less than(<)
largest_so_far=None
print('largest so far',largest_so_far)
for i in(21,200,7008,99,10098,6054,1023,7898):
    if largest_so_far is None or i <largest_so_far:
        largest_so_far=i
    print('Loop:',i,largest_so_far)
print('Largest So Far',largest_so_far)
quit()     