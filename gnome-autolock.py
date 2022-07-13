# github.com/smcclennon/gnome-autolock
import os, time, subprocess
for _ in range(150):
    time.sleep(0.1)  # 150 x 0.1 = Try to lock for 15 seconds
    os.system("gnome-screensaver-command --lock")  # Attempt to lock
    lock_status = subprocess.getoutput("gnome-screensaver-command --query")  # Get current lock status
    if "The screensaver is inactive" not in lock_status:  # If the screensaver is active
        break  # Break from loop, stop trying to lock once successful