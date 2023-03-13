"""
Program that converts from WGS84 to L-Est97 coordinate system and vice versa.

Author: Danyil Kurbatov
"""

import tkinter as tk
import tkinter.messagebox
from tkinter import *

from pyproj import Transformer


def convert_wgs_to_est(lat: float, lon: float) -> tuple:
    """Convert from WGS84 coordinate system into L-Est97 coordinate system."""
    transformer = Transformer.from_crs("EPSG:4326", "EPSG:3301")
    x, y = transformer.transform(lat, lon)

    return round(x, 2), round(y, 2)


def convert_est_to_wgs(lat: float, lon: float) -> tuple:
    """Convert from L-Est97 coordinate system into WGS84 coordinate system."""
    transformer = Transformer.from_crs("EPSG:3301", "EPSG:4326")
    x, y = transformer.transform(lat, lon)

    return round(x, 6), round(y, 6)


def converter_ui():
    """Main method for drawing a graphical converter by using tkinter elements."""

    def conversion():
        """Make a conversion according to the person's chose and display the result."""
        if op.get() == 1:
            x, y = convert_wgs_to_est(x1.get(), y1.get())
            tk.messagebox.showinfo('Converted result', f'X={str(x)} \nY={str(y)}')
        elif op.get() == 2:
            x, y = convert_est_to_wgs(x1.get(), y1.get())
            tk.messagebox.showinfo('Converted result', f'X={str(x)} \nY={str(y)}')

    window = tk.Tk()
    window.title('GEO converter')
    window.geometry("500x300")

    # Longitude entry
    tk.Label(window, text='Longitude').place(x=30, y=50)
    x1 = tk.StringVar()
    Entry(window, width=20, textvariable=x1).place(x=100, y=50)

    # Latitude entry
    tk.Label(window, text='Latitude').place(x=30, y=90)
    y1 = tk.StringVar()
    Entry(window, width=20, textvariable=y1).place(x=100, y=90)

    # Radio buttons
    op = tk.IntVar()
    op.set(1)
    tk.Radiobutton(window, text='wgs84 to est97', variable=op, value=1).place(x=30, y=130)
    tk.Radiobutton(window, text='est97 to wgs84', variable=op, value=2).place(x=30, y=150)

    # Calculate button
    tk.Button(window, text="Convert", activebackground="pink", activeforeground="blue", command=conversion).place(
        x=30, y=180)

    window.mainloop()


if __name__ == '__main__':
    converter_ui()
