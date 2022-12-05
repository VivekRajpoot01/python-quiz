question = {
  "Q. Atomic number of Lithium is 17.":
  "false",
  "Q. An octopus has 3 hearts.":
  "true",
  "Q. Output of 2**3=4*2.":
  "true",
  "Q. Thomas Edison discovered gravity":
  "false",
  "Q. define keyword used to declare a function.":
  "false",
  "Q. Bill gates is the founder of Amazon .":
  "false",
  "Q. Mice have more bones than humans.":
  "true",
  "Q. The first product with a bar code was chewing gum":
  "true",
  "Q. Peanuts are nuts":
  "false",
  "Q. The star is the most common symbol used in all national flags around the world.":
  "false",
  "Q. Fish can not blink.":
  "true"
}  # Pool of questions
import random

questionlist = []
while (len(questionlist) != 5):  # list of 5 questions
  i = random.choice(list(question.keys(
  )))  #Choose Random question from question pool and make a list of it
  if (i not in questionlist):
    questionlist.append(i)  # make a list of random qustions
score = 0
print(""" ________________________________________________________
******************____________________********************
                       QUIZ GAME
                                                  
                                                   """)
for i in questionlist:
  print("\n" + i)
  a = input("\nEnter true or false: ")
  if (a == question[i]):
    print("\nRight answer! +5 points")
    score += 5
  else:
    print("\nWrong answer!")
print("\nTotal Score is :", score)
