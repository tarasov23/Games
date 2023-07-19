import pygame as p
import sys
from komanda import Level
from level import level_data, lev
from komanda import Level, Knopka
from lokacii import issledovanie, h_komand
from withual1 import bou
from noch import noch

glava = input()
p.init()
p.font.init()
screen = p.display.set_mode((1900, 1000))
#screen.image = p.image.load('image/боссы/первый_герой/ожидание/Первый_герой.png')
clock = p.time.Clock()
#fon = p.image.load('image/боссы/первый_герой/ожидание/Первый_герой.png')

missii = {}
with open('Сюжет/глава' + glava + '/локации/Миссии') as f:
    s = f.readline()
    while s != '':
        s = s.split(':')
        missii[s[0]] = s[1][:-1]
        s = f.readline()

level_data, dlina, shirina, sdvig_horizontalm, sdvig_vertikal, lok = level_data(glava)
heroi = lev()
level = Level(screen, glava)
level.setup_level(level_data, dlina, shirina, sdvig_horizontalm, sdvig_vertikal, heroi, lok)
schot_deis = 6

iss_lok = Knopka(screen, '0', 'Исследовать', 1600, 100)
f1 = p.font.Font(None, 32)
text1 = f1.render(str(schot_deis), True, (43,255,1))
screen.blit(text1, (1700, 460))

missia = 'Исследовать_Дозор'
tex_miss = Knopka(screen, missia, 'Текущая миссия', 1600, 500)
f2 = p.font.Font(None, 32)
text2 = f2.render(missii[missia], True, (100,255,100))
screen.blit(text2, (10, 10))
gl_ok = False

zav_hod = Knopka(screen, '0', 'Завершить день', 1600, 500)

with open('Сюжет/глава' + glava + '/Начало') as f:
    s = f.readline()
    while s != '':
        fl1 = False
        s = s.split('*')
        s[-1] = s[-1][:-1]
        while True:
            for event in p.event.get():
                if event.type == p.QUIT:
                    p.quit()
                    sys.exit()
                if event.type == p.MOUSEBUTTONDOWN:
                    fl1 = True
            if fl1:
                break
            screen.fill((0, 0, 0))
            for st in range(len(s)):
                f9 = p.font.Font(None, 32)
                text9 = f9.render(s[st], True, (255, 255, 255))
                screen.blit(text9, (100, 100 + st * 50))
            p.display.flip()#Обновление окна
            clock.tick(60)
        s = f.readline()
l = l1 = False
while True:
    #l = l1 = False
    if schot_deis > 0:
        f1 = p.font.Font(None, 32)
        text1 = f1.render(str(schot_deis), True, (43,255,1))
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                sys.exit()
            
            if event.type == p.MOUSEMOTION:
                a = event.pos
                iss_lok.navedenie(a)
                l = tex_miss.nagatie(a)
                l1 = level.level_lok1(a[0], a[1])
            
            if event.type == p.MOUSEBUTTONDOWN:
                a = event.pos
                if schot_deis > 0:
                    issl = iss_lok.nagatie(a)
                    kom = level.peremeshenie(a)
                    if issl:
                        schot_deis -= 1
                        koman = level.komand.sprite
                        x, y = koman.rect.topleft
                        name = level.level_lok(x, y)
                        missia, gl_ok = issledovanie(screen, clock, name, glava, missia)
                if kom:
                    schot_deis -= 1
                    pass

            '''
            keys = p.key.get_pressed() #считывание нажатия клавиши
            if keys[p.K_d]:
                speed_x = 50
                speed_y = 0
                level.sdvig(speed_x, speed_y)
            if keys[p.K_a]:
                speed_x = -50
                speed_y = 0
                level.sdvig(speed_x, speed_y)
            if keys[p.K_w]:
                speed_x = 0
                speed_y = -50
                level.sdvig(speed_x, speed_y)
            if keys[p.K_s]:
                speed_x = 0
                speed_y = 50
                level.sdvig(speed_x, speed_y)
            '''
        her_komand = h_komand()
        screen.fill((0, 0, 0))
        
        if l:
            f2 = p.font.Font(None, 32)
            text2 = f2.render(missii[missia], True, (100,255,100))
            screen.blit(text2, (10, 10))
        if l1:
            f10 = p.font.Font(None, 32)
            text10 = f10.render(str(l1), True, (100,255,100))
            screen.blit(text10, (10, 10))
        
        iss_lok.output()
        tex_miss.output()
        screen.blit(text1, (1700, 460))
        her_komand.output(screen)
        #screen.blit(fon, (0, 0))
        level.output()
        p.display.flip()#Обновление окна
        clock.tick(60)
        if gl_ok:
            break
    else:
        koman = level.komand.sprite
        x, y = koman.rect.topleft
        name = level.level_lok(x, y)
        while True:
            for event in p.event.get():
                if event.type == p.QUIT:
                    p.quit()
                    sys.exit()
                if event.type == p.MOUSEBUTTONDOWN:
                    a = event.pos
                    f = zav_hod.nagatie(a)
                    if f:
                        schot_deis = noch(screen, clock, her_komand, name)
                        break
            if f:
                break
            screen.fill((0, 0, 0))
            level.output()
            her_komand.output(screen)
            zav_hod.output()
            p.display.flip()#Обновление окна
            clock.tick(60)

                    
        #print('день окончен')
        #break
        #noch(screen, clock, her_komand)
        #schot_deis = noch(screen, clock, her_komand)
