# print("hello world!\t", "mamad")
# print("hello world!\n", "mamad")
# print(""" He told me "don't do anything" .""")
# # ' and " and """ can be used for printing a string
# age = 25
# # print("My age is", age,",how about you?")
# #=====================================================
# max_degree = 46
# avrage_temprture = 32
# min_degree = 25
# print("\nmax degree is:",max_degree
#        ,"\navrage tempture is:", avrage_temprture
#         ,"\nmin degree is:" ,min_degree)
# #enter wasn't effective
# #=================================================================
#
# age = 19
# score = 15.4
# name = "Nima"
# job ="programmer"
# print(type(name),type(age),type(score),type(job))
# print("My name is",name,";")
# print("I'm",age,".")
# print("My score was",score,"in yesterday exam.")
# print("My job is",job)
# #===================================================================
# print("lets get known with you more,tell me about yourself.")
# name=input("what is your name?")
# job = input("what's your job?")
# age = int(input("How old are you?"))
# # age = int(age)
#
# print("So your name is",name)
# print(",You are",age)
# print("And you are a/an",job)
#
# print("It's nice to see you :)")
# print(type(name),type(job),type(age))
# #===================================================================
# print(5/2)
# print(5//2)
# print(5//3)
# #the second one just gives the int part
#
# #======================================================================
# print("For starting business with us you have to pay 20% of the house price")
# House_Price=135000.00
# pay = House_Price * 0.20
# print("Which means you have to pay",pay,"to start your business.")
# #===========================================================
# print("You have bought 3 books and you will have 20% discount.")
# pay=(21000+78000+65000)*0.8
#
# print("So your cost aftrer discont would be:",pay)
# #================================================================================
#
#
#
# number=int(input("Enter a number in seconds:"))
# hours=number//3600
# remainingSeconds1=number-(hours*3600)
# minutes=remainingSeconds1//60
# seconds=remainingSeconds1-(minutes*60)
# # print("It would be :\n",hours,"hours ,",minutes,"minutes and",seconds,"seconds")
# print(hours,minutes,seconds,sep=":")
# # print("Hours :) .")
# # ================================================================
# print("5200",end=" ")
# print("hello world!")
# # ================================================================
# presentMoney=int(input("How much money do you want to investigate ?"))
# years=int(input("For how long?(Please insert in years): "))
# rate=float(1.2)
# finalMoney=presentMoney*(rate**years)
# print("After ",years,"years yor money would be :",finalMoney)

# finalMoney=int(input("How much money do you want to earn?"))
# years=int(input("For how long?(Please insert in years): "))
# rate=float(1.2)
# presentMoney=finalMoney/(rate**years)
# print("So you should invest ",presentMoney,"to earn",finalMoney, "after",years,"years.",sep=" ")
#   #=============================================================================
# print('they\'re falling.')
# print("c:\\user\\desktop\\nima")
#   #===========================================================================
# print(format(112.3568,'.2f'))
# celsius=float(input("Enter temperature in celsius:"))
# fahrenheit=(1.8*celsius)+32
# print("It's",fahrenheit,"degrees in fahrenheit.",sep=" ")
#   # ========================================================================
#   # def for making functions
# def convert(number):
#     hours = number // 3600
#     remainingSeconds1 = number - (hours * 3600)
#     minutes = remainingSeconds1 // 60
#     seconds = remainingSeconds1 - (minutes * 60)
#     print(hours,minutes,seconds,sep=":")

#
# number=1501
# convert(number)
# convert(5623)
# convert(1)
#   #=============================================================================


# print("It would be :\n",hours,"hours ,",minutes,"minutes and",seconds,"seconds")

# print("Hours :) .")
# def main():
#     print("I have a massage for you.")
#     message()
#     print("That was it, have a great day.")
#
# def message():
#     print("I am Cyrus")
#     print("King of persian empire")
#
# main()

#   #  ========================================================
# def step1():
#     input("Please write your first name. ")
# def step2():
#     input("Please write your last name.")
# def step3():
#     input("Please enter your job.")
# def step4():
#     input("How much do you earn?")
# def finish():
#     print("You are registered successfully.")
#
# def main():
#     print("Welcome to registration.Will you please fill the list?")
#     step1()
#     print("good!")
#     step2()
#     step3()
#     print("oh!really!!?")
#     step4()
#     finish()
#     print("thanks for collaboration")
# main()
#   #====================================================================
# def calculator(x,y):
#     print("summation=",x+y)
#     print("subtraction=",x-y)
#     print("multiplication=",x*y)
#     print("division=",x/y)
#
# calculator(50,5)
#   #====================================================================
# x,y,z=10,2,6
# # flag=x>10 and y<3 and z==6
# flag=x>10 or y<3 or z==6
# print(flag)
#   #===================================================================
# number=int(input("enter your number:"))
# if number==1:
#     print("I")
# elif number==2:
#     print("II")
# elif number==3:
#     print("III")
# elif number==4:
#     print("IV")
# elif number==5:
#     print("V")
# elif number==6:
#     print("VI")
# else:
#     print("Not in range.")
#   #=======================================================================================
# weight=float(input("enter your weight in kg:"))
# height=float(input("enter your height in meter:"))
# bmi=weight*(height**2)
#
# if bmi>250:
#     print("over weight!")
# elif bmi<180:
#     print("under weight!")
# else:
#     print("normal range.")
#   #=============================================================================================
# i=1
# while i<=10:
#     print("hello")
#     i=i+1
# print("finish")
#   #==================================fuck to real========================================
# p=1
# i=1
# n=int(input("Enter your number:"))
# while i<=n:
#     p=p*i
#     i=i+1
# print(p)
# n=int(input("Enter your number:"))
# i=1
# s=0
# while i<=n:
#     s=s+i
#     i=i+1
# print(s)
# n=int(input("Enter your number:"))
# i=1
# s=0
# while i<=n:
#     if i%2==0:
#         s=s+i
#     i=i+1
# print(s)
#  #  ======     i=i+1 , i+=1 they are equal also we can use *,/,-, ========
# x=5
# y=3
# # x=x+y
# x+=y
# print(x)
#   #=================================================================================
# check="y"
# while check=="y":
#     object_name=str(input("what is your object's name?"))
#     object_quantity=int(input("how many of that do you have?"))
#     print("so you have",object_quantity,"of",object_name)
#     check=input("do you wanna add another object?(y/n)")
# print("that was it. thanks for your patience.")
#   #===================================================================================
# def fuck_to_real():
#     p=1
#     i=1
#     n=int(input("Enter your number:"))
#     while i<=n:
#         p=p*i
#         i=i+1
#     print(p)
# fuck_to_real()
# #=====================================================================================
# nrow=8
# ncol=6
# for i in range(nrow):
#     for i in range(ncol):
#         print("*",end="")
#     print("\n")
#   #====================================================================================
def fuck_to_real(n):
    p=1
    for i in range(1,n+1):
        p=p*i
    return p
def tarkib(n,k):
    return fuck_to_real(n)/(fuck_to_real(n-k)*fuck_to_real(k))
print(tarkib(5,2))

nrow=5
for i in range(nrow):
    for j in range(i+1):
        print(tarkib(i,j),"     ",end=" ")
    print()