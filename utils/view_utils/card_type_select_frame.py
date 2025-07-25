"""Modular frame for selecting card type."""
import customtkinter as ctk
from customtkinter import CTkCheckBox


class CardTypeSelectFrame(ctk.CTkFrame):
    """Custom class for card type selection."""

    def __init__(self, parent):
        ctk.CTkFrame.__init__(self, parent)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.card_types_to_select = []

        # Variables

        live_var = ctk.IntVar(value=1)
        nl_var = ctk.IntVar(value=2)
        rookie_var = ctk.IntVar(value=3)
        legend_var = ctk.IntVar(value=4)
        allstar_var = ctk.IntVar(value=5)
        fl_var = ctk.IntVar(value=6)
        snapshot_var = ctk.IntVar(value=7)
        unsung_var = ctk.IntVar(value=8)
        hardware_var = ctk.IntVar(value=9)

        frame_label = ctk.CTkLabel(self, text='Select Card Type')
        frame_label.grid(row=0, column=0, columnspan=3, sticky='nsew')

        def set_selected_card_types():
            """Set the list of selected card types."""
            self.card_types_to_select.clear()
            all_checkboxes = self.winfo_children()
            for checkbox_select in all_checkboxes:
                if isinstance(checkbox_select, CTkCheckBox):
                    if checkbox_select.get() != 0:
                        self.card_types_to_select.append(checkbox_select.get())

        rating_num = 0

        live_checkbox = ctk.CTkCheckBox(
            self,
            text='Live',
            variable=live_var,
            onvalue=1,
            offvalue=0,
            command=set_selected_card_types
        )
        live_checkbox.grid(row=rating_num // 3, column=rating_num % 3, sticky='nsew')
        rating_num += 1

        nl_checkbox = ctk.CTkCheckBox(
            self,
            text='NL',
            variable=nl_var,
            onvalue=2,
            offvalue=0,
            command=set_selected_card_types
        )
        nl_checkbox.grid(row=rating_num // 3, column=rating_num % 3, sticky='nsew')
        rating_num += 1

        rookie_checkbox = ctk.CTkCheckBox(
            self,
            text='Rookie',
            variable=rookie_var,
            onvalue=3,
            offvalue=0,
            command=set_selected_card_types
        )
        rookie_checkbox.grid(row=rating_num // 3, column=rating_num % 3, sticky='nsew')
        rating_num += 1

        legend_checkbox = ctk.CTkCheckBox(
            self,
            text='Legend',
            variable=legend_var,
            onvalue=4,
            offvalue=0,
            command=set_selected_card_types
        )
        legend_checkbox.grid(row=rating_num // 3, column=rating_num % 3, sticky='nsew')
        rating_num += 1

        allstar_checkbox = ctk.CTkCheckBox(
            self,
            text='Allstar',
            variable=allstar_var,
            onvalue=5,
            offvalue=0,
            command=set_selected_card_types
        )
        allstar_checkbox.grid(row=rating_num // 3, column=rating_num % 3, sticky='nsew')
        rating_num += 1

        future_checkbox = ctk.CTkCheckBox(
            self,
            text='FL',
            variable=fl_var,
            onvalue=6,
            offvalue=0,
            command=set_selected_card_types
        )
        future_checkbox.grid(row=rating_num // 3, column=rating_num % 3, sticky='nsew')
        rating_num += 1

        snapshot_checkbox = ctk.CTkCheckBox(
            self,
            text='Snapshot',
            variable=snapshot_var,
            onvalue=7,
            offvalue=0,
            command=set_selected_card_types
        )
        snapshot_checkbox.grid(row=rating_num // 3, column=rating_num % 3, sticky='nsew')
        rating_num += 1

        unsung_checkbox = ctk.CTkCheckBox(
            self,
            text='Unsung',
            variable=unsung_var,
            onvalue=8,
            offvalue=0,
            command=set_selected_card_types
        )
        unsung_checkbox.grid(row=rating_num // 3, column=rating_num % 3, sticky='nsew')
        rating_num += 1

        hardware_checkbox = ctk.CTkCheckBox(
            self,
            text='Hardware',
            variable=hardware_var,
            onvalue=9,
            offvalue=0,
            command=set_selected_card_types
        )
        hardware_checkbox.grid(row=rating_num // 3, column=rating_num % 3, sticky='nsew')
        rating_num += 1



    def get_selected_card_types(self):
        """Return the selected card types."""
        return self.card_types_to_select
