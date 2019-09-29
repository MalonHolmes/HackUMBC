import pygame
pygame.init()

win = pygame.display.set_mode((800,800)) #Windows Size
pygame.display.set_caption("Pong")#Name of the Window
class player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 20
        self.color = color
        self.isLost = False

class ball:
    def __init__(self, x, y, radius, width, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.width = width
        self.color = color
        self.vel = 15


run = True

p1 = player(50,50,10,70,(255,0,0))
p2 = player(750,50,10,70,(0,0,255))
ball = ball(200,200,3,3,(0,255,0))

while run:
    
    
    keys = pygame.key.get_pressed()
    ball.x += ball.vel
    ball.y += ball.vel
    
    pygame.time.delay(0)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if keys[pygame.K_UP]:
        p1.y -= p1.vel
    if keys[pygame.K_DOWN]:
        p1.y += p1.vel
    if keys[pygame.K_w]:
        p2.y -= p2.vel
    if keys[pygame.K_s]:
        p2.y += p2.vel
    if p1.y > 730 or p1.y < 0:
        if p1.y > 730:
            p1.y = 730
        else:
            p1.y = 0
    if p2.y > 730 or p2.y < 0:
        if p2.y > 730:    
            p2.y = 730
        else:
            p2.y = 0
    
    win.fill((0,0,0))
    pygame.draw.rect(win, p1.color, (p1.x, p1.y, p2.width, p2.height))
    pygame.draw.rect(win, p2.color, (p2.x, p2.y, p2.width, p2.height))
    pygame.draw.line(win, (255,255,255),(400,0),(400,800))
    pygame.draw.circle(win, ball.color, (ball.x,ball.y) ,ball.radius, ball.width)
    pygame.display.update()
    
    
pygame.quit()
