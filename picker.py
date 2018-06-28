try:
    import tkinter as tk
    from tkinter import ttk, Text, Entry, Button
except ImportError:
    import Tkinter as tk
    import ttk

from PIL import ImageTk, Image
from tkcalendar import Calendar, DateEntry

def cal_widget():
    def print_sel():
        print(cal.selection_get())

    top = tk.Toplevel(root)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=2018, month=2, day=5)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()

def date_entry_widget():
    top = tk.Toplevel(root)

    ttk.Label(top, text='Choose date').pack(padx=10, pady=10)

    cal = DateEntry(top, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
    cal.pack(padx=10, pady=10)


def print_time():
    print(e.get())


def on_enter(event):
    print(e.get())


def callback(event):
    # select text
    event.widget.select_range(0, 'end')
    # move cursor to the end
    event.widget.icursor('end')


root = tk.Tk()

size_x = 800
size_y = 500
root.geometry('{}x{}'.format(size_x, size_y))
s = ttk.Style(root)
s.theme_use('clam')

root.bind('<Return>', on_enter)

# image 1
img = ImageTk.PhotoImage(Image.open('images/20170828112200.jpg'))
panel = tk.Label(root, image = img)
panel.grid(row=3, column=1, rowspan=2, sticky='NSEW')

# image 2
img2 = ImageTk.PhotoImage(Image.open('images/20170828112200.png'))
panel = tk.Label(root, image = img2)
panel.grid(row=3, column=2, rowspan=2, sticky='NSEW')

# calendar
cal_button = ttk.Button(root, text='Select date', command=cal_widget)
cal_button.grid(row=3, column=4, columnspan=2, sticky='EW')

# time
e = Entry(root, width=10)
e.grid(row=4, column=4)
e.delete(0, tk.END)
e.insert(0, 'hour:minute')
e.bind('<Control-KeyRelease-a>', callback)

# time button
time_button = Button(root, text='Go', width=10, command=print_time)
time_button.grid(row=4, column=5)

# title
title = Text(root, height=1)
title.insert(tk.INSERT,'Select a date and time')
title.grid(row=1, column=1, columnspan=5)

# info
info = Text(root, height=3)
info.insert(tk.INSERT,'Cloud cover:x \nAzimuth:x \nAltitude:x')
info.grid(row=6, column=1, columnspan=4)

# alignments
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_rowconfigure(7, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(6, weight=1)


# ttk.Button(root, text='DateEntry', command=date_entry_widget).pack(padx=10, pady=10)

root.mainloop()
