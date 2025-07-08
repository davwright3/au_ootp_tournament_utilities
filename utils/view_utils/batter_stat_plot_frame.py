"""Frame for plotting batters stats over time."""
import customtkinter as ctk
from utils.data_utils.data_store import data_store
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np

class BatterStatPlotFrame(ctk.CTkFrame):
    def __init__(self, parent, card_id=None):
        super().__init__(parent)
        df = data_store.get_data()

        # One df for the league and one for the player
        df1 = df.copy()
        player_df = df1[df1['CID'] == int(card_id)]

        frame_label = ctk.CTkLabel(self,text="Batter plot frame")
        frame_label.grid(column=0, row=0, sticky='nsew')

        fig, ax = plt.subplots(figsize=(12,8))
        x = np.linspace(0,10,100)
        y = np.sin(x)
        ax.plot(x,y)
        ax.set_title("Batter stats")

        self.canvas = FigureCanvasTkAgg(fig, self)
        self.canvas.draw()

        self.toolbar_frame = ctk.CTkFrame(self)
        self.toolbar_frame.grid(column=0, row=0, sticky='nsew')
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.toolbar_frame)
        self.toolbar.update()

        self.canvas.get_tk_widget().grid(row=1, column=1, sticky='nsew')
        plt.close(fig)


    def destroy(self):
        print("Destroying parent batter plot frame")
        try:
            if self.canvas and self.canvas.figure:
                try:
                    self.canvas.figure._axobservers.callbacks.clear()
                except Exception as e:
                    print("Error clearing observers", e)

            if hasattr(self, 'toolbar'):
                self.toolbar.update = lambda: None
                self.toolbar.set_history_buttons= lambda *args, **kwargs: None
                self.toolbar._Button = lambda *args, **kwargs: None

                self.toolbar.destroy()
                self.toolbar = None

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




