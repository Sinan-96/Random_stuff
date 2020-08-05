import math
from typing import List, Any

import time
import datetime
import pathlib
import serial.tools.list_ports


path = r"C:\Users\Sinan\Documents\Datasett\Tempratur og fuktighet" + "\\" + datetime.datetime.now().strftime("%m_%d_%Y") + ".txt" #Creates new file with the current date at end of file name
file = pathlib.Path(path)
if not file.exists():
    file = open(path, "w+")
    file.close()
file = open(path,"a")
ports = list(serial.tools.list_ports.comports())

#Goes through every port, and
#checks if it as the name standard in ite
#the port which is used does not have
#standard in its name, at least for me
for p in ports:
    if "Standard" not in p.description:
        ser = serial.Serial(p.device,9600)

while ser.readline()is not None:# continiues as long as the serial port is providing new data
    b = ser.readline()  # read a byte string
    string_n = b.decode()  # decode byte string into Unicode
    string = string_n.rstrip() # remove \n and \r
    currentDay = datetime.datetime.now().weekday()#saves the current weekday
    timestr =datetime.datetime.now().strftime("%m/%d/%Y   %H:%M:%S") # Datetime to string without microseconds (Timestamp)
    data_n_time = string + "   " + timestr
    file.write("\n")
    file.write(data_n_time)
    file.flush()
    time.sleep(2)
    if datetime.datetime.now().weekday() != currentDay: #Checks if it is the same day, if not create a new file
        path = r"C:\Users\Sinan\Documents\Datasett\Tempratur og fuktighet" + "\\" + datetime.datetime.now().strftime("%m_%d_%Y") + ".txt"
        file = open(path, "w+")
        file.close()
        file = open(path, "a")

file.close()# close the data file
ser.close() # if no new data comes



