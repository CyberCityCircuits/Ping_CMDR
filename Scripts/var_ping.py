# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 14:49:57 2017

@author: DREAM
"""

import datetime as dt

app_name = "Ping_CMDR"
version = "0.07.00"
name = app_name + "  V" + version
email = "David@DREAM-Enterprise.com"
build_date = "09-17-2017"


#set date and time        
startdate = dt.date.today().strftime("%m%d%Y")
start_time = dt.datetime.now().strftime("%H%M%S")
currdate = dt.date.today().strftime("%m/%d/%Y")
currtime = dt.datetime.now().strftime("%H:%M:%S")

    

#define system varibles
dev_count = 6
dev_range = range(dev_count)
max_dev_count = 10

wait = 1
splash_wait = 2.5

width = 20
lines = 4
cent_width = int(width)-1
dev_width = 10

diag = 0
loop_count = 0

log_option = 0
file_log = "Ping Log - " + startdate + " - " + start_time
dir_log = "Ping Logs"

option_0 = "Exit"
option_1 = "Feature Not Supported"
option_2 = "Set POS Count"
option_3 = "Run Ping Tool"
option_4 = "Feature Not Supported"
option_5 = "Toggle Log File Function"


ip_scheme = "192.168.31."

ip_internet = "8.8.8.8"

dev_list = ["Commander", "Router",
            "POS 1", "POS 2", 
            "Pinpad 1", "Pinpad 2", 
            "POS 3", "Pinpad 3",
            "POS 4", "Pinpad 4"]

ip_list = ["11", "31",
           "101", "102",
           "126", "127",
           "103", "128",
           "104", "129"]

status_internet = ""

status_list = ["","",
               "","",
               "","",
               "","",
               "",""]

conn_internet = 0

conn_list = [0,0,
             0,0,
             0,0,
             0,0,
             0,0]

show = ["","",
       "","",
       "","",
       "","",
       "",""]

diff_internet = 0

diff = [0,0,
        0,0,
        0,0,
        0,0,
        0,0]

uptime_internet = currtime

uptime = [currtime,currtime,
         currtime,currtime,
         currtime,currtime,
         currtime,currtime,
         currtime,currtime]



