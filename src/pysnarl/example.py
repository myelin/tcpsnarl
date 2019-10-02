#! /usr/bin/python
import PySnarl
if PySnarl.snGetVersion() != False:
    (major, minor) = PySnarl.snGetVersion()
    print("Found Snarl version",str(major)+"."+str(minor),"running.")
    PySnarl.snShowMessage("Test Message", "Hello World!")
else:
    print("Sorry Snarl does not appear to be running")
