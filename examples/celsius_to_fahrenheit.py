import tkinter as tk
from tkinter import ttk


class CelsiusToFahrenheit:
    def __init__(self, root) -> None:
        root.title("Image Browser")
        root.geometry(self.center_geometry(root))
        root.resizable(False, False)

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=tk.NSEW)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.celsius = tk.StringVar()
        celsius_entry = ttk.Entry(
            mainframe,
            width=10,
            textvariable=self.celsius,
        )
        celsius_entry.grid(column=2, row=1, sticky=tk.EW)

        self.fahrenheit = tk.StringVar()
        ttk.Label(
            mainframe,
            textvariable=self.fahrenheit,
        ).grid(column=2, row=2, sticky=tk.EW)

        ttk.Button(
            mainframe,
            text="Convert",
            command=self.convert,
        ).grid(column=3, row=3, sticky=tk.W)

        ttk.Label(
            mainframe,
            text="\N{DEGREE SIGN}C",
        ).grid(column=3, row=1, sticky=tk.W)
        ttk.Label(
            mainframe,
            text="\N{DEGREE SIGN}F",
        ).grid(column=3, row=2, sticky=tk.W)
        ttk.Label(
            mainframe,
            text="is equivalent to",
        ).grid(column=1, row=2, sticky=tk.E)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        celsius_entry.focus()
        root.bind("<Return>", lambda event: self.convert())

    def center_geometry(self, root: tk.Tk):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        WINDOW_WIDTH = 1600
        WINDOW_HEIGHT = 900

        position_right = int((screen_width - WINDOW_WIDTH) / 2)
        position_top = int((screen_height - WINDOW_HEIGHT) / 2)

        return f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{position_right}+{position_top}"

    def convert(self):
        try:
            value = float(self.celsius.get())
            self.fahrenheit.set(str((value * 9 / 5) + 32))
        except ValueError:
            pass


if __name__ == "__main__":
    root = tk.Tk()
    CelsiusToFahrenheit(root=root)
    root.mainloop()
