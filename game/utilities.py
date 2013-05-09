# Utility Functions

import platform
if platform.system() == 'Windows':
    from time import clock as getTime
else:
    from time import time as getTime

def distance(point1x, point1y, point2x, point2y):
    '''
    Use Pythagorus' theorem to calculate distance of two cartesian points
    '''
    return ((point1x - point2x) ** 2 + (point1y - point2y) ** 2) ** 0.5

# Pygame Utilities
import pygame

def launch_pygame_window(width, height):
    '''
    Launches a pygame window
    '''
    pygame.init()
    pygame.display.init()
    return pygame.display.set_mode((width, height), 0)
    

def set_pygame_caption(caption):
    '''
    Sets the caption on the pygame window
    '''
    pygame.display.set_caption(caption)

def close_pygame_window():
    '''
    Closes the pygame window
    '''
    pygame.quit()

def run_pygame_loop(gameObj):
    '''
    Runs a game loop.
    '''
    screen = launch_pygame_window(*gameObj.getSize())
    set_pygame_caption(gameObj.getCaption())
    lastTime = getTime()
    try:
        finished = False
        while not finished:
            # Process the events in the event queue.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                    break
                elif event is not None:
                    gameObj.processEvent(event)

            # Give things an opportunity to update their state.
            now = getTime()
            deltaT = now - lastTime
            lastTime = now
            
            gameObj.tick(deltaT)

            if pygame.display.get_active():
                # Update the screen.
                try:
                    gameObj.draw(screen)
                except pygame.error, e:
                    # Surface may have been lost (DirectDraw error)
                    log.exception('Pygame error: %s' % (e,))

                # Flip the display.
                pygame.display.flip()
                
    finally:
        close_pygame_window()