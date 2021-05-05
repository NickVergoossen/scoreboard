import pygame

Maaseik = 0
Elen = 0
WIDTH = 800
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
                Elen = Elen + 1
            if event.key == pygame.K_r:
                Maaseik = 0
                Elen = 0
    screen.fill("white")

    label = f"""De score tijdens de match is {Maaseik} - {Elen}"""
    text = font.render(f"""De score  is {Maaseik} - {Elen}""", True, "black")
    tekstbreedte = text.get_width()
    teksthoogte = text.get_height()

    screen.blit(text, (WIDTH / 2 - tekstbreedte / 2, HEIGHT / 2 - teksthoogte / 2))
    pygame.display.flip()