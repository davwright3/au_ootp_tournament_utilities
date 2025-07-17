"""Frame for plotting batters stats over time."""
import customtkinter as ctk
from utils.data_utils.data_store import data_store
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from utils.trend_utils.batter_trends import get_player_trends
import matplotlib.dates as mdates


class BatterStatPlotFrame(ctk.CTkFrame):
    """Frame for plotting batters stats over time."""

    def __init__(self, parent, card_id=None):
        """Initialize batters stats plotting frame."""
        super().__init__(parent)
        df = data_store.get_data()
        self.is_closing = False

        # One df for the league and one for the player
        df1 = df.copy()
        self.player_df = (
            df1[df1['CID'] == int(card_id)][['PA', 'AB', 'H',
                                             '1B', '2B', '3B',
                                             'HR', 'BB', 'IBB',
                                             'SO', 'HP', 'SF',
                                             'TB', 'Trny']]
        )

        del df1

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.checkbox_frame = ctk.CTkFrame(
            self
        )
        self.checkbox_frame.grid(row=0, column=0, sticky='nsew')

        # create the checkbox
        self.stat_options = {
            'PA': ctk.BooleanVar(value=True),
            'wOBA': ctk.BooleanVar(value=True),
            'OBP': ctk.BooleanVar(value=True),
            'SLG': ctk.BooleanVar(value=True),
            'AVG': ctk.BooleanVar(value=True)
        }

        self.checkboxes = []
        for idx, stat in enumerate(self.stat_options):
            cb = ctk.CTkCheckBox(
                self.checkbox_frame,
                text=stat,
                variable=self.stat_options[stat],
                command=self.update_plot
            )
            cb.grid(row=idx, column=0, sticky='nsew')
            self.checkboxes.append(cb)

        # Get the proper dataframe and format it
        dataframes = get_player_trends(
            self.player_df, self.get_selected_stats()
        )

        self.plot_chart(dataframes)

    def plot_chart(self, dataframes):
        """Plot the chart into the CTKFrame using matplotlib."""
        # Clear a canvas if it already exists
        if hasattr(self, 'canvas') and self.canvas:
            self.canvas.get_tk_widget().destroy()
            self.canvas = None

        self.figure = Figure(figsize=(5, 4), dpi=80, constrained_layout=True)
        ax = self.figure.add_subplot(111)

        for idx, dataframe in enumerate(dataframes):
            x = dataframe.iloc[:, 0]
            y = dataframe.iloc[:, 1]
            ax.plot(x, y, label=dataframe.columns[1])

        ax.set_title("Trends")
        ax.set_xlabel(dataframes[0].columns[0])
        ax.set_ylabel(dataframes[0].columns[1])
        ax.set_ylim(0.15, 0.55)
        ax.legend()
        ax.grid(True)
        ax.xaxis.set_major_locator(
            mdates.AutoDateLocator(minticks=5, maxticks=7)
        )
        self.figure.autofmt_xdate()

        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.draw()

        self.canvas.get_tk_widget().grid(row=0, column=1, sticky='nsew')
        plt.close(self.figure)

        self.bind("<Configure>", self._resize)

    def get_selected_stats(self):
        """Get stats that user selects."""
        pa = self.stat_options['PA'].get()
        woba = self.stat_options['wOBA'].get()
        obp = self.stat_options['OBP'].get()
        slg = self.stat_options['SLG'].get()
        avg = self.stat_options['AVG'].get()

        return {'pa': pa,
                'woba': woba,
                'obp': obp,
                'slg': slg,
                'avg': avg
                }

    def update_plot(self):
        """Update plot on stat select (placeholder)."""
        if self.is_closing:
            return

        selected_stats = self.get_selected_stats()
        new_stats = get_player_trends(
            selected_stats=selected_stats,
            df=self.player_df
        )
        self.plot_chart(new_stats)

    def _resize(self, event=None):
        if self.is_closing or not hasattr(self, 'canvas') or not self.canvas:
            return
        try:
            # self.canvas.figure.tight_layout()
            self.canvas.draw()
        except Exception as e:
            print("Failed to set tight layout: ", e)

    def destroy(self):
        """Override destroy function for plot cleanup."""
        self.is_closing = True
        self.unbind("<Configure>")

        for cb in self.checkboxes:
            cb.configure(command=lambda: None)

        try:
            if self.canvas and self.canvas.figure:
                try:
                    self.canvas.figure._axobservers.callbacks.clear()
                except Exception as e:
                    print("Error clearing observers", e)

            if hasattr(self, 'toolbar_frame'):
                self.toolbar_frame.destroy()
                self.toolbar_frame = None

            if hasattr(self, 'canvas') and self.canvas:
                widget = self.canvas.get_tk_widget()
                if widget.winfo_exists():
                    widget.destroy()
                if hasattr(self.canvas, 'figure') and self.canvas.figure:
                    self.canvas.figure.clf()
                    self.canvas.figure = None
                self.canvas = None
                # self.canvas.get_tk_widget().destroy()
                # self.canvas.figure.clf()
                # self.canvas.figure = None
                # self.canvas = None
        except Exception as e:
            print("Exception: ", e)
            pass
        super().destroy()
