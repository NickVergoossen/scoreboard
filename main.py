import datetime
import sys
import time
import pygame
from game import Game

WIDTH = 1200
HEIGHT = 600

score_home = 0
score_away = 0
sets_home = 0
sets_away = 0
set = 5
game = Game()

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont("Arial", 90)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.score("H")

            if event.key == pygame.K_RIGHT:
                game.score("A")

            elif event.key == pygame.K_r:
                game.points_home = 0
                game.points_away = 0
                game.sets_home = 0
                game.sets_away = 0

    if score_home >= set and score_home >= score_away + 2:
        score_home = 0
        score_away = 0
        sets_home = sets_home + 1

    if score_away >= set and score_away >= score_home + 2:
        score_home = 0
        score_away = 0
        sets_away = sets_away + 1

    screen.fill("white")

    label = f"""De score tijdens de match is {game.points_home} - {game.points_away}"""
    text = font.render(f"""Maaseik {game.points_home} - {game.points_away}  Roeselare""", True, "black")
    reset = font.render(f"""reset de score met r knop""", True, "black")
    sets = font.render(f"""{game.sets_home} - {game.sets_away}""", True, "black")
    tekstbreedte = text.get_width()
    teksthoogte = text.get_height()
    team_A_logo = pygame.image.load("maaseik.jpg").convert_alpha()
    team_A_logo = pygame.transform.smoothscale(team_A_logo, (200, 200))
    team_B_logo = pygame.image.load("roeselare.png").convert_alpha()
    team_B_logo = pygame.transform.smoothscale(team_B_logo, (200, 200))

    screen.blit(text, (WIDTH / 2 - tekstbreedte / 2, HEIGHT / 2 - teksthoogte / 2))
    screen.blit(reset, (170, 500))
    screen.blit(team_A_logo, (230, 0))
    screen.blit(team_B_logo, (800, 0))
    screen.blit(sets, (485, 400))

    pygame.display.flip()