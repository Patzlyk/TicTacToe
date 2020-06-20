def checkForWin(allFields, winner):
    # Cross horizontal
    if allFields[0] == allFields[1] == allFields[2] == 1:
        winner = "cross"
        return winner
    if allFields[3] == allFields[4] == allFields[5] == 1:
        winner = "cross"
        return winner
    if allFields[6] == allFields[7] == allFields[8] == 1:
        winner = "cross"
        return winner

    # Cross vertical
    if allFields[0] == allFields[3] == allFields[6] == 1:
        winner = "cross"
        return winner
    if allFields[1] == allFields[4] == allFields[7] == 1:
        winner = "cross"
        return winner
    if allFields[2] == allFields[5] == allFields[8] == 1:
        winner = "cross"
        return winner

    # Cross diagonal
    if allFields[0] == allFields[4] == allFields[8] == 1:
        winner = "cross"
        return winner
    if allFields[6] == allFields[4] == allFields[2] == 1:
        winner = "cross"
        return winner



    # Circle horizontal
    if allFields[0] == allFields[1] == allFields[2] == 2:
        winner = "circle"
        return winner
    if allFields[3] == allFields[4] == allFields[5] == 2:
        winner = "circle"
        return winner
    if allFields[6] == allFields[7] == allFields[8] == 2:
        winner = "circle"
        return winner

    # Circle vertical
    if allFields[0] == allFields[3] == allFields[6] == 2:
        winner = "circle"
        return winner
    if allFields[1] == allFields[4] == allFields[7] == 2:
        winner = "circle"
        return winner
    if allFields[2] == allFields[5] == allFields[8] == 2:
        winner = "circle"
        return winner

    # Circle diagonal
    if allFields[0] == allFields[4] == allFields[8] == 2:
        winner = "circle"
        return winner
    if allFields[6] == allFields[4] == allFields[2] == 2:
        winner = "circle"
        return winner



    else:
        winner = "none"
        return winner

def evaluateMove(allFields):
    print("Evaluating next move")

    circleCords = dict()
    circleCords["x"] = 0
    circleCords["y"] = 0

    winningFields = {
        "horizontal1": [allFields[0], allFields[1], allFields[2]],
        "horizontal2": [allFields[3], allFields[4], allFields[5]],
        "horizontal3": [allFields[6], allFields[7], allFields[8]],

        "vertical1":  [allFields[0], allFields[3], allFields[6]],
        "vertical2":  [allFields[1], allFields[4], allFields[7]],
        "vertical3":  [allFields[2], allFields[5], allFields[8]],

        "diagonal1":  [allFields[0], allFields[4], allFields[8]],
        "diagonal2":  [allFields[6], allFields[4], allFields[2]]
    }

    isFieldAvailible = {
        "horizontal1": False,
        "horizontal2": False,
        "horizontal3": False,

        "vertical1":  False,
        "vertical2":  False,
        "vertical3":  False,

        "diagonal1":  False,
        "diagonal2":  False
    }

    currentIteration = 0
    for winningField in winningFields:
        currentWinningField = winningFields[winningField]
        print("Currently checked field:" + str(currentWinningField))
        currentFieldAvailible = False

        for field in currentWinningField:
            print(field)
            #currentField = currentWinningField[0]
            #print("Currently checked field:" + str(field))
            if field == 1:
                currentFieldAvailible = False
                break
            elif field == 2:
                currentFieldAvailible = True
            else:
                currentFieldAvailible = True
        
        if currentFieldAvailible == True:
            print("This field is availible")
            isFieldAvailible[winningField] = True
        else:
            print("This field is not availible")
        currentIteration += 1


    return circleCords