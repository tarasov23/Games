import pygame as p

class Text_loc():
    def __init__(self, screen, text, x, y):
        self.screen = screen
        self.text = text
        self.x = x
        self.y = y
        
    def output(self):
        for i in range(len(self.text)):
            f1 = p.font.Font(None, 32)
            text1 = f1.render(self.text[i] , True, (180, 0, 0))
            self.screen.blit(text1, (self.x, (self.y + i * 30)))

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
        else:
            self.cvet = (180, 0, 0)
        
    def nagatie(self, cord_mish):
        if ((cord_mish[0] > self.x) and (cord_mish[0] < (self.x + 800))) and ((cord_mish[1] > self.y) and (cord_mish[1] < (self.y + 40))):
            return self.name
        else:
            return False
