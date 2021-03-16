def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - idd
    if 65 > idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    elif 16 > idade < 18:
        return f'Com {idade} anos: NÃO VOTA'
    elif idade >= 65 or 16 <= idade <= 18:
        return f'Com {idade} anos: VOTO OPCIONAL'


idd = int(input('Em que ano você nasceu? '))
print(voto(idd))
