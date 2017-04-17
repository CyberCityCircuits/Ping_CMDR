import var

import os, sys, subprocess
from time import sleep
import datetime as dt

#define vaariables
var.log_option = 0
diag = 0
scan = 31
pinpad_ui = 1



def check_status_dev():
    
    for i in var.dev_range:
        if var.conn_list[i] == 1:
            var.status_list[i] = "UP"
        else:
            var.status_list[i] = "DOWN"
                                 

def check_status_internet():
    if var.conn_internet == 1:
        var.status_internet = "UP"
    else:
        var.status_internet = "DOWN"
    
        

def end():
    os.system("cls")
    print ()
    print ()
    print (var.name.center(var.cent_width))
    print ()
    print ()
    print ("...Program Ending...".center(var.cent_width))
    print ()
    print ()
    print ()
    sleep(var.splash_wait)
    sys.exit()

#initialize date time                      
def init_date_time():
    var.uptime_internet = var.currtime

    var.uptime = [var.currtime,var.currtime,
         var.currtime,var.currtime,
         var.currtime,var.currtime,
         var.currtime,var.currtime,
         var.currtime,var.currtime]
    
def funct_not_supp():
    os.system("cls")
    print ()
    print ()
    print (var.name.center(var.cent_width))
    print ()
    print ()
    print ("FUNCTION NOT SUPPORTED".center(var.cent_width))
    print ()
    print ()
    print ()
    sleep(var.splash_wait)
    main_menu()
                             
            
def logo():
    os.system("cls")
    os.system("echo off")
    print ()
    print ("   .______    __  .__   __.   _______      ".center(var.cent_width))
    print ("   |   _  \  |  | |  \ |  |  /  _____|     ".center(var.cent_width))
    print ("   |  |_)  | |  | |   \|  | |  |  __       ".center(var.cent_width))
    print ("   |   ___/  |  | |  . `  | |  | |_ |      ".center(var.cent_width))
    print ("   |  |      |  | |  |\   | |  |__| |      ".center(var.cent_width))
    print ("   | _|      |__| |__| \__|  \______|      ".center(var.cent_width))
    print ("  ______ .___  ___.  _______  .______      ".center(var.cent_width))
    print (" /      ||   \/   | |       \ |   _  \     ".center(var.cent_width))
    print ("|  ,----'|  \  /  | |  .--.  ||  |_)  |    ".center(var.cent_width))
    print ("|  |     |  |\/|  | |  |  |  ||      /     ".center(var.cent_width))
    print ("|  `----.|  |  |  | |  '--'  ||  |\  \----.".center(var.cent_width))
    print (" \______||__|  |__| |_______/ | _| `._____|".center(var.cent_width))
    print ()
    print (var.name.center(var.cent_width))
    print ("David A Ray".center(var.cent_width))
    print ()
    print (("Contact: " + var.email).center(var.cent_width))

    
    sleep(var.splash_wait)
    
    


def main_menu():
    global pinpad_ui
    os.system("cls")
    print ()
    print ()
    print (var.name.center(var.cent_width))
    print ()
    print (("Current POS Count: " + str(int(var.dev_count/2))).center(var.cent_width))
    print ()
    if var.log_option == (0):
        print ("Logging Function Disabled".center(var.cent_width))
    else:
        print ("Logging Function  Enabled".center(var.cent_width))
    if var.diag == (1):
        print ("Diagnostics Mode Enabled".center(var.cent_width))
    print ()
    print ("  0 - " + var.option_0)
    print ("  1 - " + var.option_1)
    print ("  2 - " + var.option_2)
    print ("  3 - " + var.option_3)
    print ("  4 - " + var.option_4)
    print ("  5 - " + var.option_5)
    print ()
    option = input("  Enter Your Selection: [0/1/2/3/4/5] ")
    if option == ("0"):
        end()
    elif option == ("1"):
        funct_not_supp()
    elif option == ("2"):
        set_pos_count()
        main_menu()
    elif option == ("3"):
        pinpad_ui = 1
    elif option == ("4"):
        funct_not_supp()
    elif option == ("5"):
        if var.log_option == 0:
            var.log_option = 1
            main_menu()
        else:
            var.log_option = 0
            main_menu()
    elif option.lower() == ("diag"):
        if var.diag == 0:
            var.diag = 1
            main_menu()
        else:
            var.diag = 0
            main_menu()
    else:
        main_menu()
        
    
#create folder for logs
def mk_dir(name):
    if not os.path.exists(name):
        os.makedirs(name)
    
    
def mk_log():
    if var.log_option == 1:
        mk_dir(var.dir_log)
        #creates and writes to log file
        f = open(var.dir_log + "\\" + var.file_log + ".txt","w")
        #log_currdate = dt.date.today().strftime("%m/%d/%Y")
        #log_currtime = dt.datetime.now().strftime("%H:%M:%S")
        f.write(var.name + "\n"
                "Starting Date - " + var.currdate + "\n"
                "Starting Time - " + var.currtime + "\n"
                "\n")
        f.close()    
    

#ping by variable
def ping(id_no):
    host = var.ip_scheme + var.ip_list[id_no]
    ping = subprocess.Popen(["ping.exe","-n","1","-w","1",host],stdout = subprocess.PIPE).communicate()[0]
    if ('unreachable' in str(ping)) or ('timed' in str(ping)) or ('failure' in str(ping)):
        var.conn_list[int(id_no)] = 0
    else:
        var.conn_list[int(id_no)] = 1

#ping internet
def ping_internet():
    host = var.ip_internet
    ping = subprocess.Popen(["ping.exe","-n","1","-w","1",host],stdout = subprocess.PIPE).communicate()[0]
    if ('unreachable' in str(ping)) or ('timed' in str(ping)) or ('failure' in str(ping)):
        var.conn_internet = 0
    else:
        var.conn_internet = 1
    

#changes console size based on dev_count    
def set_console():
    
    var.lines = int(var.dev_count/2) + 13
    #define cosole size and color
    os.system("mode con: cols=" + str(var.width) + " lines=" + str(var.lines))

    
#set date and time        
def set_date_time():
    global currdate, currtime
    var.currdate = dt.date.today().strftime("%m/%d/%Y")
    var.currtime = dt.datetime.now().strftime("%H:%M:%S")
    

#sets dev_count        
def set_pos_count():
    os.system("cls")
    print ()
    print ()
    print (var.name.center(var.cent_width))
    print ()
    print ()
    option = input("  What is your POS Count: ")
    if option == "0":
        os.system("cls")
        print ()
        print ()
        print (var.name.center(var.cent_width))
        print ()
        print ()
        print ("POS Count can not be 0.".center(var.cent_width))
        sleep(var.splash_wait)
    elif not option.isdigit():
        os.system("cls")
        print ()
        print ()
        print (var.name.center(var.cent_width))
        print ()
        print ()
        print ("POS Count must be an integer.".center(var.cent_width))
        sleep(var.splash_wait)
    elif int(option) > int(var.max_dev_count/2):
        os.system("cls")
        print ()
        print ()
        print (var.name.center(var.cent_width))
        print ()
        print ()
        print ("Exceeded POS Count Limit.".center(var.cent_width))
        sleep(var.splash_wait)
        
        
    else:
        var.dev_count = int(option)*2
        var.dev_range = range(var.dev_count)

#Sets currtime when the status changes.
#Writes to log file if logging is enabled
def set_uptime():
    var.currtime = dt.datetime.now().strftime("%H:%M:%S")
    if var.diff_internet != var.conn_internet:
        var.diff_internet = var.conn_internet
        var.uptime_internet = var.currtime
        if var.log_option == 1:
           
            f = open(var.dir_log + "\\" + var.file_log + ".txt","a")
            if var.diag == 1:
                f.write((str(var.loop_count)) + "\n")
            f.write("Internet is " + var.status_internet + " - " + 
                    var.currdate + " - " + var.uptime_internet + "\n")
            f.close()
            
    for i in var.dev_range:
        if var.diff[i] != var.conn_list[i]:
            var.diff[i] = var.conn_list[i]
            var.uptime[i] = var.currtime
            if var.log_option == 1:
                f = open(var.dir_log + "\\" + var.file_log + ".txt","a")
                if var.diag == 1:
                    f.write(str(var.loop_count) + "\n")
                f.write(var.dev_list[i] + " is " + var.status_list[i] + " - " + 
                var.currdate + " - " + var.uptime[i] + "\n")
                f.close()
   
    
def ui_screen():
    global scan
    
    os.system("cls")
    os.system("echo off")
    
    show_internet = ("Internet is " + var.status_internet + " - " + var.uptime_internet)
    
    for i in var.dev_range:
        var.show[i] = (var.dev_list[i] + " is " + var.status_list[i] + " - " + 
                var.uptime[i])
            
    if var.diag == 1:
        print (str(var.loop_count).rjust(var.cent_width))
    print ()
    print ((var.name).center(var.cent_width))
    print ()
    print (("Current Time - " + var.currtime).center(var.cent_width))
    print ()
    if scan == 22:
        print (("<**               >").center(var.cent_width))
    elif scan == 23 or scan == 21:
        print (("<***              >").center(var.cent_width))
    elif scan == 24 or scan == 20:
        print (("< ***             >").center(var.cent_width))
    elif scan == 25 or scan == 19:
        print (("<  ***            >").center(var.cent_width))
    elif scan == 26 or scan == 18:
        print (("<   ***           >").center(var.cent_width))
    elif scan == 27 or scan == 17:
        print (("<    ***          >").center(var.cent_width))
    elif scan == 28 or scan == 16:
        print (("<     ***         >").center(var.cent_width))
    elif scan == 29 or scan == 15:
        print (("<      ***        >").center(var.cent_width))
    elif scan == 30 or scan == 14:
        print (("<       ***       >").center(var.cent_width))
    elif scan == 31 or scan == 13:
        print (("<        ***      >").center(var.cent_width))
    elif scan == 0 or scan == 12:
        print (("<         ***     >").center(var.cent_width))
    elif scan == 1 or scan == 11:
        print (("<          ***    >").center(var.cent_width))
    elif scan == 2 or scan == 10:
        print (("<           ***   >").center(var.cent_width))
    elif scan == 3 or scan == 9:
        print (("<            ***  >").center(var.cent_width))
    elif scan == 4 or scan == 8:
        print (("<             *** >").center(var.cent_width))
    elif scan == 5 or scan == 7:
        print (("<              ***>").center(var.cent_width))
    elif scan == 6:
        print (("<               **>").center(var.cent_width))
    print ()
    print ((show_internet).center(var.cent_width))
    print ()
    print ((var.show[0] + "     " + var.show[1]).center(var.cent_width))
    if var.dev_count >= 2:
        print ((var.show[2] + "     " + var.show[3]).center(var.cent_width))
    if var.dev_count >= 3:
        print ((var.show[4] + "     " + var.show[5]).center(var.cent_width))
    if var.dev_count >= 4:
        print ((var.show[6] + "     " + var.show[7]).center(var.cent_width))
    if var.dev_count >= 5:
        print ((var.show[8] + "     " + var.show[9]).center(var.cent_width))


    scan += 1
    if scan == 32:
        scan = 0    
        
