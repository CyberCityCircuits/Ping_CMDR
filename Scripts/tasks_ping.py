import var_ping

import os, sys, subprocess
from time import sleep
import datetime as dt

#define vaariables
var_ping.log_option = 0
diag = 0
scan = 31
pinpad_ui = 1



def check_status_dev():
    
    for i in var_ping.dev_range:
        if var_ping.conn_list[i] == 1:
            var_ping.status_list[i] = "UP"
        else:
            var_ping.status_list[i] = "DOWN"
                                 

def check_status_internet():
    if var_ping.conn_internet == 1:
        var_ping.status_internet = "UP"
    else:
        var_ping.status_internet = "DOWN"
     

def end():
    os.system("cls")
    print ()
    print ()
    print (var_ping.name.center(var_ping.cent_width))
    print ()
    print ()
    print ("...Program Ending...".center(var_ping.cent_width))
    print ()
    print ()
    print ()
    sleep(var_ping.splash_wait)
    sys.exit()

#initialize date time                      
def init_date_time():
    var_ping.uptime_internet = var_ping.currtime

    var_ping.uptime = [var_ping.currtime,var_ping.currtime,
         var_ping.currtime,var_ping.currtime,
         var_ping.currtime,var_ping.currtime,
         var_ping.currtime,var_ping.currtime,
         var_ping.currtime,var_ping.currtime]
    
def funct_not_supp():
    os.system("cls")
    print ()
    print ()
    print (var_ping.name.center(var_ping.cent_width))
    print ()
    print ()
    print ("FUNCTION NOT SUPPORTED".center(var_ping.cent_width))
    print ()
    print ()
    print ()
    sleep(var_ping.splash_wait)
    main_menu()
                             
            
def logo():
    os.system("cls")
    os.system("echo off")
    print ()
    print ("   .______    __  .__   __.   _______      ".center(var_ping.cent_width))
    print ("   |   _  \  |  | |  \ |  |  /  _____|     ".center(var_ping.cent_width))
    print ("   |  |_)  | |  | |   \|  | |  |  __       ".center(var_ping.cent_width))
    print ("   |   ___/  |  | |  . `  | |  | |_ |      ".center(var_ping.cent_width))
    print ("   |  |      |  | |  |\   | |  |__| |      ".center(var_ping.cent_width))
    print ("   | _|      |__| |__| \__|  \______|      ".center(var_ping.cent_width))
    print ("  ______ .___  ___.  _______  .______      ".center(var_ping.cent_width))
    print (" /      ||   \/   | |       \ |   _  \     ".center(var_ping.cent_width))
    print ("|  ,----'|  \  /  | |  .--.  ||  |_)  |    ".center(var_ping.cent_width))
    print ("|  |     |  |\/|  | |  |  |  ||      /     ".center(var_ping.cent_width))
    print ("|  `----.|  |  |  | |  '--'  ||  |\  \----.".center(var_ping.cent_width))
    print (" \______||__|  |__| |_______/ | _| `._____|".center(var_ping.cent_width))
    print ()
    print (var_ping.name.center(var_ping.cent_width))
    print ("David A Ray".center(var_ping.cent_width))
    print ()
    print (("Contact: " + var_ping.email).center(var_ping.cent_width))

    
    sleep(var_ping.splash_wait)
    
    


def main_menu():
    global pinpad_ui
    os.system("cls")
    print ()
    print ()
    print (var_ping.name.center(var_ping.cent_width))
    print ()
    print (("Current POS Count: " + str(int(var_ping.dev_count/2))).center(var_ping.cent_width))
    print ()
    if var_ping.log_option == (0):
        print ("Logging Function Disabled".center(var_ping.cent_width))
    else:
        print ("Logging Function  Enabled".center(var_ping.cent_width))
    if var_ping.diag == (1):
        print ("Diagnostics Mode Enabled".center(var_ping.cent_width))
    print ()
    print ("  0 - " + var_ping.option_0)
    print ("  1 - " + var_ping.option_1)
    print ("  2 - " + var_ping.option_2)
    print ("  3 - " + var_ping.option_3)
    print ("  4 - " + var_ping.option_4)
    print ("  5 - " + var_ping.option_5)
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
        if var_ping.log_option == 0:
            var_ping.log_option = 1
            main_menu()
        else:
            var_ping.log_option = 0
            main_menu()
    elif option.lower() == ("diag"):
        if var_ping.diag == 0:
            var_ping.diag = 1
            main_menu()
        else:
            var_ping.diag = 0
            main_menu()
    else:
        main_menu()
        
    
#create folder for logs
def mk_dir(name):
    if not os.path.exists(name):
        os.makedirs(name)
    
    
def mk_log():
    if var_ping.log_option == 1:
        mk_dir(var_ping.dir_log)
        #creates and writes to log file
        f = open(var_ping.dir_log + "\\" + var_ping.file_log + ".txt","w")
        #log_currdate = dt.date.today().strftime("%m/%d/%Y")
        #log_currtime = dt.datetime.now().strftime("%H:%M:%S")
        f.write(var_ping.name + "\n"
                "Starting Date - " + var_ping.currdate + "\n"
                "Starting Time - " + var_ping.currtime + "\n"
                "\n")
        f.close()    
    

#ping by var_pingiable
def ping(id_no):
    host = var_ping.ip_scheme + var_ping.ip_list[id_no]
    ping = subprocess.Popen(["ping.exe","-n","1","-w","1",host],stdout = subprocess.PIPE).communicate()[0]
    if ('unreachable' in str(ping)) or ('timed' in str(ping)) or ('failure' in str(ping)):
        var_ping.conn_list[int(id_no)] = 0
    else:
        var_ping.conn_list[int(id_no)] = 1

#ping internet
def ping_internet():
    host = var_ping.ip_internet
    ping = subprocess.Popen(["ping.exe","-n","1","-w","1",host],stdout = subprocess.PIPE).communicate()[0]
    if ('unreachable' in str(ping)) or ('timed' in str(ping)) or ('failure' in str(ping)):
        var_ping.conn_internet = 0
    else:
        var_ping.conn_internet = 1
    

#changes console size based on dev_count    
def set_console():
    
    var_ping.lines = int(var_ping.dev_count/2) + 13
    #define cosole size and color
    os.system("mode con: cols=" + str(var_ping.width) + " lines=" + str(var_ping.lines))

    
#set date and time        
def set_date_time():
    global currdate, currtime
    var_ping.currdate = dt.date.today().strftime("%m/%d/%Y")
    var_ping.currtime = dt.datetime.now().strftime("%H:%M:%S")
    

#sets dev_count        
def set_pos_count():
    os.system("cls")
    print ()
    print ()
    print (var_ping.name.center(var_ping.cent_width))
    print ()
    print ()
    option = input("  What is your POS Count: ")
    if option == "0":
        os.system("cls")
        print ()
        print ()
        print (var_ping.name.center(var_ping.cent_width))
        print ()
        print ()
        print ("POS Count can not be 0.".center(var_ping.cent_width))
        sleep(var_ping.splash_wait)
    elif not option.isdigit():
        os.system("cls")
        print ()
        print ()
        print (var_ping.name.center(var_ping.cent_width))
        print ()
        print ()
        print ("POS Count must be an integer.".center(var_ping.cent_width))
        sleep(var_ping.splash_wait)
    elif int(option) > int(var_ping.max_dev_count/2):
        os.system("cls")
        print ()
        print ()
        print (var_ping.name.center(var_ping.cent_width))
        print ()
        print ()
        print ("Exceeded POS Count Limit.".center(var_ping.cent_width))
        sleep(var_ping.splash_wait)
        
        
    else:
        var_ping.dev_count = int(option)*2
        var_ping.dev_range = range(var_ping.dev_count)

#Sets currtime when the status changes.
#Writes to log file if logging is enabled
def set_uptime():
#    var_ping.currtime = dt.datetime.now().strftime("%H:%M:%S")
#    if var_ping.diff_internet != var_ping.conn_internet:
#        var_ping.diff_internet = var_ping.conn_internet
#        var_ping.uptime_internet = var_ping.currtime
#        if var_ping.log_option == 1:
#           
#            f = open(var_ping.dir_log + "\\" + var_ping.file_log + ".txt","a")
#            if var_ping.diag == 1:
#                f.write((str(var_ping.loop_count)) + "\n")
#            f.write("Internet is " + var_ping.status_internet + " - " + 
#                    var_ping.currdate + " - " + var_ping.uptime_internet + "\n")
#            f.close()
            
    for i in var_ping.dev_range:
        if var_ping.diff[i] != var_ping.conn_list[i]:
            var_ping.diff[i] = var_ping.conn_list[i]
            var_ping.uptime[i] = var_ping.currtime
            if var_ping.log_option == 1:
                f = open(var_ping.dir_log + "\\" + var_ping.file_log + ".txt","a")
                if var_ping.diag == 1:
                    f.write(str(var_ping.loop_count) + "\n")
                f.write(var_ping.dev_list[i] + " is " + var_ping.status_list[i] + " - " + 
                var_ping.currdate + " - " + var_ping.uptime[i] + "\n")
                f.close()
   
    
def ui_screen():
    global scan
    
    os.system("cls")
    os.system("echo off")
    
    show_internet = ("Internet is " + var_ping.status_internet + " - " + var_ping.uptime_internet)
    
    for i in var_ping.dev_range:
        var_ping.show[i] = (var_ping.dev_list[i] + " is " + var_ping.status_list[i] + " - " + 
                var_ping.uptime[i])
            
    if var_ping.diag == 1:
        print (str(var_ping.loop_count).rjust(var_ping.cent_width))
    print ()
    print ((var_ping.name).center(var_ping.cent_width))
    print ()
    print (("Current Time - " + var_ping.currtime).center(var_ping.cent_width))
    print ()
    if scan == 22:
        print (("<**               >").center(var_ping.cent_width))
    elif scan == 23 or scan == 21:
        print (("<***              >").center(var_ping.cent_width))
    elif scan == 24 or scan == 20:
        print (("< ***             >").center(var_ping.cent_width))
    elif scan == 25 or scan == 19:
        print (("<  ***            >").center(var_ping.cent_width))
    elif scan == 26 or scan == 18:
        print (("<   ***           >").center(var_ping.cent_width))
    elif scan == 27 or scan == 17:
        print (("<    ***          >").center(var_ping.cent_width))
    elif scan == 28 or scan == 16:
        print (("<     ***         >").center(var_ping.cent_width))
    elif scan == 29 or scan == 15:
        print (("<      ***        >").center(var_ping.cent_width))
    elif scan == 30 or scan == 14:
        print (("<       ***       >").center(var_ping.cent_width))
    elif scan == 31 or scan == 13:
        print (("<        ***      >").center(var_ping.cent_width))
    elif scan == 0 or scan == 12:
        print (("<         ***     >").center(var_ping.cent_width))
    elif scan == 1 or scan == 11:
        print (("<          ***    >").center(var_ping.cent_width))
    elif scan == 2 or scan == 10:
        print (("<           ***   >").center(var_ping.cent_width))
    elif scan == 3 or scan == 9:
        print (("<            ***  >").center(var_ping.cent_width))
    elif scan == 4 or scan == 8:
        print (("<             *** >").center(var_ping.cent_width))
    elif scan == 5 or scan == 7:
        print (("<              ***>").center(var_ping.cent_width))
    elif scan == 6:
        print (("<               **>").center(var_ping.cent_width))
    print ()
    print ((show_internet).center(var_ping.cent_width))
    print ()
    print ((var_ping.show[0] + "     " + var_ping.show[1]).center(var_ping.cent_width))
    if var_ping.dev_count >= 2:
        print ((var_ping.show[2] + "     " + var_ping.show[3]).center(var_ping.cent_width))
    if var_ping.dev_count >= 3:
        print ((var_ping.show[4] + "     " + var_ping.show[5]).center(var_ping.cent_width))
    if var_ping.dev_count >= 4:
        print ((var_ping.show[6] + "     " + var_ping.show[7]).center(var_ping.cent_width))
    if var_ping.dev_count >= 5:
        print ((var_ping.show[8] + "     " + var_ping.show[9]).center(var_ping.cent_width))


    scan += 1
    if scan == 32:
        scan = 0    
        
