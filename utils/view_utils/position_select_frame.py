"""Frame for selecting which position to view."""
import customtkinter as ctk


class PositionSelectFrame(ctk.CTkFrame):
    def __init__(self, parent):
        ctk.CTkFrame.__init__(self, parent)

        self.selected_position = ctk.StringVar(value='')

        self.catcher_radio = ctk.CTkRadioButton(self, text='C', variable=self.selected_position, value='LearnC')
        self.catcher_radio.grid(row=0, column=0, sticky='nsew')

        self.first_base_radio = ctk.CTkRadioButton(self, text='1B', variable=self.selected_position, value='Learn1B')
        self.first_base_radio.grid(row=0, column=1, sticky='nsew')

        self.second_base_radio = ctk.CTkRadioButton(self, text='2B', variable=self.selected_position, value='Learn2B')
        self.second_base_radio.grid(row=0, column=2, sticky='nsew')

        self.third_base_radio = ctk.CTkRadioButton(self, text='3B', variable=self.selected_position, value='Learn3B')
        self.third_base_radio.grid(row=1, column=0, sticky='nsew')

        self.shortstop_radio = ctk.CTkRadioButton(self, text='SS', variable=self.selected_position, value='LearnSS')
        self.shortstop_radio.grid(row=1, column=1, sticky='nsew')

        self.left_field_radio = ctk.CTkRadioButton(self, text='LF', variable=self.selected_position, value='LearnLF')
        self.left_field_radio.grid(row=1, column=2, sticky='nsew')

        self.center_field_radio = ctk.CTkRadioButton(self, text='CF', variable=self.selected_position, value='LearnCF')
        self.center_field_radio.grid(row=2, column=0, sticky='nsew')

        self.right_field_radio = ctk.CTkRadioButton(self, text='RF', variable=self.selected_position, value='LearnRF')
        self.right_field_radio.grid(row=2, column=1, sticky='nsew')

        self.batters_radio = ctk.CTkRadioButton(self, text='Bats', variable=self.selected_position, value='Batters')
        self.batters_radio.grid(row=2, column=2, sticky='nsew')

        self.pitchers_radio = ctk.CTkRadioButton(self, text='P', variable=self.selected_position, value='LearnP')
        self.pitchers_radio.grid(row=3, column=1, sticky='nsew')


    def get_selected_position(self):
        return self.selected_position.get()