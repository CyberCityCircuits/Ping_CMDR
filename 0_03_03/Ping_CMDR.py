# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 21:50:36 2016

@author: David Ray
"""

#Import Libraries
import os
import datetime as dt
import requests
import subprocess
from time import sleep as sleep


#set console size and color
os.system("mode con: cols=65 lines=16")
os.system('color F')

#Set Varibles
version = "0.03"
long_version = "0.03.03"
ip_cmdr = "192.168.31.11"
ip_ezr = "192.168.31.31"
ip_pos1 = "192.168.31.101"
ip_pos2 = "192.168.31.102"
website = "http://www.google.com/"
wait = 1.0

ping_internet = 0
ping_cmdr = 0
ping_ezr = 0
ping_pos1 = 0
ping_pos2 = 0

var_internet = 0
var_cmdr = 0
var_ezr = 0
var_pos1 = 0
var_pos2 = 0

scan = 27

#Define Commands
def main_menu():
    logo()
 #   confirm = raw_input("        Are You Ready? (Y/N)")
 #   if confirm == 'y' or confirm == 'Y':
 #       print ("Stand By")
 #   else:
 #       return main_menu()

def logo():
    os.system('cls')
    os.system('echo off')
    print ""
    print "              .______    __  .__   __.   _______      "
    print "              |   _  \  |  | |  \ |  |  /  _____|     "
    print "              |  |_)  | |  | |   \|  | |  |  __       "
    print "              |   ___/  |  | |  . `  | |  | |_ |      "
    print "              |  |      |  | |  |\   | |  |__| |      "
    print "              | _|      |__| |__| \__|  \______|      "
    print "             ______ .___  ___.  _______  .______      "
    print "            /      ||   \/   | |       \ |   _  \     "
    print "           |  ,----'|  \  /  | |  .--.  ||  |_)  |    "
    print "           |  |     |  |\/|  | |  |  |  ||      /     "
    print "           |  `----.|  |  |  | |  '--'  ||  |\  \----."
    print "            \______||__|  |__| |_______/ | _| `._____|"
    print "           "
    print "                      Ping_CMDR V" + long_version
    print "                          David A Ray"
    
#set initial starting times
def init_time():
    global currtime
    global uptime_internet
    global uptime_cmdr
    global uptime_ezr
    global uptime_pos1
    global uptime_pos2
    currtime = dt.datetime.now().strftime("%H:%M:%S")
    uptime_internet = currtime
    uptime_cmdr = currtime
    uptime_ezr = currtime
    uptime_pos1 = currtime
    uptime_pos2 = currtime

def setcurrdt():
    global currdate
    global currtime
    currdate = dt.date.today().strftime("%Y/%m/%d")
    currtime = dt.datetime.now().strftime("%H:%M:%S")

def check_internet(host=website, timeout=5):
    global ping_internet
    global uptime_internet
    global var_internet
    var_internet = ping_internet
    try:
        _ = requests.get(host, timeout=timeout)
        ping_internet = 1
        return True
    except requests.ConnectionError:
        ping_internet = 0
    return False
    
def check_cmdr():
    global ping_cmdr
    global uptime_cmdr
    global var_cmdr
    var_cmdr = ping_cmdr    
    host = ip_cmdr
    ping = subprocess.Popen(["ping.exe","-n","1","-w","1",host],stdout = subprocess.PIPE).communicate()[0]
    if ('unreachable' in ping) or ('timed' in ping) or ('failure' in ping):
        ping_cmdr = 0
    else:
        ping_cmdr = 1
  
def check_ezr():
    global ping_ezr
    global uptime_ezr
    global var_ezr
    var_ezr = ping_ezr
    host = ip_ezr
    ping = subprocess.Popen(["ping.exe","-n","1","-w","1",host],stdout = subprocess.PIPE).communicate()[0]
    if ('unreachable' in ping) or ('timed' in ping) or ('failure' in ping):
        ping_ezr = 0
    else:
        ping_ezr = 1    
        
def check_pos1():
    global ping_pos1
    global uptime_pos1
    global var_pos1
    var_pos1 = ping_pos1
    host = ip_pos1
    ping = subprocess.Popen(["ping.exe","-n","1","-w","1",host],stdout = subprocess.PIPE).communicate()[0]
    if ('unreachable' in ping) or ('timed' in ping) or ('failure' in ping):
        ping_pos1 = 0
    else:
        ping_pos1 = 1   
        
def check_pos2():
    global ping_pos2
    global uptime_pos2
    global var_pos2
    var_pos2 = ping_pos2
    host = ip_pos2
    ping = subprocess.Popen(["ping.exe","-n","1","-w","1",host],stdout = subprocess.PIPE).communicate()[0]
    if ('unreachable' in ping) or ('timed' in ping) or ('failure' in ping):
        ping_pos2 = 0
    else:
        ping_pos2 = 1  

def set_uptime():
    global uptime_internet
    global uptime_cmdr
    global uptime_ezr
    global uptime_pos1
    global uptime_pos2
    global up_internet
    setcurrdt()
    if var_internet != ping_internet: 
        uptime_internet = currtime
    if var_cmdr != ping_cmdr: 
        uptime_cmdr = currtime
    if var_ezr != ping_ezr: 
        uptime_ezr = currtime
    if var_pos1 != ping_pos1: 
        uptime_pos1 = currtime
    if var_pos2 != ping_pos2: 
        uptime_pos2 = currtime
     
def ui():
    os.system('cls')
    os.system('echo off')
    
    if ping_internet == 1:
        show_internet = "   Internet is UP   - " + uptime_internet
    else:
        show_internet = "   Internet is DOWN - " + uptime_internet

    if ping_cmdr == 1:
        show_cmdr = "  Commander is UP   - " + uptime_cmdr
    else:
        show_cmdr = "  Commander is DOWN - " + uptime_cmdr

    if ping_ezr == 1:
        show_ezr = "     Router is UP   - " + uptime_ezr
    else:
        show_ezr = "     Router is DOWN - " + uptime_ezr

    if ping_pos1 == 1:
        show_pos1 = "        WS 1 is UP   - " + uptime_pos1
    else:
        show_pos1 = "        WS 1 is DOWN - " + uptime_pos1
        
    if ping_pos2 == 1:
        show_pos2 = "        WS 2 is UP   - " + uptime_pos2
    else:
        show_pos2 = "        WS 2 is DOWN - " + uptime_pos2

    print ""
    print ""
    print ""
    print "                          PING_CMDR V" + version
    print ""
    print "                      Current Time - " + currtime
    print ""
    if scan == 20:
        print "                         <**             >"
    elif scan == 21 or scan == 19:
        print "                         <***            >"
    elif scan == 22 or scan == 18:
        print "                         < ***           >"
    elif scan == 23 or scan == 17:
        print "                         <  ***          >"
    elif scan == 24 or scan == 16:
        print "                         <   ***         >"
    elif scan == 25 or scan == 15:
        print "                         <    ***        >"
    elif scan == 26 or scan == 14:
        print "                         <     ***       >"
    elif scan == 27 or scan == 13:
        print "                         <      ***      >"
    elif scan == 0 or scan == 12:
        print "                         <       ***     >"
    elif scan == 1 or scan == 11:
        print "                         <        ***    >"
    elif scan == 2 or scan == 10:
        print "                         <         ***   >"
    elif scan == 3 or scan == 9:
        print "                         <          ***  >"
    elif scan == 4 or scan == 8:
        print "                         <           *** >"
    elif scan == 5 or scan == 7:
        print "                         <            ***>"
    elif scan == 6:
        print "                         <             **>"        
    print ""
    print show_internet
    print ""
    print show_cmdr + " " + show_pos1
    print show_ezr + " " + show_pos2
    print ""
    
def scan_count():
    global scan
    scan += 1
    if scan == 28:
        scan = 0
        
def run_checks():
    check_internet()
    check_cmdr()
    check_ezr()
    check_pos1()
    check_pos2()
    set_uptime()
    ui()
    scan_count()
    sleep(wait)
    return run_checks()

#Run Scrpts
main_menu()
sleep(2)
init_time()
run_checks()
