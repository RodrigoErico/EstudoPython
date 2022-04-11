try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # a instância de exceção
    print(inst.args)     # argumentos armazenados em .args
    print(inst)          # __str__ permite que os argumentos sejam impressos diretamente,
#                          mas pode ser substituído em subclasses de exceção.
    x, y = inst.args     # unpack args
    print('x =', x)
    print('y =', y)
    