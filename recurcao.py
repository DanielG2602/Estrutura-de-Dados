def procurar_pela_chave(caixa_principal):
    pilha = caixa_principal.crie_uma_pilha_para_busca()
    while pilha is not None:
        caixa = pilha.pegue_caixa()
        for item in caixa:
            if item.e_uma_caixa():
                pilha.append(item)
            elif item.e_uma_chave():
                print("Chave encontrada:", item)

def procure_pela_chave(caixa):
    for item in caixa:
        if item.e_uma_caixa():
            procure_pela_chave(item)
        elif item.e_uma_chave():
            print("Chave encontrada:", item)
            
# ------------------

def regressiva(i):
    print(i)
    regressiva(i - 1)
    
def regressiva_com_condicao(i):
    print(i)
    if i <= 1:
        return
    else:
        regressiva_com_condicao(i - 1)