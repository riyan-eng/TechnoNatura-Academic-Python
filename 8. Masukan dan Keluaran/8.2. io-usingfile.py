f = open('poem.txt', 'w')

poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''
f.write(poem)
f.close()

f = open('poem.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    
    print(line, end='')
f.close()