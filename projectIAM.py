import getpass
import matplotlib.pyplot as plt
import numpy as np

flag=0
userdata = {'145':{'Name':"Vineeth"},'1000':{'Name':'Suma'}}#% and overall attendance
usermarks = {'CNS':{'145':{'att':57,'totcls':65,'ia1':15,'ia2':22,'ia3':24,'of':30,'ea':-1,'ofea':-1}},'ADP':{'145':{'att':34,'totcls':42,'ia1':22,'ia2':26,'ia3':28,'of':30,'ofea':-1}}}
userpass = {'Vineeth':{'coll_id':'145','pass':'123'}}
userpass_autherizor ={'Teacher1':{'coll_id':'1000','pass':'Abc124@Qw'},'Teacher2':{'coll_id':'10001','pass':'Abd785@fgW1'}}

def newuser():
    username = input("Enter Your Username: \n")
    while(True):
        if(not userpass.get(username,False) and not userpass_autherizor.get(username,False) ):
            while(True):
                password = getpass.getpass("Enter your Password (Note: The passwrod you enter will not be visible for security purpose: \n")
                confirmpass = getpass.getpass("Re Enter the password to confirm:\n")
                if(password == confirmpass):
                    coll_id = input("Enter your College ID:\n")
                    userpass[username]={}
                    userpass[username]['coll_id'] = coll_id
                    userpass[username]['pass'] = confirmpass
                    userdata[coll_id]={}
                    while(True):
                        if(not userdata.get(coll_id,False)):
                            name = input("Enter your Name:")
                            userdata[coll_id]["Name"] = name
                            break
                        else:
                            coll_id = print("*"*20+" ID Conflict Please enter your College ID"+"*"*20)

                    print("The user Data Base is updated\n")
                    break
                else:
                    print("!"*20+"The Passwords do not match"+"!"*20+'\n')
            break
        else:
            username = input("The Username is Already Taken Try Another one:\n")
            input()
def Login ():
    username = input("Enter the User Name: \n")
    if(userpass.get(username,False)):
        password = getpass.getpass("Enter the password:\n")
        if(password == userpass[username]['pass']):
            account(username,1)
        else:
            print("*"*20+"Password Mismatch"+"*"*20)
    elif(userpass_autherizor.get(username,False)):
        password = getpass.getpass("Enter the password:\n")
        if(password == userpass_autherizor[username]['pass']):
            account(username,2)
        else:
            print("*"*20+"Password Mismatch"+"*"*20)
    else:
        print("User Does not Exist")
            
def Attendance():
    if(flag == 2):
        gfcls=0
        gfatcls=0
        print("Enter q to Exit after Entering the Attendance of the Student")
        while(True):
            col_id = input("Enter the college ID of the Student:\n")
            subname = input("Enter the Subject Name: \n")
            totcls = int(input("Enter the Total Calsses Taken:"))
            attcls = int(input("Enter the Total Classes Attended:"))
            gfcls += totcls
            gfatcls += attcls
            usermarks[subname][col_id]['att']=attcls
            usermarks[subname][col_id]['totcls']=totcls
            print(f"Attendace of {col_id}'s Student is uploaded Successfully")
            exitstat = input()
            if(exitstat=='q'):
                break
        userdata[col_id]['ovat']=((gfatcls/gfatcls)*100)
    else:
        while(True):
            try:
                ch=int(input("1)To see Graphical reresentation of your attendance 2)To see your Attadance \n"))
                if(ch==1):
                    g1 =[]
                    g2 =[]
                    for sub,info in usermarks.items():
                        x=(usermarks[sub][userid]['att']*100)//usermarks[sub][userid]['totcls']
                        g1 += [x]   
                        g2 +=[sub+" "+str(x)]
                    g1 = np.array(g1)
                    g2 = np.array(g2)
                    myexplode = [0.2, 0, 0, 0]
                    plt.pie(g1, labels = g2,explode = myexplode,shadow=True)
                    plt.show()
                elif(ch==2):
                        for sub,info in usermarks.items():
                            x= (usermarks[sub][userid]['att']/usermarks[sub][userid]['totcls'])*100
                            print("Subject:"+sub+"\nAttended: "+usermarks[sub][userid]['att']+"\nCalsses Taken: "+usermarks[sub][userid]['totcls']+"\nPercentage : "+str(x))
                        print("Overall Attendace Percentage is: "+str(userdata[userid]['ovat']))
                    
                else:
                    break
            except:
                    print("Value May Not be Present")
def IA():
    if(flag == 2):
        print("Enter q to Exit after Entering the IA Marks of the Student")
        while(True):
            col_id = input("Enter the college ID of the Student:\n")
            subname = input("Enter the Subject Name: \n")
            ia1 = int(input("Enter the Marks Scored in IA1:(-ve if event is not occured"))
            ia2 = int(input("Enter the Marks Scored in IA2:(-ve if event is not occured"))
            ia3 = int(input("Enter the Marks Scored in IA3:(-ve if event is not occured"))
            of = int(input("Enter the Total Marks of IA:"))
            usermarks[subname][col_id]['ia1']=ia1
            usermarks[subname][col_id]['ia2']=ia2
            usermarks[subname][col_id]['ia3']=ia3
            usermarks[subname][col_id]['of']=of
            print(f"Internal marks of {col_id}'s Student is uploaded Successfully")
            exitstat = input()
            if(exitstat=='q'):
                break
    else:
        try:
            while(True):
                ch=int(input("1)To display marks of 1st IA\n2)To display marks of 2nd IA\n3)To display marks of 3rd IA\nAny number to EXIT"))
                if(ch==1):
                    z='ia1'
                elif(ch==2):
                    z='ia2'
                elif (ch==3):
                    z='ia3'
                else:
                    break
                g1 =[]
                g2 =[]
                for sub in usermarks.keys():
                    if(usermarks[sub][userid][z] > 0):
                        g1+=usermarks[sub][userid][z]
                        g2+=sub
                    else:
                        print("Graph plotted with Available Data")
                g1 = np.array(g1)
                g2 = np.array(g2)
                plt.bar(g1,g2)
                plt.show()
        except:
                    print("Value May Not be Present")
        
                   
def EA():
    if(flag==2):
        print("Enter q to Exit after Entering the EA Marks of the Student")
        while(True):
            col_id = input("Enter the college ID of the Student:\n")
            subname = input("Enter the Subject Name: \n")
            ea = int(input("Enter the Marks Scored in EA:(-ve if event is not occured"))
            ofea = int(input("Enter the Total Marks of IA:"))
            usermarks[subname][col_id]['ea']=ea
            usermarks[subname][col_id]['ofea']=ofea
            print(f"External Marks of {col_id}'s Student is uploaded Successfully")
            exitstat = input()
            if(exitstat=='q'):
                break
    else:
        try:
            g1 =[]
            g2 =[]
            for sub,info in usermarks:
                if(usermarks[sub][userid]['ea'] > 0):
                        g1+=usermarks[sub][userid]['ea']
                        g2+=sub
                else:
                        print("Graph plotted with Available Data")
            g1 = np.array(g1)
            g2 = np.array(g2)
            myexplode = [0.2, 0, 0, 0]
            plt.pie(g1, labels = g2,explode = myexplode,shadow=True)
            plt.show()
        except:
                    print("Value May Not be Present")
            

def account(username,flags):
    flag = flags
    global userid
    while(True):
        if(flag==1):
            userid = userpass[username]['coll_id']
            switcher(2+int(input(f"User ID:{userid}\nUser Name:{userdata[userpass[username]['coll_id']]['Name']}\n1)To see your attendace\n2)To see your Internal Assement Marks\n3)To see External Assement Marks\n4)To Exit")))
        else:
            switcher(2+int(input(f"User ID:{userpass_autherizor[username]['coll_id']}\nUser Name:{userdata[userpass_autherizor[username]['coll_id']]['Name']}\n1)To Enter attendace\n2)To Enter Internal Assement Marks\n3)To Enter External Assement Marks\n4)To Exit")))

def main():
    while(True):
        flag=0
        switcher(int(input("1)To Signup.\n2)To login to your account.")))

choice_mapping = {1:newuser,2:Login,3:Attendance,4:IA,5:EA,6:main}

def switcher(choice) :
    choice_mapping.get(choice,default)()
    
def default():
    switcher(input("Enter the correct choice:\n"))
    
if __name__ == "__main__":
    main()
        