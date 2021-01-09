import pygame
import random

from pygame import *

pygame.init()
window = pygame.display.set_mode((700, 800))

pygame.display.set_caption("Game: CAR")
font_family = pygame.font.SysFont("monaco", 35)

time = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)

bg = pygame.image.load("./images/bg-game.jpg")
car_img = pygame.image.load("./images/player.png")
heart = pygame.image.load("./images/heart.png")

window.blit(bg, (0, 0))


def change_score(count):
    text = font_family.render("Dodged: " + str(count), True, white)
    window.blit(text, [25, 5])


def text_time():
    text = font_family.render("Time: " + str((pygame.time.get_ticks() // 1000) - 8), True, white)
    window.blit(text, [700 * 0.5, 5])


def car(x, y):
    window.blit(car_img, (x, y))


def things(thing_x, thing_y):
    window.blit(heart, (thing_x, thing_y))


def game_loop():
    car_x = 700 * 0.5
    car_y = 800 * 0.8
    car_change = 0

    thing_startx = random.randrange(190, 505)
    thing_starty = -50
    thing_speed = 7
    score = 1

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    car_change -= 5
                elif event.key == pygame.K_RIGHT:
                    car_change += 5
            if event.type == pygame.KEYUP and (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                car_change = 0

        car_x += car_change
        window.blit(bg, (0, 0))

        if car_x >= 505 or car_x <= 190:
            car_x -= car_change

        things(thing_startx, thing_starty)
        thing_starty += thing_speed
        car(car_x, car_y)
        text_time()

        if thing_starty > 800:
            game_over = True

        if car_x <= thing_startx + 40 and car_x + 66 >= thing_startx \
                and car_y <= thing_starty + 39 and car_y + 145 >= thing_starty:
            thing_starty = -39
            thing_startx = random.randrange(190, 505)
            things(thing_startx, thing_starty)
            score += 1

        change_score(score)
        time.tick(30)
        pygame.display.update()


game_loop()
pygame.quit()
quit()
