from obj import Obj, Bee, Text
import random


class Game:

    def __init__(self):

        self.background = Obj("assets/bg.png", 0, 0)
        self.background2 = Obj("assets/bg.png", 0, -640)

        self.spider = Obj("assets/spider1.png", random.randrange(0, 300), random.randrange(-100, -50))
        self.flower = Obj("assets/florwer1.png", random.randrange(0, 300), random.randrange(-100, -50))
        self.bee = Bee("assets/bee1.png", 150, 550)

        self.change_scene = False

        self.score = Text("0", 160)
        self.lifes = Text("3", 60)

    def draw(self, window):

        self.background.drawing(window)
        self.background2.drawing(window)
        self.spider.drawing(window)
        self.flower.drawing(window)
        self.bee.drawing(window)
        self.score.draw(window, 160, 50)
        self.lifes.draw(window, 50, 50)

    def update(self):
        self.move_bg()
        self.move_spiders()
        self.move_flowers()
        self.spider.anim("spider", 8, 4)
        self.flower.anim("florwer", 8, 2)
        self.bee.anim("bee", 2, 4)
        self.bee.is_colliding(self.spider.group, "Spider")
        self.bee.is_colliding(self.flower.group, "Flower")
        self.game_over()
        self.score.update_text(str(self.bee.pts))
        self.lifes.update_text(str(self.bee.life))

    def move_bg(self):

        self.background.sprite.rect[1] += 3
        self.background2.sprite.rect[1] += 3

        if self.background.sprite.rect[1] >= 640:
            self.background.sprite.rect[1] = 0

        if self.background2.sprite.rect[1] >= 0:
            self.background2.sprite.rect[1] = -640

    def move_spiders(self):

        self.spider.sprite.rect[1] += 10

        if self.spider.sprite.rect[1] >= 700:
            self.spider.sprite.kill()
            self.spider = Obj("assets/spider1.png", random.randrange(0, 300), -50)

    def move_flowers(self):

        self.flower.sprite.rect[1] += 6

        if self.flower.sprite.rect[1] >= 700:
            self.flower.sprite.kill()
            self.flower = Obj("assets/florwer1.png", random.randrange(0, 300), -50)

    def game_over(self):

        if self.bee.life <= 0:
            self.change_scene = True