"""Frame for selecting card years."""
import customtkinter as ctk


class YearValueSelectFrame(ctk.CTkFrame):
    """Frame for getting needed information from user."""
    def __init__(self, parent):
        ctk.CTkFrame.__init__(self, parent, border_color='gray', border_width=2)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        self.min_year = ctk.StringVar(value='1871')
        self.max_year = ctk.StringVar(value='2025')

        self.frame_label = ctk.CTkLabel(
            self,
            text='Year Select',
        )
        self.frame_label.grid(row=0, column=0, columnspan=4, sticky='nsew')

        self.min_label = ctk.CTkLabel(
            self,
            text='Min'
        )
        self.min_label.grid(row=1, column=0)

        self.min_entry = ctk.CTkEntry(
            self,
            textvariable=self.min_year,
            width=40,
        )
        self.min_entry.grid(row=1, column=1)

        self.max_label = ctk.CTkLabel(
            self,
            text='Max'
        )
        self.max_label.grid(row=1, column=2, padx=10, pady=10, sticky='nsew')

        self.max_entry = ctk.CTkEntry(
            self,
            textvariable=self.max_year,
            width=40,

        )
        self.max_entry.grid(row=1, column=3, padx=10, pady=10, sticky='nsew')

    def get_min_max_year(self):
        try:
            min_year = int(self.min_year.get())
        except ValueError:
            min_year = 1850

        try:
            max_year = int(self.max_year.get())
        except ValueError:
            max_year = 2025

        return min_year, max_year
