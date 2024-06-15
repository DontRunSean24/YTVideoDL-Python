import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pytube import YouTube

def download_video():
    url = entry_url.get()
    yt = YouTube(url)
    resolution = resolution_var.get()
    if resolution == "720p":
        stream = yt.streams.get_by_resolution("720p")
    elif resolution == "1080p":
        stream = yt.streams.get_highest_resolution()
    elif resolution == "2k":
        stream = yt.streams.get_by_resolution("1440p")
    elif resolution == "4k":
        stream = yt.streams.get_by_resolution("2160p")
    else:
        stream = yt.streams.get_by_itag(18)
    
    if stream:
        stream.download()
        status_label.config(text="Downloaded Success!")
    else:
        messagebox.showerror("Error", "Not a valid resolution.")

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

resolutions = ["720p", "1080p", "2k", "4k"]
resolution_var = tk.StringVar(value="720p")  # Default resolution if all others fail
for res in resolutions:
    radio_button = ttk.Radiobutton(root, text=res, variable=resolution_var, value=res, style='Dark.TRadiobutton')
    radio_button.pack()

download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack()

status_label = tk.Label(root, text="", fg="white", bg="#333333")
status_label.pack()
root.mainloop()
