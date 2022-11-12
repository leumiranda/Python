#CLASSES


rodando = 'Y'
class pokemon:
    def __init__(self, nome, tipo, atk, cor, sexo):
        self.nome = nome
        self.tipo = tipo
        self.atk = atk
        self.cor = cor
        self.sexo = sexo
        
    def dadospokemon(self):
        print(f'Dados do Pokemon:\nNome: {self.nome}.\nTipo: {self.tipo}.\nAtk: {self.atk}.\nCor: {self.cor}.\nSexo: {self.sexo}.')
    
    def attack(self):
        print(f'{self.nome}, {self.atk}!!!!!!')

while rodando == 'Y':
    pokemon1 = pokemon(input('Nome do poke:'), input('Tipo do poke:'), input('atk do poke:'), input('cor do poke:'), input('sexo do poke:'))
    print('-------------------------------------------------')
    pokemon1.dadospokemon()
    pokemon1.attack()
    print('-------------------------------------------------')
    rodando = input('Novo Pokemon? [Y/N]:')
