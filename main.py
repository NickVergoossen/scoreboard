import pygame

Maaseik = 0
Roeselare = 0
WIDTH = 1200
HEIGHT = 600
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont("comicsansms", 90)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Maaseik = Maaseik + 1

            if event.key == pygame.K_RIGHT:
                Roeselare = Roeselare + 1
            if event.key == pygame.K_r:
                Maaseik = 0
                Roeselare = 0
    screen.fill("white")

    label = f"""De score tijdens de match is {Maaseik} - {Roeselare}"""
    text = font.render(f"""Maaseik {Maaseik} - {Roeselare}  Roeselare""", True, "black")
    tekstbreedte = text.get_width()
    teksthoogte = text.get_height()
    team_A_logo = pygame.image.load("maaseik2tr.png").convert_alpha()
    team_A_logo = pygame.transform.smoothscale(team_A_logo, (200, 200))
    team_B_logo = pygame.image.load("roeselaretr.png").convert_alpha()
    team_B_logo = pygame.transform.smoothscale(team_B_logo, (200, 200))

    screen.blit(text, (WIDTH / 2 - tekstbreedte / 2, HEIGHT / 2 - teksthoogte / 2))
    screen.blit(team_A_logo, (200, 0))
    screen.blit(team_B_logo, (800, 0))
    pygame.display.flip()