Ping_CMDR
David Ray

V0.01
***	Set up main menu and tried to get the device ping to work, but had issues.

V0.02
***	Created the UI and added script to ping CMDR, EZR, POS1, and POS2.
***	Added script to show if online or not by pinging http://www.google.com.

V0.03.00
***	Added script to UI lines to show red characters when the status is 'Down'.  This worked fine on my programming terminal, but on other's workstations it didn't work.

V0.03.01
***	Took scripting out for the red 'Down' characters.  Made all text a brighter white.

V0.03.02
***	Added the KnightRider scanner on the UI.
***	Changed the wait time between cycles from 0.5 to 1.0 to help keep the software from crashing during installations

V0.03.03
***	Used PyInstaller to compile the software into a single file.

V0.03.04
***	Rearranged the varible structure.

V0.03.05
***	Implemented justification arguments to all text printed to console.

V0.03.06
***	Corrected issues that arose from the justifications applied in V0.03.05.

V0.04.00
***	Complete rebuild of entire structure to incorportate menus.
***	Added the ability to set your NIC for Commander or DHCP with ease.
***	Now you can use the ping tool with/without checking pinpads.

V0.04.01
***	Rewrote script for compatiblity for Python 3.5.
***	Added a function to create a running log file for your pings.
***	Created a function to create a folder to store the log files if needed.