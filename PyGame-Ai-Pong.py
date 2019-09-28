import pygame
pygame.init()

win = pygame.display.set_mode((800,800)) #Windows Size
pygame.display.set_caption("Pong")#Name of the Window

ax = 50
ay = 50
width = 10
height = 70
vel = 20

bx = 750
by = 50

run = True
while run:
    
    keys = pygame.key.get_pressed()
    
    pygame.time.delay(0)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if keys[pygame.K_UP]:
        ay -= vel
    if keys[pygame.K_DOWN]:
        ay += vel
    if keys[pygame.K_w]:
        by -= vel
    if keys[pygame.K_s]:
        by += vel
    if ay > 730 or ay < 0:
        if ay > 730:
            ay = 730
        else:
            ay = 0
    if by > 730 or by < 0:
        if by > 730:    
            by = 730
        else:
            by = 0
    
    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (ax, ay, width, height))
    pygame.draw.rect(win, (255,0,0), (bx, by, width, height))
    pygame.display.update()
    
    
pygame.quit()