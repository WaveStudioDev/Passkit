# gui/animations.py

import tkinter as tk

def fade_in(widget, duration=500):
    """Fade in a widget over a specified duration."""
    widget.attributes('-alpha', 0)  # Start fully transparent

    def _fade():
        current_alpha = widget.attributes('-alpha')
        if current_alpha < 1.0:
            widget.attributes('-alpha', current_alpha + 0.05)
            widget.after(int(duration / 20), _fade)  # Repeat every 20 ms

    _fade()

def fade_out(widget, duration=500):
    """Fade out a widget over a specified duration."""
    widget.attributes('-alpha', 1)  # Start fully opaque

    def _fade():
        current_alpha = widget.attributes('-alpha')
        if current_alpha > 0:
            widget.attributes('-alpha', current_alpha - 0.05)
            widget.after(int(duration / 20), _fade)  # Repeat every 20 ms
        else:
            widget.withdraw()  # Hide the widget after fading out

    _fade()

def slide_in(widget, duration=500):
    """Slide in a widget from the left over a specified duration."""
    widget.place(x=-widget.winfo_width(), y=widget.winfo_y())  # Start off-screen

    def _slide():
        current_x = widget.winfo_x()
        if current_x < 0:
            widget.place(x=current_x + 5)  # Move 5 pixels to the right
            widget.after(int(duration / (widget.winfo_width() / 5)), _slide)  # Adjust speed

    _slide()

def slide_out(widget, duration=500):
    """Slide out a widget to the left over a specified duration."""
    def _slide():
        current_x = widget.winfo_x()
        if current_x > -widget.winfo_width():
            widget.place(x=current_x - 5)  # Move 5 pixels to the left
            widget.after(int(duration / (widget.winfo_width() / 5)), _slide)  # Adjust speed
        else:
            widget.withdraw()  # Hide the widget after sliding out

    _slide()