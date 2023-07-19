def level_data(glava):
    with open('Сюжет/глава' + glava + '/карта.txt') as f:
        num = int(f.readline())
        level_data = []
        
        for i in range(num):
            s = f.readline()
            s = s[0:-1]
            level_data.append(s.split('#'))
    with open('Сюжет/глава' + glava + '/локация героев.txt') as f:
        lok = f.readline()
        lok = lok[0:-1]
    dlina = 200
    shirina = 200
    svig_horizontal = (1900 - dlina * len(level_data[0])) // 2
    sdvig_vertikal = (1000 - shirina * len(level_data)) // 2
    #heroi = [['Эрдан',80,11,8,'кожаный доспех'], ['Торн',80,12,8,'лёгкий доспех']]
    return [level_data, dlina, shirina, svig_horizontal, sdvig_vertikal, lok]

def lev():
    heroi = []
    with open('Сюжет/герои') as f:
        s = f.readline()
        while s != '':
            s = s.split(',')
            s[-1] = s[-1][:-1]
            s[1] = int(s[1])
            s[2] = int(s[2])
            s[3] = int(s[3])
            heroi.append(s)
            s = f.readline()
    #heroi = [['Эрдан',80,11,8,'кожаный доспех'], ['Торн',80,12,8,'лёгкий доспех']]
    #heroi = [['Артур', 80, 15, 5, 'лёгкий доспех'], ['Диана',80, 12, 8, 'кожаный доспех'], ['Динар', 65, 7, 15, 'тканевый плащ'], ['Николь', 70, 6, 15, 'одежда целителя']]
    return [heroi]

