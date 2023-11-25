d = 0


def discriminant(a, b, c):
    global d
    d = b**2 - 4 * a * c
    return d


def solve(a, b, c):
    if d < 0:
        print('Нет решений')
    elif d == 0:
        print(f'x =  {- b / 2 / a}')
    else:
        print(f'x1={(-b + d**0.5) / 2 / a}\
              x2 = {(+b + d**0.5) / 2 / a}')


solve(1, -1, 3)
