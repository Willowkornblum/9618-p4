
HighScores = [[ "" for i in range(3)]for x in range(7)]             #2D array , 7 rows , 3 coloums
def ReadData():

    try:
        file = open("HighScoreTable.txt", "r")

        for row in range(7):
            for column in range(3):
                HighScores[row][column] = file.readline().strip()

        file.close()

    except:
        print("Error reading file")

    return HighScores
def outputhighscores (HighScores):
    for row in range (7):
        print( HighScores[row][0],"reached level", HighScores[row][1],"with a score of",HighScores[row][2])


def SortScores(HighScores):
    for x in range(len(HighScores) - 1):
        for y in range(len(HighScores) - 1 - x):

            if HighScores[y][1] < HighScores[y + 1][1]:
                temp = HighScores[y]
                HighScores[y] = HighScores[y + 1]
                HighScores[y + 1] = temp

            elif HighScores[y][1] == HighScores[y + 1][1]:
                if HighScores[y][2] < HighScores[y + 1][2]:
                    temp = HighScores[y]
                    HighScores[y] = HighScores[y + 1]
                    HighScores[y + 1] = temp

    return HighScores

HighScores = ReadData()
print("Before")
outputhighscores(HighScores)
HighScores = SortScores(HighScores)
print("after")
outputhighscores(HighScores)
