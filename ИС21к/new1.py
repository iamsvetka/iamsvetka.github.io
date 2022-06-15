import pygame
from random import randint
from time import time

pygame.init()

'''создаём окно программы'''

# цвет фона (background)
back = (200, 255, 255)

w = 700
h = 500

# окно программы, window - просто переменная
window = pygame.display.set_mode((w, h))

# заливаем окно цветом back
window.fill(back)

clock = pygame.time.Clock()

game = True
FPS = 40

# шрифт для надписи
t_time = pygame.font.Font(None, 50)
text_time = t_time.render('Время:', True, (0, 0, 0))
window.blit(text_time, (20, 20))

t_score = pygame.font.Font(None, 50)
text_score = t_score.render('Счёт:', True, (0, 0, 0))
window.blit(text_score, (w - 150, 20))


r1 = pygame.Rect(50, 100, 100, 250)
# рисуем в окне window прямоугольник r1 цветом (46, 139, 87)
pygame.draw.rect(window, (46, 139, 87), r1)
pygame.draw.rect(window, (255, 255, 255), r1, 10)

# шрифт для надписи
f1 = pygame.font.Font(None, 20)
text1 = f1.render('КЛИК', True, (255, 255, 255))
window.blit(text1, (r1.x + 20, 150))

r2 = pygame.Rect(170, 100, 100, 250)
pygame.draw.rect(window, (46, 139, 87), r2)
pygame.draw.rect(window, (255, 255, 255), r2, 10)

'''r3 = pygame.Rect(120, 0, 100, 250)
pygame.draw.rect(window, (46, 139, 87), r3)

r4 = pygame.Rect(200, 0, 100, 250)
pygame.draw.rect(window, (46, 139, 87), r4)'''

wait = 0 # счётчик для подсчёта кадров
while game:
    pygame.display.update()


    for event in pygame.event.get():
        # чтобы окно закрывалось по нажатию на Крестик
        if event.type == pygame.QUIT:
            game = False

        # если случилось событие нажатие кнопки мыши
        # сохранить координаты клика
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if r1.collidepoint(x, y):
                print('Попал!')
                pygame.draw.rect(window, (255, 0, 0), r1)


    if wait == 0:
        wait = 20

        num = randint(1, 5)
        if num == 1:
            window.blit(text1, (r1.x + 20, 150))
            pygame.draw.rect(window, (46, 139, 87), r2)

        if num == 2:
            pygame.draw.rect(window, (46, 139, 87), r1)
            window.blit(text1, (r2.x + 20, 150))
    else:
        wait -= 1

    clock.tick(FPS)


'''game = True
FPS = 40

r1 = pygame.Rect(50, 50, 100, 350)
pygame.draw.rect(window, (220, 20, 60), r1)
pygame.draw.rect(window, (255, 255, 255), r1, 10)

f1 = pygame.font.Font(None, 23)
text1 = f1.render('CLICK', True, (255, 255, 255))
window.blit(text1, (70, 150))


r2 = pygame.Rect(120, 50, 50, 150)
pygame.draw.rect(window, (220, 20, 60), r2)

r3 = pygame.Rect(190, 50, 50, 150)
pygame.draw.rect(window, (220, 20, 60), r3)

r4 = pygame.Rect(260, 50, 50, 150)
pygame.draw.rect(window, (220, 20, 60), r4)
'''