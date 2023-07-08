w = input()
n = int(input())
length = len(w)
table = [[' ' for x in range(length + 1)] for y in range(length + 1) ]

gram = {}

for i in range(n):
    g = input()
    k = g.split('->')
    v = k[1].split('|')
    gram[k[0]] = v


for i in range(1,length + 1):
    for key in gram.keys():
        for value in gram[key]:
            if w[i - 1] in value:
                table[i][i] += key
                break


for l in range(2, length + 1):
    for i in range(1,length - l + 2):
        j = i + l - 1
        for k in range(i, j):
            for key in gram.keys():
                for value in gram[key]:
                    if len(value) != 1:
                        if value[0] in table[i][k] and value[1] in table[k + 1][j]:
                            table[i][j] += key 


if('S' in table[1][length]):
    print("YES")
else:
    print("NO")