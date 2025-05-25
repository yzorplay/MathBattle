from pygame import *
import math
import random
wx = 700
wy = 700
window = display.set_mode((wx, wy))
display.set_caption('=0w0=')
state = 0 # 0 - противостояние, 1 - дедматч, 2 - командный
color = (255, 255, 255)
window.fill(color)
font.init()



f = font.Font(None, 36)

class Numbers():
    def __init__(self, num, x = wx/2, y = wy/2, weapon = None, delay = 50):
        self.num = num
        self.x = x
        self.y = y
        self.weapon = weapon
        self.delay = delay

    def blit(self):
        text1 = f.render(self.num, True, (0, 0, 0))
        window.blit(text1, (self.x, self.y))

    def battle(self):
        if self.weapon == None:
            self.x += (1 if self.x < oper.x else -1 if self.x > oper.x else 0)
            self.y += (1 if self.y < oper.y else -1 if self.y > oper.y else 0)
            
            if abs(self.x - oper.x) <= 2 and abs(self.y - oper.y) <= 2:
                self.weapon = oper._type
                oper.dead = True
                self.num += oper._type
        
        else:
            self.x += (1 if self.x < num2.x else -1 if self.x > num2.x else 0)
            self.y += (1 if self.y < num2.y else -1 if self.y > num2.y else 0)

            if abs(self.x - num2.x) <= 2 and abs(self.y - num2.y) <= 2:
                if self.delay <= 0:
                    print(int(num2.num))
                    num2.num = str(int(num2.num) - 1)
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




num1 = Numbers("1", wx/3)
num2 = Numbers("3", wx/2)

oper = Operators("-", wx//4, wy/6)


FPS = 60
clock = time.Clock()
game = True
while game:
    window.fill(color)
    num1.blit()
    num1.battle()

    num2.blit()

    if oper.dead != True:
        oper.blit()

    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(FPS)
    display.update()