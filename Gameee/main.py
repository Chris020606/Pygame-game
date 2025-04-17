from settings import *
from game import Game

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Game')
        self.clock = pygame.time.Clock()
        self.running = True
        self.game = Game()

    def main_loop(self):
        screen = self.screen
        game = self.game
        while self.running:
            delta_time = self.clock.tick() / 1000
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False

            game.all_sprite.update(delta_time)
            screen.fill('gray')
            game.all_sprite.draw(self.screen)

            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    main = Main()
    main.main_loop()


