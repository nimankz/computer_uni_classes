# this is class practices
# s="Ali"
# print(s[0])
#   #====================================================
# s="Alireza"
# print(s[0:4])
# print(s[0:5])
# print(s[:5])
# print(s[2:])
# print(s[0],s[4])
# print(len(s))
# print(r"alireza\n","nima")
#   #========================================================
# i=0
# while i<=10:
#     print(i)
#     i=i+1
#   # for when you do not know how many times you wanna repeat loop.
#   #================================================================
# i=0
# for i in range(0,10):
#     print(i+1)
#   # for when you know how many times you wanna repeat loop.
#   #================================================================
# i=0
# for i in range(10):
#     print(i+1)
#   # for when you know how many times you wanna repeat loop.
#   #================================================================
# i=10
# for i in range(10,0,-2):
#     print(i)
#   # for when you know how many times you wanna repeat loop.
#   #================================================================
# mylist=["nima",156,[4,8,12]]
# print(mylist[2])
# print(mylist+[2])
#   #================================================================
# mylist=[1,0,12,"alireza","nima"]
# def search(mylist,key):
#     index=-1
#     for item in range(len(mylist)):
#         if mylist[item]==key:
#             index=mylist[item]
#             break
#     print(index)
#     return index
#
# search(mylist,"nima")
#   #=================================================================
# def findmax(mylist):
#     max_index=0
#     max=mylist[0]
#     for item in range(1,len(mylist)):
#         if mylist[item]>max:
#             max=mylist[item]
#             max_index=item
#     print(max,max_index)
#     return[max,max_index]
# mylist=[1,2,3,4,8,10,15]
# findmax(mylist)
#   #=======================================================================

# count=0
# s=0
# ch="y"
# while (ch=="y" or ch=="Y"):
#         count+=1
#         grade=float(input("enter your score:"))
#         s+=grade
#         ch=input("continue? y/n")
# print(s/count)
#   #==================================================================
# def rsum(n):
#     if n==1:
#         return 1
#     else:
#         x=rsum(n-1)
#         return x+n
# print(rsum(4))
#   #==================================================================
#   #for extracting each list item
# def myprint(l,n):
#     if n==1:
#         print(l[n-1])
#     else:
#         myprint(l,n-1)
#         print(l[n-1])
# myprint([1,2,3,4],4)
#   #================================================================
# def factor(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         x=factor(n-1)
#         return x*n
# print(factor(3))
#   #===============================================================
#   #=======================hanoi tower=============================
# def hanoi(n,start,temp,dest):
#     if n==1:
#         print("move from",start,"to",dest)
#     else:
#         hanoi(n-1,start,dest,temp)
#         print("move from",start,"to",dest)
#         hanoi(n-1,temp,start,dest)


#   #=============================================================
# def fibonachi(n):
#     if (n==1) or (n==2):
#         return 1
#     else:
#         return fibonachi(n-1)+fibonachi(n-2)
# print(fibonachi(5))

#   #=================================================================
#   #==========================broken==============================
# def ehanoi(n,start,temp,dest):
#     if (n==1):
#         print("move from",start,"to",dest)
#         print("move from",temp,"to",dest)
#     else:
#         ehanoi(n-1,start,temp,dest)
#         print("move from", temp, "to", start)
#         hanoi(n-2,dest,temp,start)
#         hanoi(n,start,temp,dest)
#
# ehanoi(15,"a","b","c")
#   #===================================================================
# def tarkib(n,k):
#     if (n==k)or(k==0):
#         return 1
#     else:
#         return tarkib(n-1,k-1)+tarkib(n-1,k)
# print(tarkib(5,3))
#   #==================================================================
# def binsearch(x,first,last,item):
#     flag=False
#     result= -1
#     while(first<=last or not flag):
#         mid=(first+last)//2
#         if x[mid]==item:
#             result=mid
#             flag=True
#         elif x[mid]<item:
#             first=mid+1
#         else:
#             last=mid-1
#     return result
#   #=============================================================
# def rbinsearch(x,first,last,item):
#     if last<first:
#         return -1
#     else:
#         mid=(first+last)//2
#         if x[mid]==item:
#             return mid
#         elif item>x[mid]:
#             rbinsearch(x,mid+1,last,item)
#         else:
#             rbinsearch(x,first,mid-1,item)
#   #=============================================================
# def mySort(x):
#     for i in range(len(x)):
#         for j in  range(len(x)-1):
#             if x[j+1]<x[j]:
#                 t=x[j]
#                 x[j]=x[j+1]
#                 x[j+1]=t
#         # for j in range(i+1,len(x)):
#         #     if x[j]<x[i]:
#         #         t=x[i]
#         #         x[i]=x[j]
#         #         x[j]=t
#     return x



#   #================================================================
# def merge(x,y):
#     r=[]
#     lnx=len(x)
#     lny=len(y)
#     i=0
#     j=0
#     while i<lnx and j<lny:
#         if x[i]==y[j]
#             r.append(x[i])
#             r.append(y[j])
#             i+=1
#             j+=1
#         elif x[i]<y[j]:
#             r.append(x[i])
#             i+=1
#         else:
#             r.append(y[j])
#             j+=1
#     for k in range (i,lnx):
#         r.append(x[k])
#     for k in range(j,lny):
#         r.append(y[j])
#     return r
#   #================================================================
# myfile=open(r"I:\python\class\computer\py project\file\readme.txt","r")
# s=myfile.read()
# print(s)
# myfile.close()


# myfile1=open(r"I:\python\class\computer\py project\file\readme.txt","r")
# s=myfile1.read()
# myfile1.close()
# myfile2=open(r"I:\python\class\computer\py project\file\copyreadme.txt","w")
# myfile2.write(s)
# myfile2.close()


# def insert(num,name):
#     myfile=open(r"I:\python\class\computer\py project\file\phone number.txt","a")
#     myfile.write(num)
#     myfile.write(name)



# def insert():
#     myfile=open(r"I:\python\class\computer\py project\file\phone book.txt","a")
#     flag=True
#     while flag:
#         name=input("enter your name:")
#         num=input("enter your number:")
#         myfile.write(name+"\n")
#         myfile.write(num+"\n")
#         ch=input("do you want to continue? (y/n)")
#         if ch.lower()=="n":
#             flag=False
#     myfile.close()
# insert()

# def search(name):
#     myfile=open(r"I:\python\class\computer\py project\file\phone number.txt")
#     flag=True
#     while flag:
#         s=myfile.readline()
#         if s=="":
#             flag=False
#         else:
#             if s.rstrip("\n")==name:
#                 number=myfile.readline()
#                 print(number)
#                 flag=False
#     myfile.close()


