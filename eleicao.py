undefined

e = 0
f = 0
n = 0
p = 0

def read_int(message: str, invalid_char_message: str, invalid_value_message: str, min: int=None, max: int=None):
    value = None
    valid = False

    while not valid:
        try:
            value = int(input(message))

            if min is not None and value < min:
                print(invalid_value_message, end='\n')
                valid = False
            elif max is not None and value > max:
                print(invalid_value_message, end='\n')
                valid = False
            else:
                valid = True
        except ValueError:
            print(invalid_char_message, end='\n')
            valid = False

    return value

try:
    e = read_int(
        'Digite o número de eleitores: ',
        invalid_char_message='\nO número de eleitores deve ser inteiro\n', 
        invalid_value_message='\nA quantidade de eleitores deve ser no mínimo 3\n', 
        min=3
    )

    for eleitor in range(0, e):
        c = read_int(
            '\n1.Flávia\n2.Neném\n3.Paula\n\nDigite o número do seu candidato:\n',
            invalid_char_message='\nO número do candidato deve ser inteiro\n',
            invalid_value_message='\nO número do candidato deve ser entre 1 e 3\n',
            min=1,
            max=3
        )
        if c == 1:
            f = f+1
        elif c == 2:
            n = n+1
        elif c == 3:
            p = p+1

    if f > n and f > p:
        print('\nO vencedor foi: Flávia com {} votos'.format(f))

    elif n > f and n > p:
        print('\nO vencedor foi: Neném com {} votos'.format(n))

    elif p > f and p > n:
        print('\nO vencedor foi: Paula com {} votos'.format(p))

    elif f == n or f == p or p == n:
        print('\nHouve empate! Flávia tem {} votos, Neném {} e Paula {}'.format(f, n, p))

except (ValueError):
    print('\nDigite apenas valores inteiros.\n')
