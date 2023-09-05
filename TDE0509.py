def uniao(conjunto1, conjunto2):
    return conjunto1 + conjunto2

def inter(conjunto1, conjunto2):
    return list(set(conjunto1).intersection(conjunto2))

def dif(conjunto1, conjunto2):
    return list(set(conjunto1) - set(conjunto2))

def prod(conjunto1, conjunto2):
    return [(x, y) for x in conjunto1 for y in conjunto2]

def processar_operacoes():
    operacoes = {'U': 'União', 'I': 'Interseção', 'D': 'Diferença', 'C': 'Produto Cartesiano'}
    
    num_operacoes = int(input("Digite o número de operações: "))
    
    for _ in range(num_operacoes):
        print("Digite a operação desejada com letra maiscula! ")
        operacao = input("Digite qual operação quer realizar: (U para união, I para interseção, D para diferença, C para produto cartesiano): ")
        conjunto1 = input("Entre com os items conjunto 1 separados por vírgula: ").split(',')
        conjunto2 = input("Entre com os items conjunto 2 separados por vírgula: ").split(',')
        
        conjunto1 = [item.strip() for item in conjunto1]
        conjunto2 = [item.strip() for item in conjunto2]
        
        resultado = None
        if  operacao == 'U':
            resultado = uniao(conjunto1, conjunto2)
        elif operacao == 'I':
            resultado = inter(conjunto1, conjunto2)
        elif operacao == 'D':
            resultado = dif(conjunto1, conjunto2)
        elif operacao == 'C':
            resultado = prod(conjunto1, conjunto2)
        
        print(f'{operacoes[operacao]}: conjunto 1 {{{", ".join(conjunto1)}}}, conjunto 2 {{{", ".join(conjunto2)}}}. Resultado: {{{", ".join(map(str, resultado))}}}')

processar_operacoes()