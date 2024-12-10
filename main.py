import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 36

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")

# Load font
font = pygame.font.Font(None, FONT_SIZE)

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Game function
def get_winner(player, computer):
    if player == computer:
        return "It's a Tie!"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        return "You Win!"
    else:
        return "You Lose!"

# Main game loop
def main():
    running = True
    player_choice = None
    computer_choice = None
    result = ""

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    player_choice = "Rock"
                elif event.key == pygame.K_p:
                    player_choice = "Paper"
                elif event.key == pygame.K_s:
                    player_choice = "Scissors"

                if player_choice:
                    computer_choice = random.choice(choices)
                    result = get_winner(player_choice, computer_choice)

        # Fill the screen with white
        screen.fill(WHITE)

        # Display the choices and result
        if player_choice:
            player_text = font.render(f"You chose: {player_choice}", True, BLACK)
            computer_text = font.render(f"Computer chose: {computer_choice}", True, BLACK)
            result_text = font.render(result, True, BLACK)

            screen.blit(player_text, (50, 50))
            screen.blit(computer_text, (50, 100))
            screen.blit(result_text, (50, 150))

        # Refresh the screen
        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
