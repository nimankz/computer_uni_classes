#this is some practices in TA-class
# print(bool(15))
# print(bool("hello"))
# print(bool(""))
#   #==============================================================
# work_hours=int(input("How many hours do you work in a day?"))
# salary_per_hour=int(input("How much money do you earn per hour?"))
# salary=work_hours*salary_per_hour
# if salary>100:
#     print("rich")
# elif 50<=salary<=100:
#     print("normal")
# else:
#     print("poor")
#   #==================================================================
# x=int(input("number:"))
# if x>0:
#     print("+")
# elif x<0:
#     print("-")
# else:
#     print("0")
#   #====================================================================
# x=input("what you wanna eat?")
# if x=="egg":
#     print("300")
# elif x=="rice":
#     print("200")
# elif x=="cheese":
#     print("100")
# else:
#     print("welcome")
#   #=====================================================================
# def m(x,y,z):
#     x = (x**(y*z))
#     print(x)
# m(2,2,3)
#   #=======================================================================
# name="nima"
# print("hello , %s"%name) #    #for numbers use %i
# print("hello , {}".format(name))
# print(f"hello , {name}")
#   #=======================================================================
# def it_is_prime(number):
#     sum_of_diviseion=0
#     for item in range (1,number):
#         if number%item==0:
#             sum_of_diviseion+=item
#     if sum_of_diviseion == 1:
#         return True
#     else:
#         return False
#
# def prime_range(a,b):
#     for item in range(a,b+1):
#         if it_is_prime(item)==True:
#             print(item)
#
# prime_range(1,100)
#===============================================================================
# m="welcome to jungle"
# print(m.split())


n=int(input())

q=input().split()
for i in range(n):
    q[i]=int(q[i])

a=input().split()
for i in range(n):
    a[i]=int(a[i])

sum=0
for i in range(n):
    sum+=a[i]*q[i]
print(sum)