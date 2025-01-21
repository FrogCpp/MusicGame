from PyChecha import MainScene # this is a main file! ! ! ! !
import pygame

WIDTH = 500
HEIGHT = 500
FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
MyScene = MainScene(pygame.key.name(pygame.K_w), pygame.key.name(pygame.K_a),
                     pygame.key.name(pygame.K_s), pygame.key.name(pygame.K_d))
running = True
while running:
    screen.fill(BLACK)
    clock.tick(FPS)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) in MyScene.Input:
                MyScene.Input[pygame.key.name(event.key)] = 1

        if event.type == pygame.KEYUP:
            if pygame.key.name(event.key) in MyScene.Input:
                MyScene.Input[pygame.key.name(event.key)] = 0



    MyScene.UpdateScene()
    for i in MyScene:
        i = i.Draw()
        iR = pygame.Rect(i[0][0], i[0][1], i[0][2], i[0][3])
        if not isinstance(i[1], str):
            pygame.draw.rect(screen, color=i[1], rect=iR)
        else:
            screen.blit(source=pygame.transform.smoothscale(pygame.image.load(i[1]), (i[0][2], i[0][3])), dest=iR)


    pygame.display.flip()

pygame.quit()