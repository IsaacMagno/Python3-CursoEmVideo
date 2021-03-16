'''
prod = float(input('Qual o preço do produto? '))
print('''#Escolha de acordo com sua forma de pagamento:
#[ 1 ] À vista dinheiro/cheque: 10% de desconto
#[ 2 ] À vista no cartão: 5% de desconto
#[ 3 ] Em até 2x no cartão: Preço normal
#[ 4 ] Em 3x ou mais no cartão: 20% de juros''')'''
'''pag = int(input('Digite sua opção: '))
if pag == 1:
    print('Você escolheu o pagamento à vista em dinheiro/cheque, o total é R$ {:.2f} com 10% de desconto.'.format(prod - prod * (10/100)))
elif pag == 2:
    print('Você escolheu o pagamento à vista no cartão,o total é de R$ {:.2f} com 5% de desconto.'.format(prod - prod * (5/100)))
elif pag == 3:
    print('Você escolheu o pagamento em até 2x no cartão, o total é de R$ {:.2f} com duas prestações de R$ {:.2f}.'.format(prod, prod/2))
elif pag == 4:
    print('Você escolheu o pagamento em até 3x no cartão, o total é de R$ {:.2f} com 20% de juros e suas prestações ficaram no valor de R$ {:.2f}.'.format(prod + prod * (20/100), (prod + prod * (20/100))/3))
else:
    print('Opção invalida,tente novamente.')
'''

#Método da Aula

print('{:=^40}'.format(' LOJAS ISAAC '))
preço = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20/100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R$ {:.2f}'.format(totalparc, parcela))
else:
    total = preço
    print('Opção INVÁLIDA de pagamento. Tente novamente.')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preço, total))
