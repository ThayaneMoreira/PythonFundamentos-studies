#Cabeçalho
print('\n********** Python Calculator **********')

# Funções
def add(x, y):
	return x + y

def subtract(x, y):
	return x - y

def multiply(x, y):
	return x * y

def divide(x, y):
	return x / y


#Opções da calculadora
print('\n Selecione o número com a operação desejada: \n')
print('\n 1 - Soma')
print('\n 2 - Subtração')
print('\n 3 - Multiplicação')
print('\n 4 - Divisão')


#Escolha o usuário
escolha = input('\n Digite sua opção (1/2/3/4): ')

num1 = int(input('\n Digite o primeiro número: '))
num2 = int(input('\n Digite o segundo número: '))

#Calculos
if escolha == '1':
	print('\n')
	print(num1, '+', num2, '=', add(num1, num2))
	print('\n')

elif escolha == '2':
	print('\n')
	print(num1, '-', num2, '=', subtract(num1, num2))
	print('\n')

elif escolha == '3':
	print('\n')
	print(num1, '*', num2, '=', multiply(num1, num2))
	print('\n')

elif escolha == '4':
	print('\n')
	print(num1, '/', num2, '=', divide(num1, num2))
	print('\n')

else:
	print('\n Opção inválida!')



