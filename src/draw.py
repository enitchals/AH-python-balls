import sys
import pygame #TODO:  Fix intellisense
import random

from pygame.math import Vector2

from ball import *
from block import *

SCREEN_SIZE = [800,800]
BACKGROUND_COLOR = [255, 255, 255]


def debug_create_balls(object_list):
    ball = Ball(SCREEN_SIZE, Vector2(50, 50), Vector2(3, 3), [255, 0, 0], 10)
    object_list.append(ball)

    bouncing_ball = BouncingBall(SCREEN_SIZE, Vector2(75,75), Vector2(4,4), [0, 255, 0], 10)
    object_list.append(bouncing_ball)

    rainbow_ball = RainbowBall(SCREEN_SIZE, Vector2(100,100), Vector2(5,2), [0, 0, 0], 10)
    object_list.append(rainbow_ball)

def debug_create_all_things_balls(object_list):
    for i in range(0,5):
        ball = AllTheThings(1, object_list, SCREEN_SIZE, Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1]-20)), Vector2(2*random.random() - 2, 2*random.random() - 2), [random.randint(0,255),random.randint(0,255),random.randint(0,255)], random.randint(3,20))
        object_list.append(ball)
    
def debug_create_blocks(object_list):
    block = Block(SCREEN_SIZE, Vector2(100,100), 20, 20, [0,255,0])
    object_list.extend((block, ))

def add_ball(object_list):
    ball = AllTheThings(1, object_list, SCREEN_SIZE, Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1]-20)), Vector2(2*random.random() - 2, 2*random.random() - 2), [random.randint(0,255),random.randint(0,255),random.randint(0,255)], random.randint(3,20))
    object_list.append(ball)

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    object_list = [] # list of objects of all types in the toy

    # BOUNCE = True

    debug_create_balls(object_list)
    debug_create_all_things_balls(object_list)
    # debug_create_blocks(object_list)
     
    while (True): # TODO:  Create more elegant condition for loop
        global BACKGROUND_COLOR
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:  #TODO:  Get working
                if event.key == pygame.K_UP:
                    for item in object_list:
                        y = item.velocity.y
                        item.velocity.y = (0 - abs(y))
                if event.key == pygame.K_DOWN:
                    for item in object_list:
                        item.bounce = False
                        y = item.velocity.y
                        item.velocity.y = abs(y)
                        # item.velocity.x = 0
                if event.key == pygame.K_b:
                    BACKGROUND_COLOR = [0, 0, 0]
                if event.key == pygame.K_w:
                    BACKGROUND_COLOR = [255, 255, 255]
                if event.key == pygame.K_SPACE:
                    # BOUNCE = not(BOUNCE)
                    for item in object_list:
                        if isinstance(item, AllTheThings):
                            item.bounce = not(item.bounce)
                if event.key == pygame.K_n:
                    add_ball(object_list)

        for item in object_list:
            if hasattr(item, "bounce"):
                if item.bounce:
                    item.update()
            else:
                item.update()

        # Draw Loop
        screen.fill(BACKGROUND_COLOR)
        for item in object_list:
            item.draw(screen, pygame)
 
        clock.tick(60)
        pygame.display.flip()
 
    # Close everything down
    pygame.quit()
 
if __name__ == "__main__":
    main()
