#ARMAZENAMENTO DE DADOS.

contador = -1
id_cliente = []
clientes = []
carteiras = []
valores = []
moedas = []
cedulas = []
request = 0


#classe
class carteira:
    def __init__(self, valor, moeda, cedula):
        self.valor = valor
        self.moeda = moeda
        self.cedula = cedula
    
    def mostrar_dados():
        for n in id_cliente:
            carteiras[n] = carteira(valores[n],moedas[n],cedulas[n])
            print('-'*20)
            print(f'id_cliente: {id_cliente[n]}.\nDono da carteira: {clientes[n]}.\nValor na carteira: {valores[n]}.\nNome da moeda: {moedas[n]}.\nCédulas: {cedulas[n]}.')
            print('-'*20)

#laço
while request != 3:
    request = int(input('[1] - CRIAR CARTEIRA\n[2] - CONSULTAR CARTEIRA\n[3] - ENCERRAR PESQUISA\n--------------------\n'))
    if request == 1:
        contador += 1
        id_cliente.append(contador)
        clientes.append(str(input('Nome:')))
        carteiras.append(str(contador))
        valores.append(int(input('Valor em dinheiro:')))
        moedas.append(str(input('Nome da moeda:[1: REAL][2: DOLAR][3: EURO]')))
        cedulas.append(int(input('Quantidade de cédulas:')))
        
        print('-'*20)
        print('Cadastro Realizado com sucesso.')
        print('-'*20)
        

    elif request == 2:
        carteira.mostrar_dados()