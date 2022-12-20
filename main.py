import pygame
import random
import sys
sys.path.insert(0, 'Classes')
from HeadClass import *
from TailClass import *
from FoodClass import *

# Constants
WIDTH = 1200 # Width of screen
HEIGHT = 800 # Height of screen
FPS = 10 # frames per second

# Define The Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Global Variables
global tailSize, spawnFood, tailsX, tailsY
tailSize = 2 # the size of the tail
spawnFood = False # weather or not there is a food on screen
tailsX = [] # the x pos of the tail pieces
tailsY = [] # the y pos of the tail pieces

# Other Variables
tailNum = int()
score = 0
highScoreFile = open("HighScore.txt", "r")
highScore = highScoreFile.readline(1)

# Initalize Pygame
pygame.init()
pygame.font.init()

# Screen Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Create a screen that is WIDTH wide and HEIGHT tall
pygame.display.set_caption("PySnake") # Name the window 'PySnake'

# Clock Setup For FPS
clock = pygame.time.Clock()

# Font/Text Setup
scoreFont = pygame.font.SysFont("Halvetica", 20)
scoreText = scoreFont.render("Score: {0}".format(score), False, (WHITE))
highScoreText = scoreFont.render("High Score: {0}".format(highScore), False, (WHITE))

#~~~~~~~ Sprites Init ~~~~~~~#
# Sprite Groups
tailPieces = pygame.sprite.Group()
allSprites = pygame.sprite.Group()

# Sprites
head = Head(WIDTH, HEIGHT) # The head of the sanke
allSprites.add(head)

for i in range(tailSize): # Make the tail
    tailsX.append(head.rect.centerx + ((i + 1) * 20))
    tailsY.append(head.rect.centery)
    tailPiece = Tail(tailsX[i], tailsY[i])
    tailPieces.add(tailPiece)

#~~~~~~~~ Functions ~~~~~~~~~#
def Eat():
    global tailSize, tailsX, tailsY, spawnFood
    tailSize += 1 # Add one to tail size
    tailsX.append(head.rect.centerx) # Add a element to tails X
    tailsY.append(head.rect.centery) # Add a element to tails Y
    tailPiece = Tail(tailsX[1], tailsY[1]) # create new tail piece
    tailPieces.add(tailPiece) # Add tail piece to the tail group
    spawnFood = False

#~~~~~~ Main Game Loop ~~~~~~#
running = True
while (running):
    # print(spawnFood)
    clock.tick(FPS) # Set the Frames Per Second

    # Check to see if the snake has collided with itself, or the wall
    if (pygame.sprite.spritecollide(head, tailPieces, False) or head.rect.x > WIDTH - 10 or head.rect.x < 10 or head.rect.y > HEIGHT - 10 or head.rect.y < 10):
        running = False

    # Check events whenever some input is given
    for event in pygame.event.get():
        if (event.type == pygame.QUIT): # If the 'X' in the corner is clicked exit
            running = False
        if (event.type == pygame.KEYDOWN): # If the key is pressed
            key = pygame.key.get_pressed() # Get the key pressed
            if (key[pygame.K_UP]): # If up move up
                head.move("UP")
            if (key[pygame.K_DOWN]): # If down move down
                head.move("DOWN")
            if (key[pygame.K_LEFT]): # If left move left
                head.move("LEFT")
            if (key[pygame.K_RIGHT]): # If right move right
                head.move("RIGHT")

    # Edit Tail Positions
    for i in range(tailSize): # Repeats based off how many tail pieces there are
        if (i < tailSize - 1): # while i is 1 less than the number of tail pieces
            tailsX[(tailSize - 1) - i] = tailsX[(tailSize - 1) - (i + 1)] # Take one elenemt and move it to the right
            tailsY[(tailSize - 1) - i] = tailsY[(tailSize - 1) - (i + 1)] # Take one elenemt and move it to the right
        else:
            tailsX[0] = head.rect.centerx # Set the first element to the new x
            tailsY[0] = head.rect.centery # Set the first element to the new y

    # Update Tail Posiiton
    tailNum = 0 # Set the tail it is updating to 0 (a.k.a 1)
    for i in tailPieces: # for however many tail pieces there are
        i.update(tailsX[tailNum], tailsY[tailNum], tailNum) # Update the Tail
        tailNum += 1 # Go on to the next tail piece

    # Updates the head
    allSprites.update()

    # Spawn Food
    if (not spawnFood): # If there is no food on screen
        # Make a food at a random x and y, that is 1 grid away from the wall, and step 20 so that it is always in line with the snake
        food = Food(random.randrange(20, WIDTH - 20, 20), random.randrange(20, HEIGHT - 20, 20))
        allSprites.add(food)
        spawnFood = True

    # Check for food eaten
    if (pygame.sprite.collide_rect(head, food) == 1): # If the head is colliding with a food
        food.ate() # Get rid of food
        Eat()
        score += 1
        scoreText = scoreFont.render("Score: {0}".format(score), False, (WHITE))

    # Draw Frame
    screen.fill(BLACK) # Gets rid of everything on the screen
    allSprites.draw(screen) # Draws the head
    tailPieces.draw(screen) # Draws the blocks
    screen.blit(scoreText, (10, 10))
    # screen.blit(highScoreText, (10, 30))

    # Show Frame
    pygame.display.flip() # Flips the display to show new frame

# Quit out of pygame
highScoreFile.close()
pygame.quit()
pygame.font.quit()

if (score > highScore):
    highScoreFile = open("HighScore.txt", "w+")
    highScoreFile.write(str(highScore))
