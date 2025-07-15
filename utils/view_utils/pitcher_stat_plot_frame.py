"""Custom frame for plotting pitcher trends."""
from matplotlib import ticker
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import customtkinter as ctk
from utils.data_utils.data_store import data_store
from utils.file_utils.process_files import cull_teams
from utils.trend_utils.pitcher_trends import get_pitcher_trends


class PitcherStatPlotFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        test_label = ctk.CTkLabel(self, text='Pitcher Stat Plot Frame')
        test_label.grid(row=0, column=0, sticky='nsew')

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.stat_options = {
            'IPC': ctk.BooleanVar(value=True),
            'ERA': ctk.BooleanVar(value=True),
            'BB/9': ctk.BooleanVar(value=True),
            'K/9': ctk.BooleanVar(value=True),
            'HR/9': ctk.BooleanVar(value=True),
        }

        self.checkbox_frame = ctk.CTkFrame(
            self,
        )
        self.checkbox_frame.grid(
            row=0,
            column=0,
            sticky='nsew',
        )

        for idx, stat in enumerate(self.stat_options):
            cb = ctk.CTkCheckBox(
                self.checkbox_frame,
                text=stat,
                variable=self.stat_options[stat],
                command=self.update_plot
            )
            cb.grid(
                row=idx,
                column=0,
                sticky='nsew',
            )
        df = data_store.get_data().copy()
        player_df, removed = cull_teams(df)
        player_df = player_df[['IP', 'HR.1', 'BB.1', 'K', 'Trny']]
        dataframe = get_pitcher_trends(player_df)
        self.plot_chart(dataframe)
        del df, player_df



    def plot_chart(self, dataframe):
        # clear canvas if it exists
        if hasattr(self, 'canvas') and self.canvas:
            print("destroying old canvas")
            self.canvas.get_tk_widget().destroy()
            self.canvas = None

        self.figure = Figure(figsize=(5, 4), dpi=80, constrained_layout=True)
        ax = self.figure.add_subplot(111)

        x = dataframe.iloc[:, 0]
        y = dataframe.iloc[:, 1]
        ax.plot(x, y, label=dataframe.columns[1])

        ax.set_title("Trends")
        ax.set_xlabel("Trny")
        ax.set_ylabel("Rolling Innings")
        ax.legend()
        ax.grid(True)
        ax.xaxis.set_major_locator(ticker.MultipleLocator(5))

        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.draw()

        self.canvas.get_tk_widget().grid(row=0, column=1, sticky='nsew')
        plt.close(self.figure)

        self.bind("<Configure>", self._resize)



    def update_plot(self):
        print("Updating plot")

    def _resize(self, event=None):
        if hasattr(self, 'canvas') and self.canvas:
            print("Resizing canvas")
            try:
                self.canvas.figure.tight_layout()
                self.canvas.draw()
            except Exception as e:
                print("Failed to set tight layout". e)

    def destroy(self):
        print("Destroying pitcher chart")
        try:
            if self.canvas and self.canvas.figure:
                try:
                    self.canvas.figure._axoberserver.callbacks.clear()
                except Exception as e:
                    print("Error clearing axoberserver", e)

            if hasattr(self, 'toolbar_frame'):
                self.toolbar_frame.destroy()
                self.toolbar_frame = None

            if hasattr(self, 'canvas'):
                self.canvas.get_tk_widget().destroy()
                self.canvas.figure.clf()
                self.canvas.figure = None
                self.canvas = None
        except Exception as e:
            print("Exception: ", e)
            pass
        super().destroy()

