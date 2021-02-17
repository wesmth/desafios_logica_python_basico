# Exercício 1 - Par ou Ímpar.

numero = input('Digite um número inteiro: ')

if not numero.isnumeric():  # Checa se o valor digitado é um número inteiro e positívo.
    print('Você precisa digitar um número inteiro!')
elif int(numero) % 2 == 0:
    print('Você digitou um número par.')
else:
    print('Você digitou um número ímpar.')

# Exercício 2 - Hora do dia.

horario = input('Digite a hora atual no formato 24h sem os minutos: ')

if not horario.isnumeric():
    print('Você precisa digitar um número inteiro.')
elif int(horario) > 23:
    print('Você digitou uma hora inválida!')
elif int(horario) <= 11:
    print('Bom dia!')
elif int(horario) <= 17:
    print('Boa tarde!')
else:
    print('Boa noite!')


# Exercício 3 - Nome:

nome_usuario = input('Digite seu nome: ')
nome_tamanho = len(nome_usuario)

if not nome_usuario.isalpha():  # Checa se o valor digitado é composto apenas por letras.
    print('você precisa digitar apenas letras!')
elif nome_tamanho <= 4:
    print('Seu nome é curto!')
elif nome_tamanho <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')
