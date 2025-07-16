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
    def __init__(self, parent, cid_value):
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
        self.player_df, removed = cull_teams(df)
        self.player_df = self.player_df[self.player_df['CID'] == int(cid_value)][['CID', 'IP', 'HR.1', 'BB.1', 'K', 'ER', 'Trny']]
        dataframes = get_pitcher_trends(self.player_df, stat_options=self.get_selected_stats())
        self.plot_chart(dataframes)
        del df



    def plot_chart(self, dataframes):
        # clear canvas if it exists
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
        ax.set_xlabel("Trny")
        ax.set_ylabel("Rolling Data")
        ax.set_ylim(bottom=1, top=10)
        ax.legend()
        ax.grid(True)
        ax.xaxis.set_major_locator(ticker.MultipleLocator(5))

        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.draw()

        self.canvas.get_tk_widget().grid(row=0, column=1, sticky='nsew')
        plt.close(self.figure)

        self.bind("<Configure>", self._resize)



    def update_plot(self):
        dataframes = get_pitcher_trends(self.player_df, stat_options=self.get_selected_stats())
        self.plot_chart(dataframes)

    def _resize(self, event=None):
        if hasattr(self, 'canvas') and self.canvas:
            print("Resizing canvas")
            try:
                self.canvas.figure.tight_layout()
                self.canvas.draw()
            except Exception as e:
                print("Failed to set tight layout". e)

    def get_selected_stats(self):
        innings_select = self.stat_options['IPC'].get()
        era_select = self.stat_options['ERA'].get()
        bb_select = self.stat_options['BB/9'].get()
        k9_select = self.stat_options['K/9'].get()
        hr_select = self.stat_options['HR/9'].get()

        return {'innings': innings_select,
                'era': era_select,
                'bb': bb_select,
                'k9': k9_select,
                'hr': hr_select,}

    def destroy(self):
        try:
            if self.canvas and self.canvas.figure:
                try:
                    self.canvas.figure._axoberservers.callbacks.clear()
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

