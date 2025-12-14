import tkinter as tk   #I imported Tkinter for the User Interface
from tkinter import simpledialog

root = tk.Tk()   #Created the main window
root.title("Anti- Procrastination Room")   #Set the title of the window
root.geometry("500x500")   #Set the size of the window

#Set the color of the window
root.configure(bg="#0a0013")  #Dark Purple Background


#Creating the Countdown Function
def start_timer(seconds = 50*60):
    mins,secs = divmod(seconds,60) #Divides the total seconds into minutes and seconds
    timer_label.config(text=f"{mins:02d}:{secs:02d}") #Brings the minutes and seconds to 2 digit format
    if seconds > 0:
        root.after(1000, start_timer, seconds-1) #Calls the function again after 1 second (1000 milliseconds)
    else:
        timer_label.config(text="Time for a break!") #When the timer reaches 0, it displays "Time for a break"  


#Start Button
start_button = tk.Button(root, text="Start Study Session", font=("Kristen ITC", 14, "bold"), fg = "#ff4da6", bg = "#330033", activeforeground="#0a0013", activebackground="#ff4da6", command=start_timer) #This is the Start Button
start_button.pack(pady=10) #10px of vertical padding


#Entry Box to type tasks
task_entry = tk.Entry(root, font=("Kristen ITC", 14), fg="#ff66cc", bg="#0d001a", insertbackground="#ff4da6") #This is the Entry Box for tasks
task_entry.pack(pady=5) #5px of vertical padding


#Button to add tasks
tasks = [] #List to store the tasks
def add_task():
    task = task_entry.get() #get the text tyed in the entry box
    if task.strip() != "": #Check if the task is not empty
        tasks.append(task) #Add the task to the list
        task_list.insert(tk.END, task) #Insert the task into the Listbox
        task_entry.delete(0, tk.END) #Clear the entry box after adding the task 
#Listbox to Display Tasks
task_list = tk.Listbox(root, font=("Kristen ITC", 14), fg="#ff66cc", bg="#0d001a", selectbackground="#ff4da6", selectforeground="#0a0013") #This is the Listbox to display tasks
task_list.pack(pady=10) #10px of vertical padding

add_button = tk.Button(root, text="Add Task", font=("Comic Sans MS", 12), fg="#ff4da6", bg="#330033", activeforeground="#0a0013", activebackground="#ff4da6", command=add_task) #This is the Add Task Button
add_button.pack(pady = 5) #5px of vertical padding

task_meter = 0 #keeps track of completed tasks

def completed_task():
    global task_meter
    try:
        selected_index=  task_list.curselection()[0] #Get the index of the selected task
        task_text = task_list.get(selected_index) #Get the text of the selected task
        task_list.delete(selected_index) #Remove the task from the Listbox
        task_list.itemconfig(selected_index, fg="#888888", font=("Kristen ITC", 14, "overstrike")) #Strike through the completed task
        task_meter += 1 #Increase the task meter by 1
        task_meter_label.config(text=f"Task Meter: {task_meter}") #Update the Task Meter Label
    except IndexError:
        pass  #If no task is selected, do nothing
complete_button = tk.Button(root, text="Complete Task", font=("Kristen ITC", 14, "bold"),fg="#ff4da6", bg="#330033", activeforeground="#0a0013", activebackground="#ff4da6", command=completed_task) #This is the Complete Task Button
complete_button.pack(pady=5) #5px of vertical padding

#Making the FLash Effect Function
def flash_unlock(message):
    unlock_label.config(text=message, fg = "#ff4da6")
    #Flash Neon Effect
    def blink(times):
        if times>0:
            current_color = unclo_label.cget("fg") #Get current color
            unlock_label.config(fg="#ff99cc" if current_color=="#ff4da6" else "#ff4da6") #Toggle color
            root.after(200, blink, times-1) #Call blink again after 200 milliseconds
        else:
             unlock_label.config(fg="#ff4da6")  # reset to default neon pink
        blink(6)  # Blink 6 times        


#Linking task Completion to the meter/unlocks
def complete_task():
    global task_meter
    try:
        selected_index = task_list.curselection()[0] # Get the index of the selected task
        tast_text = task_list.get(selected_index) # Get the text of the selected task
        task_list.delete(selected_index) # Remove the task from the Listbox
        task_list.insert(selected_index, task_text) # Reinsert the task to update its appearance
        task_list.itemconfig(selected_index, fg="#888888", font=("Kristen ITC", 14, "overstrike")) # Strike through the completed task

        #update task meter
        task_meter += 1 # Increase the task meter by 1
        task_meter_label.config(text=f"Task Meter: {task_meter}") # Update the Task Meter Label

        #check unlocks
        if task_meter == 3:
            print("🎉 Milestone reached: Task streak 3!")
        elif task_meter == 5:
            print("✨ Milestone reached: Task streak 5!")    
    except IndexError:
        pass  # If no task is selected, do nothing   


#Labels
welcome_label = tk.Label(root,text="Welcome to the Anti-Procrastination Room!", font=("Kristen ITC", 16, "bold"), fg = "#ff66cc", bg = "#0a0013") #This is welcome Label
welcome_label.pack(pady=20) #20px of verticaal padding

timer_label  = tk.Label(root, text = "50:00", font = ("Kristen ITC", 24, "bold"), fg = "#ff66cc", bg = "#0a0013")  #This is Timer Label
timer_label.pack(pady=10) #10px of vertical padding

task_meter_label = tk.Label(root, text=f"Task Meter: {task_meter}", font=("Kristen ITC", 14, "bold"), fg="#ff66cc", bg="#0a0013") #This is Task Meter Label
task_meter_label.pack(pady=10)  #10px of vertical padding

unlock_label = tk.Label(root, text="", font=("Kristen ITC", 16, "bold"), fg="#ff4da6", bg="#0a0013") #This is Unlocks Label
unlock_label.pack(pady=10) #10px of vertical padding
root.mainloop()  #Start the Tkinter event loop and Keeps the window open until the user closes it