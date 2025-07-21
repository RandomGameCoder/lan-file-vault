import tkinter as tk
from tkinter import ttk

# Importing all page modules
from pages.home_page import HomePage
from pages.settings_page import SettingsPage
from pages.status_page import StatusPage
from pages.file_manager_page import FileManagerPage
from pages.server_config_page import ServerConfigPage

class App(tk.Tk):
    def __init__(self, width, height):
        # initialize the Tk class
        super().__init__()

        # set the title of the app
        self.title("Lan File Vault")

        # set offset for window to be in center of the screen
        xoffset = (self.winfo_screenwidth() - width) // 2
        yoffset = (self.winfo_screenheight() - height) // 2
        
        # set geometry of the window
        self.geometry(f"{width}x{height}+{xoffset}+{yoffset}")

        # create a container frame to hold all contents
        self.container = ttk.Frame(self)
        self.container.pack(fill=tk.BOTH, expand=True)
        
        # Configure container grid
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(0, weight=1)

        # dictionary to hold all pages
        self.frames = {}

        for F in (HomePage, SettingsPage, StatusPage, FileManagerPage, ServerConfigPage):
            # create a frame instance and add it to the container
            frame = F(parent=self.container, controller=self)
            frame.grid(row=0, column=0, sticky="nsew")

            # add frame to the frames dictionary
            page_name = F.__name__
            self.frames[page_name] = frame
        
        # show the home page by default
        self.show_frame("HomePage")

    def show_frame(self, page_name):
        """Show a frame for the given page name."""
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = App(width=800, height=600)
    app.mainloop()