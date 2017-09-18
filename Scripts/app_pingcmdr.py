import var_ping, tasks_ping, tasks_gui
import os, sys
import datetime as dt

#from tkinter import *
from tkinter import Menu, Frame, BOTH, W
from tkinter import Tk, Label, messagebox
import webbrowser

#define cosole size and color
os.system("mode con: cols=" + str(var_ping.width) + " lines=" + str(var_ping.lines))
os.system("color F")
os.system("cls")
os.system("echo off")

print("Ping Tool\nLeave Open to Use\nClose to End".center((var_ping.width)-1))


class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master

        self.init_window()
        

    def init_window(self):
        self.master.title(var_ping.name)
        
        topbar = Menu(self.master)
        self.master.config(menu=topbar)
        
        file_menu = Menu(topbar)
        #edit_menu = Menu(topbar)
        #remove_menu = Menu(topbar)
        #add_menu = Menu(topbar)
        opt_menu = Menu(topbar)
        help_menu = Menu(topbar)
        
        #file_menu.add_command(label="Import Dataset", command=import_data)
        #file_menu.add_command(label="Update", command=update)
        #file_menu.add_command(label="Export Dataset", command=tasks.export_xml)
        #file_menu.add_command(label="List All Departments", command=tasks.list_dept)
        file_menu.add_command(label="Exit", command=tasks_gui.client_exit)
        topbar.add_cascade(label="File", menu=file_menu)
        
        opt_menu.add_command(label="Start Ping", command=start_ping)
        topbar.add_cascade(label="Options", menu=opt_menu)
        
        help_menu.add_command(label="About", command=show_about)
        topbar.add_cascade(label="Help", menu=help_menu)
        
def msg(text):
    messagebox.showinfo(var_ping.app_name, text)
    
def msg_error(text):
    messagebox.showerror(var_ping.app_name, text)

def funct_not_supp():
    msg_error("Function Not Yet Supported")


    
#command for help > about
def show_about():
    msg(var_ping.name + "\n"
        "Build: " + var_ping.build_date + "\n\n"
        "By David Ray \n"
        #"\n" + var_ping.email + "\n\n"
        #"www.DREAM-Enterprise.com"
        )

       
def homepage(event):
    webbrowser.open_new(r"http://www.DREAM-Enterprise.com")
    
def unpack():
    time.forget()
        
def start_ping():
    global time
    global line0, line1, line2
    global line3, line4, line5
    
    wait = 100
    
    var_ping.log_option = 1
    
    tasks_ping.mk_log()
    tasks_ping.set_date_time()
    tasks_ping.init_date_time()
    
    #tasks_ping.set_date_time()
    time = Label(root, text=var_ping.currtime+"\n")
    
    line0 = Label(root, text=("Status Unknown"))
    line1 = Label(root, text=("Status Unknown"))
    line2 = Label(root, text=("Status Unknown"))
    line3 = Label(root, text=("Status Unknown"))
    line4 = Label(root, text=("Status Unknown"))
    line5 = Label(root, text=("Status Unknown"))
    
    lab.destroy()
    
    time.pack()
    line0.pack()
    line1.pack()
    line2.pack()
    line3.pack()
    line4.pack()
    line5.pack()

    
    #This is an important line to make the update wait to run again.
    #Never use time.sleep in a tkinter program.
    root.after(wait, lambda: run_ping()) 
    
def run_ping():   
    global time
    global line0, line1, line2
    global line3, line4, line5

    wait = 200
    
    #updates current time
    tasks_ping.set_date_time()
    
    #updates loop for diag mode
    if var_ping.diag == (1):
        var_ping.loop_count +=  1

    #pings all devices        
    for i in var_ping.dev_range:
        tasks_ping.ping(i)

    #assigns up and down values to each devices depending on ping        
    tasks_ping.check_status_dev()        
    
    #assigns uptime to devices as states change
    tasks_ping.set_uptime()
    
    for i in var_ping.dev_range:
        var_ping.show[i] = (var_ping.dev_list[i] + " is " + var_ping.status_list[i] + " - " + 
                var_ping.uptime[i])
    
    
    time.destroy()
    line0.destroy()
    line1.destroy()
    line2.destroy()
    line3.destroy()
    line4.destroy()
    line5.destroy()
    
    time = Label(root, text=var_ping.currtime+"\n", width="40")
    
    if var_ping.conn_list[0] == 1:
        line0=Label(root, text=var_ping.show[0]
                            , bg="green", fg="black", width="40")
    else:
        line0=Label(root, text=var_ping.show[0]
                            , bg="red", fg="black", width="40")
    
    if var_ping.conn_list[1] == 1:
        line1=Label(root, text=var_ping.show[1]
                            , bg="green", fg="black", width="40")
    else:
        line1=Label(root, text=var_ping.show[1]
                            , bg="red", fg="black", width="40")
        
    if var_ping.conn_list[2] == 1:
        line2=Label(root, text=var_ping.show[2]
                            , bg="green", fg="black", width="40")
    else:
        line2=Label(root, text=var_ping.show[2]
                            , bg="red", fg="black", width="40")      
        
    if var_ping.conn_list[2] == 1:
        line2=Label(root, text=var_ping.show[2]
                            , bg="green", fg="black", width="40")
    else:
        line2=Label(root, text=var_ping.show[2]
                            , bg="red", fg="black", width="40")  
        
    if var_ping.conn_list[3] == 1:
        line3=Label(root, text=var_ping.show[3]
                            , bg="green", fg="black", width="40")
    else:
        line3=Label(root, text=var_ping.show[3]
                            , bg="red", fg="black", width="40")          
        
    if var_ping.conn_list[4] == 1:
        line4=Label(root, text=var_ping.show[4]
                            , bg="green", fg="black", width="40")
    else:
        line4=Label(root, text=var_ping.show[4]
                            , bg="red", fg="black", width="40")          
        
    if var_ping.conn_list[5] == 1:
        line5=Label(root, text=var_ping.show[5]
                            , bg="green", fg="black", width="40")
    else:
        line5=Label(root, text=var_ping.show[5]
                            , bg="red", fg="black", width="40")          
        
#   print(var_ping.show[0]+"\n"+var_ping.show[1]+"\n"+var_ping.show[2]+"\n"+
#          var_ping.show[3]+"\n"+var_ping.show[4]+"\n"+var_ping.show[5]+"\n")
                    
        
    time.pack()
    line0.pack()
    line1.pack()
    line2.pack()
    line3.pack()
    line4.pack()
    line5.pack()
    
    #This is an important line to make the update wait to run again.
    #Never use time.sleep in a tkinter program.
    root.after(wait, lambda: run_ping())            

root = Tk()

w = 250 # width for the Tk root
h = 250 #height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/4) - (w/2)
y = (hs/2.5) - (h/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

header = Label(root, text=var_ping.name+"\n"
             "David Ray\n")

lab = Label(root, text="DEMO\n"
                     "Contact David Ray with Feedback\n"            
                     "Ref: "+var_ping.name
                     , bg="green", fg="black")


header.pack()
lab.pack()
    
app = Window(root)    

root.mainloop()

