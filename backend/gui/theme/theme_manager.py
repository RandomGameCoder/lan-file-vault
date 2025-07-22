from tkinter.ttk import Style
import json
import os

class ThemeManager:
    def __init__(self):
        self.theme = "dark"  # or "dark"
        self.colors = json.load(open(os.path.join(os.path.dirname(__file__), "themes.json"), "r"))

        self.style = Style()
        self.style.theme_use("clam")  # Use a base theme that supports ttk styles

        self.configure_style()

    def configure_style(self):
        """ Configures ttk base style in the current theme """

        bg = self.colors[self.theme]["bg"]
        fg = self.colors[self.theme]["fg"]
        accent = self.colors[self.theme]["accent"]

        # configure each style
        self.style.configure("Themed.TFrame", background=bg)
        self.style.configure("Accent.TFrame", background=accent)
        self.style.configure("Themed.TLabel", background=bg, foreground=fg)
        self.style.configure("Accent.TLabel", background=accent, foreground=fg)
        self.style.configure("Themed.TButton", background=self.colors[self.theme]["button_bg"], foreground=fg)
        self.style.map("Themed.TButton", 
            background=[
                ("active", self.colors[self.theme]["active_bg"]),
                ("disabled", self.colors[self.theme]["disabled_bg"]),
                ("pressed", self.colors[self.theme]["pressed_bg"]),
                ("focus", self.colors[self.theme]["focused_bg"])
            ],
            foreground=[
                ("disabled", self.colors[self.theme]["disabled_fg"]),
            ],
        )
        self.style.configure("Themed.TEntry", fieldbackground=bg, foreground=fg)
    
    def set_theme(self, theme_name):
        if theme_name in self.colors:
            self.theme = theme_name
    
