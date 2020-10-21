def click(token):
    if token == 'C':
        mem = open('../mem.txt', 'w')
        mem.write('')
        mem.close()
        mem = open('../mem.txt', 'r')
        result = mem.read()
        mem.close()
        return result
    elif token == 'CE':
        mem = open('../mem.txt', 'r')
        result = mem.read()[0:-1]
        mem.close()
        mem = open('../mem.txt', 'w')
        mem.write(result)
        mem.close()
        return result
    elif token == '=':
        try:
            mem = open('../mem.txt', 'r')
            result = eval(mem.read())
            mem.close()
            mem = open('../mem.txt', 'w')
            mem.write('')
            mem.close()
            return result
        except:
            result = 'Math Error'
            mem = open('../mem.txt', 'w')
            mem.write('')
            mem.close()
            return result
    else:    
        mem = open('../mem.txt', 'a')
        mem.write(token)
        mem.close()
        mem = open('../mem.txt', 'r')
        result = mem.read()
        mem.close()
        return result

    