

#import..........

from tkinter import *
from PIL import ImageTk,Image
from PIL import *
import  getDB
import pyrebase
import cv2
import numpy as np
import time
import math
import mediapipe as mp
pose_counter = [1]
username = [0]

#global base1 for homepage
base1 = Tk()
base1.title("Bee Yogi")
base1.iconbitmap('1.ico')
base1.geometry("1350x690")
base1.geometry("+1+1")
list1=["Boat Pose - Paripurna Navasana","Bow Pose - Dhanuarasana","Camel Pose - Ustrasana","Cat Pose - Marjaryasana","Chair Pose - Utkatasana","Chaturanga Dandasana -","Corpse Pose - Savasana","Cow Pose - Bitilasana","Crescent Lunge - Anjaneyasana","Downward Dog - Adho Mukha Svanasana","Half Boat Pose - Ardha Navasana","Half Frog Pose - Ardha Bhekasana","Half Moon Pose - Ardha Chandrasana","One Legged Upward Bow Pose - Eka Pada Urdhva Dhanurasana","Plank Pose - Phalakasana","Scorpion Pose - Vrschikasana","Side Plank Pose - Vasishtasana","Single Leg Downward Facing Dog - Eka Pada Adho Mukha Svanasana","Splits - Hanumanasana","Supported Shoulder Stand - Salamba Sarvangasana","Tree Pose - Vrksasana","Upward Facing Dog Pose - Urdhva Mukha Svanasana","Warrior III - Virabhadrasana III","Wheel Pose - Urdhva Dhanurasana"]
lm=[1]
# new user : **********
def new_user():
    # new user image :
   
    new_s3 = Image.open("GUIImage/new_user.jpg")
    new_s4 = ImageTk.PhotoImage(new_s3)
    new_s5 = Label(image=new_s4)
    new_s5.image = new_s4
    new_s5.place(x=0, y=0)

    # new user body :
    s_en1 = Entry(base1, width=35, font=("Arial", 16), bd=0)
    s_en1.place(x=100, y=120)

    s_en2 = Entry(base1, width=35, font=("Arial", 16), bd=0)
    s_en2.place(x=100, y=210)

    s_en3 = Entry(base1, width=35, font=("Arial", 16), bd=0)
    s_en3.place(x=100, y=300)

    s_en4 = Entry(base1, width=35, font=("Arial", 16), bd=0)
    s_en4.place(x=100, y=390)

    s_en5 = Entry(base1, width=35, font=("Arial", 16), bd=0)
    s_en5.place(x=100, y=480)

    s_en6 = Entry(base1, width=35, font=("Arial", 16), bd=0)
    s_en6.place(x=100, y=570)

    s_en7 = Entry(base1, width=35, font=("Arial", 17), bd=0)
    s_en7.place(x=700, y=110)

    s_en8 = Entry(base1, width=35, font=("Arial", 16), bd=0)
    s_en8.place(x=700, y=200)


    s_en9 = Entry(base1, width=35, font=("Arial", 16), bd=0)
    s_en9.place(x=700, y=290)

    s_en10 = Entry(base1, width=35, font=("Arial", 16), bd=0)
    s_en10.place(x=700, y=385)

    s_en11 = Entry(base1, width=35, font=("Arial", 16), bd=0)
    s_en11.place(x=700, y=475)
    
    # Clear user Form
    def clear_user():
        s_en1.delete(0, END)
        s_en2.delete(0, END)
        s_en3.delete(0, END)
        s_en4.delete(0, END)
        s_en5.delete(0, END)
        s_en6.delete(0, END)
        s_en7.delete(0, END)
        s_en8.delete(0, END)
        s_en9.delete(0, END)
        s_en10.delete(0, END)
        s_en11.delete(0, END)

    # submit user Form
    def submit_user():
        name = s_en1.get()
        username1 = s_en2.get()
        contact = s_en3.get()
        age = s_en4.get()
        bloodgroup = s_en5.get()
        gender = s_en6.get()
        email = s_en7.get()
        occupation = s_en8.get()
        address = s_en9.get()
        password = s_en10.get()
        cpassword = s_en11.get()

        flag=1
        if s_en1 == "":
            flag=1
        if s_en2 == "":
            flag=1
        if s_en3 == "":
            flag=1
        if s_en4 == "":
            flag=1
        if s_en5 == "":
            flag=1

        if s_en6 == "":
            flag=1

        if s_en7 == "":
            flag=1
        if s_en8 == "":
            flag=1
        if s_en9 == "":
            flag=1
        if s_en10 == "":
            flag=1
        if s_en11 == "":
            flag=1
        flag=0

        if flag==0:
            if s_en10==s_en11 or True:
                db = getDB.getDBObject()
                

                data = {'Name':name,'UserName':username1,'Contact':contact,'Age':age,'BloodGroup':bloodgroup,'Gender':gender,'Email':email,'Occupation':occupation,'Address':address,'Password':password}


                #insert
                db.child(username1).set(data)
                
                





            else:
                pass
                #confirm password not macth



        
        # Calling to user login function

        user_login()


    s_btn1 = Button(base1, text="Clear", font=("Arial Rounded MT Bold", 20), width=8, height=1, bd=0, fg="white",
                    bg="#c00000", command=clear_user)
    s_btn1.place(x=735, y=555)
    s_btn = Button(base1, text="Submit", font=("Arial Rounded MT Bold", 20), width=8, height=1, bd=0, fg="white",
                    bg="#c00000", command=submit_user)
    s_btn.place(x=965, y=555)

    back = Button(base1, text="Back", font=("Arial Rounded MT Bold", 20), width=5, height=1, bd=0, fg="white",
                   bg="#c00000", command=user_login)
    back.place(x=1225, y=53)


#password reset..........
def forget_password():
    # forget password image
    quiz1 = Image.open("GUIImage/forget_password.jpg")
    quiz2 = quiz1.resize((1350, 690))
    quiz2.save("GUIImage/forget_password.jpg")
    quiz3 = Image.open("GUIImage/forget_password.jpg")
    quiz4 = ImageTk.PhotoImage(quiz3)
    quiz5 = Label(image=quiz4)
    quiz5.image = quiz4
    quiz5.place(x=0, y=0)


    # ============================================================================
    def otp():

        

        

        
        phone_no = en1.get()

        if getDB.retriveMobileNOIsPresent(phone_no):
                
            
            
            from  twilio.rest import Client
            import random

            account_sid='ACa33823739ad05485a08f9d182ef86a0e'
            auth_token='b6a058b8caef0bc163efadf65457d893'

            twilio_number = '+19125203572'
            receiver='+917387579912'
            name = "Vasudev - Keshav - Prathmesh"

            client = Client(account_sid,auth_token)

            otp1 = str(random.randint(11111, 99999))
            txt_msg = ("\n\n**** BEE YOGI ***\nHi " + name+"\n\nYour OTP to reset/access Bee Yogi Account is  : "+otp1+"\nIt will be valid for 3 minutes.\n\n- Bee Yogi\n****")

            message = client.messages.create(
                body=txt_msg,
                from_=twilio_number,
                to=receiver

            )
            
            
            #otp1="2222"







            # OTP image
            quiz1 = Image.open("GUIImage/otp.jpg")
            quiz2 = quiz1.resize((1350, 690))
            quiz2.save("GUIImage/otp.jpg")
            quiz3 = Image.open("GUIImage/otp.jpg")
            quiz4 = ImageTk.PhotoImage(quiz3)
            quiz5 = Label(image=quiz4)
            quiz5.image = quiz4
            quiz5.place(x=0, y=0)

            # OTP body
            # otp
            en_otp = Entry(base1, width=28, font=("Arial", 15), bd=0)
            en_otp.place(x=525, y=340)
            


            # Reset Password Body.................
            def reset_password():

                if otp1 == str(en_otp.get()):
                    

                    

                    # reset password image
                    quiz1 = Image.open("GUIImage/reset_password.jpg")
                    quiz2 = quiz1.resize((1350, 690))
                    quiz2.save("GUIImage/reset_password.jpg")
                    quiz3 = Image.open("GUIImage/reset_password.jpg")
                    quiz4 = ImageTk.PhotoImage(quiz3)
                    quiz5 = Label(image=quiz4)
                    quiz5.image = quiz4
                    quiz5.place(x=0, y=0)


                    # reset_password body
                    en11 = Entry(base1, width=28, font=("Arial", 15), bd=0)
                    en11.place(x=525, y=325)

                    lb1 = Label(base1, text="", font=("Arial Rounded MT Bold", 17), width=30, height=1, bd=0, fg="#c00000",bg="white")
                    lb1.place(x=470, y=570)

                    en21 = Entry(base1, width=20, font=("Arial", 15), bd=0)
                    en21.place(x=525, y=410)

                    # new pass
                    def new_pass():
                        new = en11.get()
                        confirm = en21.get()

                        if new == confirm:
                            #print("new : ", new)
                            #print("confirm : ", confirm)


                            u = getDB.retriveUserName(phone_no)
                            ils = getDB.retrivePinfo(u)
                      

                            db = getDB.getDBObject()
                            data = {'Name':ils[6],'UserName':ils[1],'Contact':ils[3],'Age':ils[1],'BloodGroup':ils[2],'Gender':ils[5],'Email':ils[4],'Occupation':ils[7],'Address':ils[0],'Password':new,'UserName':ils[9]}
                            db.child(u).set(data)
                    



                            

                            # first check the matches and then do the login
                            user_login()
                        else:
                            lb1.config(text = "Invalid confirm password !")

                    # resett body continued
                    btn1 = Button(base1, text="Reset Password", font=("Arial Rounded MT Bold", 20), width=18, height=1,
                                  bd=0, fg="white", bg="#c00000",command=new_pass)
                    btn1.place(x=525, y=480)

                    btn2 = Button(base1, text="Back to Login", font=("Arial Rounded MT Bold", 16), width=33, height=1,
                                  bd=0, fg="black", bg="#d0cecf", command=user_login)
                    btn2.place(x=460, y=630)

                
                else:
                    lb1 = Label(base1, text="OTP did not matched !", font=("Arial Rounded MT Bold", 17), width=30,
                                height=1, bd=0, fg="#c00000", bg="white")
                    lb1.place(x=470, y=570)
                    en_otp.delete(0, END)
                    en_otp.focus()
                
            # ==============================================================================================
            btn1 = Button(base1, text=" Submit OTP ", font=("Arial Rounded MT Bold", 20), width=18, height=1, bd=0,
                              fg="white", bg="#c00000", command=reset_password)
            btn1.place(x=525, y=480)

            btn2 = Button(base1, text="Back to Login", font=("Arial Rounded MT Bold", 16), width=33, height=1, bd=0,
                              fg="black", bg="#d0cecf", command=user_login)
            btn2.place(x=460, y=630)
            # ==============================================================================================

        else:
            #we want here one label to show mobile number not present in
            pass
    # Forget password body



    # mobile no
    en1 = Entry(base1, width=28, font=("Arial", 15), bd=0)
    en1.place(x=525, y=415)

    btn1 = Button(base1, text="Send OTP", font=("Arial Rounded MT Bold", 20), width=18, height=1, bd=0,
                  fg="white", bg="#c00000", command=otp)
    btn1.place(x=525, y=480)

    btn2 = Button(base1, text="Back to Login", font=("Arial Rounded MT Bold", 16), width=33, height=1, bd=0,
                  fg="black", bg="#d0cecf", command=user_login)
    btn2.place(x=460, y=630)



'''
   

'''


# learn loga..............
def learn_yoga():
    pose_counter[0]=1

    #lm=[1]
    def shift_right():
        
        if lm[0]<=23:
            lm[0]=lm[0]+1
            pose_counter[0] = pose_counter[0]+1
            pho = ImageTk.PhotoImage(Image.open("sliderimage//"+str(lm[0])+".png"))
            img_lab5 = Label(image=pho)
            img_lab5.image = pho
            lab1.config(text=str(list1[lm[0]-1]))
            
            
            btn4.config(image=pho)
            base1.update()
        else:
            lm[0]=0
            lm[0]=lm[0]+1
            pose_counter[0]=0
            pose_counter[0] = pose_counter[0]+1
            pho = ImageTk.PhotoImage(Image.open("sliderimage//"+str(lm[0])+".png"))
            img_lab5 = Label(image=pho)
            img_lab5.image = pho
            lab1.config(text=str(list1[lm[0]-1]))
            
            
            btn4.config(image=pho)
            base1.update()
        

    def shift_left():
          
        if lm[0]>=2:
            lm[0]=lm[0]-1
            pose_counter[0] = pose_counter[0]-1
            pho = ImageTk.PhotoImage(Image.open("sliderimage//"+str(lm[0])+".png"))
            img_lab5 = Label(image=pho)
            img_lab5.image = pho
            lab1.config(text=str(list1[lm[0]-1]))
            
            
            btn4.config(image=pho)
            base1.update()
        else:
            lm[0]=25
            lm[0]=lm[0]-1
            pose_counter[0] = pose_counter[0]+1
            pose_counter[0]=25
            pho = ImageTk.PhotoImage(Image.open("sliderimage//"+str(lm[0])+".png"))
            img_lab5 = Label(image=pho)
            img_lab5.image = pho
            lab1.config(text=str(list1[lm[0]-1]))
            
            
            btn4.config(image=pho)
            base1.update()

    

    # learn_yoga image
    s1 = Image.open("GUIImage/learn_yoga.jpg")
    s2 = s1.resize((1350, 690))
    s2.save("GUIImage/learn_yoga.jpg")
    s3 = Image.open("GUIImage/learn_yoga.jpg")
    s4 = ImageTk.PhotoImage(s3)
    s5 = Label(image=s4)
    s5.image = s4
    s5.place(x=0, y=0)

    # learn yoga Body
    lab1 = Label(base1, text="Boat Pose - Paripurna Navasana", font=("Arial Rounded MT Bold", 20), width=45, height=1,bg="white", bd=0)
    lab1.place(x=535,y=100)

    lab2 = Label(base1, text="",  width=92, height=25, bg="white", bd=0)
    lab2.place(x=610, y=180)

    #show pose................
    def show_pose():
        #show pose image
        s1 = Image.open("GUIImage/show_pose.jpg")
        s2 = s1.resize((1350, 690))
        s2.save("GUIImage/show_pose.jpg")
        s3 = Image.open("GUIImage/show_pose.jpg")
        s4 = ImageTk.PhotoImage(s3)
        s5 = Label(image=s4)
        s5.image = s4
        s5.place(x=0, y=0)











        

        

        #show pose body
        lab1 = Label(base1, text=str(list1[lm[0]-1]), font=("Arial Rounded MT Bold", 18), width=50, height=1,bg="white", bd=0)
        lab1.place(x=233, y=100)

        label = Label(base1, text="", width=750, height=430, bg="white", bd=0)
        label.place(x=233, y=143)

        perform_show = Button(base1, text="Get Started", width=10, font=("Arial Rounded MT Bold", 17), height=2, bg="#f9db60",fg="black", bd=0, command=perform)
        perform_show.place(x=1170, y=192)

        back_show = Button(base1, text="Back", width=10, font=("Arial Rounded MT Bold", 17), height=2,bg="#40b9d0", fg="black", bd=0, command=learn_yoga)
        back_show.place(x=1170, y=302)


        #import numpy as np
        import cv2
        aa="video\\"+str(lm[0])+".mp4"
        
        cap = cv2.VideoCapture(r"video/"+str(lm[0])+".mp4")

        frame_number = []
        annotation_list = []

        i = 0
        flag=1
        while(True):        
            ret, frame = cap.read()
            frame = cv2.resize(frame,(750,430))
            cv2image= cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
           
            img1 = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image = img1)
            label.imgtk = imgtk
            label.configure(image=imgtk)
            base1.update()
            c = cv2.waitKey(5)
            i = i + 1

            try:
                annotation_list = annotation_list + [chr(c)]
                frame_number = frame_number + [i]
            except:
                continue
                


        
    #llearn pose body continueds
    btn1 = Button(base1, text="Select Pose",font=("Arial Rounded MT Bold", 20), width=20, height=1, bd=0,fg="black", bg="#ffbf00", command=show_pose)
    btn1.place(x=750, y=570)

    # adding images left
    photo1 = ImageTk.PhotoImage(Image.open(r"GUIImage/left_button.png"))
    img_lab1 = Label(image=photo1)
    img_lab1.image = photo1


    #--------------------------------------------------------

    photo3 = ImageTk.PhotoImage(Image.open("sliderimage/1.png"))
    img_lab3 = Label(image=photo3)
    img_lab3.image = photo3

    btn4 = Label(base1, image=photo3,width=646,height=376, bd=0)
    btn4.place(x=610, y=180)


    #--------------------------------------------------------


    # adding images right
    photo2 = ImageTk.PhotoImage(Image.open(r"GUIImage/right_button.png"))
    img_lab2 = Label(image=photo2)
    img_lab2.image = photo2

    btn2 = Button(base1, image=photo1,width=50,height=90, bd=0,command=shift_left)
    btn2.place(x=550, y=330)


    btn3 = Button(base1, image=photo2,width=50,height=90, bd=0,command = shift_right)
    btn3.place(x=1265, y=330)

    back_learn = Button(base1, text="Back", width=7, font=("Arial Rounded MT Bold", 18), height=1,bg="white", fg="black", bd=0, command=user_interface)
    back_learn.place(x=60, y=40)


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    
def perform():
    healthf = [1]





    
    lss=[1]
    #lss[0]=1



    

    
    #cap = cv2.VideoCapture(r"video\\"+str(pose_counter[0])+".mp4")
    cap = cv2.VideoCapture(0)
    
    #---------------------------------------------------
    def releasecap():
        global flag
        try:
            lss[0]=2
            cap.release()
            cap1.release()
            print('camera release')
            perform_yoga1()
            #cv2.destroyAllWindows()
            #lab2.destroy()
                
        except:
            cap.release()
            cap1.release()
            print("Exception")

    #---------------------------------------------------------
            
    # perform_yoga image
    s1 = Image.open("GUIImage/perform.jpg")
    s2 = s1.resize((1350, 690))
    s2.save("GUIImage/perform.jpg")
    s3 = Image.open("GUIImage/perform.jpg")
    s4 = ImageTk.PhotoImage(s3)
    s5 = Label(image=s4)
    s5.image = s4
    s5.place(x=0, y=0)

    stop = Button(base1, text="Stop", width=7, font=("Arial Rounded MT Bold", 18), height=1, bg="#c00000",fg="white", bd=0, command=releasecap)
    stop.place(x=638, y=80)

    lab1 = Label(base1, text=list1[pose_counter[0]-1], font=("Arial Rounded MT Bold", 20), width=45, height=1,bg="#1c4f79",fg="white", bd=0)
    lab1.place(x=18, y=165)

    base1.update()
    

    #---------------------------------------------------------------------------------------------
    
    
    count = 0
    dir = 0
    pTime = 0
    mpDraw = mp.solutions.drawing_utils
    mpPose = mp.solutions.pose
    pose = mpPose.Pose()
   
    lab2 = Label(base1, text="", width=100, height=25, bg="black", bd=0)
    lab2.place(x=19, y=220)
    lll=[1]
    sumls=[1]

    #-----------------------------------------------------------------------------------------------------------------------
    def setl(img,t):
        if t:
            
            mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS,mpDraw.DrawingSpec(color=(0,255,0),thickness=2,circle_radius=2)
                                        ,mpDraw.DrawingSpec(color=(0,255,0),thickness=2,circle_radius=3))
        
            if healthf[0]==1:

                import datetime
                time1  = datetime.datetime.now().strftime('%H:%M:%S')

                date1 = datetime.date.today().strftime('%d-%m-%y')
                
                import getDB
                db = getDB.getDBObject2()
                data = {'Time':str(time1)}
                #insert
                db.child(username[0]).child(str(date1)).child(list1[pose_counter[0]-1]).set(data)
                healthf[0]=2
        
        else:
            mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS,mpDraw.DrawingSpec(color=(0,0,255),thickness=2,circle_radius=2)
                                  ,mpDraw.DrawingSpec(color=(255,255,255),thickness=2,circle_radius=3))

                
            
        global lab2,lab3
        try:
            if lll[0]==1:
                lab2 = Label(base1, text="", width=750, height=450, bg="white", bd=0)
                lab2.place(x=19, y=220)
                lll[0]=2
                
            cv2image= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            
            img1 = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image = img1)
            lab2.imgtk = imgtk
            lab2.configure(image=imgtk,width=750,height=450)
            
        except:
            pass
        
        

    #------------------------------------------------------------------------------------------------------------------------------
    
    def findangle(v1,v2,v3):
        try:
            
            
            lmList = []
            if results.pose_landmarks:
                for id, lm in enumerate(results.pose_landmarks.landmark):
                   
                            
                        h, w, c = img.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        lmList.append([id, cx, cy])
                        
            
            
            if len(lmList) !=0:
                #print(len(lmList))
                
                x1, y1 = lmList[v1][1:]
                x2, y2 = lmList[v2][1:]
                x3, y3 = lmList[v3][1:]
                angle = math.degrees(math.atan2(y3 - y2, x3 - x2) -
                                     math.atan2(y1 - y2, x1 - x2))   

                

                if angle <0:
                    angle = angle*(-1)

                if angle>180:
                    angle=360-angle
                
                '''    
                cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
                cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), 3)
                cv2.circle(img, (x1, y1), 5, (0, 0, 255), cv2.FILLED)
                cv2.circle(img, (x2, y2), 5, (0, 0, 255), cv2.FILLED)
                cv2.circle(img, (x3, y3), 5, (0, 0, 255), cv2.FILLED)
                cv2.putText(img, str(int(angle)), (x2 - 50, y2 + 50),
                            cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
                
                #setl(img)
               
                '''

            if angle!=None:
                
                return angle
            else:
                return 0
                
                
            
        except Exception as e:
            print(e)
            #print('angle')


    #-------------------------------------------------------------------------------

    
    #-------------------------------------------------------------------------
        

    def pose1accuracy(a,angle):
        global co,sum1
        if a==1:
            if angle >140 and angle <175:
                return 25
            else:
                return 0
                    
        if a==2:
            if angle >8 and angle <70:
                return 25
            else:
                return 0
        if a==3:
            if angle >50 and angle <113:
                return 25
            else:
                return 0
        if a==4:
            if angle >130 and angle <180:
                return 25
            else:
                return 0
        if a==5: 
            if angle >140 and angle <175:
                return 25
            else:
                return 0
        if a==6:
            if angle >8 and angle <70:
                return 25
            else:
                return 0
        if a==7:
            if angle >50 and angle <130:
                return 25
            else:
                return 0
        if a==8:
            if angle >140 and angle <175:
                return 25
            else:
                return 0


    def pose1():
        sum2 = 0
        sum1=0       
        sum1 = pose1accuracy(1,findangle(12,14,16))
        sum2= sum2+sum1        
        sum1 = pose1accuracy(2,findangle(14,12,24))
        sum2= sum2+sum1
        sum1= pose1accuracy(3,findangle(12,24,26))
        sum2= sum2+sum1
        sum1 = pose1accuracy(4,findangle(28,26,24))
        sum2= sum2+sum1
        sum1 = pose1accuracy(5,findangle(15,13,11))
        sum2= sum2+sum1
        sum1 = pose1accuracy(6,findangle(13,11,23))
        sum2= sum2+sum1
        sum1 = pose1accuracy(7,findangle(11,23,25))
        sum2= sum2+sum1
        sum1 = pose1accuracy(8,findangle(27,25,23))
        sum2= sum2+sum1
        if sum2>=175:    
            setl(img,1)
        else:
            setl(img,0)   
        return sum2
    #------------------------------------------------------------------------------

    def pose2():
        findangle(12,14,16)
        #findangle(14,12,24)
        #findangle(12,24,26)
        findangle(24,26,28)
        findangle(11,13,15)
        findangle(13,11,23)
        findangle(23,25,27)
        findangle(11,23,25)


    #------------------------------------------------------------------------------
    def pose3accuracy(a,angle):
        global co,sum1
        try:
            
        
            if a==1:
                if angle >160 and angle <190:
                    return 25
                else:
                    return 0
                    
                    
            if a==2:
                if angle >30 and angle <60:
                    return 25
                else:
                    return 0
                    
            if a==3:
                if angle >110 and angle <155:
                    return 25
                else:
                    return 0
                    
            if a==4:
                if angle >70 and angle <110:
                    return 25
                else:
                    return 0
                    
        
            if a==5:
                if angle >160 and angle <190:
                    return 25
                else:
                    return 0
                    
                  
                    
            if a==6:
                if angle >30 and angle <60:
                    return 25
                else:
                    return 0
                    
                    
            if a==7:
                if angle >110 and angle <155:
                    return 25
                else:
                    return 0
                    
                    
            if a==8:
                if angle >70 and angle <100:
                    return 25
                else:
                    return 0
                    
        except:
            pass
                       




    def pose3():
        sum2 = 0
        sum1=0       
        sum1 = pose3accuracy(1,findangle(12,14,16))
        sum2= sum2+sum1        
        sum1 = pose3accuracy(2,findangle(14,12,24))
        sum2= sum2+sum1
        sum1= pose3accuracy(3,findangle(12,24,26))
        sum2= sum2+sum1
        sum1 = pose3accuracy(4,findangle(28,26,24))
        sum2= sum2+sum1
        sum1 = pose3accuracy(5,findangle(15,13,11))
        sum2= sum2+sum1
        sum1 = pose3accuracy(6,findangle(13,11,23))
        sum2= sum2+sum1
        sum1 = pose3accuracy(7,findangle(11,23,25))
        sum2= sum2+sum1
        sum1 = pose3accuracy(8,findangle(27,25,23))
        sum2= sum2+sum1
        if sum2>=175:    
            setl(img,1)
        else:
            setl(img,0)   
        return sum2
    #------------------------------------------------------------------------------
    def pose4accuracy(a,angle):
        global co,sum1
        try:
            
        
            if a==1:
                if angle >150 and angle <180:
                    return 25
                else:
                    return 0
                    
            if a==2:
                if angle >60 and angle <100:
                    return 25
                else:
                    return 0
                    
            if a==3:
                if angle >90 and angle <130:
                    return 25
                else:
                    return 0
                    
            if a==4:
                if angle >70 and angle <110:
                    return 25
                else:
                    return 0
                    
      
            if a==5:
                if angle >150 and angle <180:
                    return 25
                else:
                    return 0
                    
            if a==6:
                if angle >60 and angle <100:
                    return 25
                else:
                    return 0
                    
            if a==7:
                if angle >90 and angle <130:
                    return 25
                else:
                    return 0
                    
            if a==8:
                if angle >70 and angle <110:
                    return 25
                else:
                    return 0
                    
        except:
            pass

    def pose4():
        sum2 = 0
        sum1=0       
        sum1 = pose4accuracy(1,findangle(12,14,16))
        sum2= sum2+sum1        
        sum1 = pose4accuracy(2,findangle(14,12,24))
        sum2= sum2+sum1
        sum1= pose4accuracy(3,findangle(12,24,26))
        sum2= sum2+sum1
        sum1 = pose4accuracy(4,findangle(28,26,24))
        sum2= sum2+sum1
        sum1 = pose4accuracy(5,findangle(15,13,11))
        sum2= sum2+sum1
        sum1 = pose4accuracy(6,findangle(13,11,23))
        sum2= sum2+sum1
        sum1 = pose4accuracy(7,findangle(11,23,25))
        sum2= sum2+sum1
        sum1 = pose4accuracy(8,findangle(27,25,23))
        sum2= sum2+sum1
        if sum2>=175:    
            setl(img,1)
        else:
            setl(img,0)   
        return sum2

    #-------------------------------------------------------------------------------
    def pose5accuracy(a,angle):
        global co
        
        try: 
            if a==1:
                if angle >160 and angle <180:
                    return 25
                else:
                    return 0
                    
                    
            if a==2:
                if angle >130 and angle <180:
                    return 25
                else:
                    return 0
                    
            if a==3:
                if angle >100 and angle <160:
                    return 25
                else:
                    return 0
                    
            if a==4:
                if angle >70 and angle <150:
                    return 25
                else:
                    return 0
            
            if a==5:
                if angle >160 and angle <180:
                    return 25
                else:
                    return 0         
            if a==6:
                if angle >130 and angle <180:
                    return 25
                else:
                    return 0              
            if a==7:
                if angle >100 and angle <140:
                    return 25
                else:
                    return 0             
            if a==8:
                if angle >70 and angle <120:
                    return 25
                else:
                    return 0
                    
        except Exception as e:
            print(e)

    def pose5():
        sum2 = 0
        sum1=0       
        sum1 = pose5accuracy(1,findangle(12,14,16))
        sum2= sum2+sum1        
        sum1 = pose5accuracy(2,findangle(14,12,24))
        sum2= sum2+sum1
        sum1= pose5accuracy(3,findangle(12,24,26))
        sum2= sum2+sum1
        sum1 = pose5accuracy(4,findangle(28,26,24))
        sum2= sum2+sum1
        sum1 = pose5accuracy(5,findangle(15,13,11))
        sum2= sum2+sum1
        sum1 = pose5accuracy(6,findangle(13,11,23))
        sum2= sum2+sum1
        sum1 = pose5accuracy(7,findangle(11,23,25))
        sum2= sum2+sum1
        sum1 = pose5accuracy(8,findangle(27,25,23))
        sum2= sum2+sum1
        if sum2>=175:    
            setl(img,1)
        else:
            setl(img,0)   
        return sum2
    #---------------------------------------------------------------------------------------------

    def pose6accuracy(a,angle):
        global co,sum1
        try:
            
        
            if a==1:
                if angle >60 and angle <110:
                    return 25
                else:
                    return 0  
            if a==2:
                if angle >1 and angle <20:
                    return 25
                else:
                    return 0  
            if a==3:
                if angle >150 and angle <180:
                    return 25
                else:
                    return 0  
            if a==4:
                if angle >150 and angle <180:
                    return 25
                else:
                    return 0  
        
            if a==5:
                if angle >60 and angle <110:
                    return 25
                else:
                    return 0  
                    
            if a==6:
                if angle >1 and angle <20:
                    return 25
                else:
                    return 0  
                    
            if a==7:
                if angle >150 and angle <180:
                    return 25
                else:
                    return 0  
            if a==8:
                if angle >150 and angle <180:
                    return 25
                else:
                    return 0  
        except:
            pass

    def pose6():
        sum2 = 0
        sum1=0       
        sum1 = pose6accuracy(1,findangle(12,14,16))
        sum2= sum2+sum1        
        sum1 = pose6accuracy(2,findangle(14,12,24))
        sum2= sum2+sum1
        sum1= pose6accuracy(3,findangle(12,24,26))
        sum2= sum2+sum1
        sum1 = pose6accuracy(4,findangle(28,26,24))
        sum2= sum2+sum1
        sum1 = pose6accuracy(5,findangle(15,13,11))
        sum2= sum2+sum1
        sum1 = pose6accuracy(6,findangle(13,11,23))
        sum2= sum2+sum1
        sum1 = pose6accuracy(7,findangle(11,23,25))
        sum2= sum2+sum1
        sum1 = pose6accuracy(8,findangle(27,25,23))
        sum2= sum2+sum1
        if sum2>=175:    
            setl(img,1)
        else:
            setl(img,0)   
        return sum2
    #---------------------------------------------------------------------------------------
    def pose7accuracy(a,angle):
        global co,sum1
        try:

            if a==1:
                if angle >140 and angle <180:
                    return 25
                else:
                    return 0  
            if a==2:
                if angle >1 and angle <60:
                    return 25
                else:
                    return 0  
            if a==3:
                if angle >140 and angle <180:
                    return 25
                else:
                    return 0  
            if a==4:
                if angle >140 and angle <180:
                    return 25
                else:
                    return 0  
        
            if a==5:
                if angle >140 and angle <180:
                    return 25
                else:
                    return 0  
                    
            if a==6:
                if angle >1 and angle <60:
                    return 25
                else:
                    return 0  
                    
            if a==7:
                if angle >140 and angle <180:
                    return 25
                else:
                    return 0  
            if a==8:
                if angle >140 and angle <180:
                    return 25
                else:
                    return 0 
        except:
            pass

    def pose7():
        sum2 = 0
        sum1=0       
        sum1 = pose7accuracy(1,findangle(12,14,16))
        sum2= sum2+sum1        
        sum1 = pose7accuracy(2,findangle(14,12,24))
        sum2= sum2+sum1
        sum1 = pose7accuracy(3,findangle(12,24,26))
        sum2= sum2+sum1
        sum1 = pose7accuracy(4,findangle(28,26,24))
        sum2= sum2+sum1
        sum1 = pose7accuracy(5,findangle(15,13,11))
        sum2= sum2+sum1
        sum1 = pose7accuracy(6,findangle(13,11,23))
        sum2= sum2+sum1
        sum1 = pose7accuracy(7,findangle(11,23,25))
        sum2= sum2+sum1
        sum1 = pose7accuracy(8,findangle(27,25,23))
        sum2= sum2+sum1
        if sum2>=175:    
            setl(img,1)
        else:
            setl(img,0)   
        return sum2
    #------------------------------------------------------------------------------------------------------------------
    #angle of tree pose 
    

    def pose8accuracy(a,angle):
        global co,sum1
        try:

            if a==1:
                if angle >150 and angle <180:
                    return 25
                else:
                    return 0  
            if a==2:
                if angle >160 and angle <180:
                    return 25
                else:
                    return 0  
            if a==3:
                if angle >100 and angle <150:
                    return 25
                else:
                    return 0  
            if a==4:
                if angle >30 and angle <100:
                    return 25
                else:
                    return 0  
        
            if a==5:
                if angle >150 and angle <180:
                    return 25
                else:
                    return 0  
                    
            if a==6:
                if angle >150 and angle <180:
                    return 25
                else:
                    return 0  
                    
            if a==7:
                if angle >160 and angle <180:
                    return 25
                else:
                    return 0  
            if a==8:
                if angle >160 and angle <180:
                    return 25
                else:
                    return 0 
        except:
            pass

    def pose8():
        sum2 = 0
        sum1=0       
        sum1 = pose8accuracy(1,findangle(12,14,16))
        sum2= sum2+sum1        
        sum1 = pose8accuracy(2,findangle(14,12,24))
        sum2= sum2+sum1
        sum1 = pose8accuracy(3,findangle(12,24,26))
        sum2= sum2+sum1
        sum1 = pose8accuracy(4,findangle(28,26,24))
        sum2= sum2+sum1
        sum1 = pose8accuracy(5,findangle(15,13,11))
        sum2= sum2+sum1
        sum1 = pose8accuracy(6,findangle(13,11,23))
        sum2= sum2+sum1
        sum1 = pose8accuracy(7,findangle(11,23,25))
        sum2= sum2+sum1
        sum1 = pose8accuracy(8,findangle(27,25,23))
        sum2= sum2+sum1
        if sum2>=175:    
            setl(img,1)
        else:
            setl(img,0)   
        return sum2



    def posedumy():
            
        setl(img,1)
           
        

    

    #------------------------------------------------------------------------------------
    ll = Label(base1 , text="Vasudev",font=("Arial Rounded MT Bold", 18))
    ll.place(x=100,y=180)
    lab3 = Label(base1, text="", width=20, height=300, bg="white", bd=0)
    lab3.place(x=800, y=38)
    cap1 = cv2.VideoCapture(r"video\\"+str(pose_counter[0])+".mp4")    
    while True:
        try:
            
            if lss[0]==2:
                print('vasudev')
                break
            
            co=0
            sum1=0
            success, img = cap.read()

            #img = cv2.imread('sliderimage/5.png')
            try:
                img = cv2.resize(img, (750, 450))
            except:
                cap = cv2.VideoCapture(r"video\\"+str(pose_counter[0])+".mp4")
                
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = pose.process(imgRGB)
            
            if pose_counter[0]==1:
                print("vasudev......")
                sum1 = pose1()
                
            elif pose_counter[0]==2:           
                posedumy()
                sum1=100
            elif pose_counter[0]==3:
                sum1 = pose3()
            elif pose_counter[0]==4:
                sum1 = pose4()
            elif pose_counter[0]==5:
                sum1 = pose5()
            elif pose_counter[0]==6:
                sum1 = pose6()
            elif pose_counter[0]==7:
                sum1 = pose7()
            elif pose_counter[0]==8:
                sum1 = pose8()
            elif pose_counter[0]==9:
                posedumy()
                sum1=1
            elif pose_counter[0]==10:
                posedumy()
                sum1=100
            
            elif pose_counter[0]==11:
                posedumy()
                sum1=1
            elif pose_counter[0]==12:
                posedumy()
                sum1=1
            elif pose_counter[0]==13:
                posedumy()
                sum1=1
            elif pose_counter[0]==1:
                posedumy()
                sum1=1
            elif pose_counter[0]==15:
                posedumy()
                sum1=1
            elif pose_counter[0]==16:
                posedumy()
                sum1=1
            elif pose_counter[0]==17:
                posedumy()
                sum1=1
            elif pose_counter[0]==18:
                posedumy()
                sum1=1
            elif pose_counter[0]==19:
                posedumy()
                sum1=1
            elif pose_counter[0]==20:
                posedumy()
                sum1=1
            elif pose_counter[0]==2:
                posedumy()
                sum1=1
            elif pose_counter[0]==22:
                posedumy()
                sum1=1
            elif pose_counter[0]==2:
                posedumy()
                sum1=1
            elif pose_counter[0]==24:
                posedumy()
                sum1=1
                #sum1 = pose9()
            
            
            b = sum1/2
           
           
            ll.config(text=str(b))
            
            base1.update()
            #-----------------------------------------
            
            if cap1.isOpened():
                
                aa="video\\"+str(lm[0])+".mp4"
                
                

                frame_number = []
                annotation_list = []

                i = 0
                flag=1
                  
                ret, frame = cap1.read()
                
                try:
                    frame = cv2.resize(frame,(550,300))
                except:
                    cap1 = cv2.VideoCapture(r"video\\"+str(pose_counter[0])+".mp4")
                    
                    
                
                    
                cv2image= cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                
               
                
                img1 = Image.fromarray(cv2image)
                imgtk = ImageTk.PhotoImage(image = img1)
                lab3.imgtk = imgtk
                lab3.configure(image=imgtk,width=540,height=300)
                base1.update()
                c = cv2.waitKey(0)
                i = i + 1
                
                
                try:
                    annotation_list = annotation_list + [chr(c)]
                    frame_number = frame_number + [i]
                except:
                    continue
                
                        

                #----------------------------------------------
                
               
                cv2.imshow("Image", img)
                cv2.waitKey(1)
            
                
               
        except Exception as e:
            
            print(e)






#all perform yogaa..................

def pose_counter20():
    pose_counter[0]=20
    perform()
    
def pose_counter21():
    pose_counter[0]=21
    perform()

def pose_counter22():
    pose_counter[0]=22
    perform()
    
def pose_counter23():
    pose_counter[0]=23
    perform()

def pose_counter24():
    pose_counter[0]=24
    perform()




def perform_yoga3():
    # perform_yoga image
    s1 = Image.open("GUIImage/perform_pose3.jpg")
    s2 = s1.resize((1350, 690))
    s2.save("GUIImage/perform_pose3.jpg")
    s3 = Image.open("GUIImage/perform_pose3.jpg")
    s4 = ImageTk.PhotoImage(s3)
    s5 = Label(image=s4)
    s5.image = s4
    s5.place(x=0, y=0)

    #perform pose body
    exit_perform_pose = Button(base1, text="Back", width=7, font=("Arial Rounded MT Bold", 18), height=1,bg="black", fg="white", bd=0, command=user_interface)
    exit_perform_pose.place(x=1190, y=43)

    # adding backward button images right
    backward1 = ImageTk.PhotoImage(Image.open(r"GUIImage/backward1.png"))
    backward_lab1 = Label(image=backward1)
    backward_lab1.image = backward1
    backwardbtn1 = Button(base1, image=backward1, width=39, height=57,bg="black", bd=0,command=perform_yoga2)
    backwardbtn1.place(x=1100, y=390)

    #addding buttons with images
    photo19 = ImageTk.PhotoImage(Image.open(r"perform/19.png"))
    img_lab19 = Label(image=photo19)
    img_lab19.image = photo19
    y19 = Button(base1, image=photo19 ,width=308, height=182,bg="black", fg="white", bd=0, command=pose_counter19)
    y19.place(x=61, y=41)

    # addding buttons with images
    photo20 = ImageTk.PhotoImage(Image.open(r"perform/20.png"))
    img_lab20 = Label(image=photo20)
    img_lab20.image = photo20
    y20 = Button(base1,image=photo20, width=308, height=182, bg="black", fg="black", bd=0, command=pose_counter20)
    y20.place(x=400, y=41)

    # addding buttons with images
    photo21 = ImageTk.PhotoImage(Image.open(r"perform/21.png"))
    img_lab21 = Label(image=photo21)
    img_lab21.image = photo21
    y21 = Button(base1, image=photo21, width=308, height=182, bg="black", fg="black", bd=0, command=pose_counter21)
    y21.place(x=735, y=41)

    # addding buttons with images
    photo22 = ImageTk.PhotoImage(Image.open(r"perform/22.png"))
    img_lab22 = Label(image=photo22)
    img_lab22.image = photo22
    y22 = Button(base1, image=photo22, width=308, height=182, bg="black", fg="black", bd=0, command=pose_counter22)
    y22.place(x=61, y=257)

    # addding buttons with images
    photo23 = ImageTk.PhotoImage(Image.open(r"perform/23.png"))
    img_lab23 = Label(image=photo23)
    img_lab23.image = photo23
    y23 = Button(base1, image=photo23, width=308, height=182, bg="black", fg="black", bd=0, command=pose_counter23)
    y23.place(x=400, y=258)

    # addding buttons with images
    photo24 = ImageTk.PhotoImage(Image.open(r"perform/24.png"))
    img_lab24 = Label(image=photo24)
    img_lab24.image = photo24
    y24 = Button(base1, image=photo24, width=308, height=182, bg="black", fg="black", bd=0, command=pose_counter24)
    y24.place(x=735, y=258)




def pose_counter10():
    pose_counter[0]=10
    perform()

def pose_counter11():
    pose_counter[0]=11
    perform()

def pose_counter12():
    pose_counter[0]=12
    perform()
    
def pose_counter13():
    pose_counter[0]=13
    perform()

def pose_counter14():
    pose_counter[0]=14
    perform()

def pose_counter15():
    pose_counter[0]=15
    perform()
     
def pose_counter16():
    pose_counter[0]=16
    perform()

def pose_counter17():
    pose_counter[0]=17
    perform()

def pose_counter18():
    pose_counter[0]=18
    perform()

def pose_counter19():
    pose_counter[0]=19
    perform()









def perform_yoga2():
    # perform_yoga image
    s1 = Image.open("GUIImage/perform_pose2.jpg")
    s2 = s1.resize((1350, 690))
    s2.save("GUIImage/perform_pose2.jpg")
    s3 = Image.open("GUIImage/perform_pose2.jpg")
    s4 = ImageTk.PhotoImage(s3)
    s5 = Label(image=s4)
    s5.image = s4
    s5.place(x=0, y=0)

    #perform pose body
    exit_perform_pose = Button(base1, text="Back", width=7, font=("Arial Rounded MT Bold", 18), height=1,bg="black", fg="white", bd=0, command=user_interface)
    exit_perform_pose.place(x=1190, y=43)

    # adding foward button images right
    foward1 = ImageTk.PhotoImage(Image.open(r"GUIImage/foward1.png"))
    foward_lab1 = Label(image=foward1)
    foward_lab1.image = foward1
    fowardbtn1 = Button(base1, image=foward1, width=39, height=57,bg="black", bd=0,command=perform_yoga3)
    fowardbtn1.place(x=1100, y=610)

    # adding backword button images left
    backward1 = ImageTk.PhotoImage(Image.open(r"GUIImage/backward1.png"))
    backward_lab1 = Label(image=backward1)
    backward_lab1.image = backward1
    backwardbtn1 = Button(base1, image=backward1, width=39, height=57, bg="black", bd=0,command=perform_yoga1)
    backwardbtn1.place(x=1098, y=515)

    #addding buttons with images
    photo10 = ImageTk.PhotoImage(Image.open(r"perform/10.png"))
    img_lab10 = Label(image=photo10)
    img_lab10.image = photo10
    y10 = Button(base1, image=photo10 ,width=308, height=182,bg="black", fg="white", bd=0,command=pose_counter10)
    y10.place(x=61, y=41)

    # addding buttons with images
    photo11 = ImageTk.PhotoImage(Image.open(r"perform/11.png"))
    img_lab11 = Label(image=photo11)
    img_lab11.image = photo11
    y11 = Button(base1,image=photo11, width=308, height=182, bg="black", fg="black", bd=0, command=pose_counter11)
    y11.place(x=400, y=41)

    # addding buttons with images
    photo12 = ImageTk.PhotoImage(Image.open(r"perform/12.png"))
    img_lab12 = Label(image=photo12)
    img_lab12.image = photo12
    y12 = Button(base1, image=photo12, width=308, height=182, bg="black", fg="black", bd=0, command=pose_counter12)
    y12.place(x=735, y=41)

    # addding buttons with images
    photo13 = ImageTk.PhotoImage(Image.open(r"perform/13.png"))
    img_lab13 = Label(image=photo13)
    img_lab13.image = photo13
    y13= Button(base1, image=photo13, width=308, height=182, bg="black", fg="black", bd=0, command=pose_counter13)
    y13.place(x=61, y=257)

    # addding buttons with images
    photo14 = ImageTk.PhotoImage(Image.open(r"perform/14.png"))
    img_lab14 = Label(image=photo14)
    img_lab14.image = photo14
    y14 = Button(base1, image=photo14, width=308, height=182, bg="black", fg="black", bd=0, command=pose_counter14)
    y14.place(x=400, y=258)

    # addding buttons with images
    photo15 = ImageTk.PhotoImage(Image.open(r"perform/15.png"))
    img_lab15 = Label(image=photo15)
    img_lab15.image = photo15
    y15 = Button(base1, image=photo15, width=308, height=182, bg="black", fg="black", bd=0, command=pose_counter15)
    y15.place(x=735, y=258)

    # addding buttons with images
    photo16 = ImageTk.PhotoImage(Image.open(r"perform/16.png"))
    img_lab16 = Label(image=photo16)
    img_lab16.image = photo16
    y16 = Button(base1, image=photo16, width=308, height=182, bg="black", fg="black", bd=0, command=pose_counter16)
    y16.place(x=63, y=472)

    # addding buttons with images
    photo17 = ImageTk.PhotoImage(Image.open(r"perform/17.png"))
    img_lab17 = Label(image=photo17)
    img_lab17.image = photo17
    y17 = Button(base1, image=photo17, width=308, height=182, bg="black", fg="black", bd=0, command=pose_counter17)
    y17.place(x=400, y=472)

    # addding buttons with images
    photo18 = ImageTk.PhotoImage(Image.open(r"perform/18.png"))
    img_lab18 = Label(image=photo18)
    img_lab18.image = photo18
    y18 = Button(base1, image=photo18, width=308, height=182, bg="black", fg="black", bd=0, command=pose_counter18)
    y18.place(x=739, y=472)



def pose_counter1():
    pose_counter[0]=1
    perform()

def pose_counter2():
    pose_counter[0]=2
    perform()
    
def pose_counter3():
    pose_counter[0]=3
    perform()

def pose_counter4():
    pose_counter[0]=4
    perform()

def pose_counter5():
    pose_counter[0]=5
    perform()
     
def pose_counter6():
    pose_counter[0]=6
    perform()

def pose_counter7():
    pose_counter[0]=7
    perform()

def pose_counter8():
    pose_counter[0]=8
    perform()

def pose_counter9():
    pose_counter[0]=9
    perform()
    
    
    

def perform_yoga1():
    # perform_yoga image
    
    
    s1 = Image.open("GUIImage/perform_pose.jpg")
    s2 = s1.resize((1350, 690))
    s2.save("GUIImage/perform_pose.jpg")
    s3 = Image.open("GUIImage/perform_pose.jpg")
    s4 = ImageTk.PhotoImage(s3)
    s5 = Label(image=s4)
    s5.image = s4
    s5.place(x=0, y=0)

    #perform pose body
    exit_perform_pose = Button(base1, text="Back", width=7, font=("Arial Rounded MT Bold", 18), height=1,bg="black", fg="white", bd=0, command=user_interface)
    exit_perform_pose.place(x=1190, y=43)

    # adding foward button images right
    foward1 = ImageTk.PhotoImage(Image.open(r"GUIImage/foward1.png"))
    foward_lab1 = Label(image=foward1)
    foward_lab1.image = foward1
    fowardbtn1 = Button(base1, image=foward1, width=39, height=57,bg="black", bd=0,command=perform_yoga2)
    fowardbtn1.place(x=1100, y=610)

    #addding buttons with images
    photo1 = ImageTk.PhotoImage(Image.open(r"perform/1.png"))
    img_lab1 = Label(image=photo1)
    img_lab1.image = photo1
    y1 = Button(base1, image=photo1 ,width=308, height=182,bg="black", fg="white", bd=0, command=pose_counter1)
    y1.place(x=61, y=41)

    # addding buttons with images
    photo2 = ImageTk.PhotoImage(Image.open(r"perform/2.png"))
    img_lab2 = Label(image=photo2)
    img_lab2.image = photo2
    y2 = Button(base1,image=photo2, width=308, height=182, bg="black", fg="black", bd=0, command=pose_counter2)
    y2.place(x=400, y=41)

    # addding buttons with images
    photo3 = ImageTk.PhotoImage(Image.open(r"perform/3.png"))
    img_lab3 = Label(image=photo3)
    img_lab3.image = photo3
    y3 = Button(base1, image=photo3, width=308, height=182, bg="black", fg="black", bd=0, command=pose_counter3)
    y3.place(x=735, y=41)

    # addding buttons with images
    photo4 = ImageTk.PhotoImage(Image.open(r"perform/4.png"))
    img_lab4 = Label(image=photo4)
    img_lab4.image = photo4
    y4 = Button(base1, image=photo4, width=308, height=182, bg="black", fg="black", bd=0, command=pose_counter4)
    y4.place(x=61, y=257)

    # addding buttons with images
    photo5 = ImageTk.PhotoImage(Image.open(r"perform/5.png"))
    img_lab5 = Label(image=photo5)
    img_lab5.image = photo5
    y5 = Button(base1, image=photo5, width=308, height=182, bg="black", fg="black", bd=0, command=pose_counter5)
    y5.place(x=400, y=258)

    # addding buttons with images
    photo6 = ImageTk.PhotoImage(Image.open(r"perform/6.png"))
    img_lab6 = Label(image=photo6)
    img_lab6.image = photo6
    y6 = Button(base1, image=photo6, width=308, height=182, bg="black", fg="black", bd=0, command=pose_counter6)
    y6.place(x=735, y=258)

    # addding buttons with images
    photo7 = ImageTk.PhotoImage(Image.open(r"perform/7.png"))
    img_lab7 = Label(image=photo7)
    img_lab7.image = photo7
    y7 = Button(base1, image=photo7, width=308, height=182, bg="black", fg="black", bd=0, command=pose_counter7)
    y7.place(x=63, y=472)

    # addding buttons with images
    photo8 = ImageTk.PhotoImage(Image.open(r"perform/8.png"))
    img_lab8 = Label(image=photo8)
    img_lab8.image = photo8
    y8 = Button(base1, image=photo8, width=308, height=182, bg="black", fg="black", bd=0, command=pose_counter8)
    y8.place(x=400, y=472)

    # addding buttons with images
    photo9 = ImageTk.PhotoImage(Image.open(r"perform/9.png"))
    img_lab9 = Label(image=photo9)
    img_lab9.image = photo9
    y9 = Button(base1, image=photo9, width=308, height=182, bg="black", fg="black", bd=0, command=pose_counter9)
    y9.place(x=739, y=472)
    

#--------------------------------------------------------------------------------------------------------------------------------------------

def health_monitor():
    
    import meter1
    meter1.ff(base1,username[0])
    exit_health = Button(base1, text="Exit", width=8, font=("Arial Rounded MT Bold", 18), height=1, bg="black",
                      fg="white", bd=0, command=user_interface)
    exit_health.place(x=1160, y=40)
    
    base1.update()



    

    
def my_profile():
    # profile_image
    s3 = Image.open("GUIImage/my_profile.jpg")
    s4 = ImageTk.PhotoImage(s3)
    s5 = Label(image=s4)
    s5.image = s4
    s5.place(x=0, y=0)

    log1 = ImageTk.PhotoImage(Image.open(r"GUIImage/logout.png"))
    log_lab1 = Label(image=log1)
    log_lab1.image = log1
    logbtn1 = Button(base1, image=log1, width=45, height=57, bg="black", bd=0, command=user_login)
    logbtn1.place(x=845, y=75)

    change_pass = Button(base1, text="Change\nPassword", width=12, font=("Arial Rounded MT Bold", 12), height=2,
        bg="#c00000", fg="white", bd=0, command=forget_password)
    change_pass.place(x=456, y=560)

    back = Button(base1, text="Back", width=12, font=("Arial Rounded MT Bold", 12), height=2,
                         bg="#c00000", fg="white", bd=0, command=user_interface)
    back.place(x=620, y=560)

    s_en1 = Label(base1,width=26,bg="white", font=("Arial", 16),bd=0)
    s_en1.place(x=100, y=210)

    s_en2 = Label(base1, width=26,bg="white", font=("Arial", 16), bd=0)
    s_en2.place(x=100, y=300)

    s_en3 = Label(base1, width=26,bg="white", font=("Arial", 16), bd=0)
    s_en3.place(x=100, y=390)

    s_en4 = Label(base1, width=26,bg="white", font=("Arial", 16), bd=0)
    s_en4.place(x=100, y=480)

    s_en5 = Label(base1 ,width=26,bg="white", font=("Arial", 16), bd=0)
    s_en5.place(x=100, y=570)


    s_en6 = Label(base1, width=26,bg="white", font=("Arial", 16), bd=0)
    s_en6.place(x=440, y=210)

    s_en7 = Label(base1, width=26,bg="white", font=("Arial", 16), bd=0)
    s_en7.place(x=440, y=300)

    s_en8 = Label(base1, width=26,bg="white", font=("Arial", 16), bd=0)
    s_en8.place(x=440, y=390)

    s_en9 = Label(base1, width=26,bg="white", font=("Arial", 16), bd=0)
    s_en9.place(x=440, y=480)

    #s_en10 = Label(base1, width=26,bg="white", font=("Arial", 16), bd=0)
    #s_en10.place(x=100, y=570)



    ils = getDB.retrivePinfo(username[0])
    print(ils)



    

    s_en1.config(text=ils[6])
    s_en2.config(text=ils[3])
    s_en3.config(text=ils[1])
    s_en4.config(text=ils[2])
    s_en5.config(text=ils[5])
    s_en6.config(text=ils[9])
    s_en7.config(text=ils[4])
    s_en8.config(text=ils[7])
    s_en9.config(text=ils[0])
    


    



#user interface............
def user_interface():
    # user_interface image
    
    s3 = Image.open("GUIImage/user_interface.jpg")
    s4 = ImageTk.PhotoImage(s3)
    s5 = Label(image=s4)
    s5.image = s4
    s5.place(x=0, y=0)

    # user interface body
    exit_tea_interface = Button(base1, text="Exit", width=8, font=("Arial Rounded MT Bold", 18), height=1,
                                bg="white", fg="black", bd=0, command=user_login)
    exit_tea_interface.place(x=1084, y=55)

    i_btn1 = Button(base1, text="Learn Yoga", font=("Arial Rounded MT Bold", 18), width=12, height=1, bd=0,
                    bg="white", command=learn_yoga)
    i_btn1.place(x=115, y=235)
    i_btn2 = Button(base1, text="Perform Yoga", font=("Arial Rounded MT Bold", 18), width=12, height=1, bd=0,
                    bg="white", command=perform_yoga1)
    i_btn2.place(x=393, y=295)
    i_btn3 = Button(base1, text="Health Monitor", font=("Arial Rounded MT Bold", 18), width=12, height=1, bd=0,
                    bg="white", command=health_monitor)
    i_btn3.place(x=115, y=455)
    i_btn4 = Button(base1, text=" My Profile ", font=("Arial Rounded MT Bold", 18), width=12, height=1, bd=0,
                    bg="white", command=my_profile)
    i_btn4.place(x=393, y=525)






# user Login................
def user_login():

   
    def passwordValidation():
        usern = en1.get()
        pass1 = en2.get()
        username[0] = usern

        #password = retrivedata()
        password = getDB.retrivePass(usern)
        #print(password,pass1)

        if password == "UserName not found":
            sm.config(text = "Invalid User Name !")

        if(pass1!=''):
        
        
            if password==pass1:
                print('login successfuly')
                user_interface()
            else:
                sm.config(text = "Invalid Password !")
        if password == "UserName not found":
            sm.config(text = "Invalid User Name !")

                

        
    




    
    # user_login image
    
    s3 = Image.open("GUIImage/user_login.jpg")
    s4 = ImageTk.PhotoImage(s3)
    s5 = Label(image=s4)
    s5.image = s4
    s5.place(x=0, y=0)

    # login_page body
    en1 = Entry(base1, width=28, font=("Arial", 15), bd=0)
    en1.place(x=491, y=220)
    en2 = Entry(base1, width=28, font=("Arial", 15), bd=0, show="*")
    en2.place(x=490, y=300)
    btn1 = Button(base1, text="Login", font=("Arial Rounded MT Bold", 20), width=19, height=1, bd=0, fg="white",
                  bg="#c00000",activebackground="red", command=passwordValidation , cursor = "hand2")
    btn1.place(x=470, y=465)
    btn2 = Button(base1, text="New user ? Sign Up! ", font=("Calibri (Body)", 15), width=27, height=1, bd=0, bg="white",
                  command=new_user)
    btn2.place(x=480, y=350)
    btn3 = Button(base1, text="Forget password ? ", font=("Calibri (Body)", 14), width=27, height=1, bd=0, bg="white",
                  command=forget_password)
    btn3.place(x=480, y=390)

    sm = Label(base1 ,text="",font=("Calibri (Body)", 14), width=27, height=1, bd=0, bg="white",fg = "red")
    sm.place(x=480,y=550)

    
    btn4 = Button(base1, text="<  Back to Homepage  >", font=("Arial Rounded MT Bold", 16), width=33, height=1, bd=0,
                  fg="black", bg="#d0cecf", command=first)
    btn4.place(x=416, y=630)




#Home page.......
def first():

    # home page image
    
    my=Image.open("GUIImage/homepage.jpg")
    my_hp = ImageTk.PhotoImage(my)
    my_hp2=Label(image=my_hp)
    my_hp2.image=my_hp
    my_hp2.place(x=0,y=0)

    # home page body******************

    btn2 = Button(base1, text="Login", font=("Arial Rounded MT Bold", 19), width=5, height=2, bd=0, bg="white",command=user_login)
    btn2.place(x=930, y=355)
    base1.mainloop()


first()
#user_login()
#perform_yoga1()

#forget_password()
