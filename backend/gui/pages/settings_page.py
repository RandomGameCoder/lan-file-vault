import tkinter as tk
from tkinter import ttk

# importing parent Page class
from .basic_page import Page

class SettingsPage(Page):
    def __init__(self, parent, controller, theme_manager=None):
        # initialize the Frame class
        super().__init__(parent, controller, theme_manager)

        # create the title bar and content area
        self.title_bar("Settings", show_back=True, show_settings=False)
        self.content_area()
    
    def content_area(self):
        """ Create the content area for the settings page """
        pass