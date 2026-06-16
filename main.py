import pygame

from objects.player import Player

pygame.init()

my_player = Player()
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Поедатель печенек")

dt = 0
clock = pygame.time.Clock()



run_game_loop = True
while run_game_loop:
    # Обработка события выхода
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run_game_loop = False

    screen.fill("black")
    my_player.draw(screen)

    pygame.display.flip()

    my_player.handle_keys(dt)

    dt = clock.tick(60) / 1000

pygame.quit()