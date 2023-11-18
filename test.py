import pygame
from objects import Player
from objects import Platform
pygame.init()

window = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")

# player vars
x = 0
y = 400
width = 40
height = 60
vel = 5

# platform vars
px1 = 100
py1 = 300
pwidth1 = 100
pheight1 = 10

# player
player = Player(x, y, width, height)

# platforms
platform1 = Platform(px1, py1, pwidth1, pheight1)

isJump = False
jumpCount = 10

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a] and player.x > vel: 
        player.x -= vel

    if keys[pygame.K_d] and player.x < 500 - vel - player.width:  
        player.x += vel
        
    if not(isJump): 
        #print("not jumping")
        #if keys[pygame.K_w] and player.y > vel:
            #player.y -= vel

        #if keys[pygame.K_s] and player.y < 500 - player.height - vel:
            #player.y += vel

        if keys[pygame.K_n]:
            isJump = True
    else:
        #print("jumping")
        if jumpCount >= -10:
            player.y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False
    
    window.fill((255,255,255))
    Player.create(player, window)
    Platform.create(platform1, window)
    pygame.display.update() 
    
pygame.quit()