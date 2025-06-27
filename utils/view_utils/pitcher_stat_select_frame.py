"""Frame for selecting which pitcher stats to view."""
import customtkinter as ctk


class PitcherStatSelectFrame(ctk.CTkFrame):
    """View class for pitch stats."""

    def __init__(self, parent):
        """Initialize the frame."""
        ctk.CTkFrame.__init__(self, parent)

        available_stats = ['FIP', 'ERA', 'K/9', 'KPct', 'BB/9',
                           'BBPct', 'HR/9', 'QSPct', 'GSPct',
                           'WHIP', 'IRSPct', 'SD/MD', 'IP/G',
                           'WAR/200']

        self.stats_to_keep = []

        def set_active_stats():
            self.stats_to_keep.clear()
            all_checkboxes = self.winfo_children()
            for checkbox_select in all_checkboxes:
                if checkbox_select.get() != "off":
                    self.stats_to_keep.append(checkbox_select.get())

        self.set_active_stats = set_active_stats

        stat_num = 0

        for stat in available_stats:
            checkbox = ctk.CTkCheckBox(
                self,
                text=stat,
                onvalue=stat,
                offvalue='off',
                command=set_active_stats
            )
            checkbox.grid(
                row=stat_num // 3,
                column=stat_num % 3,
                padx=3,
                pady=3,
                sticky='nsew',
            )
            stat_num += 1

    def get_active_stats(self):
        """Return the active stats."""
        return self.stats_to_keep
