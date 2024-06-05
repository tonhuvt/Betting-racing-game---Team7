import pygame, sys, random, os
from DinoRun import *
from pygame.locals import *
import time
sys.path.insert(0, '../../')

WINDOWWIDTH = 1280
WINDOWHEIGHT = 720

# PHan backgroud menu
BG_MENU_IMG = pygame.image.load('img/backgroundMenu.png')
BG_PLAY_IMG = pygame.image.load("img/BackGroundPlay.png")
BG_MENU_SetAV = pygame.image.load("img/GiaoDienChonSetNV.png")
BG_Betting = pygame.image.load("img/GiaoDienBetting.png")



b = [] # winning car

a=[] # car order

# Hieu ung nut
NutPlay = pygame.image.load("img/NutPlay1.png")
NutHelp = pygame.image.load("img/NutHelp.png")
NutMiniGame = pygame.image.load("img/mini.png")
NutShop = pygame.image.load("img/shop.png")

#Am thanh
menu_sound = pygame.mixer.Sound("sound/Road Tripzzz - Ofshane (2).mp3")
menu_sound.set_volume(0.25)
minigame_sound = pygame.mixer.Sound("sound/Cuckoo Clock - Quincas Moreira.mp3")
minigame_sound.set_volume(0.25)
over_sound = pygame.mixer.Sound("sound/lose.mp3")
over_sound.set_volume(0.25)
winner_sound = pygame.mixer.Sound("sound/clap.mp3")
winner_sound.set_volume(0.25)
game_sound = pygame.mixer.Sound("sound/race3.mp3")
game_sound.set_volume(0.25)
count_sound = pygame.mixer.Sound("sound/count.mp3")
count_sound.set_volume(0.25)
pygame.init()



FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.flip()
pygame.display.set_caption('BETTING RACING GAME - Team7')


RED=(255,0,0)
GREEN=(0,255,0)

X_MARGIN = 80
LANEWIDTH = 60

CARWIDTH = 0
CARHEIGHT = 0
CARSPEED = 3

class Car1():
    def __init__(self):
        self.width = CARWIDTH
        self.height = CARHEIGHT
        self.x = 0
        self.y = 312
        self.speed = CARSPEED
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill((255, 255, 255))
    def draw(self):
        DISPLAYSURF.blit(car_1, (int(self.x), int(self.y)))
        global pos_now1
        pos_now1 = self.x
        if (pos_now1 > 1181):
            a.append(1)
    def update(self):
        global pos_now1
        pos_now1 = self.x
        if self.x <= 1180:
            if self.x +6>1180:
                self.x += 8                  #bùa 0: tăng tốc
            global vt_1
            vt_1 = 0
            change = random.randint(1, 5)
            if ((self.x > 100 * change) and (self.x < 100 * change + 5)): 
                self.x = 400                  #bùa 1: đưa xe về vị trí x=400
            elif ((self.x > 105 * change) and (self.x < 105 * change + 5)):
                pass                          #bùa 2: choáng
            elif ((self.x > 125 * change) and (self.x < 125 * change + 100)): 
                self.x -= random.randint(0,3) #bùa 3: lùi
            else:
                self.x += random.randint(0,3) #bùa 4: tiến

        else:
            vt_1= 1
            self.x = 1181

class Car2():
    def __init__(self):
        self.width = CARWIDTH
        self.height = CARHEIGHT
        self.x = 0
        self.y = 388
        self.speed = CARSPEED
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill((255, 255, 255))
    def draw(self):
        DISPLAYSURF.blit(car_2, (int(self.x), int(self.y)))
        global pos_now2
        pos_now2 = self.x
        if (pos_now2 > 1181):
            a.append(2)
    def update(self):
        global pos_now2
        pos_now2 = self.x
        if self.x <= 1180:
            if self.x +6>1180:
                self.x += 8
            global vt_2
            vt_2 = 0
            change = random.randint(1, 5)
            if ((self.x > 100 * change) and (self.x < 100 * change + 5)):
                self.x = 400
            elif ((self.x > 105 * change) and (self.x < 105 * change + 5)):
                pass
            elif ((self.x > 125 * change) and (self.x < 125 * change + 100)):
                self.x -= random.randint(0, 3)
            else:
                self.x += random.randint(0, 3)

        else:
            vt_2 = 2
            self.x = 1181

class Car3():
    def __init__(self):
        self.width = CARWIDTH
        self.height = CARHEIGHT
        self.x = 0
        self.y = 479
        self.speed = CARSPEED
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill((255, 255, 255))
    def draw(self):
        DISPLAYSURF.blit(car_3, (int(self.x), int(self.y)))
        global pos_now3
        pos_now3 = self.x
        if (pos_now3 > 1181):
            a.append(3)
    def update(self):
        global pos_now3
        pos_now3 = self.x
        if self.x <= 1180:
            if self.x +6>1180:
                self.x += 8
            global vt_3
            vt_3 = 0
            change = random.randint(1, 5)
            if ((self.x > 100 * change) and (self.x < 100 * change + 5)):
                self.x = 400
            elif ((self.x > 105 * change) and (self.x < 105 * change + 5)):
                pass
            elif ((self.x > 125 * change) and (self.x < 125 * change + 100)):
                self.x -= random.randint(0, 3)
            else:
                self.x += random.randint(0, 3)

        else:
            vt_3 = 3
            self.x = 1181


class Car4():
    def __init__(self):
        self.width = CARWIDTH
        self.height = CARHEIGHT
        self.x = 0
        self.y = 564
        self.speed = CARSPEED
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill((255, 255, 255))
    def draw(self):
        DISPLAYSURF.blit(car_4, (int(self.x), int(self.y)))
        global pos_now4
        pos_now4 = self.x
        if (pos_now4 > 1181):
            a.append(4)
    def update(self):
        global pos_now4
        pos_now4 = self.x

        if self.x <= 1180:
            if self.x +6>1180:
                self.x += 8
            global vt_4
            vt_4 = 0
            change = random.randint(1, 5)
            if ((self.x > 100 * change) and (self.x < 100 * change + 5)):
                self.x = 400
            elif ((self.x > 105 * change) and (self.x < 105 * change + 5)):
                pass
            elif ((self.x > 125 * change) and (self.x < 125 * change + 100)):
                self.x -= random.randint(0, 3)
            else:
                self.x += random.randint(0, 3)

        else:
            vt_4 = 4
            self.x = 1181
            
class Car5():
    def __init__(self):
        self.width = CARWIDTH
        self.height = CARHEIGHT
        self.x = 0
        self.y = 646
        self.speed = CARSPEED
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill((255, 255, 255))
    def draw(self):
        DISPLAYSURF.blit(car_5, (int(self.x), int(self.y)))
        global pos_now5
        pos_now5=self.x
        if (pos_now5>1181):
            a.append(5)
    def update(self):
        if self.x <= 1180:
            if self.x +6>1180:
                self.x += 8
            global vt_5
            vt_5 = 0
            change = random.randint(1, 5)
            if self.x==1280:
                self.x+=2
            if ((self.x > 100 * change) and (self.x < 100 * change + 5)):
                self.x = 400
            elif ((self.x > 105 * change) and (self.x < 105 * change + 5)):
                pass
            elif ((self.x > 125 * change) and (self.x < 125 * change + 100)):
                self.x -= random.randint(0, 3)
            else:
                self.x += random.randint(0, 3)

        else:
            vt_5 = 5
            self.x = 1181

def gamePlay(bg, car1, car2, car3, car4, car5):
    tmp = 10
    global  coin, tienCuoc
    car1.__init__()
    car2.__init__()
    car3.__init__()
    car4.__init__()
    car5.__init__()
    bg.__init__()
    menu_sound.stop()
    count_sound.play(-1)
    bg.count_321()
    count_sound.stop()
    game_sound.play(-1)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        bg.draw()
        car1.draw()
        car1.update()
        car2.draw()
        car2.update()
        car3.draw()
        car3.update()
        car4.draw()
        car4.update()
        car5.draw()
        car5.update()
        print(chon_xe)
        print(a)
        if (vt_1==1 and vt_2==2 and vt_3== 3 and vt_4==4 and vt_5==5):

            if (chon_xe[0]== a[0]):
                win_bg = pygame.image.load("img\giaodienWin.png")
                DISPLAYSURF.blit(win_bg, (0, 0))
                if ( tmp == 10):
                    coin[0] += int(tienCuoc[0]) * 10
                    tmp += 10
                game_sound.stop()
                winner_sound.play(1)
            else:
                over_bg = pygame.image.load("img\giaodienOver.png")
                DISPLAYSURF.blit(over_bg, (0, 0))
                if (tmp == 10 ):
                    coin[0] -= int(tienCuoc[0])
                    tmp += 10
                game_sound.stop()
                over_sound.play(1)
            file_2 = open(coin_username_info, 'w')
            file_2.write(str(coin[0]))
            file_2.close()
            for i in range(5):
                if i == 0:
                    DISPLAYSURF.blit(b[a[i] - 1], (551, 245))
                if i == 1:
                    DISPLAYSURF.blit(b[a[i] - 1], (406, 340))
                if i == 2:
                    DISPLAYSURF.blit(b[a[i] - 1], (690, 377))
                if i == 3:
                    DISPLAYSURF.blit(b[a[i] - 1], (274, 426))
                if i == 4:
                    DISPLAYSURF.blit(b[a[i] - 1], (836, 460))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    a.clear()
                    b.clear()
                    winner_sound.stop()
                    over_sound.stop()
                    menu_sound.stop()
                    MeNu()
        pygame.display.update()
        fpsClock.tick(FPS)

def start_the_game():
    bg = Back_ground()
    car1 = Car1()
    car2 = Car2()
    car3 = Car3()
    car4 = Car4()
    car5 = Car5()
    gamePlay(bg, car1, car2, car3, car4, car5)

def drawCoin():  
    draw_text(str(coin[0]) + "$", "font/monofonto.ttf", 38, (255, 255, 255), SCREEN_WIDTH - 70, 170, "topright")


def draw_Race(race_img): 
    DISPLAYSURF.blit(race_img, 0, 0)


#Các giao diện
def HamGiaoDienSetNV():
    while True:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (event.button == 1) & (mouse_x >= 1173) & (mouse_x <= 1259) & (mouse_y >= 32) & (mouse_y <= 112):
                    return
                if (event.button == 1) & (mouse_x >= 1032) & (mouse_x <= 1090) & (mouse_y >= 270) & (mouse_y <= 328):
                    HamGiaoDienBetting(1)
                if (event.button == 1) & (mouse_x >= 1032) & (mouse_x <= 1090) & (mouse_y >= 417) & (mouse_y <= 478):
                    HamGiaoDienBetting(3)
                if (event.button == 1) & (mouse_x >= 1032) & (mouse_x <= 1090) & (mouse_y >= 566) & (mouse_y <= 624):
                    HamGiaoDienBetting(5)

        DISPLAYSURF.blit(BG_MENU_SetAV, (0, 0))

        # Hieu ung nut
        if (mouse_x >= 1173) & (mouse_x <= 1259) & (mouse_y >= 32) & (mouse_y <= 112):
            DISPLAYSURF.blit(pygame.image.load("img/NutBack.png"), (0, 0))
        if (mouse_x >= 1032) & (mouse_x <= 1090) & (mouse_y >= 270) & (mouse_y <= 328):
            DISPLAYSURF.blit(pygame.image.load("img/NutTickSet1.png"), (0, 0))
        if (mouse_x >= 1032) & (mouse_x <= 1090) & (mouse_y >= 417) & (mouse_y <= 478):
            DISPLAYSURF.blit(pygame.image.load("img/NutTickSet3.png"), (0, 0))
        if (mouse_x >= 1032) & (mouse_x <= 1090) & (mouse_y >= 566) & (mouse_y <= 624):
            DISPLAYSURF.blit(pygame.image.load("img/NutTickSet5.png"), (0, 0))
        pygame.display.update()


FONT = pygame.font.Font("font/monofonto.ttf", 32)
tienCuoc = [0]
class InputBox:
    def __init__(self, x, y, w, h, text= '0' ):
        global tienCuoc
        self.rect = pygame.Rect(x, y, w, h)
        self.color = pygame.Color((0, 0, 0))
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = pygame.Color((255, 255, 255)) if self.active else pygame.Color((0, 0, 0))
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        DISPLAYSURF.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(DISPLAYSURF, self.color, self.rect, 2)


def HamGiaoDienBetting(set):
    global  chon_xe
    chon_xe = [1]
    global car_1, car_2, car_3, car_4, car_5, tienCuoc
    if (set == 1):
        car_1 = pygame.image.load("img/Set Xe/set1/16.png")
        car_2 = pygame.image.load("img/Set Xe/set1/17.png")
        car_3 = pygame.image.load("img/Set Xe/set1/18.png")
        car_4 = pygame.image.load("img/Set Xe/set1/19.png")
        car_5 = pygame.image.load("img/Set Xe/set1/20.png")
    elif (set == 3):
        car_1 = pygame.image.load("img/Set Xe/set3/10.png")
        car_2 = pygame.image.load("img/Set Xe/set3/7.png")
        car_3 = pygame.image.load("img/Set Xe/set3/6.png")
        car_4 = pygame.image.load("img/Set Xe/set3/8.png")
        car_5 = pygame.image.load("img/Set Xe/set3/9.png")
    elif (set == 5):
        car_1 = pygame.image.load("img/Set Xe/set5/21.png")
        car_2 = pygame.image.load("img/Set Xe/set5/22.png")
        car_3 = pygame.image.load("img/Set Xe/set5/23.png")
        car_4 = pygame.image.load("img/Set Xe/set5/24.png")
        car_5 = pygame.image.load("img/Set Xe/set5/25.png")

    b.append(car_1)
    b.append(car_2)
    b.append(car_3)
    b.append(car_4)
    b.append(car_5)

    Nut1 = False
    Nut2 = False
    Nut3 = False
    Nut4 = False
    Nut5 = False
    clock = pygame.time.Clock()
    input_box = InputBox(680, 458, 140, 42) 
    while True:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        DISPLAYSURF.blit(BG_Betting, (0, 0))
        draw_text(" Enter your stake: ", "font/monofonto.ttf", 38, (255, 255, 255), 680, 453, "topright")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            input_box.handle_event(event)
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                global choose_1, choose_2, choose_3, choose_4, choose_5
                if (event.button == 1) & (mouse_x >= 1173) & (mouse_x <= 1259) & (mouse_y >= 32) & (mouse_y <= 112):
                    return
                # Chon nut 1
                if (event.button == 1) & (mouse_x >= 334) & (mouse_x <= 396) & (mouse_y >= 347) & (mouse_y <= 407):
                    Nut1 = True
                    Nut2 = False
                    Nut3 = False
                    Nut4 = False
                    Nut5 = False
                    chon_xe[0] = 1
                # Chon nut 2
                if (event.button == 1) & (mouse_x >= 471) & (mouse_x <= 532) & (mouse_y >= 347) & (mouse_y <= 407):
                    Nut1 = False
                    Nut2 = True
                    Nut3 = False
                    Nut4 = False
                    Nut5 = False
                    chon_xe[0] = 2
                # chon nut 3
                if (event.button == 1) & (mouse_x >= 606) & (mouse_x <= 668) & (mouse_y >= 347) & (mouse_y <= 407):
                    Nut1 = False
                    Nut2 = False
                    Nut3 = True
                    Nut4 = False
                    Nut5 = False
                    chon_xe[0] = 3
                # Chon nut 4
                if (event.button == 1) & (mouse_x >= 751) & (mouse_x <= 810) & (mouse_y >= 347) & (mouse_y <= 407):
                    Nut1 = False
                    Nut2 = False
                    Nut3 = False
                    Nut4 = True
                    Nut5 = False
                    chon_xe[0] = 4
                if (event.button == 1) & (mouse_x >= 888) & (mouse_x <= 950) & (mouse_y >= 347) & (mouse_y <= 407):
                    Nut1 = False
                    Nut2 = False
                    Nut3 = False
                    Nut4 = False
                    Nut5 = True
                    chon_xe[0] = 5
                if tienCuoc[0] == '':
                    print(tienCuoc[0])
                elif (int(tienCuoc[0]) <= int(coin[0])) & (int(tienCuoc[0]) > 0) & (event.button == 1) & (mouse_x >= 570) & (mouse_x <= 754) & (mouse_y >= 540) & (mouse_y <= 607):
                    start_the_game()

        # in set nhan vat ra
        if set == 1:
            DISPLAYSURF.blit(pygame.image.load("img/Set 1.png"), (0, 0))
        if set == 3:
            DISPLAYSURF.blit(pygame.image.load("img/Set 3.png"), (0, 0))
        if set == 5:
            DISPLAYSURF.blit(pygame.image.load("img/Set 5.png"), (0, 0))

        input_box.update()
        # Hieu ung chon
        if Nut1 == True:
            DISPLAYSURF.blit(pygame.image.load("img/NutTick1.png"), (0, 0))
        elif Nut2 == True:
            DISPLAYSURF.blit(pygame.image.load("img/NutTick2.png"), (0, 0))
        elif Nut3 == True:
            DISPLAYSURF.blit(pygame.image.load("img/NutTick3.png"), (0, 0))
        elif Nut4 == True:
            DISPLAYSURF.blit(pygame.image.load("img/NutTick4.png"), (0, 0))
        elif Nut5 == True:
            DISPLAYSURF.blit(pygame.image.load("img/NutTick5.png"), (0, 0))

        # Hieu ung nut
        if (mouse_x >= 1173) & (mouse_x <= 1259) & (mouse_y >= 32) & (mouse_y <= 112):
            DISPLAYSURF.blit(pygame.image.load("img/NutBack.png"), (0, 0))
        if (mouse_x >= 334) & (mouse_x <= 396) & (mouse_y >= 347) & (mouse_y <= 407):
            DISPLAYSURF.blit(pygame.image.load("img/NutTick1.png"), (0, 0))
        if (mouse_x >= 471) & (mouse_x <= 532) & (mouse_y >= 347) & (mouse_y <= 407):
            DISPLAYSURF.blit(pygame.image.load("img/NutTick2.png"), (0, 0))
        if (mouse_x >= 606) & (mouse_x <= 668) & (mouse_y >= 347) & (mouse_y <= 407):
            DISPLAYSURF.blit(pygame.image.load("img/NutTick3.png"), (0, 0))
        if (mouse_x >= 751) & (mouse_x <= 810) & (mouse_y >= 347) & (mouse_y <= 407):
            DISPLAYSURF.blit(pygame.image.load("img/NutTick4.png"), (0, 0))
        if (mouse_x >= 888) & (mouse_x <= 950) & (mouse_y >= 347) & (mouse_y <= 407):
            DISPLAYSURF.blit(pygame.image.load("img/NutTick5.png"), (0, 0))
        if (mouse_x >= 570) & (mouse_x <= 754) & (mouse_y >= 540) & (mouse_y <= 607):
            DISPLAYSURF.blit(pygame.image.load("img/NutStart.png"), (0, 0))

        input_box.draw(DISPLAYSURF)
        tienCuoc[0] = input_box.text
        drawCoin()
        pygame.display.flip()
        pygame.display.update()
        clock.tick(30)

class Back_ground():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.img = map
        
    def draw(self):
        DISPLAYSURF.blit(self.img, (int(self.x), int(self.y)))

    def count_321(self):
        count = 3
        while count >= 0:
            DISPLAYSURF.blit(self.img, (int(self.x), int(self.y)))
            if count == 0:
                message_display("GO!", 100, -70, (0, 255, 255), 1)
            elif count == 3:
                message_display(str(count), 100, -70, (255,0,0), 0.75)
            elif count == 2:
                message_display(str(count), 100, -70, (255, 255, 0), 0.75)
            elif count == 1:
                message_display(str(count), 100, -70, (0, 255, 0), 0.75)
            count -= 1
        fpsClock.tick(FPS)
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text, shift_x, shift_y, color, sleep_time):
    largeText = pygame.font.SysFont('comicsansms', 72, True)
    TextSurf, TextRect = text_objects(text, largeText, color)
    TextRect.center = ((WINDOWWIDTH / 2 - shift_x), (WINDOWHEIGHT / 2 - shift_y))
    DISPLAYSURF.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(sleep_time)


def HamGiaoDienHelp():
    while True:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Quay lại
                if (event.button == 1) & (mouse_x >= 1173) & (mouse_x <= 1259) & (mouse_y >= 32) & (mouse_y <= 112):
                    return
        DISPLAYSURF.blit(pygame.image.load("img/GiaodienHelp.png"), (0, 0))
        if (mouse_x >= 1173) & (mouse_x <= 1259) & (mouse_y >= 32) & (mouse_y <= 112):
            DISPLAYSURF.blit(pygame.image.load("img/NutBack.png"), (0, 0))
        pygame.display.update()


def HamGiaoDienShop():
    while True:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Quay lại
                if (event.button == 1) & (mouse_x >= 1173) & (mouse_x <= 1259) & (mouse_y >= 32) & (mouse_y <= 112):
                    return
        DISPLAYSURF.blit(pygame.image.load("img/GiaoDienShop.png"), (0, 0))
        if (mouse_x >= 1173) & (mouse_x <= 1259) & (mouse_y >= 32) & (mouse_y <= 112):
            DISPLAYSURF.blit(pygame.image.load("img/NutBack.png"), (0, 0))
        pygame.display.update()

def HamGiaoDienPlay():
    global map,car1,car2,car3,car4,car5
    while True:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (event.button == 1) & (mouse_x >= 1173) & (mouse_x <= 1259) & (mouse_y >= 32) & (mouse_y <= 112):
                    return
                if (event.button == 1) & (mouse_x >= 0) & (mouse_x <= 415) & (mouse_y >= 460) & (mouse_y <= 690):
                    map=pygame.image.load("img/Map1.png")
                    HamGiaoDienSetNV()
                if (event.button == 1) & (mouse_x >= 858) & (mouse_x <= 1280) & (mouse_y >= 151) & (mouse_y <= 392):
                    map=pygame.image.load("img/Map2.png")
                    HamGiaoDienSetNV()

        DISPLAYSURF.blit(BG_PLAY_IMG, (0, 0)) # Background sau khi ấn nút Play
        
        # Hiệu ứng nút Play
        if (mouse_x >= 1173) & (mouse_x <= 1259) & (mouse_y >= 32) & (mouse_y <= 112):
            DISPLAYSURF.blit(pygame.image.load("img/NutBack.png"), (0, 0))
        if (mouse_x >= 0) & (mouse_x <= 415) & (mouse_y >= 460) & (mouse_y <= 690):
            DISPLAYSURF.blit(pygame.image.load("img/NutChoseMap1.png"), (0, 0))
        if (mouse_x >= 858) & (mouse_x <= 1280) & (mouse_y >= 151) & (mouse_y <= 392):
            DISPLAYSURF.blit(pygame.image.load("img/NutChoseMap2.png"), (0, 0))
        pygame.display.update()

def MeNu():
    menu_sound.play(-1) 
    global coin
    while True:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (event.button == 1) & (coin[0] > 0) & (mouse_x >= 506) & (mouse_x <= 817) & (mouse_y >= 210) &( mouse_y <= 294): #vào play
                    HamGiaoDienPlay()
                if (event.button == 1) & (mouse_x >= 506) & (mouse_x <= 817) & (mouse_y >= 334) &( mouse_y <= 420):
                    HamGiaoDienShop()
                if (event.button == 1) & (coin[0] == 0) & (mouse_x >= 506) & (mouse_x <= 817) & (mouse_y >= 454) &( mouse_y <= 537):
                    print("MiniGame")
                    menu_sound.stop()
                    minigame_sound.play()
                    start_game(coin)
                    file_2 = open(coin_username_info, 'w')
                    file_2.write(str(coin[0]))
                    file_2.close()
                    minigame_sound.stop()
                    menu_sound.play(-1)
                if (event.button == 1) & (mouse_x >= 610) & (mouse_x <= 717) & (mouse_y >= 576) &( mouse_y <= 670):
                    HamGiaoDienHelp()

        DISPLAYSURF.blit(BG_MENU_IMG, (0, 0))
        drawCoin()

        # Hiệu ứng nút
        if (mouse_x >= 506) & (mouse_x <= 817) & (mouse_y >= 210) & (mouse_y <= 294):
            DISPLAYSURF.blit(NutPlay, (0, 0))
        if (mouse_x >= 506) & (mouse_x <= 817) & (mouse_y >= 334) & (mouse_y <= 420):
            DISPLAYSURF.blit(NutShop, (0, 0))
        if (mouse_x >= 506) & (mouse_x <= 817) & (mouse_y >= 454) & (mouse_y <= 537):
            DISPLAYSURF.blit(NutMiniGame, (0, 0))
        if (mouse_x >= 610) & (mouse_x <= 717) & (mouse_y >= 576) & (mouse_y <= 670):
            DISPLAYSURF.blit(NutHelp, (0, 0))

        pygame.display.update()

def main():
    MeNu()

from tkinter import *
import os


def delete2():
    screen3.destroy()


def delete3():
    screen4.destroy()


def delete4():
    screen5.destroy()


def login_sucess():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("150x100")
    Label(screen3, text="Login Sucess").pack()
    Button(screen3, text="OK", command=delete2).pack()


def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Success")
    screen4.geometry("150x100")
    Label(screen4, text="Password Error").pack()
    Button(screen4, text="OK", command=delete3).pack()


def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Success")
    screen5.geometry("150x100")
    Label(screen5, text="User Not Found").pack()
    Button(screen5, text="OK", command=delete4).pack()


def register_user():
    print("working")
    global username_info
    username_info = username.get()
    password_info = password.get()
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
    
    global coin_username_info
    coin_username_info =username_info+"_coin"
    file_1 = open(coin_username_info, "w")
    file_1.write(str(0))
    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registration Sucess", fg="green", font=("calibri", 11)).pack()


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        global  coin_username_info
        coin_username_info=username1+"_coin"
        if password1 in verify:
            global coin
            coin=[]
            file_1=open(coin_username_info,'r')
            n=file_1.read()
            coin.append(int(n))
            if __name__ == '__main__':
                main()
        else:
            password_not_recognised()

    else:
        user_not_found()


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username * ").pack()

    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password * ").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, height=1, command=register_user).pack()


def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text="Please enter details below to login").pack()
    Label(screen2, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text="Username * ").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password * ").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, height=1, command=login_verify).pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Account")
    Label(text="Account", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    screen.mainloop()


main_screen()

# By Team 7 - IS208.O21

