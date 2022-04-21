from pytube import YouTube
import tkinter as tk

resolutions = ['144p', '240p', '360p', '480p', '720p', '1080p']
window_width = 300
window_height = 150


def main():
    # initialize the window
    root = tk.Tk()
    root.title("YouTube Downloader")
    root.geometry(f"{window_width}x{window_height}")
    root.resizable(False, False)
    # label
    tk.Label(root, text="Enter YouTube URL:").pack()
    # text box
    entry = tk.Entry(root, width=40)
    entry.pack()
    # label
    tk.Label(root, text="Select Quality").pack()
    # dropdown menu
    variable = tk.StringVar(root)
    variable.set(resolutions[0])
    resolutions_dropdown = tk.OptionMenu(root, variable, resolutions[0], resolutions[1], resolutions[2],
                                         resolutions[3], resolutions[4], resolutions[5])
    resolutions_dropdown.pack()
    # download button
    button = tk.Button(root, text="Download", command=lambda: download(entry.get(), variable.get()))
    button.pack()
    root.mainloop()


def download(url: str, resolution: str):
    yt = YouTube(url)
    yt.streams.filter(res=resolution).first().download()


if __name__ == '__main__':
    main()
