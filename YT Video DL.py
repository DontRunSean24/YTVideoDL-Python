import os
import tkinter as tk
import configparser
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from pytube import YouTube


def download_video():
    status_label.config(text="Downloading video...")
    root.update()
    url = entry_url.get()
    
    try:
        yt = YouTube(url)
        resolution = resolution_var.get()
        if resolution == "720p":
            stream = yt.streams.get_by_resolution("720p")
        elif resolution == "1080p":
            stream = yt.streams.get_highest_resolution()
        else:
            stream = yt.streams.get_by_itag(18)
        
        if stream:
            config_exists = os.path.isfile('config.ini')
            if config_exists:
                config = configparser.ConfigParser()
                config.read('config.ini')
                download_path = config['DEFAULT']['download_path']
            else:
                download_path = filedialog.askdirectory(title="Select Download Location")
            
            if download_path:
                stream.download(download_path)
                status_label.config(text="Downloaded Success!")
                if not config_exists:
                    config = configparser.ConfigParser()
                    config['DEFAULT'] = {'download_path': download_path}
                    with open('config.ini', 'w') as configfile:
                        config.write(configfile)
            else:
                status_label.config(text="No download location selected.")
        else:
            status_label.config(text="No video found.")
    except Exception as e:
        status_label.config(text="Error: " + str(e))


root = tk.Tk()
root.title("YouTube Downloader")
root.configure(bg="#333333")
root.resizable(False, False)

label = tk.Label(root, text="Enter YouTube URL:", fg="white", bg="#333333")
label.pack()
entry_url = tk.Entry(root, width=50)
entry_url.pack()

s = ttk.Style()
s.configure('Dark.TRadiobutton', foreground='white', background='#333333', selectcolor='#000000')
resolutions = ["720p", "1080p"]
resolution_var = tk.StringVar(value="720p")
for res in resolutions:
    radio_button = ttk.Radiobutton(root, text=res, variable=resolution_var, value=res, style='Dark.TRadiobutton')
    radio_button.pack()

download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack()
status_label = tk.Label(root, text="", fg="white", bg="#333333")
status_label.pack()
root.mainloop()
