d = float(input('Quantos dias foi alugado? '))
k = float(input('Quantos km foram rodados? '))
dp = d * 60
kp = k * 0.15
tt = dp + kp
print('Você alugou o carro por {:.0f} Dias e rodou {:.0f}KM. O total a pagar é R$ {:.2f}'.format(d, k, tt))
print('O valor em dias é de R$ {:.2f} e o de kilometros é R$ {:.2f}'.format(dp, kp))
