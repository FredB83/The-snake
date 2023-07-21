import pygame
import sys
import random
import time


pygame.init()

# Définir les dimensions de l'écran du jeu
screen_width = 640
screen_height = 480

# Couleurs
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Définir la taille d'une cellule du serpent et la vitesse du jeu
cell_size = 20
fps = 10

# Initialisation de la fenêtre du jeu
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, green, (segment[0], segment[1], cell_size, cell_size))

def draw_apple(apple_pos):
    pygame.draw.rect(screen, red, (apple_pos[0], apple_pos[1], cell_size, cell_size))

def generate_apple():
    apple_x = random.randint(0, (screen_width - cell_size) // cell_size) * cell_size
    apple_y = random.randint(0, (screen_height - cell_size) // cell_size) * cell_size
    return apple_x, apple_y

def game_over():
    font = pygame.font.Font(None, 50)
    game_over_surface = font.render('Game Over', True, white)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (screen_width / 2, screen_height / 4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    sys.exit()

def snake_game():
    # Initialisation du serpent
    snake = [(screen_width / 2, screen_height / 2)]
    snake_direction = (0, 0)
    snake_length = 1

    # Initialisation de la pomme
    apple_pos = generate_apple()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake_direction = (0, -cell_size)
                elif event.key == pygame.K_DOWN:
                    snake_direction = (0, cell_size)
                elif event.key == pygame.K_LEFT:
                    snake_direction = (-cell_size, 0)
                elif event.key == pygame.K_RIGHT:
                    snake_direction = (cell_size, 0)

        # Mise à jour de la position de la tête du serpent
        snake_head = (snake[-1][0] + snake_direction[0], snake[-1][1] + snake_direction[1])

        # Vérification des collisions avec les bords de l'écran
        if snake_head[0] < 0 or snake_head[0] >= screen_width or snake_head[1] < 0 or snake_head[1] >= screen_height:
            game_over()

        # Vérification des collisions avec le corps du serpent
        if snake_head in snake[:-1]:
            game_over()

        snake.append(snake_head)

        # Si le serpent mange la pomme
        if snake_head == apple_pos:
            apple_pos = generate_apple()
            snake_length += 1
        else:
            snake = snake[1:]

        # Dessiner l'écran du jeu
        screen.fill(black)
        draw_snake(snake)
        draw_apple(apple_pos)
        pygame.display.update()

        # Contrôle de la vitesse du jeu
        clock.tick(fps)

if __name__ == '__main__':
    snake_game()
