# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 21:50:36 2016

@author: David Ray
"""

#Import Libraries
from os import system
import datetime as dt
from requests import ConnectionError as ConnErr
import subprocess
from time import sleep as sleep

#set console size and color
system("mode con: cols=65 lines=16")
system('color F')

#Set Varibles
version = "0.03.04"

dev_1 = "  Commander"
ip_1 = "192.168.31.11"

dev_2 = "     Router"
ip_2 = "192.168.31.31"

dev_3 = "      POS 1"
ip_3 = "192.168.31.101"

dev_4 = "      POS 2"
ip_4 = "192.168.31.102"

website = "http://www.google.com/"
wait = 1.0

ping_internet = 0
ping_1 = 0
ping_2 = 0
ping_3 = 0
ping_4 = 0

var_internet = 0
var_1 = 0
var_2 = 0
var_3 = 0
var_4 = 0

scan = 29

#Define Commands

def logo():
    system('cls')
    system('echo off')
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
    print "                      Ping_CMDR V" + version
    print "                          David A Ray"
    
#set initial starting times
def init_time():
    global currtime
    global uptime_internet
    global uptime_1
    global uptime_2
    global uptime_3
    global uptime_4
    currtime = dt.datetime.now().strftime("%H:%M:%S")
    uptime_internet = currtime
    uptime_1 = currtime
    uptime_2 = currtime
    uptime_3 = currtime
    uptime_4 = currtime

def setcurrtime():
    global currtime
    currtime = dt.datetime.now().strftime("%H:%M:%S")

def check_internet(host=website, timeout=5):
    global ping_internet
    global uptime_internet
    global var_internet
    var_internet = ping_internet
    try:
        ping_internet = 1
        return True
    except ConnErr:
        ping_internet = 0
    return False
    
def check_1():
    global ping_1
    global uptime_1
    global var_1
    var_1 = ping_1    
    host = ip_1
    ping = subprocess.Popen(["ping.exe","-n","1","-w","1",host],stdout = subprocess.PIPE).communicate()[0]
    if ('unreachable' in ping) or ('timed' in ping) or ('failure' in ping):
        ping_1 = 0
    else:
        ping_1 = 1
  
def check_2():
    global ping_2
    global uptime_2
    global var_2
    var_2 = ping_2
    host = ip_2
    ping = subprocess.Popen(["ping.exe","-n","1","-w","1",host],stdout = subprocess.PIPE).communicate()[0]
    if ('unreachable' in ping) or ('timed' in ping) or ('failure' in ping):
        ping_2 = 0
    else:
        ping_2 = 1    
        
def check_3():
    global ping_3
    global uptime_3
    global var_3
    var_3 = ping_3
    host = ip_3
    ping = subprocess.Popen(["ping.exe","-n","1","-w","1",host],stdout = subprocess.PIPE).communicate()[0]
    if ('unreachable' in ping) or ('timed' in ping) or ('failure' in ping):
        ping_3 = 0
    else:
        ping_3 = 1   
        
def check_4():
    global ping_4
    global uptime_4
    global var_4
    var_4 = ping_4
    host = ip_4
    ping = subprocess.Popen(["ping.exe","-n","1","-w","1",host],stdout = subprocess.PIPE).communicate()[0]
    if ('unreachable' in ping) or ('timed' in ping) or ('failure' in ping):
        ping_4 = 0
    else:
        ping_4 = 1  

def set_uptime():
    global uptime_internet
    global uptime_1
    global uptime_2
    global uptime_3
    global uptime_4
    global up_internet
    setcurrtime()
    if var_internet != ping_internet: 
        uptime_internet = currtime
    if var_1 != ping_1: 
        uptime_1 = currtime
    if var_2 != ping_2: 
        uptime_2 = currtime
    if var_3 != ping_3: 
        uptime_3 = currtime
    if var_4 != ping_4: 
        uptime_4 = currtime
     
def ui():
    system('cls')
    system('echo off')
    
    if ping_internet == 1:
        show_internet = "   Internet is UP   - " + uptime_internet
    else:
        show_internet = "   Internet is DOWN - " + uptime_internet

    if ping_1 == 1:
        show_1 = dev_1 + " is UP   - " + uptime_1
    else:
        show_1 = dev_1 + " is DOWN - " + uptime_1

    if ping_2 == 1:
        show_2 = dev_2 + " is UP   - " + uptime_2
    else:
        show_2 = dev_2 + " is DOWN - " + uptime_2

    if ping_3 == 1:
        show_3 = dev_3 + " is UP   - " + uptime_3
    else:
        show_3 = dev_3 + " is DOWN - " + uptime_3
        
    if ping_4 == 1:
        show_4 = dev_4 + " is UP   - " + uptime_4
    else:
        show_4 = dev_4 + " is DOWN - " + uptime_4

    print ""
    print ""
    print ""
    print "                        PING_CMDR V" + version
    print ""
    print "                      Current Time - " + currtime
    print ""
    if scan == 21:
        print "                        <**              >"
    elif scan == 22 or scan == 20:
        print "                        <***             >"
    elif scan == 23 or scan == 19:
        print "                        < ***            >"
    elif scan == 24 or scan == 18:
        print "                        <  ***           >"
    elif scan == 25 or scan == 17:
        print "                        <   ***          >"
    elif scan == 26 or scan == 16:
        print "                        <    ***         >"
    elif scan == 27 or scan == 15:
        print "                        <     ***        >"
    elif scan == 28 or scan == 14:
        print "                        <      ***       >"
    elif scan == 29 or scan == 13:
        print "                        <       ***      >"    
    elif scan == 0 or scan == 12:
        print "                        <        ***     >"
    elif scan == 1 or scan == 11:
        print "                        <         ***    >"
    elif scan == 2 or scan == 10:
        print "                        <          ***   >"
    elif scan == 3 or scan == 9:
        print "                        <           ***  >"
    elif scan == 4 or scan == 8:
        print "                        <            *** >"
    elif scan == 5 or scan == 7:
        print "                        <             ***>"
    elif scan == 6:
        print "                        <              **>"        
    print ""
    print show_internet
    print ""
    print show_1 + " " + show_3
    print show_2 + " " + show_4
    print ""
    
def scan_count():
    global scan
    scan += 1
    if scan == 30:
        scan = 0
        
def run_checks():
    check_internet()
    check_1()
    check_2()
    check_3()
    check_4()
    set_uptime()
    ui()
    scan_count()
    sleep(wait)
    return run_checks()

#Run Scrpts
logo()
sleep(2)
init_time()
run_checks()
