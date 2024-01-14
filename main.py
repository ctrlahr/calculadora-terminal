n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
soma = n1 + n2
sub = n1 - n2
multi = n1 * n2
div = n1 / n2
print('''
[ 1 ] SOMA 
[ 2 ] SUBTRAÇÃO
[ 3 ] MULTIPLICAÇÃO
[ 4 ] DIVISÃO''')

escolha = int(input('Sua escolha... '))

if escolha == 1:
    print('A soma entre {} e {} dá {}'.format(n1, n2, soma))
elif escolha == 2:
    print('A subtração entre {} e {} dá {}'.format(n1, n2, sub))
elif escolha == 3:
    print('A multiplicação entre {} e {} dá {}'.format(n1, n2, multi))
elif escolha == 4:
    print('A divisão entre {} e {} dá {}'.format(n1, n2, div))

else:
    print('Numero invalido, escreva entre 1 e 4 seu animal!')






