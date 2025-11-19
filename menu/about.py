from tkinter import Menu
import webbrowser

def open_url(url):
    webbrowser.open_new(url)

def about(menubar):
    about_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="About", menu=about_menu)
    about_menu.add_command(label="Aplikasi Pengolahan Citra Digital", state="disabled")
    about_menu.add_separator()
    about_menu.add_command(label="Developed by:", state="disabled")

    ridwan = Menu(about_menu, tearoff=0)
    about_menu.add_cascade(label="  • Muhammad Ridwan", menu=ridwan)
    ridwan.add_command(label="https://github.com/Riidwann", command=lambda:open_url("https://github.com/Riidwann"))

    arif = Menu(about_menu, tearoff=0)
    about_menu.add_cascade(label="  • Muhammad Arif Syafitra", menu=arif)
    arif.add_command(label="https://github.com/Rifsy2", command=lambda:open_url("https://github.com/Rifsy2"))

    dani = Menu(about_menu, tearoff=0)
    about_menu.add_cascade(label="  • Safrin Nada Ramdhani", menu=dani)
    dani.add_command(label="https://github.com/Danydanz", command=lambda:open_url("https://github.com/Danydanz"))
    
    about_menu.add_separator()
    about_menu.add_command(label="Find us at:", state="disabled")
    about_menu.add_command(label="  Source Code", command=lambda: open_url("https://github.com/Riidwann"))
    about_menu.add_command(label="  YouTube", command=lambda: open_url("https://youtube.com/channel-anda"))