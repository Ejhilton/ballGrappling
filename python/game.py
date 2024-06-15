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
playerInitPos = pygame.math.Vector2(width/2, height/2)
playerInitVel = pygame.math.Vector2(0, 0)
playerSize = 20
playerColor = "Green"

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

    # update
    player.update()

    # render
    window.clear()

    # draw below here

    player.draw()

    window.swapBuffers()

    # frame rate
    window.clock.tick(60)

pygame.quit()
