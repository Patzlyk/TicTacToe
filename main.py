import pygame
import random
import ai

# Clock
clock = pygame.time.Clock()

# Variables
windowWidth = 300
windowHeight = 300
windowColor = (120, 120, 120)
windowCaption = "Tic Tac Toe"

crossImg = pygame.image.load("cross.png")
circleImg = pygame.image.load("circle.png")

row1 = [0, 0, 0]
row2 = [0, 0, 0]
row3 = [0, 0, 0]

max0 = 0
max1 = 100
max2 = 200
max3 = 300

winner = "none"
currentTurn = 0

# Create window
pygame.init()
pygame.display.init()
gameDisplay = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption(windowCaption)
gameDisplay.fill(windowColor)

# Functions
def placeCross(x, y):
    gameDisplay.blit(crossImg, (x * 100, y * 100))
    if y == 0:
        row1[x] = 1
    if y == 1:
        row2[x] = 1
    if y == 2:
        row3[x] = 1
        
    return row1, row2, row3

def placeCircle(x, y):
    gameDisplay.blit(circleImg, (x * 100, y * 100))
    if y == 0:
        row1[x] = 2
    if y == 1:
        row2[x] = 2
    if y == 2:
        row3[x] = 2

    return row1, row2, row3

# Place a circle
# [1], [2], [3]
# [4], [5], [6]
# [7], [8], [9]
def evaluateMove(row1, row2, row3, allFields):
    print("moooooooove")
    #allFields = [row1[0], row1[1], row1[2], row2[0], row2[1], row2[2], row3[0], row3[1], row3[2]]
    
    circleCords = ai.evaluateMove(allFields)


    placeCircle(circleCords["x"], circleCords["y"])
    #currentTurn = 0


crashed = False

# This executes in every frame
while not crashed:

    # Quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        # Place cross on mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:# and currentTurn == 0:
            if event.pos[0] > max0 and event.pos[0] < max1 and event.pos[1] > max0 and event.pos[1] < max1:
                placeCross(0, 0)
                #row1[0] = 1

            elif event.pos[0] > max1 and event.pos[0] < max2 and event.pos[1] > max0 and event.pos[1] < max1:
                placeCross(1, 0)
                #row1[1] = 1

            elif event.pos[0] > max2 and event.pos[0] < max3 and event.pos[1] > max0 and event.pos[1] < max1:
                placeCross(2, 0)
                #row1[2] = 1

            elif event.pos[0] > max0 and event.pos[0] < max1 and event.pos[1] > max1 and event.pos[1] < max2:
                placeCross(0, 1)
                #row2[0] = 1

            elif event.pos[0] > max1 and event.pos[0] < max2 and event.pos[1] > max1 and event.pos[1] < max2:
                placeCross(1, 1)
                #row2[1] = 1

            elif event.pos[0] > max2 and event.pos[0] < max3 and event.pos[1] > max1 and event.pos[1] < max2:
                placeCross(2, 1)
                #row2[2] = 1

            elif event.pos[0] > max0 and event.pos[0] < max1 and event.pos[1] > max2 and event.pos[1] < max3:
                placeCross(0, 2)
                #row3[0] = 1

            elif event.pos[0] > max1 and event.pos[0] < max2 and event.pos[1] > max2 and event.pos[1] < max3:
                placeCross(1, 2)
                #row3[1] = 1

            elif event.pos[0] > max2 and event.pos[0] < max3 and event.pos[1] > max2 and event.pos[1] < max3:
                placeCross(2, 2)
                #row3[2] = 1

            currentTurn = 1

            # Merge list of three rows to one list
            allFields = [row1[0], row1[1], row1[2], row2[0], row2[1], row2[2], row3[0], row3[1], row3[2]]

            # Check for win and color the window accoring to winner
            winner = ai.checkForWin(allFields, winner)
            if winner == "cross":
                print ("CROSS WINS")
                gameDisplay.fill((150, 0, 0))
            elif winner == "circle":
                print ("CIRCLE WINS")
                gameDisplay.fill((0, 0, 150))
            else:
                print("nobody wins")

            evaluateMove(row1, row2, row3, allFields)

            print(row1)
            print(row2)
            print(row3)
            print(allFields)
            

        #print(event)

    # Main code
    


    pygame.display.update()
    clock.tick(30)

pygame.quit()