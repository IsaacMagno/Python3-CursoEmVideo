try:
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    r = a / b
except KeyboardInterrupt:
    print('O usuario não digitou os dados!')
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('Não é possivel dividir numeros por 0.')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}.')
else:
    print(f'O resultado é {r}.')
finally:
    print('Volte sempre!')
