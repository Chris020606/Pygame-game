from settings import *

class Player(pygame.sprite.Sprite):

    def __init__(self, group):
        super().__init__(group)
        self.name = "Victor"
        self.level = 1
        self.alive = True
        self.health = 100
        self.max_health = 100

        self.base_damage = 20
        self.damage = self.base_damage

        self.base_speed = 300
        self.speed = self.base_speed

        # pos, size
        self.x_pos = WIDTH // 2
        self.y_pos = HEIGHT // 2

        # size 32 x 32
        self.width = 140
        self.height = 140
        self.player_tex = pygame.image.load('assets/sprites/player/player_1.png').convert_alpha()
        self.player_tex_scaled = pygame.transform.scale(self.player_tex, (self.width, self.height))
        self.image = self.player_tex_scaled
        self.rect = self.image.get_frect(center=(self.x_pos + self.width // 2, self.y_pos + self.height // 2))

        # mask
        mask = pygame.mask.from_surface(self.image)
        # when using collisions use this
        # collision = pygame.sprite.spritecollide(player, meteor_sprite, True, pygame.sprite.collide_mask)
        # and then delethe the mask
        # don't use for every collision

        # direction
        self.direction = pygame.Vector2()

        # Inventory
        self.inventory = []

    def input(self):
        keys = pygame.key.get_pressed()
        # make if, if the player wants to play with the following code or "WASD"
        # make it go faster with shift
        # game.player.direction.x = int(keys[pygame.K_RIGHT] - int(keys[pygame.K_LEFT]))
        # game.player.direction.y  = int(keys[pygame.K_DOWN] - int(keys[pygame.K_UP]))

        self.direction.x = int(keys[pygame.K_d] - int(keys[pygame.K_a]))
        self.direction.y = int(keys[pygame.K_s] - int(keys[pygame.K_w]))
        if keys[pygame.K_a]:
            flipped = pygame.transform.flip(self.player_tex, True, False)
            self.image = pygame.transform.scale(flipped, (self.width, self.height))
        elif keys[pygame.K_d]:
            self.image = pygame.transform.scale(self.player_tex, (self.width, self.height))

        if self.direction.length_squared() > 0:
            self.direction = self.direction.normalize()

    def move(self, dt):
        self.x_pos += self.direction.x * self.speed * dt
        self.y_pos += self.direction.y * self.speed * dt

        # Update rect position
        self.rect.topleft = (self.x_pos, self.y_pos)

    def update(self, dt):
        # Update position based on direction and speed
        self.input()
        self.move(dt)

    def player_attack(self):
        # make it attack with the hand
        pass

    def player_healing(self):
        # make an inventory and if player has a healing potion make it heal
        pass

    def level_up(self):
        self.level += 1
        return self.level