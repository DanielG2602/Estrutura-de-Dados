

def sauda (nome):
    print(f'Olá {nome}, tudo bem?')
    sauda(nome)
    print(f'Tchau {nome}, até logo!')
    tchau()
    
def sauda2(nome):
    print(f"como vai {nome}?")

def tchau():
    print("Tchau, até logo!")
    
# pilha de chamada com recursão

def fat(x):
    if x == 1:
        return 1
    else:
        return x * fat(x - 1)