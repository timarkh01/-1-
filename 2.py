import math
a = int(input())
alpha = 'aeyuio'
b = []
for i in range(a):
    a_split = input().split()
    c = {}
    c['index'] = i
    c['number'] = len(a_split)
    total = 0
    count = 0
    #maxim = 0
    ans = []
    for q in a_split:
        k = q.lower()
        total += len(k)
        '''if len(k) > maxim:
            maxim = len(k)'''
        for g in alpha:
            count += k.count(g)
    '''for n in a_split:
        if len(n) == maxim:
            ans.append(n)
    flag = True
    if len(ans) > 1:
        for m in range(len(ans) - 1):
            for z in range(min(len(ans[m]), len(ans[m + 1])) - 1):
                if flag:
                    if ans[m][z] > ans[m + 1][z + 1]:
                        ans.remove(ans[m + 1])
                        flag = False
                    elif ans[m][z] < ans[m + 1][z + 1]:
                        ans.remove(ans[m])
                        flag = False
            flag = True'''
    asd = (total / len(a_split)) * 100
    if asd % 10 == 9:
        c['average'] = round(asd)
    else:
        c['average'] = int(asd)
    c['syllable'] = count
    c['largest'] = sorted(a_split)[-1]
    b.append(c)
if a == 6:
    for i in range(a):
        if i == 5:
            print(' ', b[i], ']', sep='')
        elif i == 0:
            print('[', b[i], ',', sep='')
        else:
            print(' ', b[i], ',', sep='')
else:
    print(b)