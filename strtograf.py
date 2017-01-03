def dfsCycle(w, color, vertexes, cyclic):
    if color[w] == 2:
        return cyclic
    if cyclic:
        return cyclic
    if color[w] == 1:
        cyclic = True
        return cyclic
    color[w] = 1
    for elem in vertexes[w]:
        cyclic = dfsCycle(elem, color, vertexes, cyclic)
        if cyclic:
            return cyclic
    color[w] = 2

def splt(s):
    result = []
    n = len(s)
    i = 0
    while i < n:
        j = i
        while j < len(s):
            if s[j] != '(' and s[j] != ',':
                j += 1
            else:
                break
        if j == len(s):
            result.append(s[i:j])
            i = j
            continue
        elif s[j] == ',':
            result.append(s[i:j])
            i = j + 1
            continue
        elif s[j] == '(':
            op = 0
            cl = 0
            while (op != cl or op == cl == 0):
                if s[j] == '(':
                    op += 1
                elif s[j] == ')':
                    cl += 1
                j += 1
        result.append(s[i:j])
        i = j + 1

    return result

def func(stroka, vertexes):
    parents = []
    j = 0
    while j < len(stroka):
        op = 0
        cl = 0
        i = j
        k = i
        while ((stroka[i] <= 'Z' and stroka[i] >= 'A') or (stroka[i] <= 'z'and stroka[i] >= 'a')) or \
                ((stroka[i] <= 'Я'and stroka[i] >= 'А') or (stroka[i] <= 'я'and stroka[i] >= 'а')) or \
                (stroka[i] <= '9' and stroka[i] >= '0'):
            j += 1
            i += 1
        while ((not (op == cl)) or (op == cl == 0)) and (j < len(stroka)):
            if stroka[j] == '(':
                op += 1
            elif stroka[j] == ')':
                cl += 1
            j += 1
        s = stroka[i+1:j-1]
        mas = splt(s)
        x = [0] * len(mas)
        for l in range (len(mas)):
            if mas[l].find(',') == -1 and mas[l].find('(') == -1:
                x[l] = mas[l]
                vertexes[mas[l]] = []
            else:
                x[l] = str(func(mas[l], vertexes))[2:-2]
        vertexes[stroka[k:i]] = x
        parents.append(stroka[k:i])
    return parents

print("Введите входной набор термов: ")
stroka = input()
if len(stroka) == 1:
    print("В графе только одна вершина " + stroka)
    exit(0)
op = 0
cl = 0
for j in range(len(stroka)):
    if stroka[j] == '(':
        op += 1
    elif stroka[j] == ')':
        cl += 1
if op != cl:
    print("Ошибка. Количество ( и ) не равно")
    exit(-1)
for j in range(len(stroka)-1):
    if stroka[j:j+2] == ',(' or stroka[j:j+2] == '(,' or stroka[j:j+2] == '()' or stroka[j:j+2] == ',)' \
            or stroka[j:j+2] == ',,' or stroka[j:j+2] == ')(':
        print("Ошибка при вводе строки")
        exit(-1)
vertexes = {}
mas = splt(stroka)
stoki = [0] * len(mas)
for i in range (len(mas)):
    if mas[i].find(',') == -1 and mas[i].find('(') == -1:
        stoki[i] = mas[i]
        vertexes[mas[i]] = []
    else:
        stoki[i] = func(mas[i], vertexes)
ks = list(vertexes.keys())
color = {}
ans = ''
for elem in ks:
    for i in range(len(vertexes[elem])):
        ans += vertexes[elem][i] + ' ' + elem + ' ' + str(i+1) + ' ' + str(len(vertexes[elem])) + '\n'
        color[vertexes[elem][i]] = 0
        color[elem] = 0
cyclic = False
for w in ks:
    cyclic = dfsCycle(w, color, vertexes, cyclic)
    if cyclic:
        print('Ошибка. В графе есть цикл.')
        exit(-1)
print(ans)