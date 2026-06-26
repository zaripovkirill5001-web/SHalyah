import pygame 
from objects.UI import HPBar
from objects.player import Player


# GameScene - PaskalCase (Classes)
# gameScene - CamelCase (Для объектов)
# game_scene - SnakeCase (Для всего остального)


class GameScene:
    bullets = []

    ui = {
        'hpbar': HPBar('illah', {'x':20, 'y': 20})
    }

    def __init__(self):
        self.screen = pygame.display.set_mode((803,802))
        pygame.display.set_caption("11 сентября 2001 год")

        self.player = Player()
        self.dt = 0
        self.clock = pygame.time.Clock()

    def _restart_game(self):
        self.player = Player()
        self.dt = 0
    
    def _check_restart_call(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self._restart_game()

    def _handle_time(self):
        self.dt = self.clock.tick(60) / 1000
    
    def draw_all(self):
        self.screen.fill("black")

        save_bullet = self.bullets.copy()
        for bullet in save_bullet:
            answer = bullet.draw(self.screen)
            if answer == None:
                self.bullets.remove(bullet)

        self.player.draw(self.screen)

        self.ui['hpbar'].percent = self.player.hp / self.player.max_hp
        for ui_element in self.ui:
            self.ui[ui_element].draw(self.screen)

        pygame.display.flip()
        # print('Кол-во пуль на карте:', len(self.bullets))
    
    def handle_game_logic(self):
        self.player.handle_keys(self,self.dt)
        for bullet in self.bullets:
            bullet.handle_logic(self.dt)
        self._check_restart_call()
        self._handle_time()