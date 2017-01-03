from tkinter.filedialog import *

def open_file():
    op = askopenfile()
    op = str(op)
    st = op.find('name=') + 6
    fin = op.find('mode') - 2
    path = op[st:fin]
    return path

def dfs(w, dictvertex, s):
    s += w
    if dictvertex.get(w) == None:
        return s
    else:
        s += '('
        i = 1
        for elem in dictvertex[w]:
            if i > 1:
                s += ','
            s = dfs(elem, dictvertex, s)
            i += 1
        s += ')'
    return s

def dfsCycle(w, color, matr, cyclic):
    if color[w] == 2:
        return cyclic
    if cyclic:
        return cyclic
    if color[w] == 1:
        cyclic = True
        return cyclic
    color[w] = 1
    for i in range(len(matr[w])):
        if matr[w][i] == 1:
            cyclic = dfsCycle(i, color, matr, cyclic)
            if cyclic:
                return cyclic
    color[w] = 2

if __name__ == '__main__':
    setvertex = set()
    dictvertex = {}
    numvertex = {}
    namevertex = {}
    print("Выберите файл с входными данными")
    path = open_file()
    f = open(path, 'r')
    i = 0
    checking = set()
    for line in f:
        linesplt = line.split()
        check = linesplt[1] + linesplt[2] + linesplt[3]
        if check not in checking:
            checking.add(check)
        else:
            print("Ошибка. В данной позиции ребро уже есть")
            exit(-1)
        if linesplt[2] > linesplt[3]:
            print("Ошибка. Преышен максимальный номер ребра здесь: " + line)
            exit(-1)
        try:
            int(linesplt[2])
        except ValueError:
            print("Ошибка. На третьей позиции должны быть числовые данные: " + line)
            exit(-1)
        try:
            int(linesplt[3])
        except ValueError:
            print("Ошибка. На четвёртой позиции должны быть числовые данные: " + line)
            exit(-1)
        if not linesplt[0] in setvertex:
            numvertex[linesplt[0]] = i
            namevertex[i] = linesplt[0]
            setvertex.add(linesplt[0])
            dictvertex[linesplt[0]] = None
            i += 1
        if not linesplt[1] in setvertex:
            dictvertex[linesplt[1]] = [''] * int(linesplt[3])
            setvertex.add(linesplt[1])
            numvertex[linesplt[1]] = i
            namevertex[i] = linesplt[1]
            i += 1
        else:
            if dictvertex[linesplt[1]] == None:
                dictvertex[linesplt[1]] = [''] * int(linesplt[3])
        dictvertex[linesplt[1]][int(linesplt[2]) - 1] = linesplt[0]

    for elem in dictvertex:
        if dictvertex.get(elem) != None:
            for i in range(len(dictvertex[elem])):
                if dictvertex[elem][i] == '':
                    print('Ошибка. Возможно есть неописанные рёбра')
                    exit(-1)
    ks = list(dictvertex.keys())
    n = len(setvertex)
    matr = [[0] * n for i in range(n)]
    for elem in ks:
        if dictvertex[elem] != None:
            for t in dictvertex[elem]:
                matr[numvertex[t]][numvertex[elem]] = 1

    color = [0] * n
    cyclic = False
    for w in range(n):
        cyclic = dfsCycle(w, color, matr, cyclic)
    if cyclic:
        print('Ошибка. В графе есть цикл.')

    stoki = []
    for i in range(n):
        flag = False
        for j in range(n):
            if matr[i][j] != 0:
                flag = True
                break
        if not flag:
            stoki.append(namevertex[i])

    s = ''
    used = {}
    for elem in setvertex:
        used[elem] = False
    i = 1
    for elem in stoki:
        if i > 1:
            s = s + ','
        s = dfs(elem, dictvertex, s)
        i += 1
    print("Результат: " + s)