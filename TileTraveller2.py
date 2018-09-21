# https://github.com/DTRedemption/TileTraveller
# Q1: I would say Part 2 was more difficult as transitioning the code from Part 1 required a lot of refactoring and planning.
# Q2: I would say Part 2 was more readable, Part 1 was a lot to go through in general and putting them into functions made it easier
# Q3: I was able to simplify the way directions were calculated and make the code overall look cleaner and less messy.

# maze set up
MAZE = """x x x
 @@@ 
x x@x
 @ @ 
x@x@x"""

# "generate" maze and check available directions
def maze_check(grid, playerX, playerY):
    # Check directions
    realX = (playerX - 1) * 2
    realY = 4 - (playerY - 1) * 2
    # Check the grid
    charY = -1
    # order: NESW
    directions = "0000"
    for row in grid.split('\n'):
        charY += 1
        charX = -1
        for char in row:
            # here I modify the directions string and change 0 to 1 if the direction is available
            charX += 1
            # check UP
            if realX == charX and realY - 1 == charY and char == ' ':
                directions = "1" + directions[1:]
            # check DOWN
            if realX == charX and realY + 1 == charY and char == ' ':
                directions = directions[:2] + "1" + directions[3:]
            # check LEFT
            if realY == charY and realX - 1 == charX and char == ' ':
                directions = directions[:3] + "1"
            # check RIGHT
            if realY == charY and realX + 1 == charX and char == ' ':
                directions = directions[:1] + "1" + directions[2:]
    # return a string of 0s and 1s corresponding to available directions
    return directions

# show the available directions to the player
def show_directions(directions):
    # movements
    movements = "You can travel:"
    if int(directions[0]):
        movements += " (N)orth"
        if int(directions[1:]):
            movements += " or"
    if int(directions[1]):
        movements += " (E)ast"
        if int(directions[2:]):
            movements += " or"
    if int(directions[2]):
        movements += " (S)outh"
        if int(directions[3:]):
            movements += " or"
    if int(directions[3]):
        movements += " (W)est"
    # add full stop to the end as mimir requested
    return movements + "."

# moves player on x axis
def move_player_x(directions, playerInput, playerX):
    newX = playerX
    if playerInput == 'E' and int(directions[1]):
        newX += 1
    if playerInput == 'W' and int(directions[3]):
        newX -= 1
    return newX

# moves player on y axis
def move_player_y(directions, playerInput, playerY):
    newY = playerY
    if playerInput == 'N' and int(directions[0]):
        newY += 1
    if playerInput == 'S' and int(directions[2]):
        newY -= 1
    return newY

# Checks if player is at 3, 1
def has_arrived(playerX, playerY):
    if playerX == 3 and playerY == 1:
        print("Victory!")
        return True
    return False

# game loop and functions executed here
def game():
    pX = 1
    pY = 1

    # game loop
    arrived = False
    while not arrived:
        # start by checking available directions
        directions = maze_check(MAZE, pX, pY)
        movements = show_directions(directions)
        # ask for a direction then move accordingly
        playerInput = str(input(movements + "\nDirection: ")).upper()
        newX = move_player_x(directions, playerInput, pX)
        newY = move_player_y(directions, playerInput, pY)
        # check for invalid movement
        while newX == pX and newY == pY:
            print("Not a valid direction!")
            playerInput = str(input("Direction: ")).upper()
            newX = move_player_x(directions, playerInput, pX)
            newY = move_player_y(directions, playerInput, pY)
        # movement validated
        pX = newX
        pY = newY

        # Reevaluate finish condition at loop end
        arrived = has_arrived(pX, pY)

# starts the game
game()
