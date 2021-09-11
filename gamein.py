import pygame
x = pygame.init()
gamewindows = pygame.display.set_mode((500,500))
pygame.display.set_caption("Summer project")

exit_game = False
game_over = False

while not exit_game :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

pygame.quit()
quit()
