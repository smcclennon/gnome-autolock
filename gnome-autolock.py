# github.com/smcclennon/gnome-autolock
import os, time, subprocess
for i in range(0, 150):  # Try to lock 150 times
    time.sleep(0.1)  # 150 x 0.1 = Try to lock for 15 seconds
    os.system("gnome-screensaver-command --lock")  # Attempt to lock
    lock_status = subprocess.getoutput("gnome-screensaver-command --query")  # Get current lock status
    if "The screensaver is inactive" not in lock_status:  # If the screensaver is active
        break  # Break from loop, stop trying to lock once successful