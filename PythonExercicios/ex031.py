v = float(input('Digite a distância da sua viagem: '))
if v <= 200:
    print('O custo da sua viagem é de {:.2f}'.format(v*0.50))
else:
    print('O custo da sua viagem é de {:.2f}'.format(v*0.45))

#metodo da aula

distancia = float(input('Qual a distancia da sua viagem?'))
print('Você está prestes a começar  uma viagem de {}Km.'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45 # if simplificado
print('E o preço da sua passagem será de {:.2f}'.format(preço))
