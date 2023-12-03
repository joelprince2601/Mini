import os
import time

usb_path = "/media/pi/USB_DRIVE"

=file_name = "my_script.py"

while True:
    if os.path.exists(usb_path):
        print("USB drive detected!")
        # Check if the Python file exists in the USB drive
        if os.path.exists(os.path.join(usb_path, file_name)):
            print("Running Python script...")
            # Run the Python file using the os.system() function
            os.system("python " + os.path.join(usb_path, file_name))
        else:
            print("Python script not found in USB drive.")
        # Wait for 5 seconds before checking again
        time.sleep(5)
    else:
        print("USB drive not detected.")
        # Wait for 5 seconds before checking again
        time.sleep(5)
