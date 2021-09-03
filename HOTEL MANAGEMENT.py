print("WARNING : If you will eneter wrong data the program will automatically terminate for security purposes")
print()
usernam=input('Enter your USERNAME associated with MYSQL: ')
paswr=input('Enter your PASSWORD associated with MYSQL: ')

import mysql.connector
db=mysql.connector.connect(host="localhost",user=usernam,passwd=paswr)

obj=open('pr.txt','a+')
obj.write('0')
obj.seek(0)
x=obj.read()

if x=='0':
    import mysql.connector
    db=mysql.connector.connect(host="localhost",user=usernam,passwd=paswr)
    obj1=db.cursor()
    s1='create database projects'
    obj1.execute(s1)
    db.commit()
    
    db=mysql.connector.connect(host="localhost",user=usernam,passwd=paswr,database="projects")

    muneem=db.cursor()
    s1='create table dataq(name char(20),phone char(20),address char(100),pincode char(20),age char(3),checkin date,checkout date,username char(20),password char(20),room_no int(3),bill int(5));'
    s2='create table food(breakfast char(20),costb int(4),lunch char(50),costl int(4),dinner char(50),costd int(4));'
    s3='create table gym(Time_Of_Workout char(50),price int(50),Services char(50),Prices int(50));'
    s4='create table orderforfood(username char(50),b char(50),l char(50),d char(50),room_no char(5));'
    s5='create table room(ac_single char(3),ac_double char(3),non_ac_single char(3),non_ac_double char(3));'
    muneem.execute(s1)
    muneem.execute(s2)
    muneem.execute(s3)
    muneem.execute(s4)
    muneem.execute(s5)

    s6='insert into food values("Poha",%s,"Pizza",%s,"Chicken Biryaani",%s)'
    s61=(120,100,160)
    muneem.execute(s6,s61)
    db.commit()
    s7='insert into food values("Paasta",%s,"Thali",%s,"Korma",%s)'
    s71=(120,210,150)
    muneem.execute(s7,s71)
    db.commit()
    s8='insert into food values("Spring Rolls",%s,"Daal Makhni & Lachha Paratha",%s,"Soya Chaap",%s)'
    s81=(130,110,140)
    muneem.execute(s8,s81)
    db.commit()
    s9='insert into food values("Sandwich",%s,"Daal Bhaati",%s,"Khichdi",%s)'
    s91=(130,110,200)
    muneem.execute(s9,s91)
    db.commit()

    s10='insert into gym values("20 min",%s,"Trainer",%s)'
    s101=(200,350)
    muneem.execute(s10,s101)
    db.commit()
    s11='insert into gym values("30 min",%s,"Sauna",%s)'
    s111=(275,300)
    muneem.execute(s11,s111)
    db.commit()
    s12='insert into gym values("40 min",%s,"Pool",%s)'
    s121=(350,200)
    muneem.execute(s12,s121)
    db.commit()
    s13='insert into gym values("50 min",%s,"Massage",%s)'
    s131=(425,250)
    muneem.execute(s13,s131)
    db.commit()
    s14='insert into gym values("60 min",%s,"Spa",%s)'
    s141=(500,200)
    muneem.execute(s14,s141)
    db.commit()

    s15='insert into orderforfood values("hotel","0","0","0","0")'
    muneem.execute(s15)
    db.commit()

    st1='insert into room values("301","326","351","376")'
    muneem.execute(st1)
    st2='insert into room values("302","327","352","377")'
    muneem.execute(st2)
    st3='insert into room values("303","328","353","378")'
    muneem.execute(st3)
    st4='insert into room values("304","329","354","379")'
    muneem.execute(st4)
    st5='insert into room values("305","330","355","380")'
    muneem.execute(st5)
    st6='insert into room values("306","331","356","381")'
    muneem.execute(st6)
    st7='insert into room values("307","332","357","382")'
    muneem.execute(st7)
    st8='insert into room values("308","333","358","383")'
    muneem.execute(st8)
    st9='insert into room values("309","334","359","384")'
    muneem.execute(st9)
    st10='insert into room values("310","335","360","385")'
    muneem.execute(st10)
    st11='insert into room values("311","336","361","386")'
    muneem.execute(st11)
    st12='insert into room values("312","337","362","387")'
    muneem.execute(st12)
    st13='insert into room values("313","338","363","388")'
    muneem.execute(st13)
    st14='insert into room values("314","339","364","389")'
    muneem.execute(st14)
    st15='insert into room values("315","340","365","390")'
    muneem.execute(st15)
    st16='insert into room values("316","341","366","391")'
    muneem.execute(st16)
    st17='insert into room values("317","342","367","392")'
    muneem.execute(st17)
    st18='insert into room values("318","343","368","393")'
    muneem.execute(st18)
    st19='insert into room values("319","344","369","394")'
    muneem.execute(st19)
    st20='insert into room values("320","345","370","395")'
    muneem.execute(st20)
    st21='insert into room values("321","346","371","396")'
    muneem.execute(st21)
    st22='insert into room values("322","347","372","397")'
    muneem.execute(st22)
    st23='insert into room values("323","348","373","398")'
    muneem.execute(st23)
    st24='insert into room values("324","349","374","399")'
    muneem.execute(st24)
    st25='insert into room values("325","350","375","400")'
    muneem.execute(st25)
    db.commit()



    
def homepage():
    print("              ****Welcome to HOTEL J.K. TOWER****\n 1.REGISTER A NEW ACCOUNT\n 2.BOOK A ROOM HERE\n 3.BOOK YOUR MEALS\n 4.TRY OUR GYM SERVICES\n 5.FOR CHECK-OUT\n 6.EXIT")
    print()
    inpu=int(input("Enter you reponse: "))
    if inpu==1:
        data()
        homepage()
    if inpu==2:
        roomrent()
    if inpu==3:
        food()
    if inpu==4:
        gym()
    if inpu==5:
        bill()
    if inpu==6:
        EXIT()
    else:
        print("Enter valid value!")
        homepage()
def data():
    db=mysql.connector.connect(host="localhost",user=usernam,passwd=paswr,database="projects")
    muneemji=db.cursor()
    name=input("Enter you Name: ")
    i=1
    while i>0:
        phone=input("Enter you Phone No.: ")
        if len(phone)>10:
            print('Enter phone Number Again!')
            i=1
        else:
            i=0
    
    add=input("Enter you Address: ")
    j=1
    while j>0:
        pincode=input("Enter you Pincode: ")
        if len(pincode)>6:
            print('Enter Pincode Again!')
            j=1
        else:
            j=0
    age=input('Enter your Age: ')
    
    def use():
        s1="select username from dataq"
        muneemji.execute(s1,)
        usernames=muneemji.fetchall()
        global username
        username=input("Enter your username: ")
        global a
        a=0
        for i in range(len(usernames)):
            if usernames[i][0]==username:
                a=1
    use()
    x=0
    while a==1:
        x=1
        print('Already Exists!!!')
        y=use()
    else:
        print('You are a new user. Welcome!!!')
        if x==0:
            z=username
        else:
            z=username
        
        
      
    
    passw=input("Enter pasword: ")
    room=0
    bill=0
    stat1="insert into dataq (name,phone,address,pincode,age,username,password,room_no,bill) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    stat2=(name,phone,add,pincode,age,z,passw,room,bill)
    muneemji.execute(stat1,stat2)
    db.commit()
    print()
    print("Data Entry Succesfull!")
    print()

def roomrent():
    db=mysql.connector.connect(host="localhost",user=usernam,passwd=paswr,database="projects")
    mycus=db.cursor()
    user=input("Enter username: ")
    stat1="select password from dataq where username=%s"
    stat2=(user,)
    mycus.execute(stat1,stat2)
    passw=mycus.fetchall()
    if len(passw)==0:
        print("Usrname doesn't exist.Please go on 1st option to register.")
        homepage()
    else:
        passw1=input("Enter your password: ")
        if passw1==passw[0][0]:
            print()
            print("Login successful!\n ")
            print()
            
        else:
            print()
            print("Wrong data entered!!!")

            roomrent()
            
        checkin_date=input("Enter Check-in date(YYYYMMDD): ")
        checkout_date=input("Enter Check-out date(YYYYMMDD): ")
        if len(checkin_date)>8 and len(checkout_date)>8:
            print("enter it again")
            roomrent()
        t1="update dataq set checkin=%s,checkout=%s where username=%s"
        t2=(checkin_date,checkout_date,user)
        mycus.execute(t1,t2)
        db.commit()
        print()

        s1="select checkin from dataq where username=%s"
        s2=(user,)
        mycus.execute(s1,s2)
        date8=mycus.fetchall()
        y1=date8[0][0]
        z1=str(y1)
        a1=z1[0:4]
        b1=z1[5:7]
        c1=z1[8:10]
        if b1[0]=='0':
            b1=b1[1]
        if c1[0]=='0':
            c1=c1[1]
        ss1="select checkout from dataq where username=%s"
        ss2=(user,)
        mycus.execute(ss1,ss2)
        date=mycus.fetchall()
        y2=date[0][0]
        z2=str(y2)
        a2=z2[0:4]
        b2=z2[5:7]
        c2=z2[8:10]
        if b2[0]=='0':
            b2=b2[1]
        if c2[0]=='0':
            c2=c2[1]
        from datetime import date 
  
        def numOfDays(date1, date2): 
            return (date2-date1).days
            
        date1 = date(int(a1), int(b1), int(c1)) 
        date2 = date(int(a2), int(b2), int(c2))
        days=numOfDays(date1, date2)
        if days==0:
            days=days+1
        elif days<0:
            print("wrong value entered.Enter the date again")
            print()
            roomrent()
        else:
            pass
        
        print("                   ****Which type of room you want?**** \n 1.non-ac double bed(1500\day) \n 2.non-ac single bed(1100\day) \n 3.ac double bed(3500\day) \n 4,ac single bed(2600\day )")

        print()
        
        response=int(input("Enter the room  you want: "))
        print()
        if (response>4) or (response<1):
            print("Kindly enter correct value!")
            roomrent()
        else:
            cost1=1500
            cost2=1100
            cost3=3500
            cost4=2600
            if response==1:
                stateme1="select ac_single from room where ac_single like '___'"
            if response==2:
                stateme1="select ac_double from room where ac_double like '___'"
            if response==3:
                stateme1="select non_ac_single from room where non_ac_single like '___'"
            if response==4:
                stateme1="select non_ac_double from room where non_ac_double like '___'"
            print()
            mycus.execute(stateme1)
            avairooms=mycus.fetchall()
            print("The rooms avilable for you are: ")
            print()
            p=len(avairooms)
            r=0
            for i in range(0,5):
                for j in range(0,5):
                    if r<p:
                        print(avairooms[r][0],end=' ')
                        r=r+1
                    else:
                        pass
                print()
            
         
    
            
            
            if response==1:
                print("\nYour cost for ",days,"days is: ", days*cost1)
                print()
                cost=days*cost1
            if response==2:
                print("\nYour cost for ",days,"days is: ", days*cost2)
                print()
                cost=days*cost2
            if response==3:
                print("\nYour cost for ",days,"days is: ", days*cost3)
                print()
                cost=days*cost3
            if response==4:
                print("\nYour cost for ",days,"days is: ", days*cost4)
                print()
                cost=days*cost4
            print("\nDo you want to book it?\n (Answer 1 if yes and 0 if no)")
            print()
            resp=input("Enter your response: ")
            print()
            if resp!='1' and resp!='0':
                print("Enter correct input!")
                roomrent()
            if resp=='1':
                roomno=input("Select your room no.: ")
                print()
                if len(roomno)>3 or len(roomno)<3:
                    print("enter valid value!")
                    roomrent()
                else:
                    x='0'
                
                    if response==1:
                        s1="update room set ac_single=%s where ac_single=%s"
                        s2=(x,roomno)
                        mycus.execute(s1,s2)
                        db.commit()
                        print("You have booked your room!\n")
                        ss1="update dataq set room_no=%s where username=%s"
                        ss2=(roomno,user)
                        mycus.execute(ss1,ss2)
                        db.commit()
                        sss1='update dataq set bill=%s where username=%s'
                        sss2=(days*cost1,user)
                        mycus.execute(sss1,sss2)
                        db.commit()
                        homepage()
                    if response==2:
                        s1="update room set ac_double=%s where ac_double=%s"
                        s2=(x,roomno)
                        mycus.execute(s1,s2)
                        db.commit()
                        print("You have booked your room!\n")
                        ss1="update dataq set room_no=%s where username=%s"
                        ss2=(roomno,user)
                        mycus.execute(ss1,ss2)
                        db.commit()
                        sss1='update dataq set bill=%s where username=%s'
                        sss2=(days*cost2,user)
                        mycus.execute(sss1,sss2)
                        db.commit()
                        homepage()
                    if response==3:
                        s1="update room set non_ac_single=%s where non_ac_single=%s"
                        s2=(x,roomno)
                        mycus.execute(s1,s2)
                        db.commit()
                        print("You have booked your room!\n")
                        ss1="update dataq set room_no=%s where username=%s"
                        ss2=(roomno,user)
                        mycus.execute(ss1,ss2)
                        db.commit()
                        sss1='update dataq set bill=%s where username=%s'
                        sss2=(days*cost3,user)
                        mycus.execute(sss1,sss2)
                        db.commit()
                        homepage()
                    if response==4:
                        s1="update room set non_ac_double=%s where non_ac_double=%s"
                        s2=(x,roomno)
                        mycus.execute(s1,s2)
                        db.commit()
                        print("You have booked your room!\n")
                        ss1="update dataq set room_no=%s where username=%s"
                        ss2=(roomno,user)
                        mycus.execute(ss1,ss2)
                        db.commit()
                        sss1='update dataq set bill=%s where username=%s'
                        sss2=(days*cost4,user)
                        mycus.execute(sss1,sss2)
                        db.commit()
                        homepage()
            if resp=='0':
                print()
                print("Enter 1 to calculate room rent again....\n Enter 0 to go to home page.....")
                print()
                r1=int(input('Enter your response: '))
                if r1==1:
                    roomrent()
                if r1==0:
                    homepage()
                else:
                    print("Enter valid value!")
def food():
    db=mysql.connector.connect(host="localhost",user=usernam,passwd=paswr,database="projects")
    h=0
    mycus=db.cursor()
    user=input("Enter username: ")
    stat1="select password from dataq where username=%s"
    stat2=(user,)
    mycus.execute(stat1,stat2)
    passw=mycus.fetchall()
    if len(passw)==0:
        print("Usrname doesn't exist.Please go on 1st option to register.")
        homepage()
    else:
        passw1=input("Enter you password: ")
        print()
        if passw1==passw[0][0]:
            print("Login successful!\n ")
        else:
            print("Wrong data entered!!!")
            food()
    state1='select username from orderforfood'
    mycus.execute(state1,)
    data1=mycus.fetchall()
    y=len(data1)
    i=y
    x=1
    while i==y and x==1:
        if data1[i-1][0]==user:
            x=0
            y=y-1
        
        else:
            speciall1='select room_no from dataq where username=%s'
            speciall2=(user,)
            mycus.execute(speciall1,speciall2)
            dataa=mycus.fetchall()
            rooom=dataa[0][0]
            statement1='insert into orderforfood values(%s,%s,%s,%s,%s)'
            statement2=(user,h,h,h,str(rooom))
            mycus.execute(statement1,statement2)
            db.commit()
            x=0
            
    print()
    print('What you want to have? \n 1.breakfast \n 2.lunch \n 3.dinner')
    print()
    resp=int(input('Enter you response: '))
    print()
    if resp==1:
        state1='select breakfast,costb from food'
        mycus.execute(state1,)
        data=mycus.fetchall()
        print('The menu for breakfast is: ')
        i=1
        cost=0
        while i>0:
            for i in range(0,4):
                print(str(i+1),data[i][0],' - ',data[i][1])
            print()
            print('Kindly enter the no. of item you want to have....')
            print()
            respo=int(input('Enter your response: '))
            cost+=int(data[respo-1][1])
            sss1='update orderforfood set b=%s where username=%s'
        
            special1='select b from orderforfood where username=%s'
            special2=(user,)
            mycus.execute(special1,special2)
            dat=mycus.fetchall()
            if dat[0][0]=='0':
                sss2=(respo,user)
                mycus.execute(sss1,sss2)
                db.commit()
            else:
                y=str(dat[0][0])+'+'+str(respo)
                sss2=(y,user)
                mycus.execute(sss1,sss2)
                db.commit()
            print("Want to have more items?\n Enter any no. for yes and 0 for no.....")
            print()
            respo2=int(input("Enter your response: "))
            i=respo2
        print()   
        print("Your total expenses for Breakfast is: ", cost)
        s1='select bill from dataq where username=%s'
        s2=(user,)
        mycus.execute(s1,s2)
        bill=mycus.fetchall()
        inbill=bill[0][0]
        ss1='update dataq set bill=%s where username=%s'
        ss2=(inbill+cost,user)
        mycus.execute(ss1,ss2)
        db.commit()
        sss1='update orderforfood set b=%s where username=%s'
        
        special1='select b from orderforfood where username=%s'
        special2=(user,)
        mycus.execute(special1,special2)
        dat=mycus.fetchall()
        if dat[0][0]=='0':
            sss2=(respo,user)
            mycus.execute(sss1,sss2)
            db.commit()
        else:
            y=str(dat[0][0])+'+'+str(respo)
            sss2=(y,user)
            mycus.execute(sss1,sss2)
            db.commit()
        
        print("You have booked your items for breakfast!!!")
        homepage()
    if resp==2:
        state1='select lunch,costl from food'
        mycus.execute(state1,)
        data=mycus.fetchall()
        print('The menu for lunch is: ')
        i=1
        cost=0
        while i>0:
            print()
            for i in range(0,4):
                print(str(i+1),data[i][0],' - ',data[i][1])
            print()
            print('Kindly enter the no. of item you want to have....')
            respo=int(input('Enter your response: '))
            cost+=int(data[respo-1][1])
            print("Want to have more items?\n Enter any no. for yes and 0 for no.....")
            respo2=int(input("Enter your response: "))
            i=respo2
            sss1='update orderforfood set l=%s where username=%s'
        
            special1='select l from orderforfood where username=%s'
            special2=(user,)
            mycus.execute(special1,special2)
            dat=mycus.fetchall()
            if dat[0][0]=='0':
                sss2=(respo,user)
                mycus.execute(sss1,sss2)
                db.commit()
            else:
                y=str(dat[0][0])+'+'+str(respo)
                sss2=(y,user)
                mycus.execute(sss1,sss2)
                db.commit()
        print()
        print("Your total expenses for Lunch is: ", cost)
        s1='select bill from dataq where username=%s'
        s2=(user,)
        mycus.execute(s1,s2)
        bill=mycus.fetchall()
        inbill=bill[0][0]
        ss1='update dataq set bill=%s where username=%s'
        ss2=(inbill+cost,user)
        mycus.execute(ss1,ss2)
        db.commit()
        print()
        print("You have booked your items for Lunch!!!")
        homepage()
    if resp==3:
        state1='select dinner,costd from food'
        mycus.execute(state1,)
        data=mycus.fetchall()
        print('The menu for Dinner is: ')
        print()
        i=1
        cost=0
        while i>0:
            for i in range(0,4):
                print(str(i+1),data[i][0],' - ',data[i][1])
            print()
            print('Kindly enter the no. of item you want to have.')
            respo=int(input('Enter your response: '))
            cost+=int(data[respo-1][1])
            print("\nWant to have more items?\n Enter any number for YES and 0 for NO")
            respo2=int(input("Enter your response: "))
            i=respo2
            sss1='update orderforfood set d=%s where username=%s'
        
            special1='select d from orderforfood where username=%s'
            special2=(user,)
            mycus.execute(special1,special2)
            dat=mycus.fetchall()
            if dat[0][0]=='0':
                sss2=(respo,user)
                mycus.execute(sss1,sss2)
                db.commit()
            else:
                y=str(dat[0][0])+'+'+str(respo)
                sss2=(y,user)
                mycus.execute(sss1,sss2)
                db.commit()
    else:
        print("wrong value entered")
        food()
        print()
        
        print("Your total expenses for Dinner is: ", cost)
        s1='select bill from dataq where username=%s'
        s2=(user,)
        mycus.execute(s1,s2)
        bill=mycus.fetchall()
        inbill=bill[0][0]
        ss1='update dataq set bill=%s where username=%s'
        ss2=(inbill+cost,user)
        mycus.execute(ss1,ss2)
        db.commit()
        print()
        print("You have booked youe items for Dinner!!!")
        homepage()

def gym():
    db=mysql.connector.connect(host="localhost",user=usernam,passwd=paswr,database="projects")
    mycus=db.cursor()
    user=input("Enter username:")
    stat1="select password from dataq where username=%s"
    stat2=(user,)
    mycus.execute(stat1,stat2)
    passw=mycus.fetchall()
    if len(passw)==0:
        print("Usrname doesn't exist.Please go on 1st option to register.")
        homepage()
    else:
        passw1=input("Enter you password: ")
        print()
        if passw1==passw[0][0]:
            print("Login successful!\n ")
        else:
            print("Wrong data entered!!!")
            gym()
        print("                         ***For how much time do you want to workout?*** \n 1. 20 min - 200 rs \n 2. 30 min - 275 rs \n 3. 40 min - 350 rs \n 4. 50 min - 425 rs \n 5. 60 min - 500 rs")
        print()
        res=int(input("Enter your response:  "))
        if res==1 or res==2 or res==3 or res==4 or res==5:
            state1='select price from gym'
            mycus.execute(state1)
            data1=mycus.fetchall()
            count=data1[res-1][0]
            print()
            ext=int(input("do you want any extra service? \n 1. Yes \n 2. No \n :"))
            if ext==1:
                    state2='select services,PriceS from gym'
                    mycus.execute(state2,)
                    data=mycus.fetchall()
                    print("Extra Services are: ")
                    i=1
                    cost=0
                    while i>=1:
                        for i in range(0,5):
                            print(str(i+1),data[i][0],' - ',data[i][1])
                        print()
                        print('Kindly enter the no. of service you want to have.')
                        respo=int(input('Enter your response: '))
                        print()
                        print("Want to have more items?\n Enter 1 for yes and 0 for no.....")
                        respo2=int(input("Enter your response: "))
                        cost+=data[respo-1][1]
                        i=respo2
                    print()   
                    print("Your total expenses for workout is: ", cost+count)
                    s1='select bill from dataq where username=%s'
                    s2=(user,)
                    mycus.execute(s1,s2)
                    bill=mycus.fetchall()
                    inbill=bill[0][0]
                    ss1='update dataq set bill=%s where username=%s'
                    ss2=(inbill+cost+cost,user)
                    mycus.execute(ss1,ss2)
                    db.commit()
                    print()
                    print("You have booked your services!!!")
                    homepage()
            else:
                print()
                print("Your total expenses for workout is: ", count)
                print()
                s1='select bill from dataq where username=%s'
                s2=(user,)
                mycus.execute(s1,s2)
                bill=mycus.fetchall()
                inbill=bill[0][0]
                ss1='update dataq set bill=%s where username=%s'
                ss2=(inbill+count,user)
                mycus.execute(ss1,ss2)
                db.commit()
                print("You have booked your services!!!")
                homepage()
def bill():
    db=mysql.connector.connect(host="localhost",user=usernam,passwd=paswr,database="projects")
    mycus=db.cursor()
    user=input("Enter username: ")
    stat1="select password from dataq where username=%s"
    stat2=(user,)
    mycus.execute(stat1,stat2)
    passw=mycus.fetchall()
    if len(passw)==0:
        print("Usrname doesn't exist.Please go on 1st option to register.")
        homepage()
    else:
        passw1=input("Enter you password: ")
        print()
        if passw1==passw[0][0]:
            print("Login successful!\n ")
        else:
            print("Wrong data entered!!!")
            bill()
    s1='select bill from dataq where username=%s'
    s2=(user,)
    mycus.execute(s1,s2)
    billl=mycus.fetchall()
    print()
    print('Your total bill upto now is: ',billl[0][0])
    print()
    print('Do you want to checkout?\n 1.Enter 1 for yes\n2.Enter 0 for no...')
    re=int(input('Enter your response: '))
    if re==1:
        ss1='delete from dataq where username=%s'
        ss2=(user,)
        mycus.execute(ss1,ss2)
        db.commit()
        sss1='delete from orderforfood where username=%s'
        sss2=(user,)
        mycus.execute(sss1,sss2)
        db.commit()
        print('You have successfully checked-out from the hotel. \nTHANK YOU FOR USING OUR SERVICE WE WILL LOVE TO SEE YOU SOON!!! \nPlease pay your bill on the counter of the hotel.')



    
def EXIT():
    import sys
    print('You have exited the program.')
    sys.exit()
    











homepage()
                
    
