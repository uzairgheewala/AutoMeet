import tkinter as tk
import ctypes
from tkinter import ttk
import pathlib
import time
import sys
from APS import scheduler
from Subs import addjob, deletejob
import six
import packaging
import packaging.version
import packaging.specifiers

path = pathlib.Path("__file__").parent.resolve()
pathstr = str(path) + "\\"

ctypes.windll.shcore.SetProcessDpiAwareness(1)

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
screen_dimensions = str(screen_width) + "x" + str(screen_height)

#root.attributes('-fullscreen',True)
root.geometry(screen_dimensions)
root.title("AutoMeet")
tabControl = ttk.Notebook(root)

current_row = 0
current_col = 0
meeting_num_display = 0
meeting_num_counter = 0

mondaynum = 0
tuesdaynum = 0
wednesdaynum = 0
thursdaynum = 0
fridaynum = 0
saturdaynum = 0
sundaynum = 0

current_tab = ""
lines = []

#Style configuration

white = "#FFFFFF"
black = "#000000"
peach = "#FFE5CC"
red = "#FF0000"
lightgrey = ""
darkgrey = ""

style = ttk.Style(root)
style.theme_create("yammy", parent="alt", settings={
    "TFrame":{"configure": {"background": white, "foreground": black, "borderwidth": 0, "highlightthickness": 0}},
    "TNotebook":{"configure": {"tabmargins": [2, 5, 2, 0], "background": white, "foreground": black}},
    "TNotebook.Tab":{"configure": {"padding": [5, 1], "background":peach, "width": 20},
                     "map": {"background": [("selected", peach)], "expand": [("selected", [1, 1, 1, 0])]}
                    },
    "TButton":{"configure":{"font":("Lato", 8)}}
})
style.theme_use("yammy")

#TABS

Info = ttk.Frame(tabControl)
Monday = ttk.Frame(tabControl)
Tuesday = ttk.Frame(tabControl)
Wednesday = ttk.Frame(tabControl)
Thursday = ttk.Frame(tabControl)
Friday = ttk.Frame(tabControl)
Saturday = ttk.Frame(tabControl)
Sunday = ttk.Frame(tabControl)

Info.configure(width=screen_width, height=screen_height)

all_meetings = []
#DISPLAYMEETINGS FUNCTION

def displayallmeetings(tab):
    
    global all_meetings, mondaynum, mondaynumstr, tuesdaynum, tuesdaynumstr, wednesdaynum, wednesdaynumstr, thursdaynum, thursdaynumstr, fridaynum, fridaynumstr, saturdaynum, saturdaynumstr, sundaynum, sundaynumstr, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, mondaynum, tuesdaynum, wednesdaynum, thursdaynum, fridaynum, saturdaynum, sundaynum
    
    filename = ""
    meetingtext = ""
    datentime = ""
    linenum = 0
    r=0
    col = 0
    meetings = []
    #all_meetings = []
  
    if tab != "Info":
        
        filename = tab + ".txt"
        
        file1 = open(filename, 'r')
        meetings = file1.readlines()
        file1.close()
        
        fileline = ""
        
        for m in range(len(meetings)):
            linenum += 1
            meeting = meetings[linenum-1]
            datetime = meeting[:8]
            meetinglink = meeting[8:]
            
            if datetime == "0":
                meetingtext = "No meetings set for this day"
                datentime = ""
            else:
                datentime = str(int(datetime[3:5])) + " : " + str(int(datetime[6:]))
                meetingtext = "Meeting: " + str(linenum)
            
            if tab == "Monday":
                    
                label_meetingnum = tk.Label(Monday, bg=white, text=meetingtext, font=("Lato", 10), fg=black)
                label_date = tk.Label(Monday, bg=white, text=datentime, font=("Lato", 10), fg=black)
                label_link = tk.Label(Monday, bg=white, text=meetinglink, font=("Lato", 10), fg=black)
                
                all_meetings.append(label_meetingnum)
                all_meetings.append(label_date)
                all_meetings.append(label_link)
                
                label_meetingnum.grid(row=r, column=col, padx=10, pady=10)
                label_date.grid(row=r+1, column=col, padx=10, pady=10)
                label_link.grid(row=r+1, column=col+1, padx=10, pady=10)
            
            elif tab == "Tuesday":
                
                label_meetingnum = tk.Label(Tuesday, bg=white, text=meetingtext, font=("Lato", 10), fg=black)
                label_date = tk.Label(Tuesday, bg=white, text=datentime, font=("Lato", 10), fg=black)
                label_link = tk.Label(Tuesday, bg=white, text=meetinglink, font=("Lato", 10), fg=black)
                
                all_meetings.append(label_meetingnum)
                all_meetings.append(label_date)
                all_meetings.append(label_link)
                
                label_meetingnum.grid(row=r, column=col, padx=10, pady=10)
                label_date.grid(row=r+1, column=col, padx=10, pady=10)
                label_link.grid(row=r+1, column=col+1, padx=10, pady=10)
            
            elif tab == "Wednesday":
                
                label_meetingnum = tk.Label(Wednesday, bg=white, text=meetingtext, font=("Lato", 10), fg=black)
                label_date = tk.Label(Wednesday, bg=white, text=datentime, font=("Lato", 10), fg=black)
                label_link = tk.Label(Wednesday, bg=white, text=meetinglink, font=("Lato", 10), fg=black)
                
                all_meetings.append(label_meetingnum)
                all_meetings.append(label_date)
                all_meetings.append(label_link)
                
                label_meetingnum.grid(row=r, column=col, padx=10, pady=10)
                label_date.grid(row=r+1, column=col, padx=10, pady=10)
                label_link.grid(row=r+1, column=col+1, padx=10, pady=10)
            
            elif tab == "Thursday":
                
                label_meetingnum = tk.Label(Thursday, bg=white, text=meetingtext, font=("Lato", 10), fg=black)
                label_date = tk.Label(Thursday, bg=white, text=datentime, font=("Lato", 10), fg=black)
                label_link = tk.Label(Thursday, bg=white, text=meetinglink, font=("Lato", 10), fg=black)
                
                all_meetings.append(label_meetingnum)
                all_meetings.append(label_date)
                all_meetings.append(label_link)
                
                label_meetingnum.grid(row=r, column=col, padx=10, pady=10)
                label_date.grid(row=r+1, column=col, padx=10, pady=10)
                label_link.grid(row=r+1, column=col+1, padx=10, pady=10)
            
            elif tab == "Friday":
                
                label_meetingnum = tk.Label(Friday, bg=white, text=meetingtext, font=("Lato", 10), fg=black)
                label_date = tk.Label(Friday, bg=white, text=datentime, font=("Lato", 10), fg=black)
                label_link = tk.Label(Friday, bg=white, text=meetinglink, font=("Lato", 10), fg=black)
                
                all_meetings.append(label_meetingnum)
                all_meetings.append(label_date)
                all_meetings.append(label_link)
                
                label_meetingnum.grid(row=r, column=col, padx=10, pady=10)
                label_date.grid(row=r+1, column=col, padx=10, pady=10)
                label_link.grid(row=r+1, column=col+1, padx=10, pady=10)
                
            elif tab == "Saturday":
                
                label_meetingnum = tk.Label(Saturday, bg=white, text=meetingtext, font=("Lato", 10), fg=black)
                label_date = tk.Label(Saturday, bg=white, text=datentime, font=("Lato", 10), fg=black)
                label_link = tk.Label(Saturday, bg=white, text=meetinglink, font=("Lato", 10), fg=black)
                
                all_meetings.append(label_meetingnum)
                all_meetings.append(label_date)
                all_meetings.append(label_link)
                
                label_meetingnum.grid(row=r, column=col, padx=10, pady=10)
                label_date.grid(row=r+1, column=col, padx=10, pady=10)
                label_link.grid(row=r+1, column=col+1, padx=10, pady=10)
                
            elif tab == "Sunday":
                
                label_meetingnum = tk.Label(Sunday, bg=white, text=meetingtext, font=("Lato", 10), fg=black)
                label_date = tk.Label(Sunday, bg=white, text=datentime, font=("Lato", 10), fg=black)
                label_link = tk.Label(Sunday, bg=white, text=meetinglink, font=("Lato", 10), fg=black)
                
                all_meetings.append(label_meetingnum)
                all_meetings.append(label_date)
                all_meetings.append(label_link)
                
                label_meetingnum.grid(row=r, column=col, padx=10, pady=10)
                label_date.grid(row=r+1, column=col, padx=10, pady=10)
                label_link.grid(row=r+1, column=col+1, padx=10, pady=10)
                
            if col >= 4:
                r += 3
                col = 0
            else:
                col += 2
            
        
#TABSWITCH FUNCTION

def on_tab_selected(event):
    
    global current_tab
    
    #Get name of current tab
    selected_tab = event.widget.select()
    tab_text = event.widget.tab(selected_tab, "text")
    
    current_tab = tab_text
    
    displayallmeetings(current_tab)
    
#TABS
    
tabControl.bind("<<NotebookTabChanged>>", on_tab_selected)

tabControl.add(Info, text = 'Info')
tabControl.add(Monday,text = 'Monday')
tabControl.add(Tuesday, text = 'Tuesday')
tabControl.add(Wednesday, text = 'Wednesday')
tabControl.add(Thursday, text = 'Thursday')
tabControl.add(Friday, text = 'Friday')
tabControl.add(Saturday, text = 'Saturday')
tabControl.add(Sunday, text = 'Sunday')

#VARIABLES

dateerroradd1 = tk.StringVar(root)
dateerroradd2 = tk.StringVar(root)
dateerroradd3 = tk.StringVar(root)
dateerroradd4 = tk.StringVar(root)
dateerroradd5 = tk.StringVar(root)
dateerroradd6 = tk.StringVar(root)
dateerroradd7 = tk.StringVar(root)

extraerroradd1 = tk.StringVar(root)
extraerroradd2 = tk.StringVar(root)
extraerroradd3 = tk.StringVar(root)
extraerroradd4 = tk.StringVar(root)
extraerroradd5 = tk.StringVar(root)
extraerroradd6 = tk.StringVar(root)
extraerroradd7 = tk.StringVar(root)

dateerrordel1 = tk.StringVar(root)
dateerrordel2 = tk.StringVar(root)
dateerrordel3 = tk.StringVar(root)
dateerrordel4 = tk.StringVar(root)
dateerrordel5 = tk.StringVar(root)
dateerrordel6 = tk.StringVar(root)
dateerrordel7 = tk.StringVar(root)

extraerrordel1 = tk.StringVar(root)
extraerrordel2 = tk.StringVar(root)
extraerrordel3 = tk.StringVar(root)
extraerrordel4 = tk.StringVar(root)
extraerrordel5 = tk.StringVar(root)
extraerrordel6 = tk.StringVar(root)
extraerrordel7 = tk.StringVar(root)

browsererror1 = tk.StringVar(root)
browsererror2 = tk.StringVar(root)
browsererror3 = tk.StringVar(root)
browsererror4 = tk.StringVar(root)
browsererror5 = tk.StringVar(root)
browsererror6 = tk.StringVar(root)
browsererror7 = tk.StringVar(root)

browserreply = "Please enter a value between 1 and 4"
typereply = "You can do better"
lengthreply = "Check the Info tab"
formatreply = "Please enter it in the correct format"
presencereply = "You didn't enter anything!"
rangereply = "Really?"
doublereply = "You already have a meeting at that time!"
addreply = "This meeting already exists!"
addreply2 = "Meeting successfully added"
delreply = "Meeting wasn't found!"
delreply2 = "Meeting successfully deleted"

validdate = True
validbrowser = True

#VALIDATION FUNCTIONS

def browservalidation(choice):
    
    valid = True
    
    try:
        intchoice = int(choice)
    except ValueError:
        valid = False
    else:
    
        if intchoice != 1 and intchoice != 2 and intchoice != 3 and intchoice != 4 or choice == "":
            valid = False
        
    return valid
        
def datevalidation(choice, file):
    
    valid = True
    double = False
    reason = ""
    l = []
    
    #Presence check
    if choice != "":
        
        #Length check
        if len(choice) == 5:
        
            #Format check
    
            if choice[2] == "/":
    
                #Range checks
    
                try:
                    hr = int(choice.split("/")[0])
                except:
                    valid = False
                    reason = "Type"
                else:
                    minute = int(choice.split("/")[1])
    
                    if hr > 0 and hr < 24 and minute > 0 and minute < 59:
                        
                        #Check if already present
                        with open(file+".txt") as f:
                            l = f.readlines()
                            
                        for L in l:
                            if L[3:8] == choice:
                                double = True
                        if double:
                            valid = False
                            reason = "Double"
                
                    else:
                        valid = False
                        reason = "Range"
                    
            else:
                valid = False
                reason = "Format"
                
        else:
            valid=False
            reason = "Length"
            
    else:
        
        valid = False
        reason = "Presence"
    
    return valid, reason

def clear_frame(frame):
    frame.winfo_children()[18].destroy()

#ADDMEETING FUNCTION

def addmeeting():
    
    global doublereply, addreply, addreply2, browserreply, typereply, lengthreply, rangereply, formatreply, presencereply, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, validdate, validbrowser, date1, date2, date3, date4, date5, date6, date7, browsererror1, browsererror2, browsererror3, browsererror4, browsererror5, browsererror6, browsererror7, dateerroradd1, dateerroradd2, dateerroradd3, dateerroradd4, dateerroradd5, dateerroradd6, dateerroradd7, current_tab, ent_add_date1, ent_add_date2, ent_add_date3, ent_add_date4, ent_add_date5, ent_add_date6, ent_add_date7, ent_add_link1, ent_add_link2, ent_add_link3, ent_add_link4, ent_add_link5, ent_add_link6, ent_add_link7, ent_add_browser1, ent_add_browser2, ent_add_browser3, ent_add_browser4, ent_add_browser5, ent_add_browser6, ent_add_browser7    
    
    filename = ""
    datentime = ""
    meetinglink = ""
    browser = ""
    daystr = ""
    day = 0
    duplicate = False
    
    dateerroradd1.set("")
    dateerroradd2.set("")
    dateerroradd3.set("")
    dateerroradd4.set("")
    dateerroradd5.set("")
    dateerroradd6.set("")
    dateerroradd7.set("")
    
    browsererror1.set("")
    browsererror2.set("")
    browsererror3.set("")
    browsererror4.set("")
    browsererror5.set("")
    browsererror6.set("")
    browsererror7.set("")
    
    extraerroradd1.set("")
    extraerroradd2.set("")
    extraerroradd3.set("")
    extraerroradd4.set("")
    extraerroradd5.set("")
    extraerroradd6.set("")
    extraerroradd7.set("")
    
    if current_tab == "Monday":
        
        meetinglink = ent_add_link1.get()
        #Add tick
        
        
        if browservalidation(ent_add_browser1.get()) == True:
            browser = ent_add_browser1.get()
            validbrowser = True
            #Show tick
        else:
            browsererror1.set(browserreply)
            validbrowser = False
                    
        validdate, check = datevalidation(date1.get(), "Monday")
        
        if validdate == True:
            datentime = ent_add_date1.get()
            datentime = "00/" + datentime
            #Show tick
        else:
            if check == "Format":
                dateerroradd1.set(formatreply)
            elif check == "Presence":
                dateerroradd1.set(presencereply)
            elif check == "Type":
                dateerroradd1.set(typereply)
            elif check == "Range":
                dateerroradd1.set(rangereply)
            elif check == "Length":
                dateerroradd1.set(lengthreply)
            elif check == "Double":
                dateerroradd1.set(doublereply)
        
    elif current_tab == "Tuesday":
        
        meetinglink = ent_add_link2.get()
        
        if browservalidation(ent_add_browser2.get()) == True:
            browser = ent_add_browser2.get()
            validbrowser = True
            #Show tick
        else:
            browsererror2.set(browserreply)
            validbrowser = False
            
        validdate, check = datevalidation(ent_add_date2.get(), "Tuesday")
        
        if validdate == True:
            datentime = ent_add_date2.get()
            datentime = "01/" + datentime
            #Show tick
        else:
            if check == "Format":
                dateerroradd2.set(formatreply)
            elif check == "Presence":
                dateerroradd2.set(presencereply)
            elif check == "Type":
                dateerroradd2.set(typereply)
            elif check == "Range":
                dateerroradd2.set(rangereply)
            elif check == "Length":
                dateerroradd2.set(lengthreply)
            elif check == "Double":
                dateerroradd2.set(doublereply)
    
    elif current_tab == "Wednesday":
        
        meetinglink = ent_add_link3.get()
        
        if browservalidation(ent_add_browser3.get()) == True:
            browser = ent_add_browser3.get()
            validbrowser = True
            #Show tick
        else:
            browsererror3.set(browserreply)
            validbrowser = False
            
        validdate, check = datevalidation(ent_add_date3.get(), "Wednesday")
        
        if validdate == True:
            datentime = ent_add_date3.get()
            datentime = "02/" + datentime
            #Show tick
        else:
            if check == "Format":
                dateerroradd3.set(formatreply)
            elif check == "Presence":
                dateerroradd3.set(presencereply)
            elif check == "Type":
                dateerroradd3.set(typereply)
            elif check == "Range":
                dateerroradd3.set(rangereply)
            elif check == "Length":
                dateerroradd3.set(lengthreply)
            elif check == "Double":
                dateerroradd3.set(doublereply)
        
    elif current_tab == "Thursday":
        
        meetinglink = ent_add_link4.get()
        
        if browservalidation(ent_add_browser4.get()) == True:
            browser = ent_add_browser4.get()
            validbrowser = True
            #Show tick
        else:
            browsererror4.set(browserreply)
            validbrowser = False
            
        validdate, check = datevalidation(ent_add_date4.get(), "Thursday")
        
        if validdate == True:
            datentime = ent_add_date4.get()
            datentime = "03/" + datentime
            #Show tick
        else:
            if check == "Format":
                dateerroradd4.set(formatreply)
            elif check == "Presence":
                dateerroradd4.set(presencereply)
            elif check == "Type":
                dateerroradd4.set(typereply)
            elif check == "Range":
                dateerroradd4.set(rangereply)
            elif check == "Length":
                dateerroradd4.set(lengthreply)
            elif check == "Double":
                dateerroradd4.set(doublereply)
        
    elif current_tab == "Friday":
        
        meetinglink = ent_add_link5.get()
        
        if browservalidation(ent_add_browser5.get()) == True:
            browser = ent_add_browser5.get()
            validbrowser = True
            #Show tick
        else:
            browsererror5.set(browserreply)
            validbrowser = False
            
        validdate, check = datevalidation(ent_add_date5.get(), "Friday")
        
        if validdate == True:
            datentime = ent_add_date5.get()
            datentime = "04/" + datentime
            #Show tick
        else:
            if check == "Format":
                dateerroradd5.set(formatreply)
            elif check == "Presence":
                dateerroradd5.set(presencereply)
            elif check == "Type":
                dateerroradd5.set(typereply)
            elif check == "Range":
                dateerroradd5.set(rangereply)
            elif check == "Length":
                dateerroradd5.set(lengthreply)
            elif check == "Double":
                dateerroradd5.set(doublereply)
        
    elif current_tab == "Saturday":
        
        meetinglink = ent_add_link6.get()
        
        if browservalidation(ent_add_browser6.get()) == True:
            browser = ent_add_browser6.get()
            validbrowser = True
            #Show tick
        else:
            browsererror6.set(browserreply)
            validbrowser = False
            
        validdate, check = datevalidation(ent_add_date6.get(), "Saturday")
        
        if validdate == True:
            datentime = ent_add_date6.get()
            datentime = "05/" + datentime
            #Show tick
        else:
            if check == "Format":
                dateerroradd6.set(formatreply)
            elif check == "Presence":
                dateerroradd6.set(presencereply)
            elif check == "Type":
                dateerroradd6.set(typereply)
            elif check == "Range":
                dateerroradd6.set(rangereply)
            elif check == "Length":
                dateerroradd6.set(lengthreply)
            elif check == "Double":
                dateerroradd6.set(doublereply)
        
    elif current_tab == "Sunday":
        
        meetinglink = ent_add_link7.get()
        
        if browservalidation(ent_add_browser7.get()) == True:
            browser = ent_add_browser7.get()
            validbrowser = True
            #Show tick
        else:
            browsererror7.set(browserreply)
            validbrowser = False
            
        validdate, check = datevalidation(ent_add_date7.get(), "Sunday")
        
        if validdate == True:
            datentime = ent_add_date7.get()
            datentime = "06/" + datentime
            #Show tick
        else:
            if check == "Format":
                dateerroradd7.set(formatreply)
            elif check == "Presence":
                dateerroradd7.set(presencereply)
            elif check == "Type":
                dateerroradd7.set(typereply)
            elif check == "Range":
                dateerroradd7.set(rangereply)
            elif check == "Length":
                dateerroradd7.set(lengthreply)
            elif check == "Double":
                dateerroradd7.set(doublereply)
    
    if validdate == True and validbrowser == True:
    
        #Add to txt file
        daystr = datentime[0:2]
        day = int(daystr)
    
        if day == 0:
            filename = "Monday.txt"
        elif day == 1:
            filename = "Tuesday.txt"
        elif day == 2:
            filename = "Wednesday.txt"
        elif day == 3:
            filename = "Thursday.txt"
        elif day == 4:
            filename = "Friday.txt"
        elif day == 5:
            filename = "Saturday.txt"
        elif day == 6:
            filename = "Sunday.txt"
        
        #Check for Duplicates
        
        with open(filename) as f:
            lines = f.readlines()
    
        fileline = datentime + " " + meetinglink + "\n"
        
        for line in lines:
            if fileline == line:
                duplicate = True
                break
        
        if duplicate == True:
            #Error
            if day == 0:
                extraerroradd1.set(addreply)
            elif day == 1:
                extraerroradd2.set(addreply)
            elif day == 2:
                extraerroradd3.set(addreply)
            elif day == 3:
                extraerroradd4.set(addreply)
            elif day == 4:
                extraerroradd5.set(addreply)
            elif day == 5:
                extraerroradd6.set(addreply)
            elif day == 6:
                extraerroradd7.set(addreply)
        
        else:
    
            if lines[0] == "0":
                f = open(filename, mode='w')
                f.write(fileline)
                f.close()
            else:
                f = open(filename, mode='a')
                f.write(fileline)
                f.close()
        
            #Sort filename
            with open(filename) as f:
                newlines = f.readlines()
            newlines.sort(key=lambda x: x[3:8])
            f = open(filename, mode='w')
            for line in newlines:
                f.write(line)
            f.close()
    
            addjob(datentime, meetinglink, browser)
        
            if day == 0:
                extraerroradd1.set(addreply2)
            elif day == 1:
                extraerroradd2.set(addreply2)
            elif day == 2:
                extraerroradd3.set(addreply2)
            elif day == 3:
                extraerroradd4.set(addreply2)
            elif day == 4:
                extraerroradd5.set(addreply2)
            elif day == 5:
                extraerroradd6.set(addreply2)
            elif day == 6:
                extraerroradd7.set(addreply2)
            
        root.update()
        
        if lines[0] == "0": #Clear no meetings today
        
            if current_tab == "Monday":
                clear_frame(Monday)
            elif current_tab == "Tuesday":
                clear_frame(Tuesday)
            elif current_tab == "Wednesday":
                clear_frame(Wednesday)
            elif current_tab == "Thursday":
                clear_frame(Thursday)
            elif current_tab == "Friday":
                clear_frame(Friday)
            elif current_tab == "Saturday":
                clear_frame(Saturday)
            elif current_tab == "Sunday":
                clear_frame(Sunday)
        
            root.update()
        
            displayallmeetings(current_tab)

#DELETEMEETING FUNCTION

def deletemeeting():
    
    global delreply, delreply2, typereply, lengthreply, rangereply, formatreply, presencereply, extraerrordel1, extraerrordel2, extraerrordel3, extraerrordel4, extraerrordel5, extraerrordel6, extraerrordel7, mondaynumstr, tuesdaynumstr, wednesdaynumstr, thursdaynumstr, fridaynumstr, saturdaynumstr, sundaynumstr, dateerrordel1, dateerrordel2, dateerrordel3, dateerrordel4, dateerrordel5, dateerrordel6, dateerrordel7, current_tab, ent_del_date1, ent_del_date2, ent_del_date3, ent_del_date4, ent_del_date5, ent_del_date6, ent_del_date7
    
    day = 0
    daystr = ""
    datentime = ""
    filename = ""
    check = ""
    delcheck = ""
    meetingfound = False
    onemeeting = False
    
    dateerrordel1.set("")
    dateerrordel2.set("")
    dateerrordel3.set("")
    dateerrordel4.set("")
    dateerrordel5.set("")
    dateerrordel6.set("")
    dateerrordel7.set("")
    
    extraerrordel1.set("")
    extraerrordel2.set("")
    extraerrordel3.set("")
    extraerrordel4.set("")
    extraerrordel5.set("")
    extraerrordel6.set("")
    extraerrordel7.set("")

    if current_tab == "Monday":
        
        #delcheck = mondaynumstr.get()
        
        validdate, check = datevalidation(ent_del_date1.get(), "Monday")
        
        if validdate == True:
            datentime = ent_del_date1.get()
            datentime = "00/"+datentime 
            #Show tick
            
        else:
            if check == "Format":
                dateerrordel1.set(formatreply)
            elif check == "Presence":
                dateerrordel1.set(presencereply)
            elif check == "Type":
                dateerrordel1.set(typereply)
            elif check == "Range":
                dateerrordel1.set(rangereply)
            elif check == "Length":
                dateerrordel1.set(lengthreply)
            elif check == "Double":
                validdate = True
                datentime = ent_del_date1.get()
                datentime = "00/"+datentime
        
    elif current_tab == "Tuesday":
        
        #delcheck = tuesdaynumstr.get()
        
        validdate, check = datevalidation(ent_del_date2.get(), "Tuesday")
        
        if validdate == True:
            datentime = ent_del_date2.get()
            datentime = "01/"+datentime 
            #Show tick
            
        else:
            if check == "Format":
                dateerrordel2.set(formatreply)
            elif check == "Presence":
                dateerrordel2.set(presencereply)
            elif check == "Type":
                dateerrordel2.set(typereply)
            elif check == "Range":
                dateerrordel2.set(rangereply)
            elif check == "Length":
                dateerrordel2.set(lengthreply)
            elif check == "Double":
                validdate = True
                datentime = ent_del_date2.get()
                datentime = "01/"+datentime
    
    elif current_tab == "Wednesday":
        
        #delcheck = wednesdaynumstr.get()
        
        validdate, check = datevalidation(ent_del_date3.get(), "Wednesday")
        
        if validdate == True:
            datentime = ent_del_date3.get()
            datentime = "02/"+datentime 
            #Show tick
            
        else:
            if check == "Format":
                dateerrordel3.set(formatreply)
            elif check == "Presence":
                dateerrordel3.set(presencereply)
            elif check == "Type":
                dateerrordel3.set(typereply)
            elif check == "Range":
                dateerrordel3.set(rangereply)
            elif check == "Length":
                dateerrordel3.set(lengthreply)
            elif check == "Double":
                validdate = True
                datentime = ent_del_date3.get()
                datentime = "02/"+datentime
        
    elif current_tab == "Thursday":
        
       # delcheck = thursdaynumstr.get()
        
        validdate, check = datevalidation(ent_del_date4.get(), "Thursday")
        
        if validdate == True:
            datentime = ent_del_date4.get()
            datentime = "03/"+datentime 
            #Show tick
            
        else:
            if check == "Format":
                dateerrordel4.set(formatreply)
            elif check == "Presence":
                dateerrordel4.set(presencereply)
            elif check == "Type":
                dateerrordel4.set(typereply)
            elif check == "Range":
                dateerrordel4.set(rangereply)
            elif check == "Length":
                dateerrordel4.set(lengthreply)
            elif check == "Double":
                validdate = True
                datentime = ent_del_date4.get()
                datentime = "03/"+datentime
                
    elif current_tab == "Friday":
        
        #delcheck = fridaynumstr.get()
        
        validdate, check = datevalidation(ent_del_date5.get(), "Friday")
        
        if validdate == True:
            datentime = ent_del_date5.get()
            datentime = "04/"+datentime 
            #Show tick
            
        else:
            if check == "Format":
                dateerrordel5.set(formatreply)
            elif check == "Presence":
                dateerrordel5.set(presencereply)
            elif check == "Type":
                dateerrordel5.set(typereply)
            elif check == "Range":
                dateerrordel5.set(rangereply)
            elif check == "Length":
                dateerrordel5.set(lengthreply)
            elif check == "Double":
                validdate = True
                datentime = ent_del_date5.get()
                datentime = "04/"+datentime
        
    elif current_tab == "Saturday":
        
        #delcheck = saturdaynumstr.get()
        
        validdate, check = datevalidation(ent_del_date6.get(), "Saturday")
        
        if validdate == True:
            datentime = ent_del_date6.get()
            datentime = "05/"+datentime 
            #Show tick
            
        else:
            if check == "Format":
                dateerrordel6.set(formatreply)
            elif check == "Presence":
                dateerrordel6.set(presencereply)
            elif check == "Type":
                dateerrordel6.set(typereply)
            elif check == "Range":
                dateerrordel6.set(rangereply)
            elif check == "Length":
                dateerrordel6.set(lengthreply)
            elif check == "Double":
                validdate = True
                datentime = ent_del_date6.get()
                datentime = "05/"+datentime
        
    elif current_tab == "Sunday":
        
        #delcheck = sundaynumstr.get()
        
        validdate, check = datevalidation(ent_del_date7.get(), "Sunday")
        
        if validdate == True:
            datentime = ent_del_date7.get()
            datentime = "06/"+datentime 
            #Show tick
            
        else:
            if check == "Format":
                dateerrordel7.set(formatreply)
            elif check == "Presence":
                dateerrordel7.set(presencereply)
            elif check == "Type":
                dateerrordel7.set(typereply)
            elif check == "Range":
                dateerrordel7.set(rangereply)
            elif check == "Length":
                dateerrordel7.set(lengthreply)
            elif check == "Double":
                validdate = True
                datentime = ent_del_date7.get()
                datentime = "06/"+datentime 
    
    if validdate == True: 
        daystr = datentime[0:2]
        day = int(daystr)
    
        if day == 0:
            filename = "Monday.txt"
        elif day == 1:
            filename = "Tuesday.txt"
        elif day == 2:
            filename = "Wednesday.txt"
        elif day == 3:
            filename = "Thursday.txt"
        elif day == 4:
            filename = "Friday.txt"
        elif day == 5:
            filename = "Saturday.txt"
        elif day == 6:
            filename = "Sunday.txt"
    
        with open(filename, "r") as f:
            lines = f.readlines()
            
        if len(lines) == 1:
            onemeeting = True
            
        for line in lines:
            if line[0:8] == datentime:
                meetingfound = True
        
        if meetingfound == False:
            #Error
            if day == 0:
                extraerrordel1.set(delreply)
            elif day == 1:
                extraerrordel2.set(delreply)
            elif day == 2:
                extraerrordel3.set(delreply)
            elif day == 3:
                extraerrordel4.set(delreply)
            elif day == 4:
                extraerrordel5.set(delreply)
            elif day == 5:
                extraerrordel6.set(delreply)
            elif day == 6:
                extraerrordel7.set(delreply)
            
        else:
        
            with open(filename, "w") as f:
                if onemeeting == False:
                    for line in lines:
                        if line[0:8] != datentime:
                            f.write(line)
                else:
                    f.write("0")
                    
            with open(filename, "w") as f:
                if len(f.readlines()) == 0:
                    f.write("0")
                
            deletejob(datentime)
            
            #Delete the record in all_meetings
            
            if day == 0:
                extraerrordel1.set(delreply2)
            elif day == 1:
                extraerrordel2.set(delreply2)
            elif day == 2:
                extraerrordel3.set(delreply2)
            elif day == 3:
                extraerrordel4.set(delreply2)
            elif day == 4:
                extraerrordel5.set(delreply2)
            elif day == 5:
                extraerrordel6.set(delreply2)
            elif day == 6:
                extraerrordel7.set(delreply2)
            
        root.update()
    
#WIDGETS FOR ADD MEETINGS

addmeetingtxt = "Add Meeting"
delmeetingtxt = "Delete Meeting"
datetxt = "Enter the meeting time:"
btntext = "Confirm"
meetingtxt = "Enter the meeting link:"
browsertxt = "Enter your browser choice:"
    
#Monday
date1 = tk.StringVar(root)
link1 = tk.StringVar(root)
browser1 = tk.StringVar(root)

label_addmeeting1 = tk.Label(Monday, bg=white, text = addmeetingtxt, font=("Lato", 10))
btn_add1 = tk.Button(Monday, text = btntext, command=addmeeting)
label_add_date1 = tk.Label(Monday, bg=white, text = datetxt, font=("Lato", 10))
label_add_link1 = tk.Label(Monday, bg=white, text = meetingtxt, font=("Lato", 10))
label_add_error1 = tk.Label(Monday, bg=white, font=("Lato", 10), textvariable=extraerroradd1, fg=red)
label_add_browser1 = tk.Label(Monday, bg=white, text = browsertxt, font=("Lato", 10))
label_add_datecheck1 = tk.Label(Monday, bg=white, font=("Lato", 8), textvariable=dateerroradd1, fg=red)
label_add_browsercheck1 = tk.Label(Monday, bg=white, font=("Lato", 8), textvariable=browsererror1, fg=red)
ent_add_date1 = tk.Entry(Monday, textvariable=date1)
ent_add_link1 = tk.Entry(Monday, textvariable=link1)
ent_add_browser1 = tk.Entry(Monday, textvariable=browser1)

#label_add_datetick1 = tk.Label(Monday, image = tick)
#label_add_datetick1.image = tick

#ent_add_date1.bind("<Return>", on_change)
#ent_add_link1.bind("<Return>", on_change)
#ent_add_browser1.bind("<Return>", on_change)

label_addmeeting1.grid(row=100, column=1, padx=15, pady=15)
label_add_date1.grid(row=103, column=0, padx=15, pady=15)
label_add_link1.grid(row=104, column=0, padx=15, pady=15)
label_add_error1.grid(row=104, column=2, padx=15, pady=15)
label_add_browser1.grid(row=108, column=0, padx=15, pady=15)
label_add_datecheck1.grid(row=102, column=1, padx=15, pady=15)
ent_add_date1.grid(row=103, column=1, padx=15, pady=15)
ent_add_link1.grid(row=104, column=1, padx=15, pady=15)
label_add_browsercheck1.grid(row=107, column=1, padx=15, pady=15)
ent_add_browser1.grid(row=108, column=1, padx=15, pady=15)
btn_add1.grid(row=110, column=0, padx=15, pady=15)

#Tuesday
date2 = tk.StringVar(root)
link2 = tk.StringVar(root)
browser2 = tk.StringVar(root)

label_addmeeting2 = tk.Label(Tuesday, bg=white, text = addmeetingtxt, font=("Lato", 10))
btn_add2 = tk.Button(Tuesday, text = btntext, command=addmeeting)
label_add_date2 = tk.Label(Tuesday, bg=white, text = datetxt, font=("Lato", 10))
label_add_link2 = tk.Label(Tuesday, bg=white, text = meetingtxt, font=("Lato", 10))
label_add_error2 = tk.Label(Tuesday, bg=white, font=("Lato", 10), textvariable=extraerroradd2, fg=red)
label_add_browser2 = tk.Label(Tuesday, bg=white, text = browsertxt, font=("Lato", 10))
label_add_datecheck2 = tk.Label(Tuesday, bg=white, font=("Lato", 8), textvariable=dateerroradd2, fg=red)
label_add_browsercheck2 = tk.Label(Tuesday, bg=white, font=("Lato", 8), textvariable=browsererror2, fg=red)
ent_add_date2 = tk.Entry(Tuesday, textvariable=date2)
ent_add_link2 = tk.Entry(Tuesday, textvariable=link2)
ent_add_browser2 = tk.Entry(Tuesday, textvariable=browser2)

#ent_add_date2.bind("<Return>", ent_add_date2.get())
#ent_add_link2.bind("<Return>", ent_add_link2.get())
#ent_add_browser2.bind("<Return>", ent_add_browser2.get())

label_addmeeting2.grid(row=100, column=1, padx=15, pady=15)
label_add_date2.grid(row=103, column=0, padx=15, pady=15)
label_add_link2.grid(row=104, column=0, padx=15, pady=15)
label_add_error2.grid(row=104, column=2, padx=15, pady=15)
label_add_browser2.grid(row=108, column=0, padx=15, pady=15)
label_add_datecheck2.grid(row=102, column=1, padx=15, pady=15)
ent_add_date2.grid(row=103, column=1, padx=15, pady=15)
ent_add_link2.grid(row=104, column=1, padx=15, pady=15)
label_add_browsercheck2.grid(row=107, column=1, padx=15, pady=15)
ent_add_browser2.grid(row=108, column=1, padx=15, pady=15)
btn_add2.grid(row=110, column=0, padx=15, pady=15)

#Wednesday
date3 = tk.StringVar(root)
link3 = tk.StringVar(root)
browser3 = tk.StringVar(root)

label_addmeeting3 = tk.Label(Wednesday, bg=white, text = addmeetingtxt, font=("Lato", 10))
btn_add3 = tk.Button(Wednesday, text = btntext, command=addmeeting)
label_add_date3 = tk.Label(Wednesday, bg=white, text = datetxt, font=("Lato", 10))
label_add_link3 = tk.Label(Wednesday, bg=white, text = meetingtxt, font=("Lato", 10))
label_add_error3 = tk.Label(Wednesday, bg=white, font=("Lato", 10), textvariable=extraerroradd3, fg=red)
label_add_browser3 = tk.Label(Wednesday, bg=white, text = browsertxt, font=("Lato", 10))
label_add_datecheck3 = tk.Label(Wednesday, bg=white, font=("Lato", 8), textvariable=dateerroradd3, fg=red)
label_add_browsercheck3 = tk.Label(Wednesday, bg=white, font=("Lato", 8), textvariable=browsererror3, fg=red)
ent_add_date3 = tk.Entry(Wednesday, textvariable=date3)
ent_add_link3 = tk.Entry(Wednesday, textvariable=link3)
ent_add_browser3 = tk.Entry(Wednesday, textvariable=browser3)

#ent_add_date3.bind("<Return>", ent_add_date3.get())
#ent_add_link3.bind("<Return>", ent_add_link3.get())
#ent_add_browser3.bind("<Return>", ent_add_browser3.get())

label_addmeeting3.grid(row=100, column=1, padx=15, pady=15)
label_add_date3.grid(row=103, column=0, padx=15, pady=15)
label_add_link3.grid(row=104, column=0, padx=15, pady=15)
label_add_error3.grid(row=104, column=2, padx=15, pady=15)
label_add_browser3.grid(row=108, column=0, padx=15, pady=15)
label_add_datecheck3.grid(row=102, column=1, padx=15, pady=15)
ent_add_date3.grid(row=103, column=1, padx=15, pady=15)
ent_add_link3.grid(row=104, column=1, padx=15, pady=15)
label_add_browsercheck3.grid(row=107, column=1, padx=15, pady=15)
ent_add_browser3.grid(row=108, column=1, padx=15, pady=15)
btn_add3.grid(row=110, column=0, padx=15, pady=15)

#Thursday
date4 = tk.StringVar(root)
link4 = tk.StringVar(root)
browser4 = tk.StringVar(root)

label_addmeeting4 = tk.Label(Thursday,  bg=white,text = addmeetingtxt, font=("Lato", 10))
btn_add4 = tk.Button(Thursday, text = btntext, command=addmeeting)
label_add_date4 = tk.Label(Thursday, bg=white, text = datetxt, font=("Lato", 10))
label_add_link4 = tk.Label(Thursday, bg=white, text = meetingtxt, font=("Lato", 10))
label_add_error4 = tk.Label(Thursday, bg=white, font=("Lato", 10), textvariable=extraerroradd4, fg=red)
label_add_browser4 = tk.Label(Thursday, bg=white, text = browsertxt, font=("Lato", 10))
label_add_datecheck4 = tk.Label(Thursday, bg=white, font=("Lato", 8), textvariable=dateerroradd4, fg=red)
label_add_browsercheck4 = tk.Label(Thursday, bg=white, font=("Lato", 8), textvariable=browsererror4, fg=red)
ent_add_date4 = tk.Entry(Thursday, textvariable=date4)
ent_add_link4 = tk.Entry(Thursday, textvariable=link4)
ent_add_browser4 = tk.Entry(Thursday, textvariable=browser4)

#ent_add_date4.bind("<Return>", ent_add_date4.get())
#ent_add_link4.bind("<Return>", ent_add_link4.get())
#ent_add_browser4.bind("<Return>", ent_add_browser4.get())

label_addmeeting4.grid(row=100, column=1, padx=15, pady=15)
label_add_date4.grid(row=103, column=0, padx=15, pady=15)
label_add_link4.grid(row=104, column=0, padx=15, pady=15)
label_add_error4.grid(row=104, column=2, padx=15, pady=15)
label_add_browser4.grid(row=108, column=0, padx=15, pady=15)
label_add_datecheck4.grid(row=102, column=1, padx=15, pady=15)
ent_add_date4.grid(row=103, column=1, padx=15, pady=15)
ent_add_link4.grid(row=104, column=1, padx=15, pady=15)
label_add_browsercheck4.grid(row=107, column=1, padx=15, pady=15)
ent_add_browser4.grid(row=108, column=1, padx=15, pady=15)
btn_add4.grid(row=110, column=0, padx=15, pady=15)

#Friday
date5 = tk.StringVar(root)
link5 = tk.StringVar(root)
browser5 = tk.StringVar(root)

label_addmeeting5 = tk.Label(Friday, bg=white, text = addmeetingtxt, font=("Lato", 10))
btn_add5 = tk.Button(Friday, text = btntext, command=addmeeting)
label_add_date5 = tk.Label(Friday, bg=white, text = datetxt, font=("Lato", 10))
label_add_link5 = tk.Label(Friday, bg=white, text = meetingtxt, font=("Lato", 10))
label_add_error5 = tk.Label(Friday, bg=white, font=("Lato", 10), textvariable=extraerroradd5, fg=red)
label_add_browser5 = tk.Label(Friday, bg=white, text = browsertxt, font=("Lato", 10))
label_add_datecheck5 = tk.Label(Friday, bg=white, font=("Lato", 8), textvariable=dateerroradd5, fg=red)
label_add_browsercheck5 = tk.Label(Friday, bg=white, font=("Lato", 8), textvariable=browsererror5, fg=red)
ent_add_date5 = tk.Entry(Friday, textvariable=date5)
ent_add_link5 = tk.Entry(Friday, textvariable=link5)
ent_add_browser5 = tk.Entry(Friday, textvariable=browser5)

#ent_add_date5.bind("<Return>", on_change)
#ent_add_link5.bind("<Return>", on_change)
#ent_add_browser5.bind("<Return>", on_change)

label_addmeeting5.grid(row=100, column=1, padx=15, pady=15)
label_add_date5.grid(row=103, column=0, padx=15, pady=15)
label_add_link5.grid(row=104, column=0, padx=15, pady=15)
label_add_error5.grid(row=104, column=2, padx=15, pady=15)
label_add_browser5.grid(row=108, column=0, padx=15, pady=15)
label_add_datecheck5.grid(row=102, column=1, padx=15, pady=15)
ent_add_date5.grid(row=103, column=1, padx=15, pady=15)
ent_add_link5.grid(row=104, column=1, padx=15, pady=15)
label_add_browsercheck5.grid(row=107, column=1, padx=15, pady=15)
ent_add_browser5.grid(row=108, column=1, padx=15, pady=15)
btn_add5.grid(row=110, column=0, padx=15, pady=15)

#Saturday
date6 = tk.StringVar(root)
link6 = tk.StringVar(root)
browser6 = tk.StringVar(root)

label_addmeeting6 = tk.Label(Saturday, bg=white, text = addmeetingtxt, font=("Lato", 10))
btn_add6 = tk.Button(Saturday, text = btntext, command=addmeeting)
label_add_date6 = tk.Label(Saturday, bg=white, text = datetxt, font=("Lato", 10))
label_add_link6 = tk.Label(Saturday, bg=white, text = meetingtxt, font=("Lato", 10))
label_add_error6 = tk.Label(Saturday, bg=white, font=("Lato", 10), textvariable=extraerroradd6, fg=red)
label_add_browser6 = tk.Label(Saturday, bg=white, text = browsertxt, font=("Lato", 10))
label_add_datecheck6 = tk.Label(Saturday, bg=white, font=("Lato", 8), textvariable=dateerroradd6, fg=red)
label_add_browsercheck6 = tk.Label(Saturday, bg=white, font=("Lato", 8), textvariable=browsererror6, fg=red)
ent_add_date6 = tk.Entry(Saturday, textvariable=date6)
ent_add_link6 = tk.Entry(Saturday, textvariable=link6)
ent_add_browser6 = tk.Entry(Saturday, textvariable=browser6)

#ent_add_date6.bind("<Return>", ent_add_date6.get())
#ent_add_link6.bind("<Return>", ent_add_link6.get())
#ent_add_browser6.bind("<Return>", ent_add_browser6.get())

label_addmeeting6.grid(row=100, column=1, padx=15, pady=15)
label_add_date6.grid(row=103, column=0, padx=15, pady=15)
label_add_link6.grid(row=104, column=0, padx=15, pady=15)
label_add_error6.grid(row=104, column=3, padx=15, pady=15)
label_add_browser6.grid(row=108, column=0, padx=15, pady=15)
label_add_datecheck6.grid(row=102, column=1, padx=15, pady=15)
ent_add_date6.grid(row=103, column=1, padx=15, pady=15)
ent_add_link6.grid(row=104, column=1, padx=15, pady=15)
label_add_browsercheck6.grid(row=107, column=1, padx=15, pady=15)
ent_add_browser6.grid(row=108, column=1, padx=15, pady=15)
btn_add6.grid(row=110, column=0, padx=15, pady=15)

#Sunday
date7 = tk.StringVar(root)
link7 = tk.StringVar(root)
browser7 = tk.StringVar(root)

label_addmeeting7 = tk.Label(Sunday, bg=white, text = addmeetingtxt, font=("Lato", 10))
btn_add7 = tk.Button(Sunday, text = btntext, command=addmeeting)
label_add_date7 = tk.Label(Sunday, bg=white, text = datetxt, font=("Lato", 10))
label_add_link7 = tk.Label(Sunday, bg=white, text = meetingtxt, font=("Lato", 10))
label_add_error7 = tk.Label(Sunday, bg=white, font=("Lato", 10), textvariable=extraerroradd7, fg=red)
label_add_browser7 = tk.Label(Sunday, bg=white, text = browsertxt, font=("Lato", 10))
label_add_datecheck7 = tk.Label(Sunday, bg=white, font=("Lato", 8), textvariable=dateerroradd7, fg=red)
label_add_browsercheck7 = tk.Label(Sunday, bg=white, font=("Lato", 8), textvariable=browsererror7, fg=red)
ent_add_date7 = tk.Entry(Sunday, textvariable=date7)
ent_add_link7 = tk.Entry(Sunday, textvariable=link7)
ent_add_browser7 = tk.Entry(Sunday, textvariable=browser7)

#ent_add_date7.bind("<Return>", ent_add_date7.get())
#ent_add_link7.bind("<Return>", ent_add_link7.get())
#ent_add_browser7.bind("<Return>", ent_add_browser7.get())

label_addmeeting7.grid(row=100, column=1, padx=15, pady=15)
label_add_date7.grid(row=103, column=0, padx=15, pady=15)
label_add_link7.grid(row=104, column=0, padx=15, pady=15)
label_add_error7.grid(row=104, column=2, padx=15, pady=15)
label_add_browser7.grid(row=108, column=0, padx=15, pady=15)
label_add_datecheck7.grid(row=102, column=1, padx=15, pady=15)
ent_add_date7.grid(row=103, column=1, padx=15, pady=15)
ent_add_link7.grid(row=104, column=1, padx=15, pady=15)
label_add_browsercheck7.grid(row=107, column=1, padx=15, pady=15)
ent_add_browser7.grid(row=108, column=1, padx=15, pady=15)
btn_add7.grid(row=110, column=0, padx=15, pady=15)

#ADD WIDGETS FOR DELETE MEETINGS

#Monday
label_delmeeting1 = tk.Label(Monday, bg=white, font=("Lato", 10), text = delmeetingtxt)
label_del_date1 = tk.Label(Monday, bg=white, font=("Lato", 10), text = datetxt)
label_del_error1 = tk.Label(Monday, bg=white, font=("Lato", 10), textvariable=extraerrordel1, fg=red)
label_del_datecheck1 = tk.Label(Monday, bg=white, font=("Lato", 8), textvariable=dateerrordel1, fg=red)
btn_del1 = tk.Button(Monday, text = btntext, command=deletemeeting)
ent_del_date1 = tk.Entry(Monday)

label_delmeeting1.grid(row=115, column=1, padx=15, pady=15)
label_del_date1.grid(row=118, column=0, padx=15, pady=15)
label_del_error1.grid(row=118, column=2, padx=15, pady=15)
label_del_datecheck1.grid(row=117, column=1, padx=15, pady=15)
ent_del_date1.grid(row=118, column=1, padx=15, pady=15)
btn_del1.grid(row=120, column=0, padx=15, pady=15)

#Tuesday
label_delmeeting2 = tk.Label(Tuesday, bg=white, font=("Lato", 10), text = delmeetingtxt)
btn_del2 = tk.Button(Tuesday, text = btntext, command=deletemeeting)
label_del_date2 = tk.Label(Tuesday, bg=white, font=("Lato", 10), text = datetxt)
label_del_error2 = tk.Label(Tuesday, bg=white, font=("Lato", 10), textvariable=extraerrordel2, fg=red)
label_del_datecheck2 = tk.Label(Tuesday, bg=white, font=("Lato", 8), textvariable=dateerrordel2, fg=red)
ent_del_date2 = tk.Entry(Tuesday)

label_delmeeting2.grid(row=115, column=1, padx=15, pady=15)
label_del_date2.grid(row=118, column=0, padx=15, pady=15)
label_del_error2.grid(row=118, column=2, padx=15, pady=15)
label_del_datecheck2.grid(row=117, column=1, padx=15, pady=15)
ent_del_date2.grid(row=118, column=1, padx=15, pady=15)
btn_del2.grid(row=120, column=0, padx=15, pady=15)

#Wednesday
label_delmeeting3 = tk.Label(Wednesday, bg=white, font=("Lato", 10), text = delmeetingtxt)
btn_del3 = tk.Button(Wednesday, text = btntext, command=deletemeeting)
label_del_date3 = tk.Label(Wednesday, bg=white, font=("Lato", 10), text = datetxt)
label_del_error3 = tk.Label(Wednesday, bg=white, font=("Lato", 10), textvariable=extraerrordel3, fg=red)
label_del_datecheck3 = tk.Label(Wednesday, bg=white, font=("Lato", 8), textvariable=dateerrordel3, fg=red)
ent_del_date3 = tk.Entry(Wednesday)

label_delmeeting3.grid(row=115, column=1, padx=15, pady=15)
label_del_date3.grid(row=118, column=0, padx=15, pady=15)
label_del_error3.grid(row=118, column=2, padx=15, pady=15)
label_del_datecheck3.grid(row=117, column=1, padx=15, pady=15)
ent_del_date3.grid(row=118, column=1, padx=15, pady=15)
btn_del3.grid(row=120, column=0, padx=15, pady=15)

#Thursday
label_delmeeting4 = tk.Label(Thursday, bg=white, font=("Lato", 10), text = delmeetingtxt)
btn_del4 = tk.Button(Thursday, text = btntext, command=deletemeeting)
label_del_date4 = tk.Label(Thursday, bg=white, font=("Lato", 10), text = datetxt)
label_del_error4 = tk.Label(Thursday, bg=white, font=("Lato", 10), textvariable=extraerrordel4, fg=red)
label_del_datecheck4 = tk.Label(Thursday, bg=white, font=("Lato", 8), textvariable=dateerrordel4, fg=red)
ent_del_date4 = tk.Entry(Thursday)

label_delmeeting4.grid(row=115, column=1, padx=15, pady=15)
label_del_date4.grid(row=118, column=0, padx=15, pady=15)
label_del_error4.grid(row=118, column=2, padx=15, pady=15)
label_del_datecheck4.grid(row=117, column=1, padx=15, pady=15)
ent_del_date4.grid(row=118, column=1, padx=15, pady=15)
btn_del4.grid(row=120, column=0, padx=15, pady=15)

#Friday
label_delmeeting5 = tk.Label(Friday, bg=white, font=("Lato", 10), text = delmeetingtxt)
btn_del5 = tk.Button(Friday, text = btntext, command=deletemeeting)
label_del_date5 = tk.Label(Friday, bg=white, font=("Lato", 10), text = datetxt)
label_del_error5 = tk.Label(Friday, bg=white, font=("Lato", 10), textvariable=extraerrordel5, fg=red)
label_del_datecheck5 = tk.Label(Friday, bg=white, font=("Lato", 8), textvariable=dateerrordel5, fg=red)
ent_del_date5 = tk.Entry(Friday)

label_delmeeting5.grid(row=115, column=1, padx=15, pady=15)
label_del_date5.grid(row=118, column=0, padx=15, pady=15)
label_del_error5.grid(row=118, column=2, padx=15, pady=15)
label_del_datecheck5.grid(row=117, column=1, padx=15, pady=15)
ent_del_date5.grid(row=118, column=1, padx=15, pady=15)
btn_del5.grid(row=120, column=0, padx=15, pady=15)

#Saturday
label_delmeeting6 = tk.Label(Saturday, bg=white, font=("Lato", 10), text = delmeetingtxt)
btn_del6 = tk.Button(Saturday, text = btntext, command=deletemeeting)
label_del_date6 = tk.Label(Saturday, bg=white, font=("Lato", 10), text = datetxt)
label_del_error6 = tk.Label(Saturday, bg=white, font=("Lato", 10), textvariable=extraerrordel6, fg=red)
label_del_datecheck6 = tk.Label(Saturday, bg=white, font=("Lato", 8), textvariable=dateerrordel6, fg=red)
ent_del_date6 = tk.Entry(Saturday)

label_delmeeting6.grid(row=115, column=1, padx=15, pady=15)
label_del_date6.grid(row=118, column=0, padx=15, pady=15)
label_del_error6.grid(row=118, column=3, padx=15, pady=15)
label_del_datecheck6.grid(row=117, column=1, padx=15, pady=15)
ent_del_date6.grid(row=118, column=1, padx=15, pady=15)
btn_del6.grid(row=120, column=0, padx=15, pady=15)

#Sunday
label_delmeeting7 = tk.Label(Sunday, bg=white, font=("Lato", 10), text = delmeetingtxt)
btn_del7 = tk.Button(Sunday, text = btntext, command=deletemeeting)
label_del_date7 = tk.Label(Sunday, bg=white, font=("Lato", 10), text = datetxt)
label_del_error7 = tk.Label(Sunday, bg=white, font=("Lato", 10), textvariable=extraerrordel7, fg=red)
label_del_datecheck7 = tk.Label(Sunday, bg=white, font=("Lato", 8), textvariable=dateerrordel7, fg=red)
ent_del_date7 = tk.Entry(Sunday)

label_delmeeting7.grid(row=115, column=1, padx=15, pady=15)
label_del_date7.grid(row=118, column=0, padx=15, pady=15)
label_del_error7.grid(row=118, column=2, padx=15, pady=15)
label_del_datecheck7.grid(row=117, column=1, padx=15, pady=15)
ent_del_date7.grid(row=118, column=1, padx=15, pady=15)
btn_del7.grid(row=120, column=0, padx=15, pady=15)

#WIDGETS FOR INFO

tzerror = tk.StringVar(root)

def validtz(entry):
    v = False
    if len(entry) >= 7 and len(entry) <= 10:
        if entry[0:7] == "Etc/GMT":
            if entry[7] == "+" or entry[7] == "-":
                if int(entry[8:]) >= 0 and int(entry[8:]) <= 14:
                    v = True
                    
    return v

def settimezone():
    global scheduler, tzerror
    
    # Validate input
    t = ent_timezone.get()
    valid = validtz(t)
    if valid == False:
        tzerror.set("Invalid timezone entered")
    else:
        tz = t
        job = ""
    
        # Delete all jobs
        jn = len(scheduler.get_jobs())
        if jn > 0:
            for i in range(0, jn-1):
                job = scheduler.get_jobs()[i].id
                filename = job + ".bat"
                if os.path.exists(filename):
                    os.remove(filename)
                scheduler.remove_job(job)
            
        with open("Monday.txt", "w") as g:
            g.write("0")
        with open("Tuesday.txt", "w") as g:
            g.write("0")
        with open("Wednesday.txt", "w") as g:
            g.write("0")
        with open("Thursday.txt", "w") as g:
            g.write("0")
        with open("Friday.txt", "w") as g:
            g.write("0")
        with open("Saturday.txt", "w") as g:
            g.write("0")
        with open("Sunday.txt", "w") as g:
            g.write("0")
    
        # Save new timezone
        with open("Timezone.txt", "w") as f:
            f.write(tz)
        
        tzerror.set("Timezone successfully changed")
        
        # Restart app
        python = sys.executable
        os.execl(python, python, * sys.argv)

daterule = "Please enter the date and time of your meeting in the format: hr/mm\nWhere hr is in 24 hour format."
dateruleex = "Eg. 11:26 pm -> 23/26"
browserrule = "When prompted to choose which browser you'd like to launch the meeting from:\n\nPlease enter 1 for Google Chrome, 2 for Microsoft Edge, 3 for Firefox and 4 for Internet Explorer"
timezonerule = "Please enter your timezone in the format: Etc/GMTx where x is any number between -14 and +12\n"
timezonewarning = "Please keep in mind that this action will delete all of your previously set meetings"

label_date = tk.Label(Info, bg=white, text="Date and time:", font=("Lato", 10), fg=black, justify="left")
label_browser = tk.Label(Info, bg=white, text="Browser:", font=("Lato", 10), fg=black, justify="left")
label_timezone = tk.Label(Info, bg=white, text="Timezone:", font=("Lato", 10), fg=black, justify="left")
label_rule_date = tk.Label(Info, bg=white, text=daterule, font=("Lato", 10), fg=black, justify="left")
label_rule_dateex = tk.Label(Info, bg=white, text=dateruleex, font=("Lato", 10), fg=black, justify="left")
label_rule_browser = tk.Label(Info, bg=white, text=browserrule, font=("Lato", 10), fg=black, justify = "left")
label_rule_timezone = tk.Label(Info, bg=white, text=timezonerule, font=("Lato", 10), fg=black, justify="left")
label_rule_tzwarning = tk.Label(Info, bg=white, text=timezonewarning, font=("Lato", 10), fg=red, justify="left")
label_error_tz = tk.Label(Info, bg=white, textvariable=tzerror, font=("Lato", 10), fg=red, justify="left")
ent_timezone = tk.Entry(Info)
btn_info = tk.Button(Info, text = btntext, command=settimezone)

label_date.grid(row=1, column=0, padx=15, pady=15)
label_browser.grid(row=2, column=0, padx=15, pady=15)
label_timezone.grid(row=4, column=0, padx=15, pady=15)
label_rule_date.grid(row = 1, column = 1, padx=100, pady=100)
label_rule_dateex.grid(row = 1, column = 2, padx=15, pady=15)
label_rule_browser.grid(row = 2, column = 1, pady=15)
label_rule_timezone.grid(row = 4, column = 1, padx=15, pady=15)
label_rule_tzwarning.grid(row=5, column=1, padx=15, pady=15)
ent_timezone.grid(row = 6, column = 1, padx=15, pady=15)
btn_info.grid(row = 6, column = 2, padx=15, pady = 15)
label_error_tz.grid(row=7, column=1, padx=15, pady=15)

#FINISH

tabControl.grid()

ttk.Label(Info)
ttk.Label(Monday)
ttk.Label(Tuesday)
ttk.Label(Wednesday)
ttk.Label(Thursday)
ttk.Label(Friday)
ttk.Label(Saturday)
ttk.Label(Sunday)

Info.grid_propagate(0)
    
root.configure(bg=white)

root.iconbitmap(pathstr+'Icon-big.ico')

if scheduler.running:
    scheduler.shutdown()
    time.sleep(100)
    scheduler.start()
else:
    scheduler.start()

root.mainloop()










