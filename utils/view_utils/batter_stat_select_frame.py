"""Modular app for checkboxes to select batter stats to view"""
import customtkinter as ctk

class BatterStatSelectFrame(ctk.CTkFrame):
    """View class for batter stats selection."""

    def __init__(self, parent):
        """Initialize the frame."""
        ctk.CTkFrame.__init__(self, parent)

        available_stats = ['AVG', 'OBP', 'SLG', 'OPS', 'wOBA',
                           'HR/600', 'K/600', 'BB/600', 'SB/600',
                           'SBPct', 'RC/600', 'WAR/600', 'BsR/600',
                           'ZR/600' ]

        self.stats_to_keep = []

        def set_active_stats():
            self.stats_to_keep.clear()
            all_checkboxes = self.winfo_children()
            for checkbox_select in all_checkboxes:
                if checkbox_select.get() != "off":
                    self.stats_to_keep.append(checkbox_select.get())

        self.set_active_stats = set_active_stats

        stat_num=0

        for stat in available_stats:
            checkbox = ctk.CTkCheckBox(
                master=self,
                text=stat,
                onvalue=stat,
                offvalue='off',
                command=set_active_stats
            )
            checkbox.grid(
                row=stat_num // 3,
                column=stat_num % 3,
                padx=2,
                pady=2,
                sticky='nsew',
            )
            stat_num += 1


    def get_active_stats(self):
        return self.stats_to_keep


