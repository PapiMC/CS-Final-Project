import json

def hScore(score):

    scoreDict = {}
    scoreDict["Your Score"] = score

    with open("HighScoreE.json", "a") as outfile:
        json.dump(scoreDict, outfile)
        #json.dump("\n", outfile)

# people = {}
# people["response"] = (E1.get(), E2.get(), E3.get(), E4.get() ... E10.get())
#
# with open("people.txt")
