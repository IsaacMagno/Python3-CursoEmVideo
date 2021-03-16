def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [2, 3, 4, 5, 6, 7]
dobra(valores)
print(valores)
