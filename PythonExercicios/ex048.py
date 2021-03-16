m = 0
c = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        m += i
        c += 1
print('A soma entre todos os {} valores é: {}'.format(c, m))
