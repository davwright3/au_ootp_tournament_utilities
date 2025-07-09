"""Frame for plotting batters stats over time."""
import customtkinter as ctk
from utils.data_utils.data_store import data_store
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from utils.trend_utils.batter_trends import get_player_trends
import matplotlib.dates as mdates
import numpy as np

class BatterStatPlotFrame(ctk.CTkFrame):
    def __init__(self, parent, card_id=None):
        super().__init__(parent)
        df = data_store.get_data()


        # One df for the league and one for the player
        df1 = df.copy()
        player_df = df1[df1['CID'] == int(card_id)][['PA', 'AB', 'H', '1B', '2B', '3B', 'HR', 'BB', 'IBB', 'SO', 'HP', 'SF', 'Trny']]
        del df1

        # Get the proper dataframe and format it
        woba_df, plate_app_df = get_player_trends(player_df)
        del player_df

        self.plot_chart_working([woba_df, plate_app_df])



    # def plot_chart(self, df1):
    #     fig, ax = plt.subplots(figsize=(6,6))
    #     x_name = df1.columns[0]
    #     y_name = df1.columns[1]
    #     # x = np.linspace(0,10,100)
    #     # y = np.sin(x)
    #     x = df1[x_name]
    #     y = df1[y_name]
    #     ax.plot(x,y)
    #     ax.set_title("Batter stats")
    #
    #     self.canvas = FigureCanvasTkAgg(fig, self)
    #     self.canvas.draw()
    #
    #     self.toolbar_frame = ctk.CTkFrame(self)
    #     # self.toolbar_frame.grid(column=0, row=0, sticky='nsew')
    #     self.toolbar = NavigationToolbar2Tk(self.canvas, self.toolbar_frame)
    #     self.toolbar.update()
    #
    #     self.canvas.get_tk_widget().grid(row=1, column=1, sticky='nsew')
    #     plt.close(fig)

    def plot_chart_working(self, dataframes):
        # Clear a canvas if it already exists
        if hasattr(self, 'canvas') and self.canvas:
            self.canvas.get_tk_widget().destroy()
            self.canvas = None

        self.figure = Figure(figsize=(5,4))
        ax = self.figure.add_subplot(111)

        for idx, dataframe in enumerate(dataframes):
            x = dataframe.iloc[:,0]
            y = dataframe.iloc[:,1]
            ax.plot(x, y, label=dataframe.columns[1])

        ax.set_title("Trends")
        ax.set_xlabel(dataframes[0].columns[0])
        ax.set_ylabel(dataframes[0].columns[1])
        ax.set_ylim(0.15, 0.55)
        ax.legend()
        ax.grid(True)
        ax.xaxis.set_major_locator(mdates.AutoDateLocator(minticks=5, maxticks=7))
        self.figure.autofmt_xdate()

        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.draw()

        # self.toolbar_frame = ctk.CTkFrame(self)
        # # self.toolbar_frame.grid(column=0, row=0, sticky='nsew')
        # self.toolbar = NavigationToolbar2Tk(self.canvas, self.toolbar_frame)
        # self.toolbar.update()

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # self.canvas.get_tk_widget().grid(row=1, column=1, sticky='nsew')
        self.canvas.get_tk_widget().grid(row=1, column=0, sticky='nsew')
        plt.close(self.figure)


        self.bind("<Configure>", self._resize)

    def _resize(self, event=None):
        if hasattr(self, 'canvas') and self.canvas:
            try:
                self.canvas.figure.tight_layout()
                self.canvas.draw()
            except Exception as e:
                pass





    def destroy(self):
        print("Destroying parent batter plot frame")
        try:
            if self.canvas and self.canvas.figure:
                try:
                    self.canvas.figure._axobservers.callbacks.clear()
                except Exception as e:
                    print("Error clearing observers", e)

            # if hasattr(self, 'toolbar'):
            #     self.toolbar.update = lambda: None
            #     self.toolbar.set_history_buttons= lambda *args, **kwargs: None
            #     self.toolbar._Button = lambda *args, **kwargs: None
            #
            #     self.toolbar.destroy()
            #     self.toolbar = None

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




