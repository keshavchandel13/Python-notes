#test-->4 file
import random
filePath=r"C:\Python\Problem\hiscore.txt"

def score():
    print("You are playing a game")
    score=random.randint(1,600)
    #fetch the file highscore file
    with open(filePath) as f:
      hiscore=f.read()
      if(hiscore!=""):
         hiscore=int(hiscore)
      else:
         hiscore=0
    print(f"Your score is {score}")
    if(score>hiscore):
       #write this hiscore in this file
       with open(filePath,"w") as f:
          f.write(str(score))
    return score
          

score()



