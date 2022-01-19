import sys
import random
import time
# Math quiz project

point = 0


def print_1(s):
  for c in s:
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(0.05)
  sys.stdout.write('\n')
  sys.stdout.flush()

def print_2(s):
  for c in s:
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(0.05)
  sys.stdout.write('')
  sys.stdout.flush()


print_1("Welcome to the Math Quiz!")
time.sleep(1)
print_1("You will be required to solve the following problems...")  

x = 0

while x < 5:
  time.sleep(3)
  num1 = random.randint(1, 20)
  num2 = random.randint(1, 20)
  Jerry = random.randint(1,3)  # randomize operation
  if Jerry == 1:
    print_2("Question " + str(x+1) + ": " + str(num1) + " + " + str(num2) + " = "  )
    t = time.time()
    user = input()
    tt = round(time.time()-t)
    if user == str(num1 + num2):
      print("correct you answered in", tt, "seconds!")
      if tt <= 3:
        point = point + 2
      elif tt >3 and tt <= 10:
        point = point + 1
      elif tt >10:
        point = point + 0.5
    else:  
      print("Incorrect")
      print("you entered:", user)
      print("correct answer for", num1, "+", num2, "is", num1 + num2)

  elif Jerry == 2:
    print_2("Question " + str(x+1) + ": " + str(num1) + " * " + str(num2) + " = "  )
    t = time.time()
    user = input()
    tt = round(time.time()-t)
    if user == str(num1 * num2):
      print("correct you answerd in", tt, "seconds!")
      if tt <= 3:
        point = point + 2
      elif tt >3 and tt <=10:
        point = point + 1
      elif tt >10:
        point = point + 0.5
    else:
      print("Incorrect")
      print("you entered:", user)
      print("correct answer for", num1, "*", num2, "is", num1 * num2)
      
  elif Jerry == 3:
    print_2("Question " + str(x+1) + ": " + str(num1) + " - " + str(num2) + " = "  )
    t = time.time()
    user = input()
    tt = round(time.time()-t)
    if user == str(num1 - num2):
      print("correct you answerd in", tt, "seconds!")
      if tt <= 3:
        point = point + 2
      elif tt > 3 and tt <= 10:
        point = point + 1
      elif tt >10:
        point = point + 0.5
      else:
        print("Incorrect")
        print("you entered:", user)
        print("correct answer for", num1, "-", num2, "is", num1 - num2)
  print()
  print()
  x = x+1


time.sleep(3)
print_2("great you had did all the questions\n")
print_2("You got "+ str(point) + " points!")
