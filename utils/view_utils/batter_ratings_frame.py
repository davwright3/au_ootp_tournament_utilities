"""Frame for displaying batter ratings."""
import customtkinter as ctk
from utils.config_utils.settings import settings as settings_module
from utils.stats_utils.get_batter_ratings import get_batter_ratings
from utils.interface_utils.rating_label import RatingLabel
import pandas as pd

class BatterRatingsFrame(ctk.CTkFrame):
    """Modular frame for displaying batter ratings.

    Requires the file location for the card dump
    from the OOTP card shop.
    """
    def __init__(self, parent, cid_value):
        """Initialize the frame."""
        super().__init__(parent)
        card_df_file_path = settings_module['InitialFileDirs']['target_card_list_file']

        self.font_style=('Arial', 18, 'bold')
        # get the dataframe to display the card's ratings
        self.ratings_df = get_batter_ratings(card_df_file_path, cid_value)


        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)

        self.title_label = RatingLabel(self, self.ratings_df.iloc[0]['Title'])
        self.title_label.grid(row=0, column=0, columnspan=3, sticky='nsew')

        # Rating and side labels
        self.overall_label = RatingLabel(self, rating_to_display="OA")
        self.overall_label.grid(row=1, column=1, sticky='nsew')

        self.v_left_label = RatingLabel(self, rating_to_display="vL")
        self.v_left_label.grid(row=1, column=2, sticky='nsew')

        self.v_right_label = RatingLabel(self, rating_to_display="vR")
        self.v_right_label.grid(row=1, column=3, sticky='nsew')

        self.babip_label = RatingLabel(self, rating_to_display="BABIP")
        self.babip_label.grid(row=2, column=0)

        self.avoid_ks_label = RatingLabel(self, rating_to_display="AvK")
        self.avoid_ks_label.grid(row=3, column=0)

        self.gap_label = RatingLabel(self, rating_to_display="GAP")
        self.gap_label.grid(row=4, column=0)

        self.power_label = RatingLabel(self, "Power")
        self.power_label.grid(row=5, column=0)

        self.eye_label = RatingLabel(self, "Eye")
        self.eye_label.grid(row=6, column=0)

        # ratings labels
        self.babip_overall_rating = RatingLabel(self, self.ratings_df.iloc[0]['BABIP'])
        self.babip_overall_rating.grid(row=2, column=1)

        self.babip_v_left_rating = RatingLabel(self, self.ratings_df.iloc[0]['BABIP vL'])
        self.babip_v_left_rating.grid(row=2, column=2)

        self.babip_v_right_rating = RatingLabel(self, self.ratings_df.iloc[0]['BABIP vR'])
        self.babip_v_right_rating.grid(row=2, column=3)

        self.avoid_k_overall_rating = RatingLabel(self, self.ratings_df.iloc[0]['Avoid Ks'])
        self.avoid_k_overall_rating.grid(row=3, column=1)

        self.avoid_k_v_left_rating = RatingLabel(self, self.ratings_df.iloc[0]['Avoid K vL'])
        self.avoid_k_v_left_rating.grid(row=3, column=2)

        self.avoid_k_v_right_rating = RatingLabel(self, self.ratings_df.iloc[0]['Avoid K vR'])
        self.avoid_k_v_right_rating.grid(row=3, column=3)

        self.gap_overall_rating =  RatingLabel(self, self.ratings_df.iloc[0]['Gap'])
        self.gap_overall_rating.grid(row=4, column=1)

        self.gap_v_left_rating = RatingLabel(self, self.ratings_df.iloc[0]['Gap vL'])
        self.gap_v_left_rating.grid(row=4, column=2)

        self.gap_v_right_rating = RatingLabel(self, self.ratings_df.iloc[0]['Gap vR'])
        self.gap_v_right_rating.grid(row=4, column=3)

        self.power_overall_rating = RatingLabel(self, self.ratings_df.iloc[0]['Power'])
        self.power_overall_rating.grid(row=5, column=1)

        self.power_v_left_rating = RatingLabel(self, self.ratings_df.iloc[0]['Power vL'])
        self.power_v_left_rating.grid(row=5, column=2)

        self.power_v_right_rating = RatingLabel(self, self.ratings_df.iloc[0]['Power vR'])
        self.power_v_right_rating.grid(row=5, column=3)

        self.eye_overall_rating = RatingLabel(self, self.ratings_df.iloc[0]['Eye'])
        self.eye_overall_rating.grid(row=6, column=1)

        self.eye_v_left_rating = RatingLabel(self, self.ratings_df.iloc[0]['Eye vL'])
        self.eye_v_left_rating.grid(row=6, column=2)

        self.eye_v_right_rating = RatingLabel(self, self.ratings_df.iloc[0]['Eye vR'])
        self.eye_v_right_rating.grid(row=6, column=3)
