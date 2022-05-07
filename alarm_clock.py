
from tkinter import *
import datetime 
import time
import winsound

from numpy import size


def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")      # %H for 24 hour format and %I for 12 hour format 
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        if now == set_alarm_timer:
            #you can set date and time here
            print("Time to Wake up")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)
        
    
clock = Tk()

clock.title("Alarm Clock")
clock.geometry("400x400")
time_format = Label(clock, text= "Enter time in 24 hour format!",fg="red",bg="black",font="Arial").place(x=90,y=280)
addTime = Label(clock,text = "Hour            Min            Sec",font=80).place(x = 50 , y=150)
setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",20,"bold")).place(x=30, y=80)


# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 25).place(x=30,y=180)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 25).place(x=100,y=180)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 25).place(x=180,y=180)


#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="red",width = 20,height=1,command = actual_time).place(x =110,y=230)
clock.mainloop()
#Execution of the window.
        

