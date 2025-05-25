import customtkinter as ctk

class Header(ctk.CTkFrame):
    def __init__(self, parent, height, width, title="My app"):
        super().__init__(parent, height=height, width=width)
        label = ctk.CTkLabel(self, text=title, font=("Arial", 20))
        label.pack(pady=10)

class Footer(ctk.CTkFrame):
    def __init__(self, parent, height, width):
        super().__init__(parent, height=height, width=width)
        label = ctk.CTkLabel(self, text="Footer is here")
        label.pack(pady=5)