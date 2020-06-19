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