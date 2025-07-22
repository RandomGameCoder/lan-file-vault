import tkinter as tk
from tkinter import ttk

class Page(ttk.Frame):
    def __init__(self, parent, controller, theme_manager=None):
        # initialize the Frame class
        super().__init__(parent)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # set the navigation controller for the frame
        self.controller = controller

        # set the theme manager if provided
        self.theme_manager = theme_manager
    
    def title_bar(self, title, show_back=False, show_settings=True):
        """ Create a title bar for the page """
        top_frame = ttk.Frame(self)
        top_frame.grid(row=0, column=0, sticky="ew", pady=20, padx=20)
        top_frame.grid_columnconfigure(1, weight=1)  # Make column 1 expand

        self.title_label = ttk.Label(top_frame, text=title, font=("Arial", 24))
        self.title_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # frame to hold the buttons
        button_frame = ttk.Frame(top_frame)
        button_frame.grid(row=0, column=1, sticky="e")

        if show_back:
            self.back_button = ttk.Button(button_frame, text="← Back", command=lambda: self.controller.show_frame("HomePage"))
            self.back_button.grid(row=0, column=0, padx=(0, 10))
        else:
            self.back_button = None  # if you want to check later

        if show_settings:
            self.settings_button = ttk.Button(button_frame, text="Settings", command=lambda: self.controller.show_frame("SettingsPage"))
            self.settings_button.grid(row=0, column=1, padx=10, pady=10)
        else:
            self.settings_button = None
        
        # Apply theme to the title bar
        if self.theme_manager:
            self._apply_accent(top_frame)
    
    def content_area(self):
        """ Create the content area for the home page """
        pass

    def _apply_accent(self, widget):
        """ Apply accent colors to a widget and its children """
        widget_type = widget.winfo_class()

        try:
            if widget_type in ["TFrame", "Frame"]:
                widget.configure(style="Accent.TFrame")
            elif widget_type in ["TLabel", "Label"]:
                widget.configure(style="Accent.TLabel")
        except tk.TclError:
            pass

        for child in widget.winfo_children():
            self._apply_accent(child)
        

    def apply_theme(self, widget):
        """
        Recursively apply a theme dictionary { "bg": ..., "fg": ... } to self and all child widgets.
        """
        theme = self.theme_manager.theme

        def _apply(widget):
            widget_type = widget.winfo_class()

            if "style" in widget.configure() and widget.cget("style").startswith("Accent."):
                widget_type = None

            try:
                if widget_type in ["TFrame", "Frame"]:
                    widget.configure(style="Themed.TFrame")
                elif widget_type in ["TLabel", "Label"]:
                    widget.configure(style="Themed.TLabel")
                elif widget_type in ["TButton", "Button"]:
                    widget.configure(style="Themed.TButton")
                elif widget_type in ["TEntry", "Entry"]:
                    widget.configure(style="Themed.TEntry")
                elif widget_type in ["Canvas"]:
                    widget.configure(background=self.theme_manager.colors[theme]["bg"])
            except tk.TclError:
                pass

            for child in widget.winfo_children():
                _apply(child)

        _apply(widget)
        
