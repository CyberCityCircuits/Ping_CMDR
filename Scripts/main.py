# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 14:51:14 2017

@author: DREAM
"""

import var, tasks

import os


#define cosole size and color
os.system("mode con: cols=" + str(var.width) + " lines=" + str(var.lines))
os.system("color F")
os.system("cls")
os.system("echo off")


if __name__ == "__main__":
    tasks.logo()
    tasks.main_menu()
    tasks.mk_log()
    tasks.set_console()
    tasks.set_date_time()
    tasks.init_date_time()
    while 1==1:
        tasks.set_date_time()
        if var.diag == (1):
            var.loop_count +=  1
        for i in var.dev_range:
            tasks.ping(i)
        tasks.ping_internet()
        tasks.check_status_internet()
        tasks.check_status_dev()
        tasks.set_uptime()
        tasks.ui_screen()
        tasks.sleep(0.5)
            