from datetime import datetime
import tkinter as tk
import requests

z = ""
button_press_choice = 0

# Important variables
first_quest = int(input("How many emergency contacts (Pick any number of people to send message)? "))
listy = []
time = str(datetime.now())
location = input("Where is your locaiton? ")
location_final = " At " + location
[]
# Non-important-ish variables
emergency_type = ""
heart_attack = " Help I am having a heart attack"
intruder_alert = " Help someone is breaking in"
unknown_medical_emergency = " Help, I don't know what is going on"
fire_emergency = " There is a fire please help"
stroke_emergency = " Help I am having a stroke"
chocking_emergency = " Help I am choking"

# We convert the phone numbers to variables of data which get stored inside the list(listy)
for p in range(first_quest):
  g = str(input("What is their number? "))
  listy.append(g)


# gets the current time and appends it to the emergency, then broadcasts it to the emergency operators' window
def submit():
    global z
    global emergency_type
    global time
    global listy
    global location_final

    # A message is chosen for the appropriate emergency
    if button_press_choice == 1:
        emergency_type = heart_attack
    elif button_press_choice == 2:
        emergency_type = intruder_alert
    elif button_press_choice == 3:
        emergency_type = unknown_medical_emergency
    elif button_press_choice == 4:
        emergency_type = fire_emergency
    elif button_press_choice == 5:
        emergency_type = stroke_emergency
    elif button_press_choice == 6:
        emergency_type = chocking_emergency

    # It takes the time and information and send the emergency signal to the appropriate people
    def emergencyfunc():
        for a in range(len(listy)):
            ninjaturtle = requests.post('https://textbelt.com/text', {
                'phone': listy[a],
                'message': (time, location_final, emergency_type),
                'key': '3194af59217b43aec6fdcf1e751afa494918a797QP9a9t8zFkSIk2I8Ja8hg7YFV',
            })
            print(ninjaturtle)

    emergencyfunc()
    x = str(datetime.now())
    emergencieslist.append(z + x)
    text.delete(1.0, "end")
    z = ""
    btn_1.grid_remove()


# initiates a login screen
def emergency():

    def refresh():
        # clears old broadcasts and
        text2.delete(1.0, "end")
        for q in range(len(emergencieslist)):
            text2.insert(1.0, ", ")
            text2.insert(1.0, emergencieslist[q])
    # creates a second window for emergency operators, showing past broadcasts
    root2 = tk.Tk()
    root2.geometry("900x900")

    text2 = tk.Text(root2, height=2, width=48, font=("Arial", 24))
    text2.grid(columnspan=5)

    for x in range(len(emergencieslist)):
        text2.insert(1.0, ", ")
        text2.insert(1.0, emergencieslist[x])

    btn_ref = tk.Button(root2, text="refresh", command=lambda: refresh(), width=5, font="arial")
    btn_ref.grid(row=1, column=0)

    root2.mainloop()


def fire():
    global z
    global button_press_choice
    button_press_choice = 4
    text.delete(1.0, "end")
    text.insert(1.0, "Fire")
    z = "Fire: "
    btn_1.grid(row=1, column=4)


def heart():
    global z
    global button_press_choice
    button_press_choice = 1
    text.delete(1.0, "end")
    text.insert(1.0, "Heart attack")
    z = "Heart attack: "
    btn_1.grid(row=1, column=4)


def stroke():
    global z
    global button_press_choice
    button_press_choice = 5
    text.delete(1.0, "end")
    text.insert(1.0, "Stroke")
    z = "Stroke: "
    btn_1.grid(row=1, column=4)


def unknown():
    global z
    global button_press_choice
    button_press_choice = 3
    text.delete(1.0, "end")
    text.insert(1.0, "Unknown medical emergency")
    z = "Unknown medical emergency: "
    btn_1.grid(row=1, column=4)


def robber():
    global z
    global button_press_choice
    button_press_choice = 2
    text.delete(1.0, "end")
    text.insert(1.0, "Break in")
    z = "Break in: "
    btn_1.grid(row=1, column=4)


def choking():
    global z
    global button_press_choice
    button_press_choice = 6
    text.delete(1.0, "end")
    text.insert(1.0, "Choking")
    z = "Choking: "
    btn_1.grid(row=1, column=4)


# creates a list for all broadcasts to be added to, then referenced by the operator window
emergencieslist = []

# civilian user interface
root = tk.Tk()
root.geometry("900x900")

# text window
text = tk.Text(root, height=2, width=48, font=("Arial", 24))
text.grid(columnspan=5)

# buttons
btn_1 = tk.Button(root, bg="green", text="submit", command=lambda: submit(), width=22, font="Arial")
btn_2 = tk.Button(root, bg="orange", text="emergency operator window", command=lambda: emergency(), width=22, font="arial")
btn_2.grid(row=3, column=0)
btn_3 = tk.Button(root, text="fire", command=lambda: fire(), width=22, font="arial")
btn_3.grid(row=1, column=1)
btn_4 = tk.Button(root, text="heart attack", command=lambda: heart(), width=22, font="arial")
btn_4.grid(row=1, column=2)
btn_5 = tk.Button(root, text="stroke", command=lambda: stroke(), width=22, font="arial")
btn_5.grid(row=2, column=0)
btn_6 = tk.Button(root, text="unknown medical emergency", command=lambda: unknown(), width=22, font="arial")
btn_6.grid(row=1, column=0)
btn_7 = tk.Button(root, text="robber", command=lambda: robber(), width=22, font="arial")
btn_7.grid(row=2, column=1)
btn_8 = tk.Button(root, text="choking", command=lambda: choking(), width=22, font="arial")
btn_8.grid(row=2, column=2)
root.mainloop()
