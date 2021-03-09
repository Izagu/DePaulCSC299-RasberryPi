
from tkinter import*
from tkinter.messagebox import showinfo
###RPi Stuff
#import RPi.GPIO as GPIO
import time
#import smtplib
#Timestamp
import datetime ##used to return the time of the break in
###########set up stuff ###################
## GPIO Configuration
#GPIO.setmode(GPIO.BCM)
##GPIO Setup
#GPIO.setup(18,GPIO.IN)
#GPIO.setup(24,GPIO.OUT)


class IntruderSystem(Frame):
    'Activates the alarm, you enter the email'
        
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        ##instance variables
        self.email=''
        self.password=''
        self.activate()
        #self.deactivate()
    def activate(self):
        'makes widgets for activation scheme'
        Label(self,text="Welcome to the RaspberryPi Intruder Alert System!").grid(row=0,column=4, columnspan=16)
        Label(self,text="TO ACTIVATE").grid(row=1, column=6)
        ##Second Row: box to enter email
        Label(self,text="Enter Email: ").grid(row=2,column=3,columnspan=3)
        self.eentry=Entry(self)
        self.eentry.grid(row=2,column=6,columnspan=12)
        ##self.wentry.insert(END,mask(self.word,""))
        ##Third Row: box to enter password of choice
        Label(self,text="Enter Password: ").grid(row=3,column=3,columnspan=3)
        self.pentry=Entry(self)
        self.pentry.grid(row=3,column=6,columnspan=12)
        def e():
            #retrieve & set the email
            self.email=self.eentry.get()
            print('email is: ' + self.email) ##TEST
            #retreieve and set the password
            self.password =self.pentry.get()
            print('password is: ' + self.password) ##TEST
            if('@' not in self.email):
                showinfo('Error','Invalid Email')
            elif(self.email=='' or self.password==''):
                showinfo('Error','You must enter email password to activate alert system!')
            else:
                showinfo('Activation Complete','RaspberryPi Intruder Alert has been successfully activated!')
                root.destroy()
                #self.deactivate()
                self.alarm(True) ##calls the motion dectector to start doing its job
                
        ##Enter button triggers activation if the input is correct    
        c=Button(self,text='Enter', command=e)
        c.grid(row=4, column=6, columnspan=5)

            
        
    def get_time(self):
        'provides a time stamp for the email'
        now=datetime.datetime.now()
        return 'Intruder alert. Motion detected at' + str(now)
        
    ##Send Email
    def send_email(self, recipient, subject, text):
        'sends email to provided email address'
        
        GMAIL_USER = 'yanaceyizaguirre@gmail.com'
        GMAIL_PASS = '86hpW2207!'
        SMTP_SERVER = 'smtp.gmail.com'
        SMTP_PORT = 587
        smtpserver= smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo
        smtpserver.login(GMAIL_USER, GMAIL_PASS)
        header= 'To:' + recipient + '\n' + 'From: ' + GMAIL_USER
        header= header + '\n' + 'Subject:' + subject + '\n'
        msg = header + '\n' + text + '\n\n'
        smtpserver.sendmail(GMAIL_USER, recipient, msg)
        smtpserver.close()
    ##Send Text
    def send_text(self):
        'sends a text'
        TO='6304563302@messaging.sprintpcs.com'
        GMAIL_USER='yanaceyizaguirre@gmail.com'
        PASS='86hpW2207!'
        SUBJECT= 'ALERT'
        TEXT= 'RP ALARM'

        print("Sending text")
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(GMAIL_USER,PASS)
        header = 'To: ' + TO + '\n' + 'From: ' + GMAIL_USER
        header = header + '\n' + 'Subject: ' + SUBJECT + '\n'
        print(header)
        msg = header + '\n' + TEXT + '\n\n'
        server.sendmail(GMAIL_USER,TO,msg)
        server.quit()
        time.sleep(1)
        print("Text sent")

    ##Buzzing
    def buzz(self,pitch,duration):
        'triggers buzzing'
        period= 1.0/pitch
        delay= period/2
        cycles= int(duration *pitch)
        for i in range(cycles):
            GPIO.output(24, True)
            time.sleep(delay)
            ## maybe ask for a password WITHIN HERE??? Have it buzz UNTIL THE RIGHT PASSWORD IS CHOSEN
            GPIO.output(24, False)
            time.sleep(delay)
    def alarm(self,state):
        'triggers the motion detecting process'
        count = 0
        ##Option to deactivate is automatic
        #root=Tk()
        yes = state
        while yes:
            count = count + 1
            input_state = GPIO.input(18)
            #input_state= True
            if input_state and count > 1:
                ## String to acknowledge the motion - TESTING PURPOSES ONLY
                print('Motion Detected')
                #while(p!=P)
                ## Set off the alarm
                #self.buzz(5000,1) ##Pitch, Length
                
                ## send the email to the user
                #self.send_email(self.email, 'INTRUDER ALERT!',text)
                self.send_email(self.email, 'INTRUDER ALERT!',self.get_time())
                time.sleep(3)
               
                #send text message
                self.send_text()
                
            else:
                time.sleep(1) ##how often it checks the motion
        
root=Tk()
IntruderSystem(root).pack()

#def main():
  #  root=Tk()
  #  IntruderSystem(root).pack() ## call this when you need to activate the system - right away
    #print(y.get_time())
    #deactivate(root).pack() ## call this when


