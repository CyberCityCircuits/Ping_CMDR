# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 21:50:36 2016

@author: David Ray
"""

#Import Libraries
import os

#Set Varibles
ip_cmdr = "192.168.31.11"
ip_ezr = "192.168.31.31"
ip_pos1 = "192.168.31.101"
ip_pos2 = "192.168.31.102"
start_ping = "start cmd.exe @/k Ping " 
screen_resize = " & mode con: cols=50 lines=20"
start_cmd_bak = "start cmd.exe @/k mode con: cols=50 lines=20 & ping "


#Define Commands
def main_menu():
    logo()
    print ("")
    confirm = raw_input("        Are You Ready? (Y/N)")
    if confirm == 'y' or confirm == 'Y':
        print ("standy")
    else:
        return main_menu()

def logo():
    print "   .______    __  .__   __.   _______      "
    print "   |   _  \  |  | |  \ |  |  /  _____|     "
    print "   |  |_)  | |  | |   \|  | |  |  __       "
    print "   |   ___/  |  | |  . `  | |  | |_ |      "
    print "   |  |      |  | |  |\   | |  |__| |      "
    print "   | _|      |__| |__| \__|  \______|      "
    print "  ______ .___  ___.  _______  .______      "
    print " /      ||   \/   | |       \ |   _  \     "
    print "|  ,----'|  \  /  | |  .--.  ||  |_)  |    "
    print "|  |     |  |\/|  | |  |  |  ||      /     "
    print "|  `----.|  |  |  | |  '--'  ||  |\  \----."
    print " \______||__|  |__| |_______/ | _| `._____|"
    print ""
    print "          Ping_CMDR V0.01"
    print "          By David A. Ray"
    
def ping_cmdr():
    name = "Commander"
    ip_ping = ip_cmdr
    print "Pinging " + name
    os.system (start_ping + ip_ping + " -t")
    
def ping_ezr():
    name = "Router"
    ip_ping = ip_ezr
    print "Pinging " + name
    os.system (start_ping + ip_ping + " -t")
    
def ping_pos1():
    name = "POS 1"
    ip_ping = ip_pos1
    print "Pinging " + name
    os.system (start_ping + ip_ping + " -t")
    
def ping_pos2():
    name = "POS 2"
    ip_ping = ip_pos2
    print "Pinging " + name
    os.system (start_ping + ip_ping + " -t")
    
#Run Scrpts
main_menu()
ping_cmdr()
ping_ezr()
ping_pos1()
ping_pos2()