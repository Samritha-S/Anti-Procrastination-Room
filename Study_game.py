import tkinter as tk   #I imported Tkinter for the User Interface
from tkinter import simpledialog

root = tk.Tk()   #Created the main window
root.title("Anti- Procrastination Room")   #Set the title of the window
root.geometry("500x500")   #Set the size of the window


#Labels
welcome_label = tk.Label(root,text="Welcome to the Anti-Procrastination Room!", font=("Kristen ITC", 16)) #This is welcome Label
welcome_label.pack(pady=20) #20px of verticaal padding

timer_label  = tk.Label(root, text = "50:00", font = ("Kristen ITC", 24, "bold"), fg = "#ff66cc", bg = "#0a0013")  #This is Timer Label
timer_label.pack(pady=10) #10px of vertical padding


root.mainloop()   #Start the Tkinter event loop and Keeps the window open until the user closes it

#Creating the Countdown Function
def start_timer(seconds = 50*60):
    mins,secs = divmod(seconds,60)
    timer_label.config(text=f"{mins:02d}:{secs:02d}") #Brings the minutes and seconds to 2 digit format
    if seconds > 0:
        root.after(1000, start_timer, seconds-1) #Calls the function again after 1 second (1000 milliseconds)
    else:
        timer_label.config(text="Time for a break!") #When the timer reaches 0, it displays "Time for a break"  


#Start Button
start_button = tk.Button(root, text="Start Study Session", font=("Kristen ITC", 14, "bold"), fg = "#ff4da6", bg = "#330033", activeforeground="#0a0013", activebackground="#ff4da6", command=start_timer) #This is the Start Button
start_button.pack(pady=10) #20px of vertical padding

