import pygame as p
#from komnata import Komnata

class Level():
    def __init__(self, screen, glava):
        self.screen = screen
        p.sprite.Sprite.__init__(self)
        self.glava = glava
        #self.comnat = p.sprite.Group()
        
    def setup_level(self, level_data, dlina, shirina, sdvig_horizontal, sdvig_vertikal, heroi, lok):
        self.lokac = p.sprite.Group()
        self.komand = p.sprite.GroupSingle()
        self.dlina = dlina
        self.shirina = shirina
        self.sdvig_horizontal =  sdvig_horizontal
        self.sdvig_vertikal = sdvig_vertikal
        self.hero_lok = lok
        #self.komanda = ''
        for i in range(len(level_data)):
            for j in range(len(level_data[i])):
                if level_data[i][j] != '*':
                    lok = Lokacia(level_data[i][j], (j * self.dlina) + sdvig_horizontal, (i * self.shirina) + sdvig_vertikal, self.dlina, self.shirina, self.glava)
                    self.lokac.add(lok)
                    if level_data[i][j] == self.hero_lok:
                        kom = Komanda(((j * self.dlina) + sdvig_horizontal), ((i * self.shirina) + sdvig_vertikal), self.dlina, self.shirina, heroi)
                        self.komand.add(kom)
                    
    def output(self):
        self.lokac.draw(self.screen)
        self.komand.draw(self.screen)
    '''
    def sdvig(self, speed_x, speed_y):
        self.lokac.update(speed_x, speed_y)
        self.komand.update(speed_x, speed_y)
    '''
    def peremeshenie(self, coord_mish):
        cm_x = coord_mish[0]
        cm_y = coord_mish[1]
        komand = self.komand.sprite
        k_x, k_y = komand.rect.topleft
        for kom in self.lokac:
            tl_x = kom.rect.topleft[0]
            tl_y = kom.rect.topleft[1]
            if (cm_x > tl_x and cm_x < (tl_x + self.dlina)) and (cm_y > tl_y and cm_y < (tl_y + self.shirina)):
                if (k_x == (tl_x - self.dlina) and k_y == tl_y) or (k_x == tl_x and k_y == (tl_y + self.shirina)) or (k_x == (tl_x + self.dlina) and k_y == tl_y) or (k_x == tl_x and k_y == (tl_y - self.shirina)):
                    for komanda in self.komand:
                        komanda.perem(tl_x, tl_y)
                    return kom
    
    def level_lok(self, cord_x, cord_y):
        for kom in self.lokac:
            tl_x = kom.rect.topleft[0]
            tl_y = kom.rect.topleft[1]
            if cord_x == tl_x and cord_y == tl_y:
                return kom.name
                break
    def level_lok1(self, cord_x, cord_y):
        for kom in self.lokac:
            tl_x = kom.rect.topleft[0]
            tl_y = kom.rect.topleft[1]
            if (cord_x < tl_x + self.dlina) and (cord_x > tl_x) and (cord_y < tl_y + self.shirina) and (cord_y > tl_y):
                return kom.name
                break
                
class Komanda(p.sprite.Sprite):
    def __init__(self, x, y, dlina, shirina, heroi):
        self.heroi = heroi
        p.sprite.Sprite.__init__(self)
        self.dlina = dlina
        self.shirina = shirina
        #self.image = p.Surface((dlina, shirina))
        self.image = p.image.load('Сюжет/команда.png')
        self.rect = self.image.get_rect(topleft = (x, y))
        #self.image.fill((250, 250, 250))
    
    def perem(self, x, y):
        self.rect.topleft = (x, y)
    
    def update(self, speed_x, speed_y):
        self.rect.centerx += speed_x
        self.rect.centery += speed_y
        #self.rect.topleft = (x, y)

class Her_komand():
    def __init__(self, heroi, eda, zoloto, opit, slava, ugas):
        self.her_max_hp = {}
        self.her_hp = {}
        self.heroi = heroi[0]
        for i in range(len(self.heroi)):
            #print(self.heroi[i])
            self.her_max_hp[self.heroi[i][0]] = self.heroi[i][1]
            self.her_hp[self.heroi[i][0]] = self.heroi[i][1]
        self.eda = eda
        self.zoloto = zoloto
        self.opit = opit
        self.slava = slava
        self.ugas = ugas
        self.resurs = {'еда': self.eda, 'золото': self.zoloto, 'опыт':self.opit, 'слава':self.slava, 'ужас':self.ugas}
    
    def izm_param_hp(self, her_hp):
        for i in range(len(self.heroi)):
            her = self.heroi[i]
            for i in range(len(her_hp)):
                if her_hp[i][0] in her:
                    her[1] = her_hp[i][1]
                    self.her_hp[her[0]] = her_hp[i][1]
                    if self.her_hp[her[0]] > self.her_max_hp[her[0]]:
                        self.her_hp[her[0]] = self.her_max_hp[her[0]]
                        her[1] = self.her_max_hp[her[0]]
                    #print(her[1], her_hp[i][1])
                    break
    
    def izm_param(self, nov_param):
        nov_param = nov_param.lower().split()
        par_izm = nov_param[0]
        znak_inm = nov_param[1]
        znach_izm = int(nov_param[2][0])
        if znak_inm == '+':
            self.resurs[par_izm] += znach_izm
        elif znak_inm == '-':
            self.resurs[par_izm] -= znach_izm
            if self.resurs[par_izm] < 0:
                self.resurs[par_izm] = 0
        
    def nach_nagrada(self, nagrada, ur):
        for i in range(len(nagrada)):
            nagr = nagrada[i]
            nagr = nagr.split()
            self.resurs[nagr[1]] += (int(nagr[0]) * ur)

    def output(self, screen):
        count = 0
        cvet1 = (0,131,0) #зелёный
        cvet2 = (255,231,0) #жёлтый
        cvet3 = (255,0,0) #красный
        for i in self.resurs:
            f1 = p.font.Font(None, 32)
            if i != 'ужас' and self.resurs[i] < 3:
                text1 = f1.render(i + ':' + str(self.resurs[i]), True, cvet3)
            if i != 'ужас' and self.resurs[i] < 6 and self.resurs[i] >= 3:
                text1 = f1.render(i + ':' + str(self.resurs[i]), True, cvet2)
            if i != 'ужас' and self.resurs[i] >= 6:
                text1 = f1.render(i + ':' + str(self.resurs[i]), True, cvet1)
            if i == 'ужас' and self.resurs[i] <= 3:
                text1 = f1.render(i + ':' + str(self.resurs[i]), True, cvet1)
            if i == 'ужас' and self.resurs[i] <= 6 and self.resurs[i] > 3:
                text1 = f1.render(i + ':' + str(self.resurs[i]), True, cvet2)
            if i == 'ужас' and self.resurs[i] > 6:
                text1 = f1.render(i + ':' + str(self.resurs[i]), True, cvet3)
            screen.blit(text1, (1700, 200 + (count * 50)))
            count += 1
        count = 0
        for i in self.her_max_hp:
            cvet1 = (0,131,0) #зелёный
            cvet2 = (255,231,0) #жёлтый
            cvet3 = (255,0,0) #красный
            f1 = p.font.Font(None, 32)
            if self.her_hp[i] >= int(self.her_max_hp[i] * 0.7):
                text1 = f1.render(i + ':' + str(self.her_hp[i]), True, cvet1)
            if self.her_hp[i] <= int(self.her_max_hp[i] * 0.7) and self.her_hp[i] >= int(self.her_max_hp[i] * 0.4):
                text1 = f1.render(i + ':' + str(self.her_hp[i]), True, cvet2)
            if self.her_hp[i] <= int(self.her_max_hp[i] * 0.4):
                text1 = f1.render(i + ':' + str(self.her_hp[i]), True, cvet3)
            screen.blit(text1, (1700, 600 + (count * 50)))
            count += 1

class Lokacia(p.sprite.Sprite):
     def __init__(self, name, x, y, dlina, shirina, glava):
        p.sprite.Sprite.__init__(self)
        self.name = name
        #self.image = p.Surface((dlina, shirina))
        self.glava = glava
        self.image = p.image.load('Сюжет/глава' + self.glava + '/локации/' + self.name + '/' + self.name + '.png')
        self.rect = self.image.get_rect(topleft = (x, y))
        #self.image.fill((50, 50, 50))
        
     def update(self, speed_x, speed_y):
        self.rect.centerx += speed_x
        self.rect.centery += speed_y


class Knopka():
    def __init__(self, screen, name, text, x, y):
        self.screen = screen
        self.name = name
        self.text = text
        self.cvet = (180, 0, 0)
        self.x = x
        self.y = y

    def output(self):
        f1 = p.font.Font(None, 32)
        text1 = f1.render(self.text, True, self.cvet)
        self.screen.blit(text1, (self.x, self.y))
        
    def navedenie(self, cord_mish):
        if ((cord_mish[0] > self.x) and (cord_mish[0] < (self.x + 800))) and ((cord_mish[1] > self.y) and (cord_mish[1] < (self.y + 40))):
            self.cvet = (0, 0, 180)
            return True
        else:
            self.cvet = (180, 0, 0)
            return False
        
    def nagatie(self, cord_mish):
        if ((cord_mish[0] > self.x) and (cord_mish[0] < (self.x + 800))) and ((cord_mish[1] > self.y) and (cord_mish[1] < (self.y + 40))):
            #print(self.name)
            return self.name
        else:
            return False
