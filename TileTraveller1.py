# https://github.com/DTRedemption/TileTraveller
# define movement limitations
# use for, if, elif and else statements within for loop
# append options to a string
# use x and y for position
# while loop steers N E S W
#

# maze set up
maze = """x x x
 @@@ 
x x@x
 @ @ 
x@x@x"""
pX = 1
pY = 1
bad_input = False
finishCheck = pX == 3 and pY == 1
# game loop
while not finishCheck:

    # Check directions
    realX = (pX - 1) * 2
    realY = 4 - (pY - 1) * 2

    north = False
    south = False
    west = False
    east = False

    charY = -1
    for row in maze.split('\n'):
        charY += 1
        charX = -1
        for char in row:
            charX += 1
            # check UP
            if realX == charX and realY - 1 == charY and char == ' ':
                north = True
            # check DOWN
            if realX == charX and realY + 1 == charY and char == ' ':
                south = True
            # check LEFT
            if realY == charY and realX - 1 == charX and char == ' ':
                west = True
            # check RIGHT
            if realY == charY and realX + 1 == charX and char == ' ':
                east = True

    # movements
    movements = ""
    # check if move was valid
    if bad_input is False:
        movements = "You can travel:"
        if north:
            movements += " (N)orth"
            if east or south or west:
                movements += " or"

        if east:
            movements += " (E)ast"
            if south or west:
                movements += " or"

        if south:
            movements += " (S)outh"
            if west:
                movements += " or"

        if west:
            movements += " (W)est"
        movements += "."
    # ask for a direction then move accordingly
    direction = str(input(movements + "\nDirection: ")).upper()
    newX = pX
    newY = pY
    if direction == 'N':
        if north:
            newY += 1
    if direction == 'S':
        if south:
            newY -= 1
    if direction == 'W':
        if west:
            newX -= 1
    if direction == 'E':
        if east:
            newX += 1
    # reset input check
    bad_input = False
    # if input was invalid, no movement and no directions printed next loop
    if newX == pX and newY == pY:
        print("Not a valid direction!")
        bad_input = True
    # else valid move
    else:
        pX = newX
        pY = newY

    # position print for debugging
    # print("New location: " + str(pX) + ", " + str(pY))

    # Reevaluate finish condition at loop end
    finishCheck = pX == 3 and pY == 1
    # if player's position is in "3,1", player has won, terminate loop
    if finishCheck:
        print("Victory!")