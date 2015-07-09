import win32com.client
import time

while True:
    win32com.client.Dispatch("WScript.Shell").SendKeys('d')
    time.sleep(1)
