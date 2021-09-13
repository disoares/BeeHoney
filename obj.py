import pygame


class Obj:

    def __init__(self, image, x, y):

        self.group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.group)

        self.sprite.image = pygame.image.load(image)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = x
        self.sprite.rect[1] = y

        self.frame = 1
        self.tick = 0

    def drawing(self, window):

        self.group.draw(window)

    def anim(self, image_name, tick, frames):

        self.tick += 1
        if self.tick >= tick:
            self.tick = 0
            self.frame += 1

        if self.frame > frames:
            self.frame = 1

        self.sprite.image = pygame.image.load(f"assets/{image_name}{self.frame}.png")


class Bee(Obj):

    def __init__(self, image, x, y):
        super().__init__(image, x, y)

        pygame.mixer.init()
        self.sound_pts = pygame.mixer.Sound("assets/sounds/score.ogg")
        self.sound_block = pygame.mixer.Sound("assets/sounds/bateu.ogg")

        self.life = 3
        self.pts = 0

    def move_bee(self, event):

        if event.type == pygame.MOUSEMOTION:
            self.sprite.rect[0] = pygame.mouse.get_pos()[0] - 35
            self.sprite.rect[1] = pygame.mouse.get_pos()[1] - 30

    def is_colliding(self, group, name):

        name = name
        is_colliding = pygame.sprite.spritecollide(self.sprite, group, True)

        if name == "Flower" and is_colliding:
            self.sound_pts.play()
            self.pts += 1
        elif name == "Spider" and is_colliding:
            self.sound_block.play()
            self.life -= 1


class Text:

    def __init__(self, text, size, ):

        self.font = pygame.font.SysFont("Arial bold", size)
        self.render = self.font.render(text, True, [0, 0, 0])

    def draw(self, window, x, y):

        window.blit(self.render, (x, y))

    def update_text(self, text):

        self.render = self.font.render(text, True, [0, 0, 0])