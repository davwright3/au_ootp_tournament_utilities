"""Menu for selecting which ratings to view and their weights."""
from tkinter import BooleanVar
from utils.view_utils.batting_weights_frame import BattingWeightsFrame
from utils.view_utils.defense_weights_frame import DefenseWeightsFrame
from utils.view_utils.pitcher_weights_frame import PitcherWeightsFrame
from utils.view_utils.card_value_select_frame import CardValueSelectFrame
import customtkinter as ctk

class RatingsMenuFrame(ctk.CTkFrame):
    """Frame for getting needed information from user."""
    def __init__(self, parent):
        ctk.CTkFrame.__init__(self, parent)

        # Set up check boxes
        available_ratings = ['BatOA', 'BatvL', 'BatvR', 'BSR', 'Catch Def',
                             'IF Def', 'OF Def', 'PitOA', 'PitvL', 'PitvR']

        self.ratings_to_keep = []

        def set_active_ratings():
            self.ratings_to_keep.clear()
            all_checkboxes = self.winfo_children()
            for widget in self.winfo_children():
                if isinstance(widget, ctk.CTkCheckBox):
                    if widget.get() != 'off':
                        self.ratings_to_keep.append(widget.get())

        self.set_active_ratings = set_active_ratings

        stat_num = 0
        for rating in available_ratings:
            var = BooleanVar(value=True)
            checkbox = ctk.CTkCheckBox(
                master=self,
                text=rating,
                onvalue=rating,
                offvalue='off',
                command=set_active_ratings
            )
            checkbox.grid(
                column=stat_num % 3,
                row=stat_num // 3,
                sticky='nsew'
            )

            stat_num += 1

        row = stat_num // 3 + 1

        self.batter_weights_frame = BattingWeightsFrame(
            self
        )
        self.batter_weights_frame.grid(
            row=row,
            column=0,
            columnspan=3,
            sticky='nsew'
        )
        row += 1

        self.pitcher_weights_frame = PitcherWeightsFrame(
            self
        )
        self.pitcher_weights_frame.grid(
            row=row,
            column=0,
            columnspan=3,
            sticky='nsew'
        )
        row += 1

        self.defense_weights_frame = DefenseWeightsFrame(
            self
        )
        self.defense_weights_frame.grid(
            row=row,
            column=0,
            columnspan=3,
            sticky='nsew'
        )
        row += 1

        self.card_value_frame = CardValueSelectFrame(
            self
        )
        self.card_value_frame.grid(
            row=row,
            column=0,
            columnspan=3,
            sticky='nsew'
        )
        row += 1



    def get_active_ratings(self):
        """Return the selected ratings to view."""
        return self.ratings_to_keep

    def get_batting_weights(self):
        """Get the weights for batting."""
        batting_weights = self.batter_weights_frame.get_batting_weights()
        return batting_weights

    def get_pitching_weights(self):
        pitching_weights = self.pitcher_weights_frame.get_pitching_weights()
        return pitching_weights

    def get_defense_weights(self):
        defense_weights = self.defense_weights_frame.get_defense_weights()
        return defense_weights

    def get_min_max_values(self):
        """Return the min and max values for batting."""
        min_value, max_value = self.card_value_frame.get_min_max_values()
        return min_value, max_value