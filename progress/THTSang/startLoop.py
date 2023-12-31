import pygame
import sys

pygame.init()

# Kích thước cửa sổ ban đầu
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Resizable Pygame Window")

# Đường dẫn đến ảnh
image_path = "assets/background/background.png"

# Đọc ảnh
original_image = pygame.image.load(image_path).convert_alpha()

# Kích thước ảnh ban đầu
original_width, original_height = original_image.get_size()

# Tạo một bản sao của ảnh để scale
scaled_image = original_image.copy()

# Tạo một font để hiển thị kích thước cửa sổ
font = pygame.font.Font(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            # Cập nhật kích thước cửa sổ khi được resize
            width, height = event.size
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

            # Scale lại ảnh
            scaled_image = pygame.transform.smoothscale(original_image, (width // 2, height // 2))

    # Hiển thị ảnh và kích thước cửa sổ
    screen.fill((255, 255, 255))  # Màu nền trắng
    screen.blit(scaled_image, (width // 4, height // 4))

    # Hiển thị kích thước cửa sổ
    text = font.render(f"Window Size: {width} x {height}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()

# import pygame_menu, pygame, random, sys, time

# from datetime import datetime
# from LoginSignup import *
# from flappybird import minigame
# #Khởi tạo các thứ
# pygame.init()
# from money_bet import *
# pygame.display.set_caption("Race game")
# clock = pygame.time.Clock()
# random.seed(datetime.now().timestamp())


# money_bet_list = [200,500,1000]
# #Các biến cần dùng
# user_id = ''
# user_pwd = ''
# user_money = 0
# set_choice = 1
# choice = 0
# bet_money = 0

# # store 5 characters
# CHARACTERS = []
# LUCKYBOX = []
# GROUP = []
# rank = [] #List nhân vật khi thắng đc thêm vào
# winner = 0
# last = 0


# #Màn hình cài đặt âm lượng
# VOLUME = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
# VOLUME_INDEX = 4
# present_volume = VOLUME[VOLUME_INDEX]
# MenuSound = False
# gameSound = False
# #Kích thước màn hình (Do chưa có pygame_menu nên tạm thời bỏ qua)
# WINDOW_SIZES = [pygame.display.get_desktop_sizes()[0], (768,432)]
# WINDOW_SIZE_INDEX = 0
# SCREEN_SIZE = ['assets/characters/']
# SCREEN_SIZE_INDEX = 0
# screen = pygame.display.set_mode(WINDOW_SIZES[WINDOW_SIZE_INDEX], pygame.RESIZABLE)
# halfScreen_active = False

# #Kiểu chữ
# KieuChu1 = pygame.font.SysFont('./assets/font/SVN-Retron_2000.ttf',60)
# KieuChu2 = pygame.font.SysFont('./assets/font/FVF Fernando 08',60)

# #Chữ các thứ
# Player_money = 0
# scoreBoard = KieuChu2.render(f"Money: {Player_money}", False, (0, 255, 255))
# scoreBoard_Box = scoreBoard.get_rect(center = (screen.get_width() * 0.13, screen.get_height() * 0.92))

# #Ảnh các loại
# map1 = pygame.image.load('assets/background/map1.png').convert_alpha()
# map1 = pygame.transform.smoothscale(map1, WINDOW_SIZES[WINDOW_SIZE_INDEX])
# map2 = pygame.image.load('assets/background/map2.png').convert_alpha()
# map2 = pygame.transform.smoothscale(map1, WINDOW_SIZES[WINDOW_SIZE_INDEX])
# map3 = pygame.image.load('assets/background/map3.png').convert_alpha()
# map3 = pygame.transform.smoothscale(map1, WINDOW_SIZES[WINDOW_SIZE_INDEX])
# map4 = pygame.image.load('assets/background/map4.png').convert_alpha()
# map4 = pygame.transform.smoothscale(map1, WINDOW_SIZES[WINDOW_SIZE_INDEX])
# map5 = pygame.image.load('assets/background/map5.png').convert_alpha()
# map5 = pygame.transform.smoothscale(map1, WINDOW_SIZES[WINDOW_SIZE_INDEX])
# MAPS = [map1, map2, map3, map4, map5]
# MAP_INDEX = 0

# #Các ảnh cần dùng đến
# #1. Nhân vật (Đặt tên theo dạng Char#Map#_#)
# Char1Map1 = ['assets/characters/Char1Map1_1.png', 'assets/characters/Char1Map1_2.png',
#             'assets/characters/Char1Map1_3.png', 'assets/characters/Char1Map1_4.png']
# Char2Map1 = ['assets/characters/Char2Map1_1.png', 'assets/characters/Char2Map1_2.png',
#             'assets/characters/Char2Map1_3.png', 'assets/characters/Char2Map1_4.png']
# Char3Map1 = ['assets/characters/Char3Map1_1.png', 'assets/characters/Char3Map1_2.png',
#             'assets/characters/Char3Map1_3.png', 'assets/characters/Char3Map1_4.png']
# Char4Map1 = ['assets/characters/Char4Map1_1.png', 'assets/characters/Char4Map1_2.png',
#             'assets/characters/Char4Map1_3.png', 'assets/characters/Char4Map1_4.png']
# Char5Map1 = ['assets/characters/Char5Map1_1.png', 'assets/characters/Char5Map1_2.png',
#             'assets/characters/Char5Map1_3.png', 'assets/characters/Char5Map1_4.png']

# Char1Map2 = ['assets/characters/Char1Map2_1.png', 'assets/characters/Char1Map2_2.png',
#             'assets/characters/Char1Map2_3.png', 'assets/characters/Char1Map2_4.png']
# Char2Map2 = ['assets/characters/Char2Map2_1.png', 'assets/characters/Char2Map2_2.png',
#             'assets/characters/Char2Map2_3.png', 'assets/characters/Char2Map2_4.png']
# Char3Map2 = ['assets/characters/Char3Map2_1.png', 'assets/characters/Char3Map2_2.png',
#             'assets/characters/Char3Map2_3.png', 'assets/characters/Char3Map2_4.png']
# Char4Map2 = ['assets/characters/Char4Map2_1.png', 'assets/characters/Char4Map2_2.png',
#             'assets/characters/Char4Map1_3.png', 'assets/characters/Char4Map2_4.png']
# Char5Map2 = ['assets/characters/Char5Map2_1.png', 'assets/characters/Char5Map2_2.png',
#             'assets/characters/Char5Map2_3.png', 'assets/characters/Char5Map2_4.png']

# Char1Map3 = ['assets/characters/Char1Map3_1.png', 'assets/characters/Char1Map3_2.png',
#             'assets/characters/Char1Map3_3.png', 'assets/characters/Char1Map3_4.png']
# Char2Map3 = ['assets/characters/Char2Map3_1.png', 'assets/characters/Char2Map3_2.png',
#             'assets/characters/Char2Map3_3.png', 'assets/characters/Char2Map3_4.png']
# Char3Map3 = ['assets/characters/Char3Map3_1.png', 'assets/characters/Char3Map3_2.png',
#             'assets/characters/Char3Map3_3.png', 'assets/characters/Char3Map3_4.png']
# Char4Map3 = ['assets/characters/Char4Map3_1.png', 'assets/characters/Char4Map3_2.png',
#             'assets/characters/Char4Map3_3.png', 'assets/characters/Char4Map3_4.png']
# Char5Map3 = ['assets/characters/Char5Map3_1.png', 'assets/characters/Char5Map3_2.png',
#             'assets/characters/Char5Map3_3.png', 'assets/characters/Char5Map3_4.png']

# Char1Map4 = ['assets/characters/Char1Map4_1.png', 'assets/characters/Char1Map4_2.png',
#             'assets/characters/Char1Map4_3.png', 'assets/characters/Char1Map4_4.png']
# Char2Map4 = ['assets/characters/Char2Map4_1.png', 'assets/characters/Char2Map4_2.png',
#             'assets/characters/Char2Map4_3.png', 'assets/characters/Char2Map4_4.png']
# Char3Map4 = ['assets/characters/Char3Map4_1.png', 'assets/characters/Char3Map4_2.png',
#             'assets/characters/Char3Map4_3.png', 'assets/characters/Char3Map4_4.png']
# Char4Map4 = ['assets/characters/Char4Map4_1.png', 'assets/characters/Char4Map4_2.png',
#             'assets/characters/Char4Map4_3.png', 'assets/characters/Char4Map4_4.png']
# Char5Map4 = ['assets/characters/Char5Map4_1.png', 'assets/characters/Char5Map4_2.png',
#             'assets/characters/Char5Map4_3.png', 'assets/characters/Char5Map4_4.png']

# Char1Map5 = ['assets/characters/Char1Map5_1.png', 'assets/characters/Char1Map5_2.png',
#             'assets/characters/Char1Map5_3.png', 'assets/characters/Char1Map5_4.png']
# Char2Map5 = ['assets/characters/Char2Map5_1.png', 'assets/characters/Char2Map5_2.png',
#             'assets/characters/Char2Map5_3.png', 'assets/characters/Char2Map5_4.png']
# Char3Map5 = ['assets/characters/Char3Map5_1.png', 'assets/characters/Char3Map5_2.png',
#             'assets/characters/Char3Map5_3.png', 'assets/characters/Char3Map5_4.png']
# Char4Map5 = ['assets/characters/Char4Map5_1.png', 'assets/characters/Char4Map5_2.png',
#             'assets/characters/Char4Map5_3.png', 'assets/characters/Char4Map5_4.png']
# Char5Map5 = ['assets/characters/Char5Map5_1.png', 'assets/characters/Char5Map5_2.png',
#             'assets/characters/Char5Map5_3.png', 'assets/characters/Char5Map5_4.png']


# #Nhân vật, tốc độ, vị trí
# CharsMap1 = [Char1Map1, Char2Map1, Char3Map1, Char4Map1, Char5Map1]
# CharsMap2 = [Char1Map2, Char2Map2, Char3Map2, Char4Map2, Char5Map2]
# CharsMap3 = [Char1Map3, Char2Map3, Char3Map3, Char4Map3, Char5Map3]
# CharsMap4 = [Char1Map4, Char2Map4, Char3Map4, Char4Map4, Char5Map4]
# CharsMap5 = [Char1Map5, Char2Map5, Char3Map5, Char4Map5, Char5Map5]
# RandSpeed = [2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4]
# Speed = []
# for x in range(5):
#     Speed.append(random.choice(RandSpeed))
# Position = [(WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.01, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.55), 
#             (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.01, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.66), 
#             (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.01, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.76), 
#             (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.01, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.87), 
#             (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.01, WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.98)]

# #Ktra nhạc đã phát chưa
# Victory_sound_Play = True

# #Các nhân vật trong game
# class Character():
#     def __init__(self, speed, pos, number, image, map):
#         self.speed = speed
#         self.tempSpeed = speed
#         self.pos = pos
#         self.x = self.pos[0]
#         self.y = self.pos[1]
#         self.number = number
#         self.run = True
#         self.count_run = 0
#         self.image = pygame.image.load(image).convert_alpha()
#         self.rect= self.image.get_rect(midbottom = (self.x, self.y))
#         self.count_run = 0
#         self.map = map
#         self.Finish = False
#         self.isGoBack = False
#         self.PhanKhich = False
#         self.TroiHon = False
#         self.NhanhNhen = False
#         self.KichHoatBua = False
#         self.active_time = pygame.time.get_ticks()
#     def animation(self):
#         #Vẽ nhân vật
#         if self.count_run >= 3:
#             self.count_run = 0
#         if self.map == 0:
#             if self.number == 0:
#                 if self.run:
#                     self.image = pygame.image.load(CharsMap1[0][int(self.count_run)]).convert_alpha()
#                     self.count_run += 0.1
#                 else:
#                     self.image = pygame.image.load(CharsMap1[0][int(self.count_run)]).convert_alpha()
#             if self.number == 1:
#                 if self.run:
#                     self.image = pygame.image.load(CharsMap1[1][int(self.count_run)]).convert_alpha()
#                     self.count_run += 0.1
#                 else:
#                     self.image = pygame.image.load(CharsMap1[1][int(self.count_run)]).convert_alpha()
#             if self.number == 2:
#                 if self.run:
#                     self.image = pygame.image.load(CharsMap1[2][int(self.count_run)]).convert_alpha()
#                     self.count_run += 0.1
#                 else:
#                     self.image = pygame.image.load(CharsMap1[2][int(self.count_run)]).convert_alpha()
#             if self.number == 3:
#                 if self.run:
#                     self.image = pygame.image.load(CharsMap1[3][int(self.count_run)]).convert_alpha()
#                     self.count_run += 0.1
#                 else:
#                     self.image = pygame.image.load(CharsMap1[3][int(self.count_run)]).convert_alpha()
#             if self.number == 4:
#                 if self.run:
#                     self.image = pygame.image.load(CharsMap1[4][int(self.count_run)]).convert_alpha()
#                     self.count_run += 0.1
#                 else:
#                     self.image = pygame.image.load(CharsMap1[4][int(self.count_run)]).convert_alpha()
#         elif self.map == 1:
#             if self.number == 0:
#                 if self.run:
#                     self.image = pygame.image.load(CharsMap2[0][int(self.count_run)]).convert_alpha()
#                     self.count_run += 0.1
#                 else:
#                     self.image = pygame.image.load(CharsMap2[0][int(self.count_run)]).convert_alpha()
#             if self.number == 1:
#                 if self.run:
#                     self.image = pygame.image.load(CharsMap2[1][int(self.count_run)]).convert_alpha()
#                     self.count_run += 0.1
#                 else:
#                     self.image = pygame.image.load(CharsMap2[1][int(self.count_run)]).convert_alpha()
#             if self.number == 2:
#                 if self.run:
#                     self.image = pygame.image.load(CharsMap2[2][int(self.count_run)]).convert_alpha()
#                     self.count_run += 0.1
#                 else:
#                     self.image = pygame.image.load(CharsMap2[2][int(self.count_run)]).convert_alpha()
#             if self.number == 3:
#                 if self.run:
#                     self.image = pygame.image.load(CharsMap2[3][int(self.count_run)]).convert_alpha()
#                     self.count_run += 0.1
#                 else:
#                     self.image = pygame.image.load(CharsMap2[3][int(self.count_run)]).convert_alpha()
#             if self.number == 4:
#                 if self.run:
#                     self.image = pygame.image.load(CharsMap2[4][int(self.count_run)]).convert_alpha()
#                     self.count_run += 0.1
#                 else:
#                     self.image = pygame.image.load(CharsMap2[4][int(self.count_run)]).convert_alpha()
#         elif self.map == 2:
#             if self.number == 0:
#                 if self.run:
#                     self.image = pygame.image.load(CharsMap3[0][int(self.count_run)]).convert_alpha()
#                     self.count_run += 0.1
#                 else:
#                     self.image = pygame.image.load(CharsMap3[0][int(self.count_run)]).convert_alpha()
#             if self.number == 1:
#                 if self.run:
#                     self.image = pygame.image.load(CharsMap3[1][int(self.count_run)]).convert_alpha()
#                     self.count_run += 0.1
#                 else:
#                     self.image = pygame.image.load(CharsMap3[1][int(self.count_run)]).convert_alpha()
#             if self.number == 2:
#                 if self.run:
#                     self.image = pygame.image.load(CharsMap3[2][int(self.count_run)]).convert_alpha()
#                     self.count_run += 0.1
#                 else:
#                     self.image = pygame.image.load(CharsMap3[2][int(self.count_run)]).convert_alpha()
#             if self.number == 3:
#                 if self.run:
#                     self.image = pygame.image.load(CharsMap3[3][int(self.count_run)]).convert_alpha()
#                     self.count_run += 0.1
#                 else:
#                     self.image = pygame.image.load(CharsMap3[3][int(self.count_run)]).convert_alpha()
#             if self.number == 4:
#                 if self.run:
#                     self.image = pygame.image.load(CharsMap3[4][int(self.count_run)]).convert_alpha()
#                     self.count_run += 0.1
#                 else:
#                     self.image = pygame.image.load(CharsMap3[4][int(self.count_run)]).convert_alpha()
#         elif self.map == 3:
#             if self.number == 0:
#                 if self.run:
#                     self.image = pygame.image.load(CharsMap4[0][int(self.count_run)]).convert_alpha()
#                     self.count_run += 0.1
#                 else:
#                     self.image = pygame.image.load(CharsMap4[0][int(self.count_run)]).convert_alpha()
#             if self.number == 1:
#                 if self.run:
#                     self.image = pygame.image.load(CharsMap4[1][int(self.count_run)]).convert_alpha()
#                     self.count_run += 0.1
#                 else:
#                     self.image = pygame.image.load(CharsMap4[1][int(self.count_run)]).convert_alpha()
#             if self.number == 2:
#                 if self.run:
#                     self.image = pygame.image.load(CharsMap4[2][int(self.count_run)]).convert_alpha()
#                     self.count_run += 0.1
#                 else:
#                     self.image = pygame.image.load(CharsMap4[2][int(self.count_run)]).convert_alpha()
#             if self.number == 3:
#                 if self.run:
#                     self.image = pygame.image.load(CharsMap4[3][int(self.count_run)]).convert_alpha()
#                     self.count_run += 0.1
#                 else:
#                     self.image = pygame.image.load(CharsMap4[3][int(self.count_run)]).convert_alpha()
#             if self.number == 4:
#                 if self.run:
#                     self.image = pygame.image.load(CharsMap4[4][int(self.count_run)]).convert_alpha()
#                     self.count_run += 0.1
#                 else:
#                     self.image = pygame.image.load(CharsMap4[4][int(self.count_run)]).convert_alpha()
#         elif self.map == 4:
#             if self.number == 0:
#                 if self.run:
#                     self.image = pygame.image.load(CharsMap5[0][int(self.count_run)]).convert_alpha()
#                     self.count_run += 0.1
#                 else:
#                     self.image = pygame.image.load(CharsMap5[0][int(self.count_run)]).convert_alpha()
#             if self.number == 1:
#                 if self.run:
#                     self.image = pygame.image.load(CharsMap5[1][int(self.count_run)]).convert_alpha()
#                     self.count_run += 0.1
#                 else:
#                     self.image = pygame.image.load(CharsMap5[1][int(self.count_run)]).convert_alpha()
#             if self.number == 2:
#                 if self.run:
#                     self.image = pygame.image.load(CharsMap5[2][int(self.count_run)]).convert_alpha()
#                     self.count_run += 0.1
#                 else:
#                     self.image = pygame.image.load(CharsMap5[2][int(self.count_run)]).convert_alpha()
#             if self.number == 3:
#                 if self.run:
#                     self.image = pygame.image.load(CharsMap5[3][int(self.count_run)]).convert_alpha()
#                     self.count_run += 0.1
#                 else:
#                     self.image = pygame.image.load(CharsMap5[3][int(self.count_run)]).convert_alpha()
#             if self.number == 4:
#                 if self.run:
#                     self.image = pygame.image.load(CharsMap5[4][int(self.count_run)]).convert_alpha()
#                     self.count_run += 0.1
#                 else:
#                     self.image = pygame.image.load(CharsMap5[4][int(self.count_run)]).convert_alpha()


#     def move(self):
#         if self.run:
#             self.rect.x += self.speed
#     #Check điều kiện thắng
#     def checkFinishLine(self):
#         if self.rect.x > WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.95:
#             if not self.Finish:
#                 rank.append(self)
#                 self.run = False
#                 self.Finish = True
        

#     def update(self):
#         self.animation()
#         self.move()
#         self.checkFinishLine()
#         if self.PhanKhich:
#             if not self.KichHoatBua:
#                 self.KichHoatBua = True
#             self.Bua()
#         if self.NhanhNhen:
#             if not self.KichHoatBua:
#                 self.active_time = pygame.time.get_ticks()
#                 self.speed += 2
#                 self.KichHoatBua = True
#             self.Bua()
#         if self.TroiHon:
#             if not self.KichHoatBua:
#                 self.active_time = pygame.time.get_ticks()
#                 for i in range(5):
#                         if(i != (choice - 1)):
#                             CHARACTERS[i].run = False
#                 self.KichHoatBua = True
#             self.Bua()
#         if self.isGoBack: #Đi ngược lại
#             goBackImage = pygame.transform.flip(self.image, True, False)
#             screen.blit(goBackImage, self.rect)
#         else:
#             screen.blit(self.image, self.rect)

#     def Bua(self):
#         if self.PhanKhich:
#             effectImage = pygame.image.load("assets/effects/hieuung_dichchuyen.png").convert_alpha() #Ảnh tạm
#             effectImage_rect = effectImage.get_rect(midbottom = self.rect.midleft)
#             screen.blit(effectImage, effectImage_rect)
#         if self.NhanhNhen:
#             effectImage = pygame.image.load("assets/effects/hieuung_dichchuyen.png").convert_alpha()
#             effectImage_rect = effectImage.get_rect(midbottom = self.rect.midleft)
#             screen.blit(effectImage, effectImage_rect)
#             current_time = pygame.time.get_ticks() #Lấy thời gian hiện tại
#             elapsed_time = current_time - self.active_time
#             if elapsed_time >= 2000:
#                     self.NhanhNhen = False
#                     self.speed = self.tempSpeed
#         if self.TroiHon:
#             effectImage = pygame.image.load("assets/effects/hieuung_dichchuyen.png").convert_alpha()
#             effectImage_rect = effectImage.get_rect(midbottom = self.rect.midleft)
#             screen.blit(effectImage, effectImage_rect)
#             current_time = pygame.time.get_ticks() #Lấy thời gian hiện tại
#             elapsed_time = current_time - self.active_time
#             if elapsed_time >= 1000:
#                     self.TroiHon = False
#                     for i in range(5):
#                         if(i != (choice - 1)):
#                             CHARACTERS[i].run = True
                    

#     def stop(self, activated):
#         if not activated:
#             self.run = False

#     def slow(self, activated):
#         if not activated:
#             if self.speed <= 3:
#                 self.speed = 1
#             elif self.speed >= 5:
#                 self.speed -= 4
#             else:
#                 self.speed -= 2

#     def accelerate(self, activated):
#         if not activated:
#             if self.speed >= 3:
#                 self.speed += 1
#             else:
#                 self.speed += 2

#     def teleport(self, activated):
#         if not activated:
#             self.rect.x = WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * 0.8

#     def goback(self, activated):
#         if not activated:
#             self.speed *= -1
#             self.isGoBack = True

# def init_character_luckybox():
#     global set_choice
#     for i in range(5):
#         new_character = Character(speed = Speed[i], 
#                                   pos = Position[i], 
#                                   number = i, 
#                                   image = SCREEN_SIZE[SCREEN_SIZE_INDEX] + 'Char' + str(i + 1) + 'Map' + str(int(set_choice)) + '_1.png', 
#                                   map = int(set_choice - 1))
#         CHARACTERS.append(new_character)
#     for i in range(10):
#             if i < 5:
#                 luckyBox = LuckyBox(pos = LuckyBox_Pos[i], character = CHARACTERS[i])
#             else:
#                 luckyBox = LuckyBox(pos = LuckyBox_Pos[i], character = CHARACTERS[i - 5])
#             LUCKYBOX.append(luckyBox)

# #Các đối tượng trong game (Hiện tại chỉ đang có chữ chạy)
# class IG_Objects():
#     def __init__(self, name, pos):
#         self.x = pos[0]
#         self.y = pos[1]
#         self.name = name
#         if self.name == "ChuChay":
#             self.pic = KieuChu1.render("THIS IS GROUP 12'S AMAZING RACE GAME!!!", False, (255, 102, 0))
#             self.image = self.pic
#             self.rect= self.image.get_rect(topleft = (self.x, self.y))
#     def move(self):
#         if self.name == "ChuChay":
#             self.rect.x -= 2
#             if self.rect.right <= 0:
#                 self.rect.x = WINDOW_SIZES[WINDOW_SIZE_INDEX][0]
#     def update(self):
#         if self.name == "ChuChay":
#             self.move()
#             screen.blit(self.image, self.rect)

# #Add object
# ChuChay = IG_Objects(name = 'ChuChay', pos = (WINDOW_SIZES[WINDOW_SIZE_INDEX][0], 0))

# #Vị trí lucky box
# LuckyBox_Pos = [(WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * random.uniform(0.28, 0.5), WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.55), 
#                 (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * random.uniform(0.28, 0.5), WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.66), 
#                 (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * random.uniform(0.28, 0.5), WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.76), 
#                 (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * random.uniform(0.28, 0.5), WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.87),
#                 (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * random.uniform(0.28, 0.5), WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.98),
#                 (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * random.uniform(0.65, 0.75), WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.55),
#                 (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * random.uniform(0.65, 0.75), WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.66),
#                 (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * random.uniform(0.65, 0.75), WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.76),
#                 (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * random.uniform(0.65, 0.75), WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.87),
#                 (WINDOW_SIZES[WINDOW_SIZE_INDEX][0] * random.uniform(0.65, 0.75), WINDOW_SIZES[WINDOW_SIZE_INDEX][1] * 0.98)]
# class LuckyBox():
#     def __init__(self, pos, character):
#         self.x = pos[0]
#         self.y = pos[1]
#         self.activated = False #Cái này để check xem lucky box đã kích hoạt chưa
#         self.active_effect = None #Kích hoạt hiệu ứng
#         self.effect_duration = random.randint(1000, 3000) #Tính theo mili giây
#         self.activation_time = None #Check lúc nào kích hoạt hiệu ứng
#         self.effects = ["stun", "stun", "stun", "stun", "stun", "stun", "slow", "slow", "slow", "slow", "slow", "slow", "slow", "accelerate", "accelerate", "accelerate", "accelerate", "accelerate", "teleport", "goback"] #Các hiệu ứng, nếu muốn hiệu ứng nào xuất hiện nhiều chỉ cần spam
#         self.image = pygame.image.load('assets/item/luckyBox.png').convert_alpha()
#         self.rect= self.image.get_rect(midbottom = (self.x, self.y))
#         self.tempSpeed = character.speed #Dùng để lưu tốc chạy của nhân vật tạm thời

#     def check_activate(self, character):
#         if character.rect.colliderect(self.rect) and (not self.activated):
#             self.activate_effect(character)
#             self.activated = True

#     def activate_effect(self, character):

#         self.active_effect = random.choice(self.effects)
#         self.activation_time = pygame.time.get_ticks()

#         if self.active_effect == "stun":
#             if character.PhanKhich:
#                 self.active_effect = None
#                 character.PhanKhich = False
#             else:
#                 character.stop(self.activated)
#         elif self.active_effect == "slow":
#             if character.PhanKhich == True:
#                 self.active_effect = None
#                 character.PhanKhich = False
#             else:
#                 character.slow(self.activated)
#         elif self.active_effect == "accelerate":
#             character.accelerate(self.activated)
#         elif self.active_effect == "teleport":
#             character.teleport(self.activated)
#         elif self.active_effect == "goback":
#             if character.PhanKhich:
#                 self.active_effect = None
#                 character.PhanKhich = False
#             else:
#                 character.goback(self.activated)

#     def effect_Image(self, character):
#         if self.active_effect == "stun":
#             effectImage = pygame.image.load("assets/effects/hieuung_choang.png").convert_alpha()
#             effectImage_rect = effectImage.get_rect(center = character.rect.midtop)
#             effectImage2 = pygame.image.load("assets/effects/tangDa.png").convert_alpha()
#             effectImage_rect2 = effectImage.get_rect(bottomleft = self.rect.midleft)
#             screen.blit(effectImage, effectImage_rect)
#             screen.blit(effectImage2, effectImage_rect2)
#         elif self.active_effect == "slow":
#             effectImage = pygame.image.load("assets/effects/hieuung_cham.png").convert_alpha()
#             effectImage_rect = effectImage.get_rect(midbottom = character.rect.midleft)
#             effectImage2 = pygame.image.load("assets/effects/hoNuoc.png").convert_alpha()
#             effectImage_rect2 = effectImage.get_rect(midleft = self.rect.bottomleft)
#             screen.blit(effectImage, effectImage_rect)
#             screen.blit(effectImage2, effectImage_rect2)
#         elif self.active_effect == "accelerate":
#             effectImage = pygame.image.load("assets/effects/hieuung_tangtoc.png").convert_alpha()
#             effectImage_rect = effectImage.get_rect(bottomright = character.rect.bottomleft)
#             screen.blit(effectImage, effectImage_rect)
#         elif self.active_effect == "teleport":
#             effectImage = pygame.image.load("assets/effects/hieuung_dichchuyen.png").convert_alpha()
#             effectImage_rect = effectImage.get_rect(bottomleft = self.rect.midbottom)
#             screen.blit(effectImage, effectImage_rect)
#         elif self.active_effect == "goback":
#             effectImage = pygame.image.load("assets/effects/hieuung_quayve.png").convert_alpha()
#             effectImage_rect = effectImage.get_rect(bottomleft = self.rect.midbottom)
#             screen.blit(effectImage, effectImage_rect)

#     def update(self, character):
#         self.check_activate(character)
#         if self.active_effect is not None:
#             self.effect_Image(character)
#             current_time = pygame.time.get_ticks() #Lấy thời gian hiện tại
#             elapsed_time = current_time - self.activation_time
#             if self.active_effect == "slow" or self.active_effect == "accelerate" or self.active_effect == "teleport":
#                 if elapsed_time >= self.effect_duration:
#                     self.active_effect = None
#                     character.speed = self.tempSpeed
                    
#             elif self.active_effect == "stun":
#                 if elapsed_time >= self.effect_duration:
#                     self.active_effect = None
#                     character.run = True

#             elif self.active_effect == "goback":
#                 if character.rect.x < 0:
#                     self.active_effect = None
#                     character.speed = self.tempSpeed
#                     character.isGoBack = False


#         if not self.activated:
#                 screen.blit(self.image, self.rect)

# #Class nút
# class Button():
#     def __init__(self, pos, imageNormal, imageChanged):
#         self.imageNormal = imageNormal
#         self.imageChanged = imageChanged
#         self.image = pygame.image.load(LANGUAGE[LANGUAGE_INDEX] + imageNormal).convert_alpha()
#         self.x = pos[0]
#         self.y = pos[1]
#         self.rect = self.image.get_rect(center=(self.x, self.y * 1.01))

#     def CheckClick(self, position):
#         if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
#             return True
#         return False
    
#     def update(self, position):
#         global LANGUAGE_INDEX
#         if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
#             self.image = pygame.image.load(LANGUAGE[LANGUAGE_INDEX] + self.imageChanged).convert_alpha()
#         else:
#             self.image = pygame.image.load(LANGUAGE[LANGUAGE_INDEX] + self.imageNormal).convert_alpha()
#         screen.blit(self.image, self.rect)
#     '''def update_images(self, imageNormal, imageChanged):
#         self.imageNormal = pygame.image.load(LANGUAGE[LANGUAGE_INDEX] + self.imageNormal).convert_alpha()
#         self.imageChanged = pygame.image.load(LANGUAGE[LANGUAGE_INDEX] + self.imageChanged).convert_alpha()'''

# #Cách xài class button
# # 1. Khởi tạo nút
# # button = Button( pos = (400, 300), imageNỏmal = "Button.png", imageChanged = "Button2.png") Chú ý: Button.png là ảnh khi chưa rê chuột vào, Button2.png là ảnh khi rê chuột vào
# # 2. Check click
# #     if event.type == pygame.MOUSEBUTTONDOWN:
# #         button.CheckClick(pygame.mouse.get_pos())
# # 3. Update button
# # 	button.update()
# # 	button.DoiMau(pygame.mouse.get_pos())

# #Quy định các thuộc tính chỉ tạo dòng chữ hiển thị trong menu
# class Label: 
#     # Khởi tạo các thuộc tính tương tự như các thuộc tính của Button
#     def __init__(self, x, y, width, height, text=None):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.text = text
#         self.font = pygame.font.Font('./assets/font/SVN-Retron_2000.ttf',40) #Font mặc định
#     # gọi hàm vẽ các Label, gồm các tham số như chính đối tượng Label, cửa sổ màn hình và đường viền, mặc định là None.
#     def draw(self, screen):
#         if self.text: # Kiểm tra xem có text được đưa vào hay không
#             text = self.font.render(self.text, 1, '#ffffff') #Màu text là màu đen, bật khử răng cưa cho text, áp dụng cho tất cả các text trong class
#             screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))  #Đưa chữ lên cửa sổ màn hình

# #Cách xài class label
# #label = Label(x, y, width, height, "Chữ")


# #Check điều kiện thắng
# def FinishLine_Pass():
#     global Victory_sound_Play
#     if len(GameInit.rank) == 5:
#         if Victory_sound_Play:
#             pygame.mixer.music.load('assets/sounds/Victorious.ogg')
#             pygame.mixer.music.play(loops = 0)
#             Victory_sound_Play = False
#             return True
#     return False

# #Đếm ngược
# countDownCheck = True
# NumberCountDown = ["assets/background/start.png", "assets/background/1.png", "assets/background/2.png", "assets/background/3.png"]
# def count_down():
#     global gameSound
#     for i in range(3, -1, -1):
#         screen.blit(MAPS[MAP_INDEX], (0, 0))
#         image = pygame.image.load(NumberCountDown[i]).convert_alpha()
#         image_rect = image.get_rect(center = (screen.get_width() / 2, screen.get_height() / 2))
#         screen.blit(image, image_rect)

#         pygame.display.update()
#         pygame.time.wait(1000)
#     pygame.mixer.music.set_volume(present_volume)
#     pygame.mixer.music.load('assets/sounds/set1.mp3')
#     pygame.mixer.music.play(loops = -1)
#     gameSound = True

# class Congratulations:
#     def __init__(self):
#         self.CONTINUE_BUTTON = Button(pos=(screen.get_width() / 2 * 1.05, screen.get_height() * 0.1), imageNormal = "continue.png", imageChanged = "continue2.png")
#     #Vẽ các thuộc tính lên màn hình
#     def draw(self, mouse_pos):
#         global rank, rankSound,  WINDOW_SIZES
#         BG = pygame.image.load(LANGUAGE[GameInit.LANGUAGE_INDEX]+'BG_congratulations.png').convert_alpha()
#         BG = pygame.transform.smoothscale(BG, WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX])
#         screen.blit(BG, (0, 0))
#         self.CONTINUE_BUTTON.update(mouse_pos)

#         if not rankSound:
#             pygame.mixer.music.set_volume(present_volume)
#             pygame.mixer.music.load('assets/sounds/rank.mp3')
#             pygame.mixer.music.play(loops = -1)
#             rankSound = True
        
#         Congratulations_pos = [(WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX][0] / 2 * 1.05, WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX][1] * 0.78), 
#                                 (WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX][0] / 2 * 0.6, WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX][1]* 0.85), 
#                                 (WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX][0] / 2 * 1.5, WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX][1]* 0.85), 
#                                 (WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX][0] / 2 * 0.42, WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX][1] * 0.93), 
#                                 (WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX][0] / 2 * 1.7, WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX][1] * 0.93)]

#         for i in range(5):
#             GameInit.rank[i].rect = GameInit.rank[i].image.get_rect(midbottom = Congratulations_pos[i])
#             screen.blit(GameInit.rank[i].image, GameInit.rank[i].rect)

        

#     # Cập nhật các trạng thái của thuộc tính
#     def update(self, event):
#         global MenuSound, gameSound, InitGame
#         if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE:
#                 Back_To_Menu = Pause_Game()
#                 if Back_To_Menu:
#                     InitGame = False
#                     return MenuClass()
            
#         return self

# #Biến được sử dụng
# InitGame = False
# rankSound = False

# class Play:
#     def __init__(self):
#         money_bet()
#         self.playButton = Button(pos = (screen.get_width() / 2, screen.get_height() / 2), imageNormal = "play.png", imageChanged = "play2.png") # Nút có dòng chữ "Play game"
#         self.settingsButton = Button(pos = (screen.get_width() / 2, screen.get_height() / 2 * 1.35), imageNormal = "settings.png", imageChanged = "settings2.png") # Nút có dòng chữ "Settings"
#         self.quitButton = Button(pos = (screen.get_width() / 2, screen.get_height() / 2 * 1.7), imageNormal = "quit.png", imageChanged = "quit2.png") # Nút có dòng chữ "Quit"
#         self.CheckPass = False #Check xem 5 nv có về đích chưa
#     #Vẽ các thuộc tính lên màn hình
#     def draw(self, mouse_pos):
#         global VOLUME_INDEX, present_volume, countDownCheck, gameSound
#         #Ảnh nền
#         if MAP_INDEX == 0:
#              screen.blit(MAPS[0],(0,0))
#         if MAP_INDEX == 1:
#              screen.blit(MAPS[1],(0,0))
#         if MAP_INDEX == 2:
#              screen.blit(MAPS[2],(0,0))
#         if MAP_INDEX == 3:
#              screen.blit(MAPS[3],(0,0))
#         if MAP_INDEX == 4:
#              screen.blit(MAPS[4],(0,0))
        
#         #Đếm ngược trước khi vào game
#         if countDownCheck:
#             count_down()
#             countDownCheck = False

#         if not gameSound:
#             pygame.mixer.music.set_volume(present_volume)
#             pygame.mixer.music.load('assets/sounds/set1.mp3')
#             pygame.mixer.music.play(loops = -1)
#             gameSound = True

#         #Chữ chạy
#         ChuChay.update()
                
#         #Update lucky box
#         for i in range(10):
#             if i < 5:
#                 LUCKYBOX[i].update(CHARACTERS[i])
#             else:
#                 LUCKYBOX[i].update(CHARACTERS[i - 5])

#         #Nhân vật
#         for i in range(5):
#             CHARACTERS[i].update()

#         #Check xong game
#         if FinishLine_Pass():
#             self.CheckPass = True

#     # Cập nhật các trạng thái của thuộc tính
#     def update(self, event):
#         global MenuSound, gameSound, InitGame
#         if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE:
#                 Back_To_Menu = Pause_Game()
#                 if Back_To_Menu:
#                     InitGame = False
#                     reset_game()
#                     return MenuClass()
#         if self.CheckPass:
#             return Congratulations()
            
#         return self

# #Tạm dừng trò chơi
# def Pause_Game():
#      while True:
#         #Ảnh nền
#         Background = pygame.image.load(LANGUAGE[GameInit.LANGUAGE_INDEX]+'background.png').convert_alpha()
#         Background = pygame.transform.smoothscale(Background, WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX])
#         screen.blit(Background,(0,0))
#         #Các nút ở trong Pause menu
#         mouse_pos = pygame.mouse.get_pos()
#         RETURN_TO_MENU = Button(pos=(screen.get_width() / 2, screen.get_height() / 2), imageNormal = "return.png", imageChanged = "return2.png")
#         RETURN_TO_GAME = Button(pos=(screen.get_width() / 2, screen.get_height() / 2 * 1.35), imageNormal = "continue.png", imageChanged = "continue2.png")
#         QUIT = Button(pos=(screen.get_width() / 2, screen.get_height() / 2 * 1.7), imageNormal = "quit.png", imageChanged = "quit2.png")
#         BUTTONS = [RETURN_TO_MENU, RETURN_TO_GAME, QUIT]

#         for button in BUTTONS:
#             button.update(mouse_pos)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if RETURN_TO_GAME.CheckClick(mouse_pos):
#                     return
#                 if QUIT.CheckClick(mouse_pos):
#                     pygame.quit()
#                     sys.exit()
#                 if RETURN_TO_MENU.CheckClick(mouse_pos):
#                     if QuitConfirm():
#                         return True
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     return

#         pygame.display.update()
#         clock.tick(60)

# def QuitConfirm():
#     while True:
#         Background = pygame.image.load(LANGUAGE[GameInit.LANGUAGE_INDEX]+'quitprompt.png').convert_alpha()
#         Background = pygame.transform.smoothscale(Background, WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX])
#         screen.blit(Background,(0,0))
#         mouse_pos = pygame.mouse.get_pos()
#         #Các nút trong quit confirm
#         yesButton = Button(pos=(screen.get_width() / 2 * 1.5, screen.get_height() / 2 * 1.2), imageNormal = "yes.png", imageChanged = "yes2.png")
#         noButton = Button(pos=(screen.get_width() / 2 * 0.5, screen.get_height() / 2 * 1.2), imageNormal = "no.png", imageChanged = "no2.png")

#         yesButton.update(mouse_pos)
#         noButton.update(mouse_pos)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if yesButton.CheckClick(mouse_pos):
#                     return True
#                 if noButton.CheckClick(mouse_pos):
#                     return False
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     return False

#         pygame.display.update()
#         clock.tick(60)


# # Lớp menu chính
# class MenuClass: 
#     #Khởi tạo các thuộc tính
#     def __init__(self):
#         global VOLUME_INDEX, present_volume
#         self.playButton = Button(pos = (screen.get_width() / 2, screen.get_height() / 2 * 0.95), imageNormal = f"play.png", imageChanged = "play2.png") # Nút có dòng chữ "Play game"
#         self.settingsButton = Button(pos = (screen.get_width() / 2, screen.get_height() / 2 * 1.2), imageNormal = "settings.png", imageChanged = "settings2.png") # Nút có dòng chữ "Settings"
#         self.minigame = Button(pos = (screen.get_width() / 2, screen.get_height() / 2 * 1.45), imageNormal = "minigame.png", imageChanged = "minigame2.png")
#         self.quitButton = Button(pos = (screen.get_width() / 2, screen.get_height() / 2 * 1.7), imageNormal = "quit.png", imageChanged = "quit2.png") # Nút có dòng chữ "Quit"
#         #v self.changeLanguageButton = Button(pos=(screen.get_width() - screen.get_width() / 16, screen.get_height() - screen.get_height() / 16), imageNormal= "lang40.png", imageChanged= "lang240.png") # Nút chuyển đổi ngôn ngữ
#     #Vẽ các thuộc tính lên màn hình
#     def draw(self, mouse_pos):
#         read_data()
#         Background = pygame.image.load(LANGUAGE[GameInit.LANGUAGE_INDEX]+'background.png').convert_alpha()
#         Background = pygame.transform.smoothscale(Background, WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX])
#         screen.blit(Background, (0, 0))
#         self.playButton.update(mouse_pos)
#         self.settingsButton.update(mouse_pos)
#         self.quitButton.update(mouse_pos)
#         self.minigame.update(mouse_pos)
#         # self.changeLanguageButton.update(mouse_pos)

#     # Cập nhật các trạng thái của thuộc tính
#     def update(self, event):
#         global MenuSound, gameSound, LANGUAGE
#         if not MenuSound:
#             pygame.mixer.music.set_volume(present_volume)
#             pygame.mixer.music.load('assets/sounds/mainmenu.mp3')
#             pygame.mixer.music.play(loops = -1)
#             MenuSound = True
#         pos = pygame.mouse.get_pos()
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if self.playButton.CheckClick(pos):
#                 # if user_money < min(money_bet_list):
#                 #     minigame.flappy_bird()
#                 # else:
#                 MenuSound = False
#                 gameSound = False
#                 return MapSelection()
#             if self.settingsButton.CheckClick(pos):
#                 return SettingClass()
#             if self.quitButton.CheckClick(pos):
#                 pygame.quit()
#                 sys.exit()
#             if self.minigame.CheckClick(pos):
#                 minigame.flappy_bird()
                    
#         return self

# class SettingClass: #Khởi tạo các nút, label và Button. 
#     def __init__(self):
#         self.soundButton = Button(pos=(screen.get_width() / 2, screen.get_height() / 2 * 0.65), imageNormal = "sound.png", imageChanged = "sound2.png")
#         self.screenButton = Button(pos=(screen.get_width() / 2, screen.get_height() / 2 * 0.9), imageNormal = "screen.png", imageChanged = "screen2.png")
#         self.escButton = Button(pos=(screen.get_width() / 2, screen.get_height() / 2 * 1.4), imageNormal = "back.png", imageChanged = "back2.png")
#         self.changeLanguageButton = Button(pos=(screen.get_width() / 2, screen.get_height() / 2 * 1.15), imageNormal = "lang.png", imageChanged = "lang2.png")
#     #Vẽ các lớp phủ, các nút và chữ
#     def draw(self, mouse_pos):
#         Background = pygame.image.load(LANGUAGE[GameInit.LANGUAGE_INDEX] + 'settingsMenu.png').convert_alpha()
#         Background = pygame.transform.smoothscale(Background, WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX])
#         screen.blit(Background,(0,0)) #Tạo một lớp phủ hình chữ nhật kích thước tối đa
#         #Vẽ nút
#         self.soundButton.update(mouse_pos)
#         self.screenButton.update(mouse_pos)
#         self.escButton.update(mouse_pos)
#         self.changeLanguageButton.update(mouse_pos)
#     #Cập nhật trạng thái của class
#     def update(self, event):
#         mouse_pos = pygame.mouse.get_pos()
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             # Kiểm tra các đối tượng như nút chọn Âm lượng, chọn tùy chọn Màn hình, nút thoát; có được nhấn hay không. 
#             # Nếu có thì trả về class tương ứng
#             if self.soundButton.CheckClick(mouse_pos):
#                 return VolumeSettingClass()
#             if self.screenButton.CheckClick(mouse_pos):
#                 return WindowModeSettingClass()
#             if self.escButton.CheckClick(mouse_pos):
#                 return MenuClass()
#             if self.changeLanguageButton.CheckClick(mouse_pos):
#                 if GameInit.LANGUAGE_INDEX == 0:
#                     GameInit.LANGUAGE_INDEX = 1
#                 elif GameInit.LANGUAGE_INDEX == 1:
#                     GameInit.LANGUAGE_INDEX = 0
#         if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#         return self


# class VolumeSettingClass:
#     #Khai báo các thuộc tính của class: 
#     def __init__(self):
#         # Khởi tạo các thuộc tính. 
#         # Chú ý các thành phần như âm lượng hiện tại và chỉ số âm lượng được đánh dấu toàn cục. Sau này sẽ thêm các thuộc tính WINDOW
#         global present_volume, VOLUME_INDEX
#         # self.label1 = Label(screen.get_width() / 2 * 0.95, screen.get_height() / 2 * 0.4,125,50,'Mute Volume') # Dòng chữ 'Mute Volume'  
#         self.esc_button = Button((screen.get_width() / 2, screen.get_height() / 2 * 1.5),imageNormal = "back.png", imageChanged = "back2.png")    # Nút có chữ 'Back'
#         self.mute_button = Button((screen.get_width() / 2, screen.get_height() / 2 * 0.55),imageNormal = "mute.png", imageChanged = "mute2.png") # Nút có chữ 'Mute'
#         # self.label2 = Label(screen.get_width() / 2 * 0.92, screen.get_height() / 2 * 0.8,125,50,'Volume')     # dòng chữ "Volume"
#         self.minusVol_button = Button((screen.get_width() / 2 * 0.6, screen.get_height() / 2 * 0.95),imageNormal = "low.png", imageChanged = "low2.png") #Các nút +, - để tăng giảm âm lượng
#         self.plusVol_button = Button((screen.get_width() / 2 * 1.4, screen.get_height() / 2 * 0.95),imageNormal = "high.png", imageChanged = "high2.png")
#         self.display_volume_label = Label(screen.get_width() / 2 * 0.95, screen.get_height() / 2,50,50, f"{present_volume * 100}") # Trường hiển thị âm lượng hiện tại
        
#         self.isMute = False #Các biến khai báo. Ở đây là biến xác định xem có đang tắt âm hay không
#         #Các khai báo cho xác định âm lượng của âm thanh
#         self.volume_list = VOLUME
#         self.volume = present_volume
#         self.previous_volume = self.volume
        
#     #Hàm vẽ các đối tượng trên màn hình
#     def draw(self, mouse_pos):
#         #Vẽ lớp phủ hình chữ nhật kích thước bằng kích thước cửa sổ hiện hành
#         Background = pygame.image.load(LANGUAGE[GameInit.LANGUAGE_INDEX]+'soundMenu.png').convert_alpha()
#         Background = pygame.transform.smoothscale(Background, WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX])
#         screen.blit(Background,(0,0))
#         #Vẽ các thuộc tính khác đã nêu
#         # self.label1.draw(screen)
#         # self.label2.draw(screen)
#         self.esc_button.update(mouse_pos)
#         self.mute_button.update(mouse_pos)
#         self.plusVol_button.update(mouse_pos)
#         self.minusVol_button.update(mouse_pos)
#         self.display_volume_label.draw(screen)
#     #Cập nhật các trạng thái. Khai báo biến toàn cục là để giữ trạng thái âm lượng
#     def update(self, event):
#         global present_volume
#         global VOLUME_INDEX
#         #Lấy vị trí đầu con trỏ chuột
#         pos = pygame.mouse.get_pos()
#         #Kiểm tra xem có nhấn chuột không
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             #Hàm isOver kiểm tra xem con trỏ chuột có đè lên các thuộc tính Button trong khi đang nhấn nút chuột trái hay không
#             if self.esc_button.CheckClick(pos):
#                 return SettingClass() #Nếu nhấn chuột vào esc_button, trả về màn hình cài đặt
#             #Kiểm tra xem các nút cộng, trừ, có được nhấn hay không
#             if self.plusVol_button.CheckClick(pos): 
#                 # Kiểm tra chỉ số VOLUME_INDEX. Chừa giá trị biên phải ra vì khi điều kiện thỏa mãn 
#                 # VOLUME_INDEX + 1 vượt quá chỉ số max của list
#                 if 0 <= VOLUME_INDEX < len(self.volume_list) -1:
#                     VOLUME_INDEX += 1 #Lưu trữ các giá trị ra biến toàn cục
#                     self.volume = self.volume_list[VOLUME_INDEX] #gán giá trị cho biến volume của class
#                     present_volume = self.volume
#                     self.isMute = False
#                     if not self.isMute:
#                         self.mute_button.textIn = 'Mute'
#                     pygame.mixer.music.set_volume(present_volume) #Đặt âm lượng theo giá trị vừa gán
#                     self.display_volume_label.text = f'{present_volume * 100}'
#             if self.minusVol_button.CheckClick(pos):
#                 # Kiểm tra chỉ số VOLUME_INDEX. Chừa giá trị biên trái ra vì khi điều kiện thỏa mãn 
#                 # VOLUME_INDEX - 1 vượt quá chỉ số min của list
#                 if len(self.volume_list) - 1 >= VOLUME_INDEX > 0 :
#                     VOLUME_INDEX -= 1 #Lưu trữ các giá trị ra biến toàn cục
#                     self.volume = self.volume_list[VOLUME_INDEX] #gán giá trị cho biến volume của class
#                     present_volume = self.volume
#                     self.isMute = False
#                     if not self.isMute:
#                         self.mute_button.textIn = 'Mute'
#                     pygame.mixer.music.set_volume(present_volume) #Đặt âm lượng theo giá trị vừa gán
#                     self.display_volume_label.text = f'{present_volume * 100}' #Đặt nội dung label hiển thị âm lượng là âm lượng hiện tại
#             # Hàm kiểm tra xem nút Mute có được nhấn hay không:     
#             if self.mute_button.CheckClick(pos):
#                 if self.isMute == False:
#                     self.isMute = True #Trả về True cho isMute rồi thực hiện lệnh setvolume về 0
#                     if self.isMute:
#                         self.mute_button.imageNormal = 'unmute.png'
#                         self.mute_button.imageChanged = 'unmute2.png'
#                         self.volume = present_volume #Lưu trữ giá trị âm lượng
#                         present_volume = 0
#                         self.display_volume_label.text = "0" #Đưa giá trị âm lượng về 0
#                         pygame.mixer.music.set_volume(present_volume)
#                 #Kiểm tra xem liệu có nhấn lại nút tắt âm hay nhấn nút cộng trừ hay không
#                 elif self.isMute == True:
#                     self.isMute = False
#                     if not self.isMute:
#                         self.mute_button.imageNormal = 'mute.png'
#                         self.mute_button.imageChanged = 'mute2.png'
#                         present_volume=self.volume  # Khôi phục giá trị âm lượng
#                         self.display_volume_label.text = f'{present_volume * 100}' #Khôi phục giá trị hiển thị âm lượng hiện tại
#                         pygame.mixer.music.set_volume(present_volume)
#         return self
    
# #Quy định đối tượng màn hình cài đặt kích thước cửa sổ
# class WindowModeSettingClass:
#     def __init__(self):
#         #Khởi tạo các thuộc tính
#         self.fullScreenButton = Button(pos=(screen.get_width() / 2, screen.get_height() / 2 * 0.9), imageNormal = "continue.png", imageChanged = "continue2.png") # Nút để chỉnh chế độ cửa sổ, mặc định có text "Window"
#         self.halfScreenButton = Button(pos=(screen.get_width() / 2, screen.get_height() / 2 * 0.9), imageNormal = "continue.png", imageChanged = "continue2.png") # Nút chuyển kích thước cửa sổ. Mặc định là 1920x1080
#         self.esc_button = Button(pos=(screen.get_width() / 2, screen.get_height() / 2 * 1.2), imageNormal = "back.png", imageChanged = "back2.png") # Nút quay về
#     #Vẽ các thuộc tính lên bề mặt
#     def draw(self, mouse_pos):
#         global LANGUAGE_INDEX
#         Background = pygame.image.load(LANGUAGE[GameInit.LANGUAGE_INDEX]+'background.png').convert_alpha()
#         Background = pygame.transform.smoothscale(Background, WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX])
#         screen.blit(Background, (0, 0))
#         if halfScreen_active:
#             self.fullScreenButton.update(mouse_pos)
#         else:
#             self.halfScreenButton.update(mouse_pos)
#         self.esc_button.update(mouse_pos)
#     #Cập nhật trạng thái cho các thuộc tính
#     def update(self, event):
#         global halfScreen_active, screen
#         #Lấy vị trí đầu con trỏ chuột
#         pos = pygame.mouse.get_pos()
#         #Kiểm tra xem có nhấn chuột không
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             #Hàm isOver kiểm tra xem con trỏ chuột có đè lên các thuộc tính Button trong khi đang nhấn nút chuột trái hay không
#             if self.fullScreenButton.CheckClick(pos):
#                 GameInit.halfScreen_active = not GameInit.halfScreen_active
#                 GameInit.WINDOW_SIZE_INDEX = 0
#                 GameInit.SCREEN_SIZE_INDEX = 0
#                 return self
#             elif self.halfScreenButton.CheckClick(pos):
#                 GameInit.WINDOW_SIZE_INDEX = 1
#                 GameInit.SCREEN_SIZE_INDEX = 1
#                 GameInit.halfScreen_active = True
#                 return self
#             if self.esc_button.CheckClick(pos):
#                 return SettingClass() #Trả về màn hình cài đặt
#             elif event.type == pygame.VIDEORESIZE:
#                 # Xử lý sự kiện resize màn hình
#                 width, height = event.w, event.h
#                 screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
#         return self
        

# class MapSelection:
#     def draw(self, mouse_pos):
#         Background = pygame.image.load(LANGUAGE[GameInit.LANGUAGE_INDEX]+'mapselection.png').convert_alpha()
#         Background = pygame.transform.smoothscale(Background, WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX])
#         screen.blit(Background, (0, 0))
#     #Cập nhật trạng thái cho các thuộc tính
#     def update(self, event):
#         global InitGame, MAP_INDEX
#         if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE:
#                 Back_To_Menu = Pause_Game()
#                 if Back_To_Menu:
#                     InitGame = False
#                     return MenuClass()
#             if event.key == pygame.K_1:
#                 GameInit.set_choice = 1
#                 MAP_INDEX = 0
#                 return CharacterSelection()
#             if event.key == pygame.K_2:
#                 GameInit.set_choice = 2
#                 MAP_INDEX = 1
#                 return CharacterSelection()
#             if event.key == pygame.K_3:
#                 GameInit.set_choice = 3
#                 MAP_INDEX = 2
#                 return CharacterSelection()
#             if event.key == pygame.K_4:
#                 GameInit.set_choice = 4
#                 MAP_INDEX = 3
#                 return CharacterSelection()
#             if event.key == pygame.K_5:
#                 GameInit.set_choice = 5
#                 MAP_INDEX = 4
#                 return CharacterSelection()
                
#         return self
    
# class CharacterSelection: 
#     def draw(self, mouse_pos):
#         Background = pygame.image.load(LANGUAGE[GameInit.LANGUAGE_INDEX]+'choose.png').convert_alpha()
#         Background = pygame.transform.smoothscale(Background, WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX])
#         screen.blit(Background, (0, 0))
#     #Cập nhật trạng thái cho các thuộc tính
#     def update(self, event):
#         global InitGame
#         if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE:
#                 Back_To_Menu = Pause_Game()
#                 if Back_To_Menu:
#                     InitGame = False
#                     return MenuClass()
#             if event.key == pygame.K_1:
#                 GameInit.choice = 1
#                 return Shop()
#             if event.key == pygame.K_2:
#                 GameInit.choice = 2
#                 return Shop()
#             if event.key == pygame.K_3:
#                 GameInit.choice = 3
#                 return Shop()
#             if event.key == pygame.K_4:
#                 GameInit.choice = 4
#                 return Shop()
#             if event.key == pygame.K_5:
#                 GameInit.choice = 5
#                 return Shop()
                
#         return self


# class Shop: 
#     def draw(self, mouse_pos):
#         Background = pygame.image.load(LANGUAGE[GameInit.LANGUAGE_INDEX]+'shopee.png').convert_alpha()
#         Background = pygame.transform.smoothscale(Background, WINDOW_SIZES[GameInit.WINDOW_SIZE_INDEX])
#         screen.blit(Background, (0, 0))
#     #Cập nhật trạng thái cho các thuộc tính
#     def update(self, event):
#         global InitGame
#         if not InitGame:
#             init_character_luckybox()
#             InitGame = True
#         if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE:
#                 Back_To_Menu = Pause_Game()
#                 if Back_To_Menu:
#                     InitGame = False
#                     return MenuClass()
#             if event.key == pygame.K_1:
#                 GameInit.CHARACTERS[GameInit.choice - 1].NhanhNhen = True
#                 return Play()
#             if event.key == pygame.K_2:
#                 GameInit.CHARACTERS[GameInit.choice - 1].TroiHon = True
#                 return Play()
#             if event.key == pygame.K_3:
#                 GameInit.CHARACTERS[GameInit.choice - 1].PhanKhich = True
#                 return Play()
                
#         return self

# #Đây là main loop
# def main():
#     global login_lock
    
#     if not login_lock:
#         pygame.quit()
#         sys.exit()
#     #Lớp phủ xuất hiện đầu tiên chính là màn hình cài đặt
#     current_class = MenuClass()
#     #Vòng lặp chính
#     while True:  # Vòng lặp vô hạn, chương trình sẽ chạy cho đến khi có sự kiện thoát
#         for event in pygame.event.get():  # Duyệt qua tất cả sự kiện đang chờ xử lý trong hàng đợi sự kiện của Pygame
#             if event.type == pygame.QUIT:  # Nếu sự kiện là loại thoát (như nhấn nút đóng cửa sổ)
#                 pygame.quit()  # Thoát khỏi Pygame
#                 sys.exit()  # Thoát khỏi chương trình
#             current_class = current_class.update(event)  # Cập nhật trạng thái của đối tượng hiện tại dựa trên sự kiện
#         mouse_pos = pygame.mouse.get_pos()
#         current_class.draw(mouse_pos)  # Vẽ đối tượng hiện tại lên màn hình

#         pygame.display.flip()  # Cập nhật toàn bộ cửa sổ
#         clock.tick(60)  # Đảm bảo chương trình chạy không quá 60 khung hình/giây
# main()


# class SHOP:

#     def __init__(self):
#         pygame.init()
#         self.shoprunning = True
#         self.xSCREEN, self.ySCREEN = 1280, 720
#         self.SCREEN = pygame.display.set_mode((self.xSCREEN, self.ySCREEN))
#         # image
#         self.bgshop = pygame.image.load("image/shop/bgshop1.png")
#         self.note1 = pygame.image.load("image/shop/note1.png")
#         self.note2 = pygame.image.load("image/shop/note2.png")
#         self.note3 = pygame.image.load("image/shop/note3.png")
#         self.ball = pygame.image.load("image/shop/ball1.png")
#         self.hand1 = pygame.image.load("image/shop/hand1.png")
#         self.hand2 = pygame.image.load("image/shop/hand2.png")
#         self.hand3 = pygame.image.load("image/shop/hand3.png")
#         self.hand4 = pygame.image.load("image/shop/hand4.png")
#         self.hand5 = pygame.image.load("image/shop/hand5.png")
#         self.sold = pygame.image.load("image/shop/sold1.png")
#         # tien
#         self.file = open('money/player_money.txt', 'r')
#         self.money = int(self.file.readline().split('=')[0])
#         self.file.close()
#         self.moneyplus = 0
#         # vi tri
#         self.dx, self.dy = 10, 10
#         self.xnote, self.ynote = 0, 150
#         self.xMoney, self.yMoney = 10, 40
#         self.r = 150
#         self.xI, self.yI = 770, 350
#         self.x1 = self.xI
#         self.y1 = self.yI - self.r
#         self.x2 = self.xI + self.r * math.sin(math.pi / 5 * 2)
#         self.y2 = self.yI - self.r * math.cos(math.pi / 5 * 2)
#         self.x3 = self.xI + self.r * math.sin(math.pi / 5)
#         self.y3 = self.yI + self.r * math.cos(math.pi / 5)
#         self.x4 = self.xI - self.r * math.sin(math.pi / 5)
#         self.y4 = self.yI + self.r * math.cos(math.pi / 5)
#         self.x5 = self.xI - self.r * math.sin(math.pi / 5 * 2)
#         self.y5 = self.yI - self.r * math.cos(math.pi / 5 * 2)
#         # cac bien kiem tra
#         self.k = 1
#         self.s = 0
#         # phim
#         self.K_LEFT = self.K_RIGHT = self.K_SPACE = self.K_DONE = False        
#         # bua
#         self.num = 0
#         self.num_bua1 = 0
#         self.num_bua2 = 0
#         self.num_bua3 = 0
#         self.num_bua4 = 0
#         # delay
#         self.clock = pygame.time.Clock()
#         self.FPS = 60

#     def show_note(self, s):
#         if s == 0:
#             self.SCREEN.blit(self.note1, (self.xnote, self.ynote))
#         if s >= 1:
#             self.SCREEN.blit(self.note2, (self.xnote, self.ynote))
#             self.show_money(600, 620, "ENTER TO CONTINUE", 40)

#     def show_money(self, x, y, money, size):
#         font = pygame.font.Font("font/minigame.ttf", size)
#         money = font.render(str(money), True, (255, 255, 255))
#         self.SCREEN.blit(money, (x, y))

#     def move_hand(self, k):
#         if k == 1:
#             self.SCREEN.blit(self.hand1, (self.xI + self.dx, self.yI - self.dy))
#         if k == 2:
#             self.SCREEN.blit(self.hand2, (self.xI + self.dx, self.yI - self.dy))
#         if k == 3:
#             self.SCREEN.blit(self.hand3, (self.xI + self.dx, self.yI - self.dy))
#         if k == 4:
#             self.SCREEN.blit(self.hand4, (self.xI + self.dx, self.yI - self.dy))
#         if k == 5:
#             self.SCREEN.blit(self.hand5, (self.xI + self.dx, self.yI - self.dy))

#     def sold_ball(self, k, s):
#         if s == 2:
#             if k == 1:
#                 self.SCREEN.blit(self.sold, (self.x1, self.y1))
#             if k == 2:
#                 self.SCREEN.blit(self.sold, (self.x2, self.y2))
#             if k == 3:
#                 self.SCREEN.blit(self.sold, (self.x3, self.y3))
#             if k == 4:
#                 self.SCREEN.blit(self.sold, (self.x4, self.y4))
#             if k == 5:
#                 self.SCREEN.blit(self.sold, (self.x5, self.y5))

#     def num_bua(self, num):
#         if num == 1:
#             self.num_bua1 = self.num_bua1 + 1
#         if num == 2:
#             self.num_bua2 = self.num_bua2 + 1
#         if num == 3:
#             self.num_bua3 = self.num_bua3 + 1
#         if num == 4:
#             self.num_bua4 = self.num_bua4 + 1

#     def run(self):
#         global lock_shop, MONEY
#         while self.shoprunning and lock_shop == False:
#             self.clock.tick(self.FPS)
#             # insert image
#             self.SCREEN.blit(self.bgshop, (0, 0))
#             self.show_money(self.xMoney, self.yMoney, "Money: {}".format(self.money), 32)
#             self.show_money(self.x1 + 50, self.y1 - 30, "100", 20)
#             self.show_money(self.x2 + 50, self.y2 - 30, "100", 20)
#             self.show_money(self.x3 + 50, self.y3 - 30, "100", 20)
#             self.show_money(self.x4 + 50, self.y4 - 30, "100", 20)
#             self.show_money(self.x5 + 50, self.y5 - 30, "100", 20)
#             self.SCREEN.blit(self.ball, (self.x1, self.y1))
#             self.SCREEN.blit(self.ball, (self.x2, self.y2))
#             self.SCREEN.blit(self.ball, (self.x3, self.y3))
#             self.SCREEN.blit(self.ball, (self.x4, self.y4))
#             self.SCREEN.blit(self.ball, (self.x5, self.y5))
#             self.move_hand(self.k)
#             self.show_note(self.s)

#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:  # su kien nhan thoat
#                     self.file.close()
#                     self.shoprunning = False
#                     pygame.quit()
#                     sys.exit()  # thoat chuong trinh

#                 if event.type == pygame.KEYDOWN:  # su kien co phim nhan xuong
#                     if event.key == pygame.K_LEFT:
#                         self.K_LEFT = True
#                     if event.key == pygame.K_RIGHT:
#                         self.K_RIGHT = True
#                     if event.key == pygame.K_SPACE:
#                         self.K_SPACE = True
#                         pygame.mixer.init()
#                         pygame.mixer.music.load('sounds/sold.mp3')
#                         pygame.mixer.music.play()

#                     if event.key == pygame.K_RETURN:
#                         self.K_DONE = True

#                 if event.type == pygame.KEYUP:  # su kien tha phm
#                     if event.key == pygame.K_LEFT:
#                         self.K_LEFT = False
#                     if event.key == pygame.K_RIGHT:
#                         self.K_RIGHT = False
#                     if event.key == pygame.K_SPACE:
#                         self.K_SPACE = False
#                     if event.key == pygame.K_RETURN:
#                         self.K_DONE = False

#             if self.K_LEFT and self.s == 0:
#                 self.k = self.k - 1
#                 if self.k < 1:
#                     self.k = self.k + 5
#                 if self.k > 5:
#                     self.k = self.k - 5
#                 self.K_LEFT = False
#             if self.K_RIGHT and self.s == 0:
#                 self.k = self.k + 1
#                 if self.k < 1:
#                     self.k = self.k + 5
#                 if self.k > 5:
#                     self.k = self.k - 5
#                 self.K_RIGHT = False
#             if self.K_SPACE and self.s == 0:
#                 self.file = open('sounds/battat.txt','r')
#                 self.file.seek(0)
#                 self.sound = str(self.file.readline())
#                 # if self.sound == 'On':
#                     # pygame.mixer.init()
#                     # pygame.mixer.music.load('sounds/sold.mp3')
#                     # pygame.mixer.music.play()

#                 self.s = self.s + 1
#                 self.K_SPACE = False

#             if self.s == 1 and self.money >= 100:
#                 self.moneyplus = self.moneyplus - 100
#                 self.num = random.randint(1, 4)
#                 self.file = open('money/player_money.txt', 'w')
#                 self.money = self.money + self.moneyplus
#                 self.file.write(str(self.money))
#                 self.file.seek(0)
#                 self.file.close()
#                 self.s = self.s + 1

#             self.num_bua(self.num)
#             self.sold_ball(self.k, self.s)
#             MONEY = self.money

#             if self.s == 1 and self.money <= 99:
#                 self.SCREEN.blit(self.note3, (self.xnote, self.ynote))

#             if self.K_DONE and self.s >= 1:
#                 lock_shop = True
#                 self.file = open('sounds/battat.txt','r')
#                 self.file.seek(0)
#                 self.sound = str(self.file.readline())
#                 if self.sound == 'On':
#                     if numMap == 1:
#                         pygame.mixer.music.load('sounds/cheering1.mp3')
#                         pygame.mixer.music.play()
#                     if numMap == 2:
#                         pygame.mixer.music.load('sounds/cheering2.mp3')
#                         pygame.mixer.music.play()
#                     if numMap == 3:
#                         pygame.mixer.music.load('sounds/cheering3.mp3')
#                         pygame.mixer.music.play()
#                     if numMap == 4:
#                         pygame.mixer.music.load('sounds/cheering4.mp3')
#                         pygame.mixer.music.play()
#                     if numMap == 5:
#                         pygame.mixer.music.load('sounds/cheering5.mp3')
#                         pygame.mixer.music.play()
#                 self.K_DONE = False
#             pygame.display.update()