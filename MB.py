from pygame import *
import math
import random
wx = 700
wy = 700
window = display.set_mode((wx, wy))
display.set_caption('=0w0=')
state = 0 # 0 - противостояние, 1 - дедматч, 2 - командный
enterD = False
final = False
color = (255, 255, 255)
window.fill(color)
font.init()

AllOpers = list()
AllNubers = list()



f = font.Font(None, 36)

class Numbers():
    def __init__(self, num, x = wx/2, y = wy/2, weapon = None, delay = 50, enemy = None):
        self.num = num
        self.x = x
        self.y = y
        self.weapon = weapon
        self.delay = delay
        self.enemy = enemy

    def blit(self):
        text1 = f.render(self.num, True, (0, 0, 0))
        window.blit(text1, (self.x, self.y))

    def battle(self):
        global enterD, final
        self.enemy = AllNubers[0]
        if self.enemy.num == self.num:
            self.enemy = AllNubers[random.randint(0, len(AllNubers)-1)]
            if enterD != True:
                enterD = True
            else:
                final = True
        enterD = False





        if self.weapon == None and AllOpers[0] != None:
            self.x += (1 if self.x < AllOpers[-1].x else -1 if self.x > AllOpers[-1].x else 0)
            self.y += (1 if self.y < AllOpers[-1].y else -1 if self.y > AllOpers[-1].y else 0)
            
            if abs(self.x - AllOpers[-1].x) <= 2 and abs(self.y - AllOpers[-1].y) <= 2:
                self.weapon = oper._type
                oper.dead = True
                AllOpers.
                self.num += oper._type
        
        else:
            self.x += (1 if self.x < self.enemy.x else -1 if self.x > self.enemy.x else 0)
            self.y += (1 if self.y < self.enemy.y else -1 if self.y > self.enemy.y else 0)

            if abs(self.x - self.enemy.x) <= 2 and abs(self.y - self.enemy.y) <= 2:
                if self.delay <= 0:
                    print(int(self.enemy.num))
                    self.enemy.num = str(int(self.enemy.num) - 1)
                    self.delay = 50
                else:
                    self.delay -= 1



        
class Operators():
    def __init__(self, _type, x, y, dead = False):
        self.x = x
        self.y = y
        self._type = _type
        self.dead = dead
    def blit(self):
        text1 = f.render(self._type, True, (0, 0, 0))
        window.blit(text1, (self.x, self.y))




AllNubers = []

num = Numbers("1", wx/3)
AllNubers.append(num)

num = Numbers("2", wx/2, wy/3)
AllNubers.append(num)





#num2 = Numbers("3", wx/2)

oper = Operators("-", wx//4, wy/6)
AllOpers.append(oper)


FPS = 60
clock = time.Clock()
game = True
while game:
    window.fill(color)
    for number in AllNubers:
        number.blit()

    for number in AllNubers:
        number.battle()


    #self.enemy.blit()

    if oper.dead != True:
        oper.blit()

    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(FPS)
    display.update()