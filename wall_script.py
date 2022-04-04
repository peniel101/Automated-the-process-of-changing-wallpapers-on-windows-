import os
import random
import ctypes
import time
from win10toast import ToastNotifier

# notify the that the program is running
notify = ToastNotifier()
notify.show_toast(
    title="Wallpaper Changer",
    msg="The script has been executed",
    duration=10
)


def set_wallpaper(path):
    list_wall = os.listdir(path)
    for wallpaper in range(0, len(list_wall)):
        # randomly choosing a wallpaper from the folder
        random_wallpaper = random.choice(list_wall)
        print(random_wallpaper)
        directory_wallpaper = os.path.join(path, random_wallpaper)
        #change_wallpaper = bytes(directory_wallpaper, "utf-8")
        print(directory_wallpaper)
        # changing the wallpaper
        location = os.getcwd()
        ctypes.windll.user32.SystemParametersInfoW(20, 0, directory_wallpaper)
        print("Wallpaper Changed.....")
        sleep_time = 10
        time.sleep(sleep_time)

# def autorun():
#     import winreg as reg
#     path = os.path.dirname(os.path.realpath(__file__))
#     print(path)
#     script_name = ""
#     address = os.join(path, script_name)
#     # changing the HKEY_CURRENT_USER
#     key = "HKEY_CURRENT_USER"
#     key_value = "Software\Microsoft\Windows\CurrentVersion\Run"
#     # open the key and make changes to it
#     open_key = reg.OpenKey(key, key_value, 0, reg.KEY_ALL_ACCESS)
#     # modified the open key
#     reg.SetValue(open_key,"Script", 0, reg.REG_SZ, address)
#     # closing the open key
#     reg.CloseKey(open_key)




path = r"G:\New folder things\Wallpapers"
set_wallpaper(path)