import pygame.math

from engine import *

pygame.init()

#window info
useScreen = True
screenWidth, screenHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
width = 1000
height = 1000
window = Window(width,height,0, "Practice project")
if useScreen:
    window = Window(screenWidth, screenHeight, pygame.FULLSCREEN, "Practice project")
    width = screenWidth
    height = screenHeight

clock = pygame.time.Clock()

# player info
playerInitPos = pygame.math.Vector2(width/2, 0)
playerInitVel = pygame.math.Vector2(0, 0)
playerSize = 20
playerColor = (0,255,0)

player = Player(window, playerInitPos, playerInitVel, playerSize, playerColor)

running = True
while running:
    # input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

            if event.key == pygame.K_LEFT:
                player.velocity += pygame.math.Vector2(-player.playerSpeed, 0)

            elif event.key == pygame.K_RIGHT:
                player.velocity += pygame.math.Vector2(player.playerSpeed, 0)

            elif event.key == pygame.K_SPACE:
                pause = True

            elif event.key == pygame.K_UP:
                pass

            elif event.key == pygame.K_DOWN:
                pass


        # if keyup
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.velocity += pygame.math.Vector2(player.playerSpeed, 0)

            elif event.key == pygame.K_RIGHT:
                player.velocity += pygame.math.Vector2(-player.playerSpeed, 0)

            elif event.key == pygame.K_SPACE:
                pause = False

    # update

    if player.pos.x <= 0  or player.pos.x >= width:
        player.velocity.x = -player.velocity.x

    if player.pos.y <= 0 or player.pos.y >= height:
        player.velocity.y = -player.velocity.y


    player.update()

    # render
    window.clear()

    # draw below here

    player.draw()

    window.swapBuffers()

    # frame rate
    clock.tick(60)

pygame.quit()
