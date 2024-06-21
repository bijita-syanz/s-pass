#s-pass v1.1 created by bjt

import os as os
import random
import lists
print('''
===================important===================
      [created by : bjt   , v1.2]
      to get more informations about victims
      you can use the OSINT tools :     ''')
print('(IMPORTANT)how to use :')
print("INTER THE NEXT INFORMATION")
print(' IF YOU DONT KNOW AN INFORMATION press INTER')
print("do you want to save this woprd list in txt filee al ready in your PC ")
savef = input("[y/n]")
if savef == "y" :
    listfile = input("inter the path of the txt file : ")
    try:
        with open(listfile ) as file :
            pass
    except FileNotFoundError :
        print("this file is NotFound")
        exit()
    except FileExistsError :
        print("this file is not ecxists")
        exit()
else :
    filenum =  random.randint(0,1000)
    filenum = str(filenum)
    print("the file is : list"+filenum+" ")
    listfile = "list"+filenum+".txt"
    pass
run = True
#must words usin in passwords
adiition = ()
name = input("firstname :")
name2 = input('lastname :')
mname = input('mother name :')
fname = input('father name :')
phnum = input('phone number :')
bf = input('boy or girl freind name :')
list1 = (name , name2 ,mname ,fname , bf , phnum)
names = (name ,name2)
print("do you want to add more's informations about victim or add a key word :")
add = input('[y/n] : ')
add = add.lower()
if add == "y" :
    add1 = input('inter information (keyword) : ')
    list1 = (name , name2 ,mname ,fname , bf , phnum , add1)
    #other information
    print("do you want to add more's informations about victim or add a key word :")
    add = input('[y/n] : ')
    add = add.lower()
    if add == "y" :
        add2 = input('inter information (keyword) : ')
        list1 = (name , name2 ,mname ,fname , bf , phnum , add1, add2)
    
    else : 
        pass
else :
    pass

print('inter the date of birth of the victim')
D = input(' inter the day of birth : ')
M = input('inter the monthe of birt : ')
Y = input('inter the year of birt : ')
if D == "pass" :
    D = ""
else :
    pass
if M == "pass" :
    M = ""
else :
    pass
if Y == "pass" :
    Y = ""
else :
    pass


for i in lists.passwords :
    if len(i) > 8 :
        print(i)
        with open(listfile ,"a") as text:
           text.write(str(i +"\n"))
    else:
       pass
if run == True :
    for i1 in list1 :
        for i2 in list1 :
            if i2 == i1 :
                pass
            else :
                print(i1+i2)
                print(i1,i2)

                with open(listfile ,"a") as text:
                    text.write(str(i1+i2 +"\n"))
                    text.write(str(i1+" "+i2 +"\n"))
if run == True:
    for i1 in list1 :
        for i2 in list1 :
            for i3 in list1:
                if i2 == i1 == i3:
                  pass
                else :
                    print(i1+i2+i3)
                    print(i1,i2,i3)
                    with open(listfile ,"a") as text:
                        text.write(str(i1+i2+i3 +"\n"))
                        text.write(str(i1+" "+i2+" "+i3 +"\n"))
if run == False :
    exit()
else :
    pass
#loops can use tje date of birth
DATELIST = (M,D)
for i in DATELIST :
    for j in DATELIST:
        if i == j :
            pass 
        else :
            for name in names :
                print(name+i+j+"\n")
                print(name+" "+i+""+j)
                with open(listfile , "a") as text:
                    text.write(name+i+j+"\n")
                    text.write(name+" "+i+" "+j+"\n")
for name in names :
    print(name+Y)
    print(name+' '+Y)
    with open(listfile ,"a") as text:
        text.write(name+Y+"\n")
        text.write(name+' '+Y+"\n")
DATELIST = (Y,M,D)
for j1 in DATELIST:
    for j2 in DATELIST:
        if j2 == Y :
            pass
        else :
            for j3 in DATELIST:
                if j1 != j2 and j3 != j2 and j1 != j3 :
                    datevar = (j1+j2+j3)
                    datevar1 = (j1+j2+j3)
                    datevar2 = (j1+"/"+j2+"/"+j3)
                    datetvarlist = (datevar,datevar1,datevar2)
                    for j4 in datetvarlist :
                        print(j4)
                    for date in datetvarlist :
                        for name in list1 :
                            print(name, date)
                            print(name+date)
                            with open(listfile ,"a") as text:
                                text.write(str(name+" "+date +"\n"))
                                text.write(str(name+date +"\n"))
                            for name2 in list1 :
                                if name2 != name :
                                    print(name,name2,date)
                                    print(name+name2+date)
                                    with open(listfile ,"a") as text:
                                        text.write(str(name+" "+name2+" "+date +"\n"))
                                        text.write(str(name+name2+date +"\n"))
                                else :
                                    pass
                else:
                    pass
for i in names:
    for j in lists.morocco_password_endings:
        print(i+j)
        with open(listfile ,"a") as text :
            text.write(i+j+"\n")
for i in names :
    for j in lists.morocco_password_endings_pins :
        print(i+j)
        with open(listfile ,"a") as text:
            text.write(i+j+"\n")           
for i in names :
    for j in lists.morocco_password_endings_pins :
        for k in lists.morocco_password_endings_sympols:
            print(i+j+k)
            with open(listfile, "a") as text:
                text.write(i+j+k+'\n')

                   
#must utilis words in passwords

print("you are using S-PASS V1.2")
print('this tool created by "Bjt"')


 








