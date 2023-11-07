import pygame
import player

pygame.init()
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
running = True
dt = 0

p1 = player.Player(50,50,"red")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("green")
    pygame.draw.rect(screen,"black",(p1.pos.pos_x,p1.pos.pos_y,25,25))
    pygame.display.flip()

    #keyevents
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        p1.pos.pos_y -= 100 *dt
    if keys[pygame.K_s]:
        p1.pos.pos_y += 100 *dt
    if keys[pygame.K_a]:
        p1.pos.pos_x -= 100 * dt
    if keys[pygame.K_d]:
        p1.pos.pos_x += 100 * dt

    dt = clock.tick(60)/ 1000



pygame.quit()