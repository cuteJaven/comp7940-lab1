import sys
from math import sqrt


def print_factor(x):
    fac = []
    if not x.isdigit():
        print('Please input an positive integer!')
        sys.exit(1)
    x_int = int(x)
    sqrt_x = int(sqrt(x_int))
    for i in range(1, sqrt_x + 1):
        fac.append(i)
        y_int = int(x_int / i)
        if y_int != i:
            fac.append(int(x_int / i))
    print(fac)


if __name__ == '__main__':
    print_factor(input('please input a positive integer:'))
