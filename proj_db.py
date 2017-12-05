# import json
# import Controller

def make_hs(score):

    try:
        hsFile = open("HighScore.txt", "a")
        hsFile.write("{}\n".format(score))
        hsFile.close()

        hsFile = open("HighScore.txt", "r")
        print(hsFile.readlines())

    except:
        print("Some Error")
    finally:
        hsFile.close()

#make_hs(80)