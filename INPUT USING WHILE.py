#{WHILE TRUE} OR {WHILE FALSE} BEHAVES AS A CONTINUE
while True:
    line = input('> ')
    if line == ('done'):
        break
    print(line)
print('Done!')
quit()