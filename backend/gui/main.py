import tkinter as tk
from tkinter import ttk

# Importing all page modules
from pages.home_page import HomePage
from pages.settings_page import SettingsPage
from pages.status_page import StatusPage
from pages.file_manager_page import FileManagerPage
from pages.server_config_page import ServerConfigPage

# Importing the theme manager
from theme.theme_manager import ThemeManager

class App(tk.Tk):
    def __init__(self, width, height):
        # initialize the Tk class
        super().__init__()

        # setup of the app
        self.width = width
        self.height = height
        self.ThemeManager = ThemeManager()  # Initialize the theme manager
        self.frames = {}                    # Dictionary to hold all frames
        self.nav_stack = []                 # Stack to manage navigation history
        self.current_page = None             # Track the current page
        
        # initialize the main window
        self._init_window()

        # show the home page by default
        self.show_frame("HomePage")
    
    def _init_window(self):
        """Initialize the main window."""
        # set the title of the window
        self.title("Lan File Vault")

        # set offset for window to be in center of the screen
        xoffset = (self.winfo_screenwidth() - self.width) // 2
        yoffset = (self.winfo_screenheight() - self.height) // 2
        
        # set geometry of the window
        self.geometry(f"{self.width}x{self.height}+{xoffset}+{yoffset}")

        # create a container frame to hold all contents
        self.container = ttk.Frame(self)
        self.container.pack(fill=tk.BOTH, expand=True)
        
        # Configure container grid
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(0, weight=1)
        

        for F in (HomePage, SettingsPage, StatusPage, FileManagerPage, ServerConfigPage):
            # create a frame instance and add it to the container
            frame = F(parent=self.container, controller=self, theme_manager=self.ThemeManager)
            frame.grid(row=0, column=0, sticky="nsew")

            # add frame to the frames dictionary
            page_name = F.__name__
            self.frames[page_name] = frame

    def show_frame(self, page_name):
        """Show a frame for the given page name."""
        if self.current_page:
            self.nav_stack.append(self.current_page)
        frame = self.frames[page_name]
        frame.tkraise()
        self.current_page = page_name
        frame.apply_theme(self.container)  # Apply the theme to the current frame

if __name__ == "__main__":
    app = App(width=800, height=600)
    app.mainloop()