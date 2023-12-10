import pygame, sys
from pygame.locals import *
# Kích thước cửa sổ
WINDOWS_SIZE = [(1536,864),(768,432)]
WINDOWS_INDEX = 0
# Khai báo thành phần tỉ lệ
ratio = WINDOWS_SIZE[WINDOWS_INDEX][0]/ WINDOWS_SIZE[0][0]
# Kết quả chọn map
index = None # Up này vô Game Function dưới dạng biến cục bộ
# Có class rồi cop vào GameFunction ha j đó cx đc
class ChooseCharacter:
    global index
    def __init__(self):
        # Nhập tỉ lệ màn hình từ cửa sổ bên ngoài
        global ratio
        # Khởi tạo kích thước cửa sổ
        self.window_width, self.window_height = WINDOWS_SIZE[WINDOWS_INDEX]
        # Khởi tạo cửa sổ màn hình
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        # Load và điều chỉnh kích thước hình nền
        self.background = pygame.image.load('./assets/background/ENG/choosemap1.jpg')
        self.background = pygame.transform.scale(self.background, (self.window_width, self.window_height))
        self.scale = 2 * ratio 
        # Load hình ảnh của các map và điều chỉnh kích thước lên 30%
        self.chars = [pygame.transform.scale(pygame.image.load(f'./assets/characters/Char{i}Map1_1.png'), (int(self.scale * pygame.image.load(f'./assets/characters/Char{i}Map1_1.png').get_width()), int(self.scale * pygame.image.load(f'./assets/characters/Char{i}Map1_1.png').get_height()))) for i in range(1, 6)]
        # Load hình ảnh cho nút "back" scale 30%
        self.back_button_img = pygame.transform.scale(pygame.image.load('assets/background/ENG/back.png'), (3 * int(self.scale * pygame.image.load('assets/background/ENG/back.png').get_width()), 3 * int(self.scale * pygame.image.load('./assets/background/ENG/back.png').get_height())))
        # Đặt nút "Back" ở giữa màn hình
        self.back_button = pygame.draw.rect(self.screen, (255, 165, 0), (self.window_width / 2 - self.back_button_img.get_width() / 2, self.window_height - self.window_height / 9, self.back_button_img.get_width(), self.back_button_img.get_height()))
    def draw(self):
        # Vẽ hình nền lên màn hình
        self.screen.blit(self.background, (0, 0))
        # Vẽ hình ảnh của các character lên màn hình
        for i, map_img in enumerate(self.chars):
            y = self.window_height / 24 * 6
            x = self.window_width / 2 - int(self.scale * pygame.image.load(f'./assets/characters/Char{i + 1}Map1_1.png').get_width()) / 2 + (i - 2) * (int(self.scale * pygame.image.load(f'./assets/characters/Char{i + 1}Map1_1.png').get_width()) / 2 + int(self.scale * pygame.image.load(f'./assets/characters/Char{i + 1}Map1_1.png').get_width()))
            self.screen.blit(map_img, (x, y))
        # Vẽ nút back lên màn hình
        self.screen.blit(self.back_button_img, (self.back_button.x, self.back_button.y))

    def update(self, event):
        # Cập nhật trạng thái của các map khi rê chuột lên và nhấn chuột
        for i, map_img in enumerate(self.chars):
            y = self.window_height / 24 * 6
            x = self.window_width / 2 - int(self.scale * pygame.image.load(f'./assets/characters/Char{i + 1}Map1_1.png').get_width()) / 2 + (i - 2) * (int(self.scale * pygame.image.load(f'./assets/characters/Char{i + 1}Map1_1.png').get_width()) / 3 + int(self.scale * pygame.image.load(f'./assets/characters/Char{i + 1}Map1_1.png').get_width()))
            rect_x = x
            rect_y = y
            if pygame.Rect(x, y, map_img.get_width(), map_img.get_height()).collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.screen, (255, 255, 255), (x, y, map_img.get_width(), map_img.get_height()), 2)
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    self.go_to_play(i) # viết tạm
            else:
                pygame.draw.rect(self.screen, (0, 0, 0), (x, y, map_img.get_width(), map_img.get_height()), 2)
        # Cập nhật trạng thái của nút "Back" khi rê chuột lên và nhấn chuột
        if self.back_button.collidepoint(pygame.mouse.get_pos()):
            # Nếu rê chuột lên nút "Back", thay đổi hình ảnh thành "back2.png"
            self.back_button_img = pygame.transform.scale(pygame.image.load('assets/background/ENG/back2.png'), (0.3 * int(self.scale * pygame.image.load('assets/background/ENG/back2.png').get_width()), 0.3 * int(self.scale * pygame.image.load('assets/background/ENG/back2.png').get_height())))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                self.back()
        else:
            self.back_button_img = pygame.transform.scale(pygame.image.load('assets/background/ENG/back.png'), (0.3 * int(self.scale * pygame.image.load('assets/background/ENG/back2.png').get_width()), 0.3 * int(self.scale * pygame.image.load('assets/background/ENG/back2.png').get_height())))


    def go_to_play(self, i):
        print(i) # Để tạm 

    def back(self):
        pygame.quit() # Để tạm
        sys.exit() # Để tạm

def main():
    # Khởi tạo Pygame
    pygame.init()
    # Tạo font chữ
    font = pygame.font.Font('./assets/font/SVN-Retron_2000.ttf', 50)
    # Thiết lập kích thước cửa sổ
    screen = pygame.display.set_mode(WINDOWS_SIZE[WINDOWS_INDEX])
    clock = pygame.time.Clock()
    # Tạo hình chữ nhật, hộp văn bản và nú
    #Vẽ các đối tượng lên màn hình
    #Vẽ nền lên
    current_class = ChooseCharacter() 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            else:
                current_class.update(event)
        current_class.draw()
        # Cập nhật màn hình
        pygame.display.flip()
        clock.tick(60)
main()