from tkinter import*
from tkinter.messagebox import showinfo

#imports
import time
import datetime ##used to return the time of the break in
#import RPi.GPIO as GPIO
#import smtplib


#Setup
#GPIO Configuration
#GPIO.setmode(GPIO.BCM)
#GPIO Setup
#GPIO.setup(18,GPIO.IN)
#GPIO.setup(24,GPIO.OUT)
#from "enter .py here" import information 

class IntruderAlertSystem(Frame): # change Frame later
    'Intruder alert system setup'

    
    def __init__(self,parent=None):
        'constructor'
        Frame.__init__(self, parent)

        self.pack() 
        IntruderAlertSystem.make_widgets(self)
        self.email=''
        self.password=''
        #Self.make_widgets()
    def submit(self):
        self.email=self.entry1.get()#code for email entry
        print('email is: ' + self.email)
        
        self.password =self.entry2.get()#code for password entry
        print('password is: ' + self.password)

        
        if('@' not in self.email): #checking for valid info
            showinfo('Error','Invalid Email')
        elif(self.email=='' or self.password==''):
            showinfo('Error','You must enter email password to activate alert system!')
        else:
            showinfo('Activation Complete','RaspberryPi Intruder Alert has been successfully activated!')
            root.destroy()
            self.alarm(True)
    
    def make_widgets(self):
        Label(self, text="Enter your email:").grid(row = 0 , column = 0)
        Label(self, text="Enter your password").grid(row = 10 , column = 0)
        
        submitButton = Button(self, text="Submit", command=self.submit).grid(row = 20, column = 10)
        
        self.entry1 = Entry(self, justify = CENTER, width=20)
        self.entry1.grid(row=0, column=3, columnspan=25)
        self.entry2 = Entry(self, justify = CENTER, width=20)
        self.entry2.grid(row=10, column=3, columnspan=25)


    

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
        
        #Import password GUI
        #it will return the password and if what ever it returns doesn't match it will
        #run the GUI again
        # there will be a counter so that if the GUI runs a certain number of time
        #then the alarm function will activate
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
IntruderAlertSystem().mainloop()
