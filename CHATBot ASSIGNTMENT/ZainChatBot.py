#_____________________________________________import_____________________________________________#
import time
from random import randint
import re
import csv
name=""
c=0
###########################################USER FUNCTION#################################################
def user():
   path="C:\\Users\\user\\Desktop\\users.csv"
   n=input("dear contact please enter your name : ")
   with open(path) as file:
       print(n)
       reader=csv.reader(file)
       next(reader)
       for row in reader:
           if row and row[0]==n :
               print("welcome contact :"+row[0]+" your phone number :"+row[1])
               return None
           
   with open(path,'a') as file:
       fieldnames = ['Name', 'Phone','Behaviour']
       w=csv.DictWriter(file , fieldnames=fieldnames)
       p=input("welcome "+n+"you are a new user enter your phone number please")
       w.writerow({'Name':n,'Phone':p,'Behaviour':"new user"})
       file.close()
###############################################LEARN FUNCTION################################################
def learn(var):
    v=var
    path="C:\\Users\\user\\Desktop\\Zain.csv"
    with open(path,'a') as file:
        fieldnames = ['Q', 'Answer']
        w=csv.DictWriter(file , fieldnames=fieldnames)
        print("im not understanding you can you give me answer for this quistion ?")
        n=input("enter string : ")
        w.writerow({'Q':v,'Answer':n})
        print("thanks you for helping me to grow")
        
        
    return ""
#############################################ZAIN DIRECTORY##################################################

def ZainDir(var):
     path="C:\\Users\\user\\Desktop\\Zain.csv"
     file = open(path)
     v= var.lower()
     reader=csv.reader(file)
     next(reader)
#__________________________     
     for row in reader:
         if row:
             a=re.findall(r".*"+row[0]+".*?",v)
             if  (len(a)>0):
                 return row[1]
                 file.close()
                 break
     return learn(var) 
 
###############################################BOT NAME################################################
def about(var):
    v=var
    a=re.findall(r"who are you?|.*?your.*?name|.*?you.*?do",var)
    if(len(a))>0:
        return "Im Zain Jordan Chat Bot ^_^ you can ask me about our :  mobile Subscriptions , internet , Service codes  and  any thing in your mind"
    else:
        return ZainDir(v)
#############################################Greeting##################################################
def greet(var):
    global c
    if(c==0):
        user()
        c+=1
    v=var
    greetkey=["hi","hello","how are you","wassap","sup","what's up"]
    grettresponse=["hi","hello","how are you","wassap","sup","what's up"]
    l=len(grettresponse)
    a=var.split()
    for i in a :
        if i.lower() in greetkey:
            return(grettresponse[randint(0,l-1)])
    return about(v)
#################################################MAIN##############################################
n=input("enter string : ")
while n!="end":
    time.sleep(1)
    print(greet(n))
    print()
    n=input("enter string : ")
