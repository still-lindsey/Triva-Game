import pickle
import random

FILENAME="game.txt"

class Question:

  def __init__(self, question, a1, a2, a3, a4, correct):
    self.__question=question
    self.__a1=a1
    self.__a2=a2
    self.__a3=a3
    self.__a4=a4
    self.__correct=correct

  def set_question(self, question):
    self.__question=question

  def set_a1(self, a1):
    self.__a1=a1

  def set_a2(self, a2):
    self.__a2=a2

  def set_a3(self, a3):
    self.__a3=a3
  
  def set_a4(self, a4):
    self.__a4=a4

  def set_correct(self, correct):
    self.__correct=correct

  def get_question(self):
    return self.__question

  def get_a1(self):
    return self.__a1

  def get_a2(self):
    return self.__a2

  def get_a3(self):
    return self.__a3
  
  def get_a4(self):
    return self.__a4

  def get_correct(self):
    return self.__correct

  def __str__(self):
    return self.__question + "\n1." + self.__a1 + "\n2." + self.__a2 + "\n3." + self.__a3 + "\n4." + self.__a4

def main():
  questions_list=get_question_file(FILENAME)

  #shuffle questions
  random.shuffle(questions_list)

  print("Player 1's Game")
  player1score=play_game("1",questions_list)

  print("Player 2's Game")
  player2score=play_game("2",questions_list)

  #display winner
  print("Player 1 score: ", player1score, sep="")
  print("Player 2 score: ", player2score, sep="")
  if player1score==player2score:
    print("Tie game.")
  elif player1score>player2score:
    print("Player 1 wins!")
  else:
    print("Player 2 wins!")

  #close and save questions file
  close_save_questions(questions_list)




def get_question_file(FILENAME):
  try:
    input_file=open(FILENAME, "rb")

    questions_list=pickle.load(input_file)

    input_file.close()
  except:
    #no questions exist so write in questions. Items will be objects
    questions_list=create_questions()

  return questions_list

def create_questions():
  questions_list=[0]*10

  for i in range(0, len(questions_list)):
    print("Enter information for Question ", i+1, ":", sep="")
    q=input("Question: ")
    a1=input("Answer choice 1: ")
    a2=input("Answer choice 2: ")
    a3=input("Answer choice 3: ")
    a4=input("Answer choice 4: ")
    correct=input("Correct answer: ")

    question=Question(q,a1,a2,a3,a4,correct)

    questions_list[i]=question

  return questions_list

def play_game(player, questions_list_shuffled):
  #display and answer 5 random questions
  if player=="1":
    score=0
    for i in range(0, 5):
      print("Question ", i+1, ":", sep="")
      #display question
      question=questions_list_shuffled[i]
      print(question)

      answer=input("Select correct answer (1-4): ")
      
      if answer==question.get_correct():
        print("Correct!")
        score+=1
      else:
        print("Incorrect.")
      print()
    
    return score
  else:
    score=0
    for i in range(5, 10):
      print("Question ", i+1, ":", sep="")
      question=questions_list_shuffled[i]
      #display question
      print(question)

      answer=input("Select correct answer (1-4): ")
      
      if answer==question.get_correct():
        print("Correct!")
        score+=1
      else:
        print("Incorrect.")
      print()
    
    return score

def close_save_questions(questions_list):
  output_file=open(FILENAME, "wb")

  pickle.dump(questions_list, output_file)

  output_file.close()

main()
