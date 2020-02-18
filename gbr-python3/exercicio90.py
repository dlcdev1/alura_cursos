'''
FAÇA UM PROGRAMA QUE LEIA NOME E MÉDIA DE UM ALUNO, GUARDANDO TAMB[EM A SITUA;ÁO EM UM
DICIONARIO. NO FINAL MOSTRE O CONTEUDO DA ESTRUTURA NA TELA

PRINT
NOME: XXXX = INPUT
MEDIA DE XXXX = INPUT

PRINT RESULT
NOME E IGUA A XXXX
MEDIA E IGUAL XXX
SITUACAO E IGUAL A APROVADO/REPROVADO

'''

nome = input('Nome: ')
media = float(input('Media: '))
dados = {'Nome':nome, 'Média':media}

for v, k in dados.items():
    print(f'{v} e igua a {k}')

if dados["Média"] >= 7:
    print('Situaçao é igual a APROVADO')
else:
    print('Situaçao é igual a REPROVADO')










