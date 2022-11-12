#LAÇOS DE REPETIÇÃO


v = True
i = 0
b = 0


# Laço for
for _ in range(5):
    print('teste 1')
print('-'*20) 

# Laço While
while v:
    print('teste 2')
    i += 1
    if i == 5:
        v = False
print('-'*20)  

#função 
def recursao(b):
    print('teste 3')
    b += 1
    if b == 5:
        return
    else:
        recursao(b)
recursao(0)