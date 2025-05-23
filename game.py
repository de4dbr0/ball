import pygame
from pygame.locals import *
from circle import Ball # Import Ball class specifically
import random
ball_list=[]
pygame.init()
white=(255,255,255)
red=(255,0,0)
blue=(0,0,255)
width, height= 640,480
screen =pygame.display.set_mode((width,height))
fps =10
clock =pygame.time.Clock()
maxradius=50
maxvelocity=50
minvelocity=-50
dt=0.1
def generateRandomBall():
    random_x=random.randint(0,width)
    random_vx=random.randint(minvelocity,maxvelocity)
    random_vy = random.randint(minvelocity, maxvelocity)
    random_radius=random.randint(0,maxradius)
    random_y=random.randint(0,height)
    random_red=random.randint(0,255)
    random_green = random.randint(0, 255)
    random_blue = random.randint(0, 255)
    random_color=(random_red, random_green, random_blue)
    # Return a Ball object instead of a tuple
    return Ball(random_x, random_y, random_vx, random_vy, random_radius, random_color)

running = True
while True:
    for event in pygame.event.get():
        if event.type == QUIT: # Add a way to quit the game
            running = False
        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                print("backspace")
                # Potentially add logic here if backspace should do something
            # Un-nest K_ESCAPE from K_BACKSPACE
            if event.key == K_ESCAPE:
                print("escape - adding a new ball")
                newball = generateRandomBall()
                ball_list.append(newball)

    if not running: # Check if we should exit the loop
        break

    # Game logic updates should happen every frame, outside the event loop
    for ball_obj in ball_list: # Use a different variable name to avoid confusion if 'ball' is used elsewhere
        # Pass width, height, minvelocity, and maxvelocity to update_position
        ball_obj.update_position(dt, width, height, minvelocity, maxvelocity)

    # Drawing should happen every frame, after updates
    screen.fill(white) # Clear the screen

    for ball_obj in ball_list:
        # Ensure ball_obj is a Ball instance (which it should be now)
        pygame.draw.circle(screen, ball_obj.color, (int(ball_obj.x), int(ball_obj.y)), ball_obj.radius)

    # Update the display and tick the clock once per frame
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
