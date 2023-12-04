import pygame_menu, pygame, random, sys
from LoginSignup import *
#Khởi tạo các thứ
pygame.init()
pygame.display.set_caption("Race game")
clock = pygame.time.Clock()

#Âm thanh
VOLUME = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
VOLUME_INDEX = 4

#Kích thước màn hình (Do chưa có pygame_menu nên tạm thời bỏ qua)
WINDOW_SIZES = [pygame.display.get_desktop_sizes()[0]]
WINDOW_SIZE_INDEX = 0
screen = pygame.display.set_mode(WINDOW_SIZES[WINDOW_SIZE_INDEX], pygame.RESIZABLE)

#Kiểu chữ
KieuChu1 = pygame.font.SysFont('arial', 20, bold=True)
KieuChu2 = pygame.font.SysFont('arial', 40, bold=True)

#Chữ các thứ
Player_money = 0
scoreBoard = KieuChu2.render(f"Money: {Player_money}", False, (0, 255, 255))
scoreBoard_Box = scoreBoard.get_rect(center = (screen.get_width() * 0.13, screen.get_height() * 0.92))

#Ảnh các loại
Background = pygame.image.load('assets/background/background.png').convert_alpha()

map1 = pygame.image.load('assets/background/map1.png').convert_alpha()
map1 = pygame.transform.smoothscale(map1, pygame.display.get_desktop_sizes()[0])
map2 = pygame.image.load('assets/background/map2.png').convert_alpha()
map2 = pygame.transform.smoothscale(map1, pygame.display.get_desktop_sizes()[0])
map3 = pygame.image.load('assets/background/map3.png').convert_alpha()
map3 = pygame.transform.smoothscale(map1, pygame.display.get_desktop_sizes()[0])
map4 = pygame.image.load('assets/background/map4.png').convert_alpha()
map4 = pygame.transform.smoothscale(map1, pygame.display.get_desktop_sizes()[0])
map5 = pygame.image.load('assets/background/map5.png').convert_alpha()
map5 = pygame.transform.smoothscale(map1, pygame.display.get_desktop_sizes()[0])
MAPS = [map1, map2, map3, map4, map5]
MAP_INDEX = 1

#Các ảnh cần dùng đến
#1. Nhân vật (Đặt tên theo dạng Char#Map#_#)
Char1Map1 = ['assets/characters/Char1Map1_1.png', 'assets/characters/Char1Map1_2.png',
            'assets/characters/Char1Map1_3.png', 'assets/characters/Char1Map1_4.png']
Char2Map1 = ['assets/characters/Char2Map1_1.png', 'assets/characters/Char2Map1_2.png',
            'assets/characters/Char2Map1_3.png', 'assets/characters/Char2Map1_4.png']
Char3Map1 = ['assets/characters/Char3Map1_1.png', 'assets/characters/Char3Map1_2.png',
            'assets/characters/Char3Map1_3.png', 'assets/characters/Char3Map1_4.png']
Char4Map1 = ['assets/characters/Char4Map1_1.png', 'assets/characters/Char4Map1_2.png',
            'assets/characters/Char4Map1_3.png', 'assets/characters/Char4Map1_4.png']
Char5Map1 = ['assets/characters/Char5Map1_1.png', 'assets/characters/Char5Map1_2.png',
            'assets/characters/Char5Map1_3.png', 'assets/characters/Char5Map1_4.png']

#Nhân vật
CharsMap1 = [Char1Map1, Char2Map1, Char3Map1, Char4Map1, Char5Map1]
Speed = [2.5, 2.5, 2.5, 2.5, 2.5]

#Các nhân vật trong game
class player(pygame.sprite.Sprite):
    def __init__(self, speed, pos, number, image, map):
        super().__init__()
        self.speed = speed
        self.x = pos[0]
        self.y = pos[1]
        self.number = number
        self.run = True
        self.count_run = 0
        self.image= pygame.image.load(image).convert_alpha()
        self.rect= self.image.get_rect(midbottom = (self.x, self.y))
        self.count_run = 0
        self.map = map
    def animation(self):
        #Vẽ nhân vật
        if self.count_run >= 3:
            self.count_run = 0
        if self.map == 0:
            if self.number == 0:
                if self.run:
                    self.image = pygame.image.load(CharsMap1[0][int(self.count_run)]).convert_alpha()
                    self.count_run += 0.1
                else:
                    self.image = pygame.image.load(CharsMap1[0][int(self.count_run)]).convert_alpha()
            if self.number == 1:
                if self.run:
                    self.image = pygame.image.load(CharsMap1[1][int(self.count_run)]).convert_alpha()
                    self.count_run += 0.1
                else:
                    self.image = pygame.image.load(CharsMap1[1][int(self.count_run)]).convert_alpha()
            if self.number == 2:
                if self.run:
                    self.image = pygame.image.load(CharsMap1[2][int(self.count_run)]).convert_alpha()
                    self.count_run += 0.1
                else:
                    self.image = pygame.image.load(CharsMap1[2][int(self.count_run)]).convert_alpha()
            if self.number == 3:
                if self.run:
                    self.image = pygame.image.load(CharsMap1[3][int(self.count_run)]).convert_alpha()
                    self.count_run += 0.1
                else:
                    self.image = pygame.image.load(CharsMap1[3][int(self.count_run)]).convert_alpha()
            if self.number == 4:
                if self.run:
                    self.image = pygame.image.load(CharsMap1[4][int(self.count_run)]).convert_alpha()
                    self.count_run += 0.1
                else:
                    self.image = pygame.image.load(CharsMap1[4][int(self.count_run)]).convert_alpha()

    def move(self):
        if self.run:
            self.rect.x += self.speed

    def update(self):
        self.animation()
        self.move()

Char1 = pygame.sprite.GroupSingle()
Char1.add(player(speed = Speed[0], 
                 pos = (screen.get_width() * 0.1, screen.get_height() * 0.55), 
                 number = 0, 
                 image = CharsMap1[0][0], 
                 map = 0))
Char2 = pygame.sprite.GroupSingle()
Char2.add(player(speed = Speed[1], 
                 pos = (screen.get_width() * 0.1, screen.get_height() * 0.66), 
                 number = 1, 
                 image = CharsMap1[1][0], 
                 map = 0))
Char3 = pygame.sprite.GroupSingle()
Char3.add(player(speed = Speed[2], 
                 pos = (screen.get_width() * 0.1, screen.get_height() * 0.76), 
                 number = 2, 
                 image = CharsMap1[2][0], 
                 map = 0))
Char4 = pygame.sprite.GroupSingle()
Char4.add(player(speed = Speed[3], 
                 pos = (screen.get_width() * 0.1, screen.get_height() * 0.87), 
                 number = 3, 
                 image = CharsMap1[3][0], 
                 map = 0))
Char5 = pygame.sprite.GroupSingle()
Char5.add(player(speed = Speed[4], 
                 pos = (screen.get_width() * 0.1, screen.get_height() * 0.98), 
                 number = 4, 
                 image = CharsMap1[4][0], 
                 map = 0))

#Các đối tượng trong game
class IG_Object(pygame.sprite.Sprite):
    def __init__(self, name, pos, image):
        super().__init__()
        self.x = pos[0]
        self.y = pos[1]
        self.name = name
        if self.name == "LuckyBox":
            self.pic= pygame.image.load(image).convert_alpha()
            self.image = self.pic
            self.rect= self.image.get_rect(midbottom = (self.x, self.y))
        elif self.name == "ChuChay":
            self.pic = KieuChu1.render("THIS IS GROUP 12'S AMAZING RACE GAME!!!", False, (255, 102, 0))
            self.image = self.pic
            self.rect= self.image.get_rect(topleft = (self.x, self.y))
    def move(self):
        if self.name == "ChuChay":
            self.rect.x -= 2
            if self.rect.right <= 0:
                self.rect.x = screen.get_width()
    def update(self):
        if self.name == "ChuChay":
            self.move()

#Add object
IG_Objects = pygame.sprite.Group()
LuckyBox_Spawn = [0.2, 0.25, 0.3, 4.5, 4.5, 0.5, 0.55, 0.6, 0.6, 0.62, 0.65, 0.66, 0.7, 0.75, 0.75, 0.8, 0.8, 0.8] #Các biến để random vị trí lucky box
IG_Objects.add(IG_Object(name = 'LuckyBox',
                         pos = (screen.get_width() * random.choice(LuckyBox_Spawn),
                         screen.get_height() * 0.55),
                         image = 'assets/item/luckyBox.png'))
IG_Objects.add(IG_Object(name = 'LuckyBox', 
                         pos = (screen.get_width() * random.choice(LuckyBox_Spawn), 
                         screen.get_height() * 0.66), 
                         image = 'assets/item/luckyBox.png'))
IG_Objects.add(IG_Object(name = 'LuckyBox', 
                         pos = (screen.get_width() * random.choice(LuckyBox_Spawn), 
                         screen.get_height() * 0.76), 
                         image = 'assets/item/luckyBox.png'))
IG_Objects.add(IG_Object(name = 'LuckyBox', 
                         pos = (screen.get_width() * random.choice(LuckyBox_Spawn), 
                         screen.get_height() * 0.87), 
                         image = 'assets/item/luckyBox.png'))
IG_Objects.add(IG_Object(name = 'LuckyBox', 
                         pos = (screen.get_width() * random.choice(LuckyBox_Spawn), 
                         screen.get_height() * 0.98), 
                         image = 'assets/item/luckyBox.png'))
IG_Objects.add(IG_Object( name = 'ChuChay', pos = (screen.get_width(), 0), image = 'None'))

#Class nút
class Button():
	def __init__(self, image, pos, textIn, font, base_color, active_color):
		self.image = image
		self.x = pos[0]
		self.y = pos[1]
		self.font = font
		self.base_color, self.active_color = base_color, active_color
		self.textIn = textIn
		self.text = self.font.render(self.textIn, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x, self.y))
		self.text_rect = self.text.get_rect(center=(self.x, self.y))

	def update(self):
		screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def CheckClick(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def DoiMau(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.textIn, True, self.active_color)
		else:
			self.text = self.font.render(self.textIn, True, self.base_color)

#Cách xài class button
# 1. Khởi tạo nút
# button_surface = pygame.image.load("button.png")
# button = Button(button_surface, (400, 300), "Button", KieuChu1, "black", "white")
# 2. Check click
#     if event.type == pygame.MOUSEBUTTONDOWN:
#         button.CheckClick(pygame.mouse.get_pos())
# 3. Update button
# 	button.update()
# 	button.DoiMau(pygame.mouse.get_pos())