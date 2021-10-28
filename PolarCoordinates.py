import cmath
import re

if __name__ == '__main__':

    pattern = "([-]?[0-9]*)([+-]?[0-9]*[a-z]{1})"
    res = re.match(pattern, input())
    x = float(res.groups()[0])
    y = float(res.groups()[1][:-1])
    print(x,y)
    print(abs(complex(x, y)))
    print(cmath.phase(complex(x, y)))

