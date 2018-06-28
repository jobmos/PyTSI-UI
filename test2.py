import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from tkcalendar import Calendar, DateEntry


class CalenderUI():
    def __init__(self, root):
        self.top = tk.Toplevel(root)

        self.cal = Calendar(self.top, font="Arial 14", selectmode='day',
                            cursor="hand1", year=2018, month=2, day=5)
        self.cal.pack(fill="both", expand=True)
        ttk.Button(self.top, text="ok", command=self.print_sel).pack()
        ttk.Button(self.top, text="exit", command=self.quit1).pack()

        self.date = ''

        self.top.grab_set()

    def print_sel(self):
        self.date = self.cal.selection_get()

    def quit1(self):
        self.top.destroy()


class App:
    def __init__(self):
        self.root = tk.Tk()
        s = ttk.Style(self.root)
        s.theme_use('clam')

        size_x = 800
        size_y = 500
        self.root.geometry('{}x{}'.format(size_x, size_y))

        self.date = tk.StringVar()
        self.time = tk.StringVar()

        # image 1
        img = ImageTk.PhotoImage(Image.open('images/20170828112200.jpg'))
        panel1 = tk.Label(self.root, image=img)
        panel1.grid(row=3, column=1, rowspan=2, sticky='NSEW')

        # image 2
        img2 = ImageTk.PhotoImage(Image.open('images/20170828112200.png'))
        panel2 = tk.Label(self.root, image=img2)
        panel2.grid(row=3, column=2, rowspan=2, sticky='NSEW')

        # calendar
        cal_button = ttk.Button(self.root, text='Select date', command=self.get_date)
        cal_button.grid(row=3, column=4, columnspan=2, sticky='EW')

        # time
        self.e = tk.Entry(self.root, width=10)
        self.e.focus_set()
        self.e.grid(row=4, column=4)
        self.e.delete(0, tk.END)
        self.e.insert(0, 'hour:minute')
        self.e.bind('<Control-KeyRelease-a>')

        # time button
        time_button = tk.Button(self.root, text='Go', width=10, command=self.get_time)
        time_button.grid(row=4, column=5)

        # title
        title = tk.Text(self.root, height=1)
        title.insert(tk.INSERT, 'Select a date and time')
        title.grid(row=1, column=1, columnspan=5)

        # info
        info = tk.Text(self.root, height=3)
        info.insert(tk.INSERT, 'Cloud cover:x \nAzimuth:x \nAltitude:x')
        info.grid(row=6, column=1, columnspan=4)

        # alignments
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(5, weight=1)
        self.root.grid_rowconfigure(7, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(3, weight=1)
        self.root.grid_columnconfigure(6, weight=1)

        self.root.mainloop()

    def get_date(self):
        cal = CalenderUI(self.root)
        self.root.wait_window(cal.top)
        self.date = cal.date

    def get_time(self):
        self.time = self.e.get()


app = App()
print(app.date, app.time)
