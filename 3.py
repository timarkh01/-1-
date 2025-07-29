def quarters(a):
    b = {}
    for i in a:
        if i[0] == 0:
            if i[1] == 0:
                if 'X-axis' not in b:
                    b['X-axis'] = [i]
                else:
                    b['X-axis'] += [i]
                if 'Y-axis' not in b:
                    b['Y-axis'] = [i]
                else:
                    b['Y-axis'] += [i]
            else:
                if 'Y-axis' not in b:
                    b['Y-axis'] = [i]
                else:
                    b['Y-axis'] += [i]
        elif i[1] == 0:
            if 'X-axis' not in b:
                b['X-axis'] = [i]
            else:
                b['X-axis'] += [i]
        elif i[0] > 0:
            if i[1] > 0:
                if 'I' not in b:
                    b['I'] = [i]
                else:
                    b['I'] += [i]
            else:
                if 'IV' not in b:
                    b['IV'] = [i]
                else:
                    b['IV'] += [i]
        elif i[0] < 0:
            if i[1] > 0:
                if 'II' not in b:
                    b['II'] = [i]
                else:
                    b['II'] += [i]
            else:
                if 'III' not in b:
                    b['III'] = [i]
                else:
                    b['III'] += [i]
    return b
points = [(0, 0), (-3, -2.1), (3, 0)]
print(quarters(points))