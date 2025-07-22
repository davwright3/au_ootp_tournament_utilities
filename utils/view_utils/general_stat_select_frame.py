"""Frame for selecting general stat options to show."""
import customtkinter as ctk


class GeneralStatSelectFrame(ctk.CTkFrame):
    """Frame for selecting general stat options to show."""

    def __init__(self, parent):
        super().__init__(parent)

        available_general_stats = ['owned', 'L10', 'L10V']

        self.general_stats_to_keep = []
        self.checkbox_vars = {}

        def set_selected_general_stats():
            self.general_stats_to_keep.clear()
            all_checkboxes = self.winfo_children()
            for checkbox_stat in all_checkboxes:
                if checkbox_stat.get() != 'off':
                    self.general_stats_to_keep.append(checkbox_stat.get())

        self.set_selected_general_stats = set_selected_general_stats

        stat_num = 0

        for stat in available_general_stats:
            var = ctk.StringVar(value='off')
            checkbox = ctk.CTkCheckBox(
                self,
                text=stat,
                variable=var,
                onvalue=stat,
                offvalue='off',
                command=set_selected_general_stats
            )
            checkbox.grid(
                row = stat_num // 3,
                column = stat_num % 3,
                padx = 3,
                pady = 3,
                sticky = 'nsew'
            )
            self.checkbox_vars[stat] = var
            stat_num += 1

    def get_selected_general_stats(self):
        return self.general_stats_to_keep
