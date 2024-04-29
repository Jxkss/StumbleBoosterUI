import tkinter as tk
from PIL import Image, ImageTk
import pypresence as presence
import subprocess
import os
import psutil
import win32api
import win32process
import win32con
from colorama import init
from colorama import Fore, Back, Style
import time
import webbrowser   
from win10toast import ToastNotifier
import pystray
from PIL import Image

#def show_notification(icon):
    #print("Notification sans toast")

#icon = pystray.Icon("example_icon", Image.open("icon.png"), "Example Icon")

script_dir4 = os.path.dirname(os.path.abspath(__file__))
image_path4 = os.path.join(script_dir4, "settings.ico")
print("Image Path Ico:", image_path4)  # Debug statement
if os.path.exists(image_path4):
    print("Image Ico found")  # Debug statement
else:
    
    print("Image Ico Not Found")  # Debug statement

toast = ToastNotifier()

path_home = os.path.expanduser('~')

discord_presence_enabled = True

unity_executable = r"C:\Program Files (x86)\Steam\steamapps\common\Stumble Guys\Stumble Guys.exe"
discord_exe_path = (path_home+"\AppData\\Local\\Discord")
print(discord_exe_path)
discord_running = any(p.name() == "Update.exe" for p in psutil.process_iter())
if discord_running:
    print("running")
else:
    os.chdir(discord_exe_path)
    subprocess.Popen('Update.exe')
    print("not running")

def set_process_realtime_priority(process_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == process_name:
            pid = proc.info['pid']
            handle = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, False, pid)
            win32process.SetPriorityClass(handle, win32process.REALTIME_PRIORITY_CLASS)
            return 0
    time.sleep(3)

def handle_fps_boost():
    os.chdir("C:\Program Files (x86)\Steam\steamapps\common\Stumble Guys\ ")
    subprocess.Popen([unity_executable, "-qualitysettings-frameRate=Unlimited"])
    return 0

def handle_high_priority():
    high_priority_button.config(text="Loading...", fg="white", font=("Coolvetica Rg", 12, "italic"), state="active")
    set_process_realtime_priority("Stumble Guys.exe")
    high_priority_button.config(text="Set High Priority (ON)", fg="green", font=("Coolvetica Rg", 12, "italic"), state="disabled")
    toast.show_toast(
    "StumbleBooster",
    "High Priority For Stumble Guys Turned On!",
    duration = 0.5,
    icon_path = image_path4,
    threaded = True,
    
)

def toggle_discord_presence():
    global discord_presence_enabled
    if discord_presence_enabled:
        rpc.clear()
        discord_presence_enabled = False
        discord_toggle_button.config(text="Toggle Discord Presence (OFF)", fg="red")
    else:
        rpc.update(
            state="Version 2.0.3 - Working On StumbleGuys...",
            large_image="stumblebooster",
            large_text="Stumble Booster v",
            buttons=[{"label": "Check It Out!", "url": "https://discord.gg/HMmrVM54r8"}]
        )
        discord_presence_enabled = True
        discord_toggle_button.config(text="Toggle Discord Presence (ON)", fg="green")

def gamemode_activation():
    subprocess.run('reg add "HKCU\SOFTWARE\Microsoft\GameBar" /v "AllowAutoGameMode" /t REG_DWORD /d "1" /f')
    subprocess.run('reg add "HKCU\SOFTWARE\Microsoft\GameBar" /v "AutoGameModeEnabled" /t REG_DWORD /d "1" /f')
    gamemode_button.config(text="Game Mode Regs (ON)", fg="green", font=("Coolvetica Rg", 12, "italic"), state="disabled")
    toast.show_toast(
      "StumbleBooster",
      "Game Mode Regs Activated!",
       duration = 0.5,
       icon_path = image_path4,
       threaded = True
    )
    return 0

settings_window_open = False

def open_settings_window():
    global settings_window_open
    
    if not settings_window_open:
        settings_window_open = True
        settings_window = tk.Toplevel(root)
        settings_window.resizable(False, False)
        settings_window.title("StumbleBooster Settings")
        settings_window.geometry("400x340")
        settings_window.configure(bg="black")
        settings_window.protocol("WM_DELETE_WINDOW", lambda: on_settings_window_close(settings_window))
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "SGbest2.png")
        if os.path.exists(image_path):
            image = Image.open(image_path)
            photo = ImageTk.PhotoImage(image)
            image_label = tk.Label(settings_window, image=photo, bg="black")
            image_label.image = photo
            image_label.pack(pady=20)
        else:
            print("Settings Image Not Found")
        
        def discord_toggle():
            webbrowser. open('https://discord.gg/6mMsTdSgMN')
        
        def credit_handler():
            credit = tk.Toplevel(root)
            credit.resizable(False, False)
            credit.title("StumbleBooster Credits")
            credit.geometry("400x340")
            credit.configure(bg="black")
            script_dir4 = os.path.dirname(os.path.abspath(__file__))
            image4_path = os.path.join(script_dir4, "SGbest3.png")
            if os.path.exists(image4_path):
                image4 = Image.open(image4_path)
                photo = ImageTk.PhotoImage(image4)
                image4_label = tk.Label(credit, image=photo, bg="black")
                image4_label.image = photo
                image4_label.pack(pady=0)
            else:
              print("Settings Image Not Found")
            
            

        discord_button = tk.Button(settings_window, text="Join Discord", font=("Coolvetica Rg", 12), fg="DodgerBlue2", bg="black", bd=3, relief=tk.RAISED, command=discord_toggle, highlightbackground="white", highlightthickness=1)
        discord_button.pack(pady=10, padx=20, ipadx=10, ipady=5)

        
        credits_button = tk.Button(settings_window, text="View Credits", font=("Coolvetica Rg", 12), fg="grey80", bg="black", bd=3, relief=tk.RAISED, command=credit_handler, highlightbackground="white", highlightthickness=1)
        credits_button.pack(pady=10, padx=20, ipadx=10, ipady=5)
        
        settings_window.protocol("WM_DELETE_WINDOW", on_settings_window_close)
        close_button = tk.Button(settings_window, text="Close", font=("Coolvetica Rg", 12), fg="white", bg="black", bd=3, relief=tk.RAISED, command=lambda: on_settings_window_close(settings_window), highlightbackground="white", highlightthickness=1)
        close_button.pack()
        version_label = tk.Label(settings_window, text="StumbleBooster v2.0.3 - Jxks", font=("Coolvetica Rg", 10), fg="white", bg="black")
        version_label.place(relx=0.5, rely=1.0, anchor="s")
        
def on_settings_window_close(window):
    global settings_window_open
    settings_window_open = False
    window.destroy()
    return 0

root = tk.Tk()
script_dir3 = os.path.dirname(os.path.abspath(__file__))
image_path3 = os.path.join(script_dir3, "stumblebooster.ico")
print("Image Path:", image_path3)  # Debug statement
if os.path.exists(image_path3):
    icon = tk.PhotoImage(file=image_path3)
    root.iconphoto(True, icon)
    print("Image icon Loaded Successfully")  # Debug statement
else:
    print("Image icon Not Found")  # Debug statement
root.title("StumbleBooster")
root.geometry("400x460")
root.configure(bg="black")
root.resizable(False, False)

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "Settings.ico")
print("Image Path:", image_path)  # Debug statement
if os.path.exists(image_path):
    image1 = Image.open(image_path)
    photo1 = ImageTk.PhotoImage(image1)
    print("Image Loaded Successfully")  # Debug statement
else:
    print("Image Not Found")  # Debug statement

rpc = presence.Presence("1219605281181401200")
rpc.connect()


rpc.update(
    state="Version 2.0.3 - Working On StumbleGuys...",
    large_image="stumblebooster",
    large_text="Stumble Booster v2.0.3",
    buttons=[{"label": "Check It Out!", "url": "https://discord.gg/HMmrVM54r8"}]
)

script_dir1 = os.path.dirname(os.path.abspath(__file__))
image_path1 = os.path.join(script_dir1, "SGBest.png")
print("Image Path:", image_path1)  # Debug statement
if os.path.exists(image_path1):
    image2 = Image.open(image_path1)
    photo2 = ImageTk.PhotoImage(image2)
    print("Image Loaded Successfully")  # Debug statement
else:
    print("Image Not Found")  # Debug statement


image2_label = tk.Label(root, image=photo2, bg="black")
image2_label.image = photo2
image2_label.pack(pady=20)

image1_label = tk.Label(root, image=photo1, bg="black")
image1_label.image = photo1
image1_label.place(relx=0, rely=1.0, anchor="sw")
image1_label.bind("<Button-1>", lambda event: open_settings_window())

fps_button = tk.Button(root, text="Start Boosted StumbleGuys", font=("Coolvetica Rg", 12), fg="grey80", bg="black", bd=3, relief=tk.RAISED, command=handle_fps_boost, highlightbackground="white", highlightthickness=1)
fps_button.pack(pady=10, padx=20, ipadx=10, ipady=5)

high_priority_button = tk.Button(root, text="Set High Priority (OFF)", font=("Coolvetica Rg", 12), fg="red", bg="black", bd=3, relief=tk.RAISED, command=handle_high_priority, highlightbackground="white", highlightthickness=1)
high_priority_button.pack(pady=10, padx=20, ipadx=10, ipady=5)

gamemode_button = tk.Button(root, text="Game Mode Regs (OFF)", font=("Coolvetica Rg", 12), fg="red", bg="black", bd=3, relief=tk.RAISED, command=gamemode_activation, highlightbackground="white", highlightthickness=1)
gamemode_button.pack(pady=10, padx=20, ipadx=10, ipady=5)

discord_toggle_button = tk.Button(root, text="Toggle Discord Presence (ON)", font=("Coolvetica Rg", 12), fg="green", bg="black", bd=3, relief=tk.RAISED, command=toggle_discord_presence, highlightbackground="white", highlightthickness=1)
discord_toggle_button.pack(pady=10, padx=20, ipadx=10, ipady=5)

root.protocol("WM_DELETE_WINDOW", on_settings_window_close)
close_button = tk.Button(root, text="Close", font=("Coolvetica Rg", 12), fg="white", bg="black", bd=3, relief=tk.RAISED, command=lambda: on_settings_window_close(root), highlightbackground="white", highlightthickness=1)
close_button.pack()

version_label = tk.Label(root, text="StumbleBooster v2.0.3 - Jxks", font=("Coolvetica Rg", 10), fg="white", bg="black")
version_label.place(relx=0.5, rely=1.0, anchor="s")


root.mainloop()