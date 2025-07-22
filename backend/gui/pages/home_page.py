import tkinter as tk
from tkinter import ttk

# importing parent Page class
from .basic_page import Page

class HomePage(Page):
    def __init__(self, parent, controller, theme_manager=None):
        # initialize the Frame class
        super().__init__(parent, controller, theme_manager)

        # create the title bar and content area
        self.title_bar("Lan File Vault")
        self.content_area()
    
    def content_area(self):
        """ Create the content area for the home page """
        content_frame = ttk.Frame(self)
        content_frame.grid(row=1, column=0, sticky="nsew", pady=(0, 20), padx=20)
        content_frame.grid_columnconfigure(0, weight=1)
        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_rowconfigure(1, weight=1)
        
        ### get status of storage ###
        status_button = ttk.Button(
            content_frame, 
            text="📊 Status\nServer Storage Info", 
            command=lambda: self.controller.show_frame("StatusPage"),
            width=25
        )
        status_button.grid(row=0, column=0, pady=20, ipady=15)

        # Configure status button font
        style = ttk.Style()
        style.configure("Large.TButton", font=("Arial", 12, "bold"))
        status_button.configure(style="Large.TButton")

        # Bottom buttons frame (positioned at bottom)
        bottom_buttons_frame = ttk.Frame(content_frame)
        bottom_buttons_frame.grid(row=1, column=0, sticky="nsew")

        # Configure grid for centering buttons within their cells
        bottom_buttons_frame.grid_columnconfigure(0, weight=1)
        bottom_buttons_frame.grid_columnconfigure(1, weight=1)
        bottom_buttons_frame.grid_rowconfigure(0, weight=1)

        # file manager button
        file_manager_btn = ttk.Button(
            bottom_buttons_frame, 
            text="📁 File Manager", 
            command=lambda: self.controller.show_frame("FileManagerPage"),
            width=18
        )
        file_manager_btn.grid(row=0, column=0, padx=(0, 10), pady=5, ipady=30, sticky="")
        file_manager_btn.configure(style="Square.TButton")

        # Server Config button with icon
        server_config_btn = ttk.Button(
            bottom_buttons_frame, 
            text="⚙️ Server Config", 
            command=lambda: self.controller.show_frame("ServerConfigPage"),
            width=18
        )
        server_config_btn.grid(row=0, column=1, padx=(10, 0), pady=5, ipady=30, sticky="")
        server_config_btn.configure(style="Square.TButton")
