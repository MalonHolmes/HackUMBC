"""Still needs to be done
Scoreboard []
Interaction with peg []
Random start []
New Game restart []
Put X in box once completed
"""

import pygame
pygame.init()

win = pygame.display.set_mode((800,800)) #Windows Size
pygame.display.set_caption("Pong")#Name of the Window
class player:
    def __init__(self, x, y, width, height, color): # Initializes object player
        self.x = x # X Coordinate for object player
        self.y = y # Y Coordinate for object player
        self.width = width # Sets width of object if choosen to draw
        self.height = height # Sets height of object if choosen to draw
        self.vel = 20 # Speed in which player can mover
        self.color = color # Gives the players color
        self.isLost = False # Determines if player lost game

class ball:
    def __init__(self, x, y, radius, width, color):
        self.x = x #ball x coordinate
        self.y = y # ball y coordinate
        self.radius = radius # ball radius
        self.width = width # ball width if choosen to draw
        self.color = color # ball color if choosen to draw
        self.vel = 15 # velocity
        self.state = 0 # ball state for movement
def ballMovement(obj,state): # Determines the direction the ball will move with interaction
    if state == 0: #\> (Backright)
        obj.x += obj.vel - 5
        obj.y += obj.vel
    if state == 1: #/> (Upright)
        obj.x += obj.vel - 5
        obj.y -= obj.vel
    if state == 2: #</ (Downleft)
        obj.x -= obj.vel - 5
        obj.y += obj.vel
    if state == 3: # <\ (Upleft)
        obj.x -= obj.vel - 5
        obj.y -= obj.vel

run = True

p1 = player(50,50,10,70,(255,0,0)) # Player 1
p2 = player(750,50,10,70,(0,0,255)) # Player 2
ball = ball(400,400,3,3,(0,255,0)) # Ball

while run:
    
    
    keys = pygame.key.get_pressed()
    ballMovement(ball, ball.state)
    
    
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
    if ball.y > 800 and ball.state == 0:
        ball.y = 800
        ball.state = 1
    if ball.y > 800 and ball.state == 2:
        ball.y = 800
        ball.state = 3
    if ball.x > 800  and ball.state == 0:
        ball.x = 800
        ball.state = 2
    if ball.x > 800 and ball.state == 1:
        ball.x = 800
        ball.state = 3
    if ball.y < 0 and ball.state == 3:
        ball.y = 0
        ball.state = 2
    if ball.y < 0 and ball.state == 1:
        ball.y = 0
        ball.state = 0
    if ball.x < 0 and ball.state == 2:
        ball.x = 0
        ball.state = 0
    if ball.x < 0 and ball.state == 3:
        ball.x = 0
        ball.state = 1
        
        
    
    win.fill((0,0,0))
    pygame.draw.rect(win, p1.color, (p1.x, p1.y, p1.width, p1.height)) # Player 1 Peg
    pygame.draw.rect(win, p2.color, (p2.x, p2.y, p2.width, p2.height)) # Player 2 Peg
    pygame.draw.line(win, (255,255,255),(400,0),(400,800)) # Middle Line
    pygame.draw.circle(win, ball.color, (ball.x,ball.y) ,ball.radius, ball.width) # Ball
    pygame.display.update() # Refreshes screen so objects dont duplicate
    
    
pygame.quit() # Quits the game once window is closed
