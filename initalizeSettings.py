from PyChecha import MainScene  # this is a main file! ! ! ! !
import pygame
import os
# a = open(f"{os.path.join(os.environ['USERPROFILE'], 'Desktop', 'stp.txt')}", 'w')
# a.close()

WIDTH = 500
HEIGHT = 600
FPS = 30

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
MyScene = MainScene(pygame.key.name(pygame.K_w), pygame.key.name(pygame.K_a), pygame.key.name(pygame.K_s), pygame.key.name(pygame.K_d), 1, 3)
print(MyScene)
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

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.dict['button'] in MyScene.Input:
                MyScene.Input[event.dict['button']] = 1

        if event.type == pygame.MOUSEBUTTONUP:
            if event.dict['button'] in MyScene.Input:
                MyScene.Input[event.dict['button']] = 0

    MyScene.UpdateScene()
    for obj in MyScene:
        try:
            coord, color_or_texture, *area = obj.Draw()
            iR = pygame.Rect((coord[0], coord[1], coord[2]['x'], coord[2]['y']))
            if isinstance(color_or_texture, tuple):
                pygame.draw.rect(screen, color=color_or_texture, rect=iR)
            else:
                tx = color_or_texture
                if not area:
                    screen.blit(source=tx,
                                dest=(coord[0], coord[1]))
                else:
                    a = tx.get_rect().center
                    coord[0] -= (a[0] / area[1]) / 1.5
                    coord[1] -= a[1]
                    screen.blit(
                        source=tx,
                        area=pygame.Rect(area[0]),
                        dest=(coord[0], coord[1]),
                        )
        except Exception as e:
            print(e)

    pygame.display.flip()

pygame.quit()
