def click(token):
    if token == '=':
        try:
            mem = open('../mem.txt', 'r')
            print(eval(mem.read()))
            mem.close()
            mem = open('../mem.txt', 'w')
            mem.write('')
            mem.close()
        except:
            print('Math Error')
            mem = open('../mem.txt', 'w')
            mem.write('')
            mem.close()
    else:    
        mem = open('../mem.txt', 'a')
        mem.write(token)
        mem.close()
        mem = open('../mem.txt', 'r')
        print(mem.read())
        mem.close()

    