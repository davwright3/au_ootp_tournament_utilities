import customtkinter as ctk

class CustomInputDialog(ctk.CTkToplevel):
    def __init__(self, parent, title="Input", prompt="Enter value"):
        super().__init__(parent)
        self.title(title)
        self.geometry("300x150")
        self.grab_set()
        self.transient(parent)

        self.user_input = None

        self.label = ctk.CTkLabel(self, text=prompt)
        self.label.pack(pady=(20,10))

        self.entry = ctk.CTkEntry(self)
        self.entry.pack(pady=5, padx=20)
        self.entry.focus_set()

        self.confirm_button = ctk.CTkButton(self, text="OK", command=self._on_confirm)
        self.confirm_button.pack(pady=10)

        self.bind("<Return>", lambda e: self._on_confirm())

    def _on_confirm(self):
        self.user_input = self.entry.get()
        self.destroy()

    def get_input(self):
        self.wait_window()
        return self.user_input

