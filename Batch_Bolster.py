import os
import sys
import subprocess
import time
import psutil
import ntpath
from datetime import datetime

def printCurrTime():
    print(datetime.now().strftime("%B %d, %Y \t %H:%M:%S"))

full_path_bat = ''

#No comand line args, get user input
if(len(sys.argv) == 1):
    full_path_bat = input('Enter in the full path of your bat file you would like to keep running: ')
elif(len(sys.argv) == 2):
    full_path_bat = sys.argv[1]
else:
    print('Too many command line arguments.\n\tUssage:\n\tBatch_bolster.py fullFileBathOfBatchFile')
    exit(3)
    
#Check if batch file exists
if not os.path.isfile(full_path_bat):
    print('Cannot find batch file. Check the name and path: ' + full_path_bat)

head, tail = ntpath.split(full_path_bat)

os.chdir(head)

print('Starting your batch in')
print('3...')
time.sleep(1)
print('2...')
time.sleep(1)
print('1...')
time.sleep(1)
print('Process started at:')
printCurrTime()

pid = subprocess.Popen(full_path_bat, creationflags=subprocess.CREATE_NEW_CONSOLE).pid

while(True):
    #Sleep for 1 minute
    time.sleep(60)
    
    #Check if pid is still running
    if not psutil.pid_exists(pid):
        #If its not running, run the bat again and update the pid
        pid = subprocess.Popen(full_path_bat, creationflags=subprocess.CREATE_NEW_CONSOLE).pid
        print('Process restarted at:')
        printCurrTime()