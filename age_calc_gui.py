#!/usr/bin/python3

#===============MODULES===============#

import tkinter as tk
from tkinter import PhotoImage, messagebox
import datetime, os

#===============ROOT WINDOW===============#

root = tk.Tk()
root.title("Age Calculator")
root.geometry("571x590")
root.minsize(450, 590)
icon_path = os.path.expanduser('~/.local/share/icons/age_calculator_gui/age_calculator.png')
icon = PhotoImage(file = icon_path)
root.iconphoto(False, icon)
root.config(bg = "#333")

'''
 _____ _   _ _   _  ____ _____ ___ ___  _   _ ____  
|  ___| | | | \ | |/ ___|_   _|_ _/ _ \| \ | / ___| 
| |_  | | | |  \| | |     | |  | | | | |  \| \___ \ 
|  _| | |_| | |\  | |___  | |  | | |_| | |\  |___) |
|_|    \___/|_| \_|\____| |_| |___\___/|_| \_|____/ 
'''

#===============Variables===============#

day_clicks = month_clicks = year_clicks = 0
y0 = int(datetime.date.today().strftime("%Y"))
m0 = int(datetime.date.today().strftime("%m"))
d0 = int(datetime.date.today().strftime("%d"))

#===============CLEAR FRAME===============#

def clear_out():
    for widgets in frame_04.winfo_children():
        widgets.destroy()
    for widgets in frame_05.winfo_children():
        widgets.destroy()

#===============TEXT OUTPUT===============#

def text_out():
    try:
        global d0, m0, y0, clicks
        d0, m0, y0 = int(entry_04.get()), int(entry_05.get()), int(entry_06.get())
        y1 = int(entry_03.get())
        m1 = int(entry_02.get())
        d1 = int(entry_01.get())
        date = datetime.date(y0, m0, d0)
        DOB = datetime.date(y1, m1, d1)
        age_days = (date - DOB).days
        age_months = age_days/30.4375
        age_weeks = age_days/7
        age_years = age_days/365.25
        age_hours = age_days*24
        age_minutes = age_hours*60
        age_seconds = age_minutes*60
        years = int(age_years)
        months = int((age_years - years)*12)
        days = int((((age_years - years)*12) - months)*30.4375)
        nxt_year = (y1+years+1)
        nxt_DOB = datetime.date(nxt_year, m1, d1)
        rem_days = (nxt_DOB - date).days
        rem_months = rem_days/30.4375
        rem_weeks = rem_days/7
        rem_hours = rem_days*24
        rem_minutes = rem_hours*60
        rem_seconds = rem_minutes*60
        rem_months1 = int(rem_months)
        rem_days1 = int((rem_months - int(rem_months))*30.4375)
        clear_out()
        
#===============ERRORS===============#

        if y1 <= 0 or y1 > y0 or y0 <= 0:
            messagebox.showerror(
                "Error",
                "Please Input The Correct Year")
            
        elif (m1 <= 0 and m0 <= 0) or (m1 == m0 and d1 >= d0 and y0 == y1):
            messagebox.showerror(
                "Error",
                "Please Input The Correct Day")
        else:
            tk.Message(
                frame_04,
                text = "Total Years: "+str(age_years)+" Years"+"\nTotal Months: "+str(age_months)+" Months"+"\nTotal Weeks: "+str(age_weeks)+" weeks"+"\nTotal Days: "+str(age_days)+" Days\nTotal Hours: "+str(age_hours)+" Hours (Approx)\n"+"Total Minutes: "+str(age_minutes)+" Minutes (Approx)\n"+"Total Seconds: "+str(age_seconds)+" Seconds (Approx)"+"\n\nYou are "+str(years)+" Years, "+str(months)+" Months, "+str(days)+" Days old",
                bg = "#333",
                fg = "#fff",
                width = 2000).pack(
                anchor = "w")
                
            tk.Message(
                frame_05,
                text = "Total Months: "+str(rem_months)+" Months\nTotal Weeks: "+str(rem_weeks)+" weeks\nTotal Days: "+str(rem_days)+" Days\nTotal Hours: "+str(rem_hours)+" Hours (Approx)\nTotal Minutes: "+str(rem_minutes)+" Minutes (Approx)\nTotal Seconds: "+str(rem_seconds)+" Seconds (Approx)"+"\n\n"+str(rem_months1)+" Months, "+str(rem_days1)+" days remainig for you next birthday",
                bg = "#333",
                fg = "#fff",
                width = 2000).pack(
                anchor = "w")
    except:
        clear_out()
        
        if m1 <= 0 or m1 > 12 or m0 <= 0 or m0 > 12:
            messagebox.showerror(
                "Error",
                "Please Input The Correct Month")
        else:
            messagebox.showerror(
                "Error",
                "An Error Occured\nPlease Check Your Input")

'''
 _____ ____      _    __  __ _____ ____  
|  ___|  _ \    / \  |  \/  | ____/ ___| 
| |_  | |_) |  / _ \ | |\/| |  _| \___ \ 
|  _| |  _ <  / ___ \| |  | | |___ ___) |
|_|   |_| \_\/_/   \_\_|  |_|_____|____/
'''

#===============FRAME 01===============#

frame_01 = tk.LabelFrame(
    root,
    text = "Your Age",
    borderwidth = 2,
    bg = "#333",
    fg = "#fff")

dateFrame = tk.Frame(frame_01, bg = "#333")

#===============FRAME 02===============#

frame_02 = tk.LabelFrame(
    root,
    text = "Date",
    borderwidth = 2,
    bg = "#333",
    fg = "#fff")

ageFrame = tk.Frame(frame_02, bg = "#333")

#===============FRAME 03===============#

frame_03 = tk.Frame(
    root,
    bg = "#333")

#===============FRAME 04===============#

frame_04 = tk.LabelFrame(
    root,
    text = "Your Age",
    borderwidth = 5,
    bg = "#333",
    fg = "#fff")

frame_05 = tk.LabelFrame(
    root,
    text = "Next Birthday",
    borderwidth = 5,
    bg = "#333",
    fg = "#fff")

'''
 _____ _   _ _____ ____  ___ _____ ____  
| ____| \ | |_   _|  _ \|_ _| ____/ ___| 
|  _| |  \| | | | | |_) || ||  _| \___ \ 
| |___| |\  | | | |  _ < | || |___ ___) |
|_____|_| \_| |_| |_| \_\___|_____|____/                                          
'''

#===============ENTRY 01===============#

def temp_text(e):
    global day_clicks
    if day_clicks == 0:
        entry_01.delete(0,"end")
    day_clicks = 1

entry_01 = tk.Entry(
    dateFrame,
    bg = "#444",
    fg = "#fff")

entry_01.insert(0, "Day")
entry_01.bind("<FocusIn>", temp_text)

#===============ENTRY 02===============#

def temp_text(e):
    global month_clicks
    if month_clicks == 0:
        entry_02.delete(0,"end")
    month_clicks = 1
entry_02 = tk.Entry(
    dateFrame,
    bg = "#444",
    fg = "#fff")
entry_02.insert(0, "Month")
entry_02.bind("<FocusIn>", temp_text)

#===============ENTRY 03===============#

def temp_text(e):
    global year_clicks
    if year_clicks == 0:
        entry_03.delete(0,"end")
    year_clicks = 1
entry_03 = tk.Entry(
    dateFrame,
    bg = "#444",
    fg = "#fff")
entry_03.insert(0, "Year")
entry_03.bind("<FocusIn>", temp_text)

#===============ENTRY 04===============#

entry_04 = tk.Entry(
    ageFrame,
    bg = "#444",
    fg = "#fff")
entry_04.insert(0, d0)

#===============ENTRY 05===============#

entry_05 = tk.Entry(
    ageFrame,
    bg = "#444",
    fg = "#fff")
entry_05.insert(0, m0)

#===============ENTRY 06===============#

entry_06 = tk.Entry(
    ageFrame,
    bg = "#444",
    fg = "#fff")
entry_06.insert(0, y0)

'''
 ____  _   _ _____ _____ ___  _   _ ____  
| __ )| | | |_   _|_   _/ _ \| \ | / ___| 
|  _ \| | | | | |   | || | | |  \| \___ \ 
| |_) | |_| | | |   | || |_| | |\  |___) |
|____/ \___/  |_|   |_| \___/|_| \_|____/ 
'''

#===============BUTTON 01===============#

button_01 = tk.Button(
    frame_03,
    text = "Claculate",
    bg = "#444",
    fg = "#fff",
    activebackground = "#555",
    command = text_out)

#===============BUTTON 02===============#

button_02 = tk.Button(
    frame_03,
    text = "Clear All",
    bg = "#444",
    fg = "#fff",
    activebackground = "#555",
    command = clear_out)

'''
 ____   _    ____ _  __     _    _   _ ____     ____ ____  ___ ____  
|  _ \ / \  / ___| |/ /    / \  | \ | |  _ \   / ___|  _ \|_ _|  _ \ 
| |_) / _ \| |   | ' /    / _ \ |  \| | | | | | |  _| |_) || || | | |
|  __/ ___ \ |___| . \   / ___ \| |\  | |_| | | |_| |  _ < | || |_| |
|_| /_/   \_\____|_|\_\ /_/   \_\_| \_|____/   \____|_| \_\___|____/ 
'''

#===============FRAMES===============#

ageFrame.pack()
dateFrame.pack()

frame_02.pack(
    padx = 5,
    pady = 0,
    fill="both")
frame_01.pack(
    padx = 5,
    pady = 0,
    fill="both")
frame_04.pack(
    pady = (5,0),
    padx = 5,
    fill = "both",
    expand = True)
frame_05.pack(
    pady = (0,5),
    padx = 5,
    fill = "both",
    expand = True)
frame_03.pack(pady=5)
frame_04.propagate(0)
frame_05.propagate(0)

#===============ENTRIES===============#

entry_01.pack(side="left", padx=(10, 0), pady=10, fill="x")
entry_02.pack(side="left", padx=(10, 0), pady=10, fill="x")
entry_03.pack(side="left", padx=(10, 0), pady=10, fill="x")
entry_04.pack(side="left", padx=(10, 0), pady=10, fill="x")
entry_05.pack(side="left", padx=(10, 0), pady=10, fill="x")
entry_06.pack(side="left", padx=(10, 0), pady=10, fill="x")

#===============BUTTONS===============#

button_01.pack(side="left", padx=(5, 0))
button_02.pack(side="left", padx=(5, 0))

#===============MAINLOOP===============#

root.mainloop()
