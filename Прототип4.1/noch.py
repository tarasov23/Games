import pygame as p
from komanda import Her_komand
from cvesti import Knopka
from random import randrange
from withual1 import bou
from Vragi_v_igre import vragi_v_igre
import sys

vragi_v_igre = vragi_v_igre()

def perehod_faz(faza, screen, clock):
    if faza == 0:
        f4 = p.font.Font(None, 60)
        text4 = f4.render('Привал.', True, (100, 100, 100))
        screen.blit(text4, (100, 200))
    if faza == 1:
        f4 = p.font.Font(None, 60)
        text4 = f4.render('Ночное событие.', True, (100, 100, 100))
        screen.blit(text4, (100, 200))
    if faza == 2:
        f4 = p.font.Font(None, 60)
        text4 = f4.render('Сон.', True, (100, 100, 100))
        screen.blit(text4, (100, 200))
    if faza == 3:
        f4 = p.font.Font(None, 60)
        text4 = f4.render('Новый день.', True, (100, 100, 100))
        screen.blit(text4, (100, 200))
    
    for i in range(200):
        screen.fill((0, 0, 0))
        screen.blit(text4, ((100 + i * 2), 300))
        p.display.flip()#Обновление окна
        clock.tick(60)
    return True
    
def son(faza, screen, clock, her_komand, name):
    snovidenie = []
    with open('Сюжет/сны/' + name) as f:
        s = f.readline()
        snovidenie = s.split('*')
    snovidenie[-1] = snovidenie[-1][:-1]
    for i in range(len(snovidenie)):
        f1 = p.font.Font(None, 32)
        text1 = f1.render(snovidenie[i], True, (100, 100, 100))
        screen.blit(text1, (100, 100 + (i * 50)))
    fl = False
    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                sys.exit()
            if event.type == p.MOUSEBUTTONDOWN:
                fl = True
        if fl:
            break
        screen.fill((0, 0, 0))
        her_komand.output(screen)
        for i in range(len(snovidenie)):
            f1 = p.font.Font(None, 32)
            text1 = f1.render(snovidenie[i], True, (100, 100, 100))
            screen.blit(text1, (100, 100 + (i * 50)))
        p.display.flip()#Обновление окна
        clock.tick(60)
    data = snovidenie[-1].lower()
    if ('золото' in data) or ('еда' in data) or ('слава' in data) or ('опыт' in data) or ('ужас' in data):
        her_komand.izm_param(data)
    
    faza = 3
    return faza

def otdih(her_komand, faza, screen, clock):
    if her_komand.resurs['еда'] >= len(her_komand.heroi):
        
        f3 = p.font.Font(None, 32)
        text3 = f3.render('Все герои поели и отдохнули.', True, (100, 100, 100))
        screen.blit(text3, (100, 200))
        
        her_komand.resurs['еда'] -= len(her_komand.heroi)
        her_komand.resurs['ужас'] -= 1
        if her_komand.resurs['ужас'] < 0:
            her_komand.resurs['ужас'] = 0
        lst = []
        for her in her_komand.her_max_hp:
            #print(her, her_komand.her_max_hp[her])
            lst.append([her, her_komand.her_hp[her] + int(her_komand.her_max_hp[her] * 0.2)])
        her_komand.izm_param_hp(lst)
        fl = False
        while True:
            for event in p.event.get():
                if event.type == p.QUIT:
                    p.quit()
                    sys.exit()
                if event.type == p.MOUSEBUTTONDOWN:
                    fl = True
            if fl:
                break
            screen.fill((0, 0, 0))
            her_komand.output(screen)
            screen.blit(text3, (300, 500))
            p.display.flip()#Обновление окна
            clock.tick(60)
            
    else:
        lst = []
        for her in heroi:
            name = Knopka(screen, her[0], her[0], 300, 500)
            net = Knopka(screen, '1', str(her[0]) + ' не ест.', 300, 600)
            f = None
            f1 = None
            while True:
                for event in p.event.get():
                    if event.type == p.QUIT:
                        p.quit()
                        sys.exit()
                    if event.type == p.MOUSEMOTION:
                        a = event.pos
                        name.navedenie(a)
                        net.navedenie(a)
                    if event.type == p.MOUSEBUTTONDOWN:
                        a = event.pos
                        f = name.nagatie(a)
                        f1 = net.nagatie(a)
                if her_komand.resurs['еда'] > 0:
                    if f:
                        lst.append([f, her_komand.her_hp[f] + int(her_komand.her_max_hp[f] * 0.2)])
                        her_komand.resurs['еда'] -= 1
                        break
                if f1:
                    break
                screen.fill((0, 0, 0))
                her_komand.output(screen)
                if her_komand.resurs['еда'] > 0:
                    name.output()
                net.output()
                p.display.flip()#Обновление окна
                clock.tick(60)
        her_komand.izm_param_hp(lst)
    faza = 1
    return faza

def neg_sob(faza, screen, clock, her_komand):
    sobitia = []
    with open('Сюжет/события.txt') as f:
        s = f.readline()
        while s != '':
            s = s.split('*')
            s[-1] = s[-1][:-1]
            sobitia.append(s)
            s = f.readline()
    sob = randrange(0, len(sobitia))
    sobit = sobitia[sob]
    count = 0
    for i in range(len(sobit)):
        f1 = p.font.Font(None, 32)
        text1 = f1.render(sobit[i], True, (100, 100, 100))
        screen.blit(text1, (100, 100 + (count * 50)))
        count += 1
    f = None
    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                sys.exit()
            if event.type == p.MOUSEBUTTONDOWN:
                f = True
        if f:
            break
        screen.fill((0, 0, 0))
        her_komand.output(screen)
        
        count = 0
        for i in range(len(sobit)):
            f1 = p.font.Font(None, 32)
            text1 = f1.render(sobit[i], True, (100, 100, 100))
            screen.blit(text1, (100, 100 + (count * 50)))
            count += 1
        p.display.flip()#Обновление окна
        clock.tick(60)
    data = sobit[-1].lower()
    if ('золото' in data) or ('еда' in data) or ('слава' in data) or ('опыт' in data) or ('ужас' in data):
        her_komand.izm_param(data)
    elif ('проведите встречу' in data):
        heroi = her_komand.heroi
        lst = data.split()
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
        her_hp = bou(heroi, [vrag], screen, clock)
        #print(her_hp)
        her_komand.izm_param_hp(her_hp)
        #print(her_komand.eda, her_komand.zoloto, her_komand.opit, her_komand.slava)
        her_komand.nach_nagrada(nagrada, ur)
        #print(2)
    faza = 2
    return 2

def noch(screen, clock, her_komand, name):
    print(name)
    faza = 0
    #her_komand.izm_param_hp([['Эрдан', 10], ['Торн',50], ['Эрдан1',30], ['Эрдан2',70], ['Эрдан3',5]])
    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                sys.exit()
            if event.type == p.MOUSEBUTTONDOWN:
                if faza == 0:
                    l = perehod_faz(faza, screen, clock)
                    faza = otdih(her_komand, faza, screen, clock)
                if faza == 1:
                    l = perehod_faz(faza, screen, clock)
                    faza = neg_sob(faza, screen, clock, her_komand)
                if faza == 2:
                    l = perehod_faz(faza, screen, clock)
                    faza = son(faza, screen, clock, her_komand, name)
                #return 10
                break
        if faza == 3:
            l = perehod_faz(faza, screen, clock)
            return 6
            break
        screen.fill((0, 0, 0))
        
        her_komand.output(screen)
        p.display.flip()#Обновление окна
        clock.tick(60)
            
