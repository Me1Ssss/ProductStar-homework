
def solve(a, b, c):
    def discriminant(a, b, c):
        d = b**2 - 4 * a * c
        return d
    if discriminant(a, b, c) < 0:
        print('Нет решений')
    elif discriminant(a, b, c) == 0:
        print(f'x =  {- b / 2 / a}')
    else:
        print(f'x1={(-b + discriminant(a,b,c)**0.5) / 2 / a}\
              x2 = {(+b + discriminant(a,b,c)**0.5) / 2 / a}')


solve(1, 2, 1)
