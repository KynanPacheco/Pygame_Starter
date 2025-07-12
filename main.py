import pygame
import Game.Manager as Manager

Manager.ChangeScene(Manager.SCENE)

while Manager.running:
                
    # Run the game loop of the current scene
    Manager.LoadScene(Manager.SCENE)

    # Flip the display
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    Manager.clock.tick(Manager.FPS)

pygame.quit()
