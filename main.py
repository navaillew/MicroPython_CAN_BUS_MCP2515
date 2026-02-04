from machine import Pin
import sys
import time
from canbus import Can, CanError, CanMsg, CanMsgFlag

can = Can(spi=0,spics=8)

ret = can.begin()
if ret != CanError.ERROR_OK:
    print("Error to initilize can!")
    sys.exit(1)
print("initlized succesufully!")