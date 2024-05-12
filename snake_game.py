import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
GRID_WIDTH = WIDTH // BLOCK_SIZE
GRID_HEIGHT = HEIGHT // BLOCK_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)

# Set up directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Set up the clock
clock = pygame.time.Clock()

# Game state
GAME_START = 0
GAME_PLAYING = 1
GAME_OVER = 2

# File to store the high score
high_score_file = "high_score.txt"

# Function to read the high score from the file
def read_high_score():
    try:
        with open(high_score_file, "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0

# Function to write the high score to the file
def write_high_score(score):
    with open(high_score_file, "w") as file:
        file.write(str(score))

# Base class for game objects
class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pass

# Snake segment class
class SnakeSegment(GameObject):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color  # Assuming color is defined and passed to the initializer

    def get_rect(self):
        """Calculate the rectangle's coordinates based on the block's position."""
        return (self.x * BLOCK_SIZE, self.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)

    def draw(self, screen):
        """Draw the block using the calculated coordinates."""
        rect = self.get_rect()  # Get the coordinates using the get_rect method
        pygame.draw.rect(screen, self.color, rect)

# Food base class
class Food(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self, screen):
        pass

    def effect(self, snake):
        pass

    @classmethod
    def create(cls, x, y, food_type="normal"):
        if food_type == "normal":
            return NormalFood(x, y)
        elif food_type == "special":
            return SpecialFood(x, y)
        else:
            raise ValueError("Invalid food type")

# Normal food class
class NormalFood(Food):
    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x * BLOCK_SIZE, self.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def effect(self, snake):
        snake.grow()

# Special food class
class SpecialFood(Food):
    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, (self.x * BLOCK_SIZE, self.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def effect(self, snake):
        snake.grow()
        snake.grow()
        global score
        score +=1

# Snake class
class Snake:
    def __init__(self):
        self.segments = [SnakeSegment(GRID_WIDTH // 2, GRID_HEIGHT // 2, WHITE)]
        self.direction = RIGHT

    def move(self):
        head = self.segments[0]
        new_head = SnakeSegment(head.x + self.direction[0], head.y + self.direction[1], WHITE)
        self.segments.insert(0, new_head)
        self.segments.pop()

    def grow(self):
        tail = self.segments[-1]
        new_tail = SnakeSegment(tail.x - self.direction[0], tail.y - self.direction[1], WHITE)  # cia
        self.segments.append(new_tail)

    def draw(self, screen):
        for segment in self.segments:
            segment.draw(screen)

# Builder method for creating the snake
def create_snake():
    snake = Snake()
    snake_direction = RIGHT
    return snake, snake_direction

# Builder method for creating the food
def create_food():
    food = Food.create(random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1), random.choice(["normal", "special"]))
    return food

# Function to reset game using builder methods
def reset_game():
    global snake, snake_direction, food, score
    snake, snake_direction = create_snake()
    food = create_food()
    score = 0

# Initialize high score
high_score = read_high_score()

# Initialize game variables
snake = None
snake_direction = None
food = None
score = 0
reset_game()

# Main game loop
game_state = GAME_START
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game_state == GAME_START:
                game_state = GAME_PLAYING
                reset_game()
            elif game_state == GAME_OVER:
                if event.key == pygame.K_SPACE:
                    game_state = GAME_PLAYING
                    reset_game()
                elif event.key == pygame.K_ESCAPE:
                    running = False
            else:
                if event.key == pygame.K_UP and snake.direction != DOWN:
                    snake.direction = UP
                elif event.key == pygame.K_DOWN and snake.direction != UP:
                    snake.direction = DOWN
                elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
                    snake.direction = LEFT
                elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                    snake.direction = RIGHT

    # Game logic
    if game_state == GAME_PLAYING:
        # Move the snake
        snake.move()

        # Check for collision with food
        head = snake.segments[0]
        if (head.x, head.y) == (food.x, food.y):
            food.effect(snake)
            food = create_food()
            score += 1
            if score > high_score:
                high_score = score
                write_high_score(high_score)  # Update high score in file

        # Check for collision with walls or self
        if (head.x < 0 or head.x >= GRID_WIDTH or
                head.y < 0 or head.y >= GRID_HEIGHT or
                (head.x, head.y) in [(segment.x, segment.y) for segment in snake.segments[1:]]):
            game_state = GAME_OVER

    # Draw everything
    screen.fill(BLACK)
    if game_state == GAME_START:
        # Display start screen
        font = pygame.font.Font(None, 36)
        text = font.render("Press any key to start", True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)
    elif game_state == GAME_PLAYING:
        # Draw snake and food
        snake.draw(screen)
        food.draw(screen)
    elif game_state == GAME_OVER:
        # Display game over screen
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over!", True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
        screen.blit(text, text_rect)

        # Display current score
        score_text = font.render(f"Your score: {score}", True, WHITE)
        score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 25))
        screen.blit(score_text, score_rect)

        # Display high score
        high_score_text = font.render(f"High Score: {high_score}", True, WHITE)
        high_score_rect = high_score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
        screen.blit(high_score_text, high_score_rect)

        score_text = font.render(f"Press SPACE to continue or ESC to close", True, WHITE)
        score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 125))
        screen.blit(score_text, score_rect)

    pygame.display.update()

    # Cap the frame rate
    clock.tick(5)

# Quit Pygame
pygame.quit()
