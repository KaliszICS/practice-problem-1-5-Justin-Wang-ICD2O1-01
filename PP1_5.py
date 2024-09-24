23
import math


def q1():
  #Write Assignment code here
    One = input("Input an integer: ")
    One = int(One)
    One = One + 3 
    print = ("The integer is:", One)
def q2():
  #Write Assignment code here
   One = input("Input a number: ")
   One = One + "4"
   One = (float(One))
   One = One + 2
   print("A number is: ", One)
def q3():
  #Write Assignment code here
   Num = input("Input a radius: ")
   radius = (float(Num))
   Pi = 3.14
   area = Pi * (radius ** 2)
   print("The area of a circle is: ", area)
def q4():
  #Write Assignment code here
  Num = input("Input a number: ")
  Num = (float(Num))
  Num = Num * 12 
  Num = math.floor(Num)
  print("The number is: ", Num)
def q5():
  #Write Assignment code here
  Set = input("Input an integer: ")
  Set = (int(Set))
  Set = Set+5
  print("Your number is :+5", Set)
#Comment this code out when running tests
#Do not comment this out when running your program normally

q1()
q2()
q3()
q4()
q5()
