#Стадии игры:
#   1) Стартовый диалог
#   2) Бой с врагами на уровне
#   3) Диалог перед битвой с боссом
#   4) Бой с боссом
#   5) Диалог после битвы с боссом
#Этапы стадий 2 и 4:
#   1) Выбор карт
#   2) Выбор атаки врагов
#   3) Анимация розыгрыша карт
#   4) Анимация атак врагов

import pygame as p
import sys
from hero import Hero, Vrag, Boss, Ramka # Karta, Vrag, Spravka, Knopka_isp
from random import randrange
from Karta import Karta
from Brona import Brona
from Naviki import Naviki
from Ataki_vragov import ataki_vragov
from komanda import Komanda

Karta = Karta()
Brona = Brona()
Naviki = Naviki()
ataki_vragov = ataki_vragov()

def pomosh(inf_her, cel, screen, heroi, vragi):
    p.display.flip()
    her = inf_her[0]
    nazv = inf_her[1]
    param = Naviki[nazv]
    #print(param)
    tip = param[0]
    sila_magia = param[1]
    mnog = param[2]
    stoim = param[3]
    f1 = False
    
    while True:
        screen.fill((0, 0, 0))
        if not f1:
            f1 = her.ataka(nazv)
        else:
            her.output()
        
        for hero in heroi:
            if hero != her:
                hero.output() #Отрисовка героев
        
        for vr in vragi:
            vr.output()
        if f1:
            break
        p.display.flip() 
    
    if tip == 'регенерация':
        cel.regen *= mnog
        cel.reg_time = 3
    if tip == 'восстановление':
        cel.hp += her.sila_magia[sila_magia] * mnog
        if cel.hp > cel.max_hp:
            cel.hp = cel.max_hp
    if tip == 'щит':
        cel.shit += her.sila_magia[sila_magia] * mnog
        cel.shit_time = 3
    if tip == 'усиление':
        #print(stoim)
        #print(cel.sila_magia)
        time = 3
        cel.uvel_param(sila_magia, mnog, time)
        #print(cel.sila_magia)
    if tip == 'мана':
        cel.mana += cel.sila_magia[sila_magia] * mnog
        if cel.mana > cel.max_mana:
            cel.mana = cel.max_mana
    her.mana -= stoim
        

def otr(inf_her, vrag, screen, vragi, heroi):#отрисовка атаки героя и обороны противника
    sm = 0
    #print(inf_her)
    her = inf_her[0]
    name_at = inf_her[1]
    tip_urona = inf_her[3]
    izn_uron = her.sila_magia[inf_her[2]]
    mod = inf_her[5]
    kol_ud = inf_her[6]
    stoim = inf_her[7]
    uron = izn_uron * mod * kol_ud
    f12 = p.font.Font(None, 32)
    text12 = f12.render(str(uron) , True, (180, 0, 0))
    screen.blit(text12, vrag.rect.topleft)
    f1 = False
    f2 = False
    while True:
        screen.fill((0, 0, 0))
        if not f1:
            #for i in range(kol_ud):
            f1 = her.ataka(name_at)
        else:
            her.output()
        
        for hero in heroi:
            if hero != her:
                hero.output() #Отрисовка героев
        
        if not f2:
            f2 = vrag.oborona()
        else:
            vrag.output()
        
        for vr in vragi:
            if vr != vrag:
                vr.output()
        screen.blit(text12, vrag.rect.topleft)
        p.display.flip()
        if f1 and f2:
            break
    screen.fill((0, 0, 0))
    for hero in heroi:
        hero.output() #Отрисовка героев
    for vr in vragi:
        vr.output()
    p.display.flip()
    vrag.priem_urona(uron, tip_urona)
    her.mana -= stoim

def otr2(inf_vrag, her, screen, heroi, vragi): #отрисовка обороны героев и атак противника
    vrag = inf_vrag[0]
    tip_urona = inf_vrag[3]
    uron = inf_vrag[7] * inf_vrag[6]
    f12 = p.font.Font(None, 32)
    text12 = f12.render(str(uron) , True, (180, 0, 0))
    screen.blit(text12, her.rect.topright)
    for i in range(200):
        screen.fill((0, 0, 0))
        for vr in vragi:
            if vr != vrag:
                vr.output()
        f = vrag.ataka()
        her.oborona()
        for hero in heroi:
            if hero != her:
                hero.output()
        screen.blit(text12, her.rect.topright)
        p.display.flip()
        if f:
            break
    screen.fill((0, 0, 0))
    for hero in heroi:
        hero.output() #Отрисовка героев
    for vr in vragi:
        vr.output()
    p.display.flip()
    her.priem_urona(uron, tip_urona)
         
def vibor_vraga(screen, heroi, vragi): #выбор цели атаки
    ramki = []
    for vr in vragi:
        ramka = Ramka(screen, vr.rect.centerx, vr.rect.centery)
        ramki.append(ramka)
    f = False
    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                sys.exit()
            if event.type == p.MOUSEBUTTONDOWN:
                a = event.pos
                for vr in vragi:
                    f = vr.vibor_vrag(a)
                    if f:
                        v = vr
                        break
        if f:
            break
        screen.fill((0, 0, 0))
        for hero in heroi:
            hero.output() #Отрисовка героев
        for vr in vragi:
            vr.output()
        for ram in ramki:
            ram.output()
        p.display.flip()
    return v

def vibor_sousn(screen, heroi, vragi): #выбор цели навыка
    ramki = []
    for her in heroi:
        ramka = Ramka(screen, her.rect.centerx, her.rect.centery)
        ramki.append(ramka)
    f = False
    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                sys.exit()
            if event.type == p.MOUSEBUTTONDOWN:
                a = event.pos
                for her in heroi:
                    f = her.vibor_sous(a)
                    if f:
                        h = her
                        break
        if f:
            break
        screen.fill((0, 0, 0))
        for hero in heroi:
            hero.output() #Отрисовка героев
        for vr in vragi:
            vr.output()
        for ram in ramki:
            ram.output()
        p.display.flip()
    return h

def pokaz(kar, mana, screen, heroi, vragi): #показ карт персонажа
    f = False
    #print(kar, mana, screen, heroi, vragi)
    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                sys.exit()
            if event.type == p.MOUSEMOTION:
                a = event.pos
                for k in kar:
                    k.navedenie(a)
            if event.type == p.MOUSEBUTTONDOWN:
                a = event.pos
                for k in kar:
                    f = k.rozigrish(a, mana) #проверка на нажатие на карту
                    if f:
                        break
        if f:
            break
        screen.fill((0, 0, 0))
        for k in kar: 
            k.output() # отрисовка карт
        for hero in heroi:
            hero.output() #Отрисовка героев
        for vr in vragi:
            vr.output() #Отрисовка противников
        p.display.flip()
    return f

def vibor_kart(ochered_kart, screen, heroi, vragi): #фаза выбора карт персонажа
    f = False
    sdelawshie_hod = []
    ataka_i_cel = []
    count = 0
    count_g = 0
    for pers in heroi:
        if pers.mana < 0:
            count_g += 1
        if count_g == len(heroi):
            f = True
    while True:
        '''
        for pers in heroi:
            if pers.mana < 0:
                count_g += 1
        if count_g == len(heroi):
            f = True
        '''
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                sys.exit()
            if event.type == p.MOUSEMOTION:
                a = event.pos
                for vr in vragi:
                    vr.navedenie_na_vraga(a)
            if event.type == p.MOUSEBUTTONDOWN:
                a = event.pos
                for pers in heroi:
                    #if pers not in sdelawshie_hod:
                    if pers.mana >= 0:
                    #if count != len(heroi) * 2:
                        #pers.karti_geroa()
                        kar = pers.pokaz_kart(a) #выбор карты
                        #print(kar)
                        if kar:
                            #stoim = int(kar[6].stoim)
                            #pers.mana = pokaz(kar, pers.mana)[1]
                            #print(pers)
                            inf_kart = [pers] + pokaz(kar, pers.mana, screen, heroi, vragi)[0]
                            #print(inf_kart)
                            #print(inf_kart)
                            #sdelawshie_hod.append(pers)
                            #count += 1
                            #print(inf_kart)
                            ataka_i_cel.append(inf_kart)
                cel_ataki = ''
                if ataka_i_cel != []:
                    if ataka_i_cel[0][4] == 'атака':
                        #print(1)
                        cel_ataki = vibor_vraga(screen, heroi, vragi)
                    elif ataka_i_cel[0][4] == 'навык':
                        #print('навык')
                        cel_ataki = vibor_sousn(screen, heroi, vragi)
                    ataka_i_cel.append(cel_ataki)
                    ochered_kart.append(ataka_i_cel)
                ataka_i_cel = []
                #print(ochered_kart)
        if len(ochered_kart) == 3:#len(heroi):
            her1, her2, her3 = ochered_kart[0][0][0], ochered_kart[1][0][0], ochered_kart[2][0][0]
            #if her1 == her2 and her2 == her3:
                #print(1)
            f = True
        if f:
            break
        screen.fill((0, 0, 0))
        for hero in heroi:
            hero.output() #Отрисовка героев
        for vr in vragi:
            vr.output()
        p.display.flip()
    return [1, ochered_kart]

def rozigrish_kart(ochered_kart, vragi, heroi, screen): #фаза розыгрыша
    for i in range(len(ochered_kart)):
        atakuysh = ochered_kart[i][0]
        zashish = ochered_kart[i][1]
        if atakuysh[0] in heroi: #атаки героев
            if zashish in heroi:
                pomosh(atakuysh, zashish, screen, heroi, vragi)
            else:
                screen.fill((0, 0, 0))
                for hero in heroi:
                    hero.output() #Отрисовка героев
                for vr in vragi:
                    vr.output()
                p.display.flip()
                otr(atakuysh, zashish, screen, vragi, heroi)
                vragi = smerti_vragov(vragi)
    for vr in vragi:
        if len(heroi) != 1:
            her = heroi[randrange(0, len(heroi))]
        else:
            her = heroi[0]
        otr2([vr] + vr.vibor_ataki(), her, screen, heroi, vragi)
        heroi = smerti_geroev(heroi)
        
    ochered_kart = []
    return [2, ochered_kart, vragi, heroi]
    
def smerti(geroi, vragi, screen):
    k = len(vragi)
    i = 0
    f = False
    if vragi == []:
        f = True
    if geroi == []:
        f = True
    return [0, geroi, vragi, f]

def smerti_vragov(vragi):
    k = len(vragi)
    i = 0
    while i < k or vragi != []:
        if i == k or vragi == []:
            break
        if vragi[i].hp <= 0:
            del vragi[i]
            i = 0
            k -= 1
            if k == 0:
                k = 1
        else:
            i += 1
    return vragi
        
def smerti_geroev(geroi):
    k = len(geroi)
    i = 0
    while i < k or geroi != []:
        if i == k or geroi == []:
            break
        if geroi[i].hp <= 0:
            del geroi[i]
            i = 0
            k -= 1
            if k == 0:
                k = 1
        else:
            i += 1
    return geroi

#def bou():
def bou(hero, protivniki, screen, clock):
    #p.init()
    #p.font.init()
    #screen = p.display.set_mode((1900, 1000))
    #clock = p.time.Clock()
    coord_ger = [[350, 200], [350, 400], [350, 600], [150, 300], [150, 500]]
    heroi = []
    heroi_na_missii = []
    for i in range(len(hero)):
        data = hero[i]
        #print(data)
        name = data[0]
        hp = data[1]
        sila = data[2]
        magia = data[3]
        brona = Brona[data[4]]
        her = Hero(screen, coord_ger[i][0], coord_ger[i][1], name, hp, Karta[name], sila, magia, brona)
        heroi.append(her)
        heroi_na_missii.append(her)
    for ger in heroi:
        ger.karti_geroa()

    bron = {'дробящий': 0.1, 'колющий': 1, 'рубящий': 0.1, 'ядовитый': 1, 'ледяной': 1.9, 'огненный': 1.9, 'грозовой': 1, 'темный': 1, 'сияющий': 1}
    mesto_vraga = [[650, 200], [650, 400], [650, 600], [850, 300], [850, 500]]
    
    vragi = []
    for i in range(len(protivniki)):
        data = protivniki[i]
        name = data[0]
        hp = data[1]
        ataki = ataki_vragov[name]
        sila = data[2]
        magia = data[3]
        brona = {'дробящий': float(data[4]), 'колющий': float(data[5]), 'рубящий': float(data[6]), 'ядовитый': float(data[7]), 'ледяной': float(data[8]), 'огненный': float(data[10]), 'грозовой': float(data[11]), 'темный': float(data[12]), 'сияющий': float(data[13])}
        vrag = Vrag(screen, mesto_vraga[i][0], mesto_vraga[i][1], str(i + 1), hp, name, ataki, sila, magia, brona)
        vragi.append(vrag)
    ochered_kart = []

    #Основной цикл игры
    faza = 0
    ok_igr = False
    a = 0
    #while True:
        #if a == 0:
    while True:
        if faza == 0:
            faza, ochered_kart =  vibor_kart(ochered_kart, screen, heroi, vragi)
        elif faza == 1:
            faza, ochered_kart, vragi, heroi = rozigrish_kart(ochered_kart, vragi, heroi, screen)
        elif faza == 2:
            faza, heroi, vragi, ok_igr = smerti(heroi, vragi, screen)
            if ok_igr:
                her_hp = []
                for her in heroi:
                    her_hp.append([her.name, her.hp])
                    #print(her_hp)
                return her_hp
                #print('Игра окончена')
                break
            for her in heroi:
                her.vosst_mana()
                her.izm_time()
                #print(her.sila_magia)
                
        clock.tick(60)
            
