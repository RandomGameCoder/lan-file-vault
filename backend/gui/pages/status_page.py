import tkinter as tk
from tkinter import ttk

# importing parent Page class
from .basic_page import Page

class StatusPage(Page):
    def __init__(self, parent, controller):
        # initialize the Frame class
        super().__init__(parent, controller)

        # create the title bar and content area
        self.title_bar("Status", show_back=True)
        self.content_area()
    
    def title_bar(self, title, show_back):
        """ Create a title bar for the home page """
        super().title_bar(title, show_back)
    
    def content_area(self):
        """ Create the content area for the settings page """
        pass