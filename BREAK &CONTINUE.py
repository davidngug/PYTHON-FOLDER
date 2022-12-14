while True:
    line = input('> ')
    if line[0] == ('#'):
        print('route 1')
        continue
    if line == ('done'):
        print('route2')
        break
    print(line)
print('Done!')
quit()
