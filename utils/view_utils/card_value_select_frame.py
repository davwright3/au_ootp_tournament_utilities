"""Frame for selecting min and max card values."""
import customtkinter as ctk


class CardValueSelectFrame(ctk.CTkFrame):
    """Frame for selecting min and max card values."""

    def __init__(self, parent):
        """Initialize the frame."""
        ctk.CTkFrame.__init__(self, parent,
                              border_color='gray',
                              border_width=2
                              )

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        self.min_val = ctk.StringVar(self, value='40')
        self.max_val = ctk.StringVar(self, value='105')

        self.frame_label = ctk.CTkLabel(
            self,
            text='Card Values'
        )
        self.frame_label.grid(row=0, column=0, columnspan=4, sticky='nsew')

        self.min_value_label = ctk.CTkLabel(
            self,
            text="Min"
        )
        self.min_value_label.grid(
            row=1,
            column=0,
            padx=5,
            pady=5
        )

        self.min_value_input = ctk.CTkEntry(
            self,
            textvariable=self.min_val,
            placeholder_text='40',
            width=45,
        )
        self.min_value_input.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )

        self.max_value_label = ctk.CTkLabel(
            self,
            text="Max",
        )
        self.max_value_label.grid(
            row=1,
            column=2,
            padx=5,
            pady=5
        )

        self.max_value_input = ctk.CTkEntry(
            self,
            textvariable=self.max_val,
            placeholder_text='105',
            width=45
        )
        self.max_value_input.grid(
            row=1,
            column=3,
            padx=5,
            pady=5
        )

    def get_min_max_values(self):
        """Get min and max selected values."""
        return self.min_val.get(), self.max_val.get()
