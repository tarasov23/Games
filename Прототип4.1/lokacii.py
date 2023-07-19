import pygame as p
import sys
from cvesti import Text_loc, Knopka
from Vragi_v_igre import vragi_v_igre
from withual1 import bou
from komanda import Her_komand
from level import lev
vragi_v_igre = vragi_v_igre()

heroi = lev()
her_komand = Her_komand(heroi, 4, 0, 0, 0, 0)

dostigenia = {}
with open('Сюжет/имеющиеся_достижения.txt') as f:
    s = f.readline()
    while s != '':
        s = s.split(':')
        s[-1] = s[-1][:-1]
        s[-1] = s[-1].split(',')
        if s[-1] == ['']:
            dostigenia[s[0]] = []
        else:
            dostigenia[s[0]] = s[1]
        #print(s)
        s = f.readline()

#print(dostigenia)
zav_issled = False

missia = 'Исследовать_Дозор'
def h_komand():
    return her_komand

def schitivanie_texta(screen, name, glava):
    with open('Сюжет/глава' + glava + '/локации/' + name + '/' + name) as f:
        text = {}
        nach_text = ''
        s = f.readline()
        count = 0
        while s != '':
            s = s[:-1]
            s = s.split('*')
            if count >= 1:
                text[s[0]] = [s[1], s[2].split('#')] #[номер, текст, текст реакции,]
            else:
                nach_text = s
            count += 1
            s = f.readline()
    #print(text)
    with open('Сюжет/глава' + glava + '/локации/' + name +'/граф.txt') as f:
        graf = {}
        s = f.readline()
        while s != '':
            s = s[:-1]
            s = s.split('*')
            graf[s[0]] = s[1].split(',')
            s = f.readline()
    text_l = Text_loc(screen, nach_text, 100, 100)
    knopki = []
    count = 0
    for i in graf['0']:
        osob = text[i][0]
        if 'Достижение' in osob:
            osob = osob.split()
            dos = osob[1]
            chast = []
            for j in range(2, len(osob)):
                chast.append(osob[j])
            if dostigenia[dos] == chast:
                knopka = Knopka(screen, i, text[i][0], 100, 700 + 50 * count)
                knopki.append(knopka)
                count += 1
        else:
            knopka = Knopka(screen, i, text[i][0], 100, 700 + 50 * count)
            knopki.append(knopka)
            count += 1
    return [text_l, knopki, text, graf]

def izmenenie(graf ,text, name, screen, clock, missia):
    #data = level_data(glava)
    okonch = False
    text_l = Text_loc(screen, text[name][1], 100, 100)
    #print(dostigenia)
    knopki = []
    count = 0
    if text[name][1] == ['Исследование окончено']:
        return [text_l, knopki, True, missia, okonch]
    if len(text[name][1]) >= 2: #если длина выбранного текста равна двум
        sob = text[name][1]
        for a in sob:
            s = a
            s = s.lower()
            if ('еда +' in s) or ('еда -' in s) or ('золото +' in s) or ('золото -' in s) or ('опыт +' in s) or ('опыт -' in s) or ('слово +' in s) or ('слово -' in s) or ('ужас +' in s) or ('ужас -' in s): #если в тексте происходит увеличение или уменьшение еды
                cena = text[name][1][1].lower()
                cena = cena[-2]
                #print(cena)
                #print(sob)
                if 'золото -' in s:
                    #print(2)
                    #print(her_komand.resurs['золото'])
                    if her_komand.resurs['золото'] >= int(cena):
                        #print(1)
                        if 'оружие' in sob[-1]:
                            pass
                            #print(1)
                        else:
                            her_komand.izm_param(s)
                else:
                    her_komand.izm_param(s)
        
            elif 'проведите встречу' in s:
                #data = level_data()
                heroi = her_komand.heroi
                lst = s.split()
                del lst[0]
                del lst[0] #враг, уровень встречи
                vrag = lst[0].lower()
                ur = int(lst[2][0])
                inf_vrag = vragi_v_igre[vrag]
                param = inf_vrag[0]
                nagrada = inf_vrag[1]
                vrag = [vrag] + param
                vrag[1] *= ur
                vrag[2] *= ur
                vrag[3] *= ur
                #print(heroi)
                her_hp = bou(heroi, [vrag], screen, clock)
                print(her_hp)
                her_komand.izm_param_hp(her_hp)
                #print(her_komand.eda, her_komand.zoloto, her_komand.opit, her_komand.slava)
                her_komand.nach_nagrada(nagrada, ur)
                #print(her_komand.eda, her_komand.zoloto, her_komand.opit, her_komand.slava)
            elif 'Получите достижение' in a:
                #inf = s.title().split()
                inf = a.split()
                dos = inf[2]
                chast = inf[3][:-1]
                dostigenia[dos].append(chast)
            
            elif 'Миссия' in a:
                missia = a.split()[1][:-1]
                #print(missia)
            elif 'Глава окончена' in a:
                with open('Сюжет/имеющиеся_достижения.txt','w') as f:
                    for dos in dostigenia:
                        s = dostigenia[dos]
                        if s == []:
                            f.write(dos + ':' + '\n')
                        elif len(s) == 1:
                            f.write(dos + ':' + s[0] + '\n')
                okonch = True
                return [text_l, knopki, True, missia, okonch]
    
    for i in graf[name]:
        osob = text[i][0]
        if 'Достижение' in osob:
            osob = osob.split()
            dos = osob[1]
            chast = []
            for j in range(2, len(osob)):
                chast.append(osob[j])
            if dostigenia[dos] == chast:
                knopka = Knopka(screen, i, text[i][0], 100, 700 + 50 * count)
                knopki.append(knopka)
                count += 1
        else:
            knopka = Knopka(screen, i, text[i][0], 100, 700 + 50 * count)
            knopki.append(knopka)
            count += 1
    return [text_l, knopki, False, missia, okonch]

def issledovanie(screen, clock, name, glava, missia):
    okonch = False
    m = missia
    text_l, knopki, text, graf = schitivanie_texta(screen, name, glava)
    
    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                sys.exit()
            if event.type == p.MOUSEBUTTONDOWN:
                a = event.pos
                for kn in knopki:
                    f = kn.nagatie(a)
                    if f:
                        text_l, knopki, okonch, missia, okonch_gl = izmenenie(graf, text, f, screen, clock, missia)
            if event.type == p.MOUSEMOTION:
                a = event.pos
                for kn in knopki:
                    kn.navedenie(a)
        if okonch:
            return [missia, okonch_gl]
            break
        screen.fill((0, 0, 0))
        her_komand.output(screen)
        text_l.output()
        for kn in knopki:
            kn.output()
        p.display.flip()#Обновление окна
        clock.tick(60)

    
