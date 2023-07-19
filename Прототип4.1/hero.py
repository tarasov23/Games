import pygame as p
from os import listdir
from random import randrange
from Naviki import Naviki

#Naviki = Naviki()

class Hero:
    def __init__(self, screen, x, y, name, hp, koloda, sila, magia, brona):
        self.screen = screen
        self.sost = 'ожидание'
        self.name = name
        self.mana = 0
        self.max_mana = 12
        #self.tec_mana = 0
        self.vosst = 1
        self.hp = hp
        self.max_hp = hp
        self.shit = 0
        self.sila_magia = {'сила':sila, 'магия':magia}
        self.izn_sila_magia = {'сила':sila, 'магия':magia}
        self.brona = brona
        self.animatik = {'ожидание': [], 'оборона': []}
        self.animatik_atk = {}
        for an in self.animatik:
            self.animatik[an] = listdir('image/герои/' + self.name + '/' + an)
            self.animatik[an].sort()
        
        self.image = p.image.load('image/герои/' + self.name + '/' + self.sost + '/' + '1.png') #найти файл
        self.rect = self.image.get_rect() #загрузить его как прямоугольник
        self.screen_rect = screen.get_rect()
        self.rect.centerx = x #картинка по центру экрана
        self.rect.centery = y #картинка снизу экрана
        self.mesta_kart = [[125, 875], [325, 875], [525, 875], [725, 875], [925, 875], [1125, 875], [1325, 875], [1525, 875]]
        self.anim = 0
        self.koloda = koloda
        self.koloda1 = []
        self.time = 0
        self.shit_time = 0
        self.reg_time = 0
        self.regen = self.max_hp
        for i in self.koloda:
            for j in range(self.koloda[i][-1]):
                self.koloda1.append(self.koloda[i][:-1])
        for k in self.koloda1:
            n = k[0]
            self.animatik_atk[n] = listdir('image/герои/' + self.name + '/атака/' + n)
            self.animatik_atk[n].sort()
        self.koloda = []
        #print(self.koloda1)
    
    def uvel_param(self, name, vel_uv, time):
        #print(self.sila_magia[name])
        self.time = time
        self.sila_magia[name] += int(vel_uv * self.sila_magia[name])
        #print(self.sila_magia[name])
    
    def izm_time(self):
        self.time -= 1
        self.shit_time -= 1
        self.reg_time -= 1
        #print(self.sila_magia, self.time)
        if self.time == 0:
            self.time = 0
            self.sila_magia = self.izn_sila_magia
        if self.shit_time == 0:
            self.shit_time = 0
            self.shit = 0
        if self.reg_time > 0:
            self.hp += self.regen
            if self.hp > self.max_hp:
                self.hp = self.max_hp
        if self.reg_time == 0:
            self.rergen = self.max_hp
            self.reg_time = 0
            #print(self.sila_magia)
        
    '''
    def izn_par(self):
        self.sila_magia = self.izn_sila_magia
    '''
    def ataka(self, name_at):
        self.sost = 'атака'
        self.anim += 0.3
        if self.anim > len(self.animatik_atk[name_at]):# если счетчик больше кольчества кадров в анимации
            self.anim = 0
            #self.sost = 'ожидание'
            return True
        self.image = p.image.load('image/герои/' + self.name + '/атака/' + name_at + '/' + self.animatik_atk[name_at][int(self.anim)])
        
        self.screen.blit(self.image, self.rect)
        f1 = p.font.Font(None, 32)
        text1 = f1.render(str(self.hp), True, (180, 0, 0))
        self.screen.blit(text1, (self.rect.centerx - 70, self.rect.centery - 50))
        f2 = p.font.Font(None, 32)
        text2 = f1.render(str(self.shit), True, (2,56,255))
        self.screen.blit(text2, (self.rect.centerx - 30, self.rect.centery - 50))
        f3 = p.font.Font(None, 32)
        text3 = f3.render(str(self.mana), True, (255,138,0))
        self.screen.blit(text3, (self.rect.centerx, self.rect.centery - 50))
    
    def oborona(self):
        self.sost = 'оборона'
        self.anim += 0.05
        if self.anim > len(self.animatik[self.sost]):# если счетчик больше кольчества кадров в анимации
            self.anim = 0
            #self.sost = 'ожидание'
            #return True
        self.image = p.image.load('image/герои/' + self.name + '/оборона/' + self.animatik[self.sost][int(self.anim)])
        
        self.screen.blit(self.image, self.rect)
        f1 = p.font.Font(None, 32)
        text1 = f1.render(str(self.hp), True, (180, 0, 0))
        self.screen.blit(text1, (self.rect.centerx - 70, self.rect.centery - 50))
        f2 = p.font.Font(None, 32)
        text2 = f1.render(str(self.shit), True, (2,56,255))
        self.screen.blit(text2, (self.rect.centerx - 30, self.rect.centery - 50))
        f3 = p.font.Font(None, 32)
        text3 = f3.render(str(self.mana), True, (255,138,0))
        self.screen.blit(text3, (self.rect.centerx, self.rect.centery - 50))
        
    def output(self):
        self.sost = 'ожидание'
        self.anim += 0.05
        if self.anim > len(self.animatik[self.sost]):
            self.anim = 0
        self.image = p.image.load('image/герои/' + self.name + '/ожидание/' + self.animatik[self.sost][int(self.anim)]) # обращение к папке 
        self.screen.blit(self.image, self.rect)
        
        self.screen.blit(self.image, self.rect)
        f1 = p.font.Font(None, 32)
        text1 = f1.render(str(self.hp), True, (180, 0, 0))
        self.screen.blit(text1, (self.rect.centerx - 70, self.rect.centery - 50))
        f2 = p.font.Font(None, 32)
        text2 = f1.render(str(self.shit), True, (2,56,255))
        self.screen.blit(text2, (self.rect.centerx - 30, self.rect.centery - 50))
        f3 = p.font.Font(None, 32)
        text3 = f3.render(str(self.mana), True, (255,138,0))
        self.screen.blit(text3, (self.rect.centerx, self.rect.centery - 50))
    
    def karti_geroa(self):
        for i in range(8):
            name = self.koloda1[i][0]
            parametr = self.koloda1[i][1]
            tip_urona = self.koloda1[i][2]
            tip_karti = self.koloda1[i][3]
            modif = self.koloda1[i][4]
            kol_udarov = self.koloda1[i][5]
            stoim = self.koloda1[i][6]
            coords = self.mesta_kart[i]
            karta = Karta(name, parametr, tip_urona, tip_karti, modif, kol_udarov, stoim, coords, self.screen, self.sila_magia[parametr])
            self.koloda.append(karta)
        self.koloda1 = self.koloda
        #print(self.koloda)
        
    
    def pokaz_kart(self, cord_mish):
        if (cord_mish[0] > self.rect[0]) and (cord_mish[0] < (self.rect[0] + self.rect[2])) and (cord_mish[1] > self.rect[1]) and (cord_mish[1] < (self.rect[1] + self.rect[3])):
            #print(self.koloda)
            return self.koloda
            
    def vibor_sous(self, cord_mish):
        if (cord_mish[0] > self.rect[0]) and (cord_mish[0] < (self.rect[0] + self.rect[2])) and (cord_mish[1] > self.rect[1]) and (cord_mish[1] < (self.rect[1] + self.rect[3])):
            return True
        else:
            return False

    def priem_urona(self, uron, tip):
        uron = int(uron * self.brona[tip])
        if self.shit != 0:
            if uron <= self.shit:
                self.shit -= uron
            else:
                uron -= self.shit
                self.shit = 0
                self.hp -= int(uron * self.brona[tip])
        else:
            self.hp -= int(uron * self.brona[tip])
            
    def vosst_mana(self):
        self.mana += self.vosst
        if self.mana > self.max_mana:
            self.mana = self.max_mana
        #self.tec_mana += self.vosst
    
    def snatie_shita(self):
        self.shit = 0


class Karta:
    def __init__(self, name, parametr, tip_urona, tip_karti, modif, kol_udarov, stoim, coords, screen, param):
        self.naviki = Naviki()
        self.screen = screen
        self.name = name
        self.parametr = parametr
        self.tip_urona = tip_urona
        self.tip_karti = tip_karti
        self.modif = modif
        self.kol_udarov = kol_udarov
        self.stoim = stoim
        self.image = p.image.load('image/карты/Эрдан/Удар.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = coords[0] #картинка по центру экрана
        self.rect.centery = coords[1] #картинка снизу экрана
        self.data = False
        self.param = param
        self.nav = Naviki()
        self.y = coords[1]
        self.y1 = coords[1] - 20
        if self.tip_karti == 'атака':
            self.lst = [self.name, self.parametr, self.param * self.modif, self.tip_urona, self.tip_karti, self.stoim, self.kol_udarov]
        elif self.tip_karti == 'навык':
            self.lst = self.nav[self.name]
    
    def rozigrish(self, cord_mish, mana):
        if self.tip_karti == 'навык':
            self.stoim = self.naviki[self.name][3]
        if (cord_mish[0] > self.rect[0]) and (cord_mish[0] < (self.rect[0] + self.rect[2])) and (cord_mish[1] > self.rect[1]) and (cord_mish[1] < (self.rect[1] + self.rect[3])):
            if self.stoim <= mana:
                mana -= self.stoim
                return [[self.name, self.parametr, self.tip_urona, self.tip_karti, self.modif, self.kol_udarov, self.stoim], mana]
            else:
                return False
        else:
            return False
    
    def navedenie(self, cord_mish):
        if (cord_mish[0] > self.rect[0]) and (cord_mish[0] < (self.rect[0] + self.rect[2])) and (cord_mish[1] > self.rect[1]) and (cord_mish[1] < (self.rect[1] + self.rect[3])):
            #if self.data:
            self.data = True
            self.rect.centery = self.y1
        else:
            #if not self.data:
            self.data = False
            self.rect.centery = self.y
            
    def output(self):
        if self.data:
            for i in range(len(self.lst)):
                f1 = p.font.Font(None, 32)
                text1 = f1.render(str(self.lst[i]) , True, (180, 0, 0))
                self.screen.blit(text1, (1000, (100 + i * 30)))
        self.screen.blit(self.image, self.rect)
    
    
class Vrag:
    def __init__(self, screen, x, y, num, hp, name, ataki, sila, magia, bron):
        self.screen = screen
        self.name = name
        self.ataki = ataki
        self.sila = sila
        self.magia = magia
        self.sost = 'ожидание'
        self.brona = bron
        self.animatik = {'атака': [], 'ожидание': [], 'оборона': []}
        for an in self.animatik:
            self.animatik[an] = listdir('image/противники/' + self.name + '/' + an)
            self.animatik[an].sort()
        #print(self.animatik)
        self.image = p.image.load('image/противники/' + self.name + '/' + self.sost + '/Медведь1.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.uron = 0
        self.anim = 0
        self.num = num
        self.hp = hp
        self.aktiv = True
        self.data_inf = False
        
    def oborona(self):
        #self.sost = 'оборона'
        self.anim += 0.05
        if self.anim > len(self.animatik[self.sost]):# если счетчик больше кольчества кадров в анимации
            self.anim = 0
            return True
        self.image = p.image.load('image/противники/' + self.name + '/оборона/' + self.animatik['оборона'][int(self.anim)])
        
        self.screen.blit(self.image, self.rect)
        f1 = p.font.Font(None, 32)
        text1 = f1.render(self.num + ' ' + str(self.hp) , True, (180, 0, 0))
        self.screen.blit(text1, (self.rect.centerx - 50, self.rect.centery - 75))
        
    def ataka(self):
        #self.sost = 'атака'
        self.anim += 0.05
        if self.anim > len(self.animatik[self.sost]):# если счетчик больше кольчества кадров в анимации
            self.anim = 0
            return True
        self.image = p.image.load('image/противники/' + self.name + '/атака/' + self.animatik['атака'][int(self.anim)])
        
        self.screen.blit(self.image, self.rect)
        f1 = p.font.Font(None, 32)
        text1 = f1.render(self.num + ' ' + str(self.hp) , True, (180, 0, 0))
        self.screen.blit(text1, (self.rect.centerx - 50, self.rect.centery - 75))
        
    def output(self):
        self.anim += 0.05
        if self.anim > len(self.animatik[self.sost]):# если счетчик больше кольчества кадров в анимации
            self.anim = 0
            self.sost = 'ожидание'
        self.image = p.image.load('image/противники/' + self.name + '/' + self.sost + '/' + self.animatik[self.sost][int(self.anim)]) # обращение к папке 
        
        self.screen.blit(self.image, self.rect)
        f1 = p.font.Font(None, 32)
        text1 = f1.render(self.num + ' ' + str(self.hp) , True, (180, 0, 0))
        self.screen.blit(text1, (self.rect.centerx - 50, self.rect.centery - 75))
        count = 0
        if self.data_inf:
            lst = [self.name, self.sila, self.magia]
            lst1 = self.brona
            for dat in range(len(lst)):
                f7 = p.font.Font(None, 32)
                text7 = f7.render(str(lst[dat]), True, (180, 0, 0))
                self.screen.blit(text7, (900, 200 + dat * 50))
                count += 1
            for i in lst1:
                f8 = p.font.Font(None, 32)
                text8 = f8.render(i + ':' + str(lst1[i]), True, (180, 0, 0))
                self.screen.blit(text8, (900, 200 + count *50))
                count += 1
        
    def navedenie_na_vraga(self, cord_mish):
        if (cord_mish[0] > self.rect[0]) and (cord_mish[0] < (self.rect[0] + self.rect[2])) and (cord_mish[1] > self.rect[1]) and (cord_mish[1] < (self.rect[1] + self.rect[3])):
            '''
            lst = [self.name, self.sila, self.magia, self.brona]
            for dat in range(len(lst)):
                f7 = p.font.Font(None, 32)
                text7 = f7.render(str(lst[i]), True, (180, 0, 0))
                self.screen.blit(text7, (200, 900 + i * 50))
            '''
            self.data_inf = True
        else:
            #pass
            self.data_inf = False
    '''
    def data_vrag(self):
        lst = [self.name, self.sila, self.magia, self.brona]
        for dat in range(len(lst)):
            f7 = p.font.Font(None, 32)
            text7 = f7.render(str(lst[i]), True, (180, 0, 0))
            self.screen.blit(text7, (200, 900 + i * 50))
    '''
    def vibor_vrag(self, cord_mish):
        if (cord_mish[0] > self.rect[0]) and (cord_mish[0] < (self.rect[0] + self.rect[2])) and (cord_mish[1] > self.rect[1]) and (cord_mish[1] < (self.rect[1] + self.rect[3])):
            return True
        else:
            return False
        
    def priem_urona(self, uron, tip):
        self.hp -= int(uron * self.brona[tip])
    
    def vibor_ataki(self):
        at = randrange(0, len(self.ataki))
        param = self.ataki[str(at)]
        naz = param[0]
        sila_magia = param[1]
        tip_urona = param[2]
        tip_karti = param[3]
        mod = param[4]
        kol_ud = param[5]
        if tip_karti == 'атака':# тип карты - атака
            if sila_magia == 'сила':
                self.uron = mod * self.sila
        return param + [self.uron]
    
class Boss:
    def __init__(self, x, y, screen):
        self.sost = 'ожидание'
        self.screen = screen
        self.animatik = {'атака': [], 'ожидание': [], 'оборона': []}
        self.image = p.image.load('image/боссы/первый_герой/' + self.sost + '/0.png')
        for an in self.animatik:
            self.animatik[an] = listdir('image/боссы/первый_герой/'+ an)
            self.animatik[an].sort()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.anim = 0
        
    def output(self):
        self.anim += 0.1
        if self.anim > len(self.animatik[self.sost]):# если счетчик больше кольчества кадров в анимации
            self.anim = 0
        self.image = p.image.load('image/боссы/первый_герой/' + self.sost + '/' + self.animatik[self.sost][int(self.anim)])
        self.screen.blit(self.image, self.rect)

class Ramka():
    def __init__(self, screen, x, y):
        self.screen = screen
        self.image = p.image.load('image/эффекты/рамка.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
    def output(self):
        self.screen.blit(self.image, self.rect)
    
'''
class Spravka():
    def __init__(self, screen, text):
        self.text = text.split('*')
        self.screen = screen
    
    def output(self):
        f1 = p.font.Font(None, 36)
        text1 = f1.render(self.text[0], True, (180, 0, 0))
        self.screen.blit(text1, (1200, 100))
'''
'''
class Knopka_isp():
    def __init__(self, x, y, screen, karta):
        self.karta = karta
        self.x = x
        self.y = y
        self.screen = screen
        self.flag = False

    def output(self):
        f1 = p.font.Font(None, 40)
        text1 = f1.render('Разыграть', True, (180, 0, 0))
        self.screen.blit(text1, (self.x, self.y))
    
    def ispolzovanie(self, cord_mish):
        if ((cord_mish[0] > self.x) and (cord_mish[0] < (self.x + 160))) and ((cord_mish[1] > self.y) and (cord_mish[1] < (self.y + 40))) and not(self.flag):
            self.flag = True
            return [self.flag, self.karta.tip, self.karta.uron]
        else:
            self.flag = False
            return [self.flag, '', 0]
'''
#class Count:
    
    
