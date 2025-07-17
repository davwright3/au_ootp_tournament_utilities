"""Custom frame to show pitcher ratings."""
from utils.interface_utils.rating_label import RatingLabel
from utils.stats_utils.get_pitcher_ratings import get_pitcher_ratings
import customtkinter as ctk


class PitcherRatingsFrame(ctk.CTkFrame):
    """Class for viewing pitcher ratings."""

    def __init__(self, parent, cid_value):
        """Initialize the pitcher view."""
        super().__init__(parent, fg_color='white')

        self.pitcher_ratings = get_pitcher_ratings(card_id=cid_value)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
        self.columnconfigure(5, weight=1)

        self.card_title_frame = RatingLabel(
            self,
            self.pitcher_ratings.iloc[0]['//Card Title'],
        )
        self.card_title_frame.grid(
            row=0,
            column=0,
            columnspan=7,
            padx=10,
            pady=10,
            sticky='nsew'
        )

        # Frames for the rating labels
        self.stuff_label = RatingLabel(
            self,
            'STF: '
        )
        self.stuff_label.grid(
            row=2,
            column=0,
            sticky='nsew'
        )

        self.phr_rating_label = RatingLabel(
            self,
            'pHR: '
        )
        self.phr_rating_label.grid(
            row=3,
            column=0,
            sticky='nsew'
        )

        self.pbabip_rating_label = RatingLabel(
            self,
            'pBABIP: '
        )
        self.pbabip_rating_label.grid(
            row=4,
            column=0,
            sticky='nsew'
        )

        self.control_rating_label = RatingLabel(
            self,
            'CON: '
        )
        self.control_rating_label.grid(
            row=5,
            column=0,
            sticky='nsew'
        )

        self.overall_label = RatingLabel(
            self,
            'OA'
        )
        self.overall_label.grid(
            row=1,
            column=1,
            sticky='nsew'
        )

        self.v_left_label = RatingLabel(
            self,
            'vL'
        )
        self.v_left_label.grid(
            row=1,
            column=2,
            sticky='nsew'
        )

        self.v_right_label = RatingLabel(
            self,
            'vR'
        )
        self.v_right_label.grid(
            row=1,
            column=3,
            sticky='nsew'
        )

        self.stamina_label = RatingLabel(
            self,
            'STA: '
        )
        self.stamina_label.grid(
            row=2,
            column=4,
            sticky='nsew'
        )

        self.hold_label = RatingLabel(
            self,
            'HLD: '
        )
        self.hold_label.grid(
            row=3,
            column=4,
            sticky='nsew'
        )

        # Get the ratings to display
        self.stuff_rating_label = RatingLabel(
            self,
            self.pitcher_ratings.iloc[0]['Stuff'],
        )
        self.stuff_rating_label.grid(
            row=2,
            column=1,
            sticky='nsew'
        )

        self.stuff_v_left_rating_label = RatingLabel(
            self,
            self.pitcher_ratings.iloc[0]['Stuff vL'],
        )
        self.stuff_v_left_rating_label.grid(
            row=2,
            column=2,
            sticky='nsew'
        )

        self.stuff_v_right_rating_label = RatingLabel(
            self,
            self.pitcher_ratings.iloc[0]['Stuff vR'],
        )
        self.stuff_v_right_rating_label.grid(
            row=2,
            column=3,
            sticky='nsew'
        )

        self.phr_rating_label = RatingLabel(
            self,
            self.pitcher_ratings.iloc[0]['pHR'],
        )
        self.phr_rating_label.grid(
            row=3,
            column=1,
            sticky='nsew'
        )

        self.phr_v_left_rating_label = RatingLabel(
            self,
            self.pitcher_ratings.iloc[0]['pHR vL'],
        )
        self.phr_v_left_rating_label.grid(
            row=3,
            column=2,
            sticky='nsew'
        )

        self.phr_v_right_rating_label = RatingLabel(
            self,
            self.pitcher_ratings.iloc[0]['pHR vR'],
        )
        self.phr_v_right_rating_label.grid(
            row=3,
            column=3,
            sticky='nsew'
        )

        self.pbabip_rating_label = RatingLabel(
            self,
            self.pitcher_ratings.iloc[0]['pBABIP'],
        )
        self.pbabip_rating_label.grid(
            row=4,
            column=1,
            sticky='nsew'
        )

        self.pbabip_v_left_rating_label = RatingLabel(
            self,
            self.pitcher_ratings.iloc[0]['pBABIP vL'],
        )
        self.pbabip_v_left_rating_label.grid(
            row=4,
            column=2,
            sticky='nsew'
        )

        self.pbabip_v_right_rating_label = RatingLabel(
            self,
            self.pitcher_ratings.iloc[0]['pBABIP vR'],
        )
        self.pbabip_v_right_rating_label.grid(
            row=4,
            column=3,
            sticky='nsew'
        )

        self.control_rating_label = RatingLabel(
            self,
            self.pitcher_ratings.iloc[0]['Control'],
        )
        self.control_rating_label.grid(
            row=5,
            column=1,
            sticky='nsew'
        )

        self.control_v_left_rating_label = RatingLabel(
            self,
            self.pitcher_ratings.iloc[0]['Control vL'],
        )
        self.control_v_left_rating_label.grid(
            row=5,
            column=2,
            sticky='nsew'
        )

        self.control_v_right_rating_label = RatingLabel(
            self,
            self.pitcher_ratings.iloc[0]['Control vR'],
        )
        self.control_v_right_rating_label.grid(
            row=5,
            column=3,
            sticky='nsew'
        )

        self.stamina_rating_label = RatingLabel(
            self,
            self.pitcher_ratings.iloc[0]['Stamina'],
        )
        self.stamina_rating_label.grid(
            row=2,
            column=5,
            sticky='nsew'
        )

        self.hold_label = RatingLabel(
            self,
            self.pitcher_ratings.iloc[0]['Hold'],
        )
        self.hold_label.grid(
            row=3,
            column=5,
            sticky='nsew'
        )

        self.pitch_rating_label = RatingLabel(
            self,
            'Pitch Ratings'
        )
        self.pitch_rating_label.grid(
            row=6,
            column=0,
            columnspan=6,
            sticky='nsew'
        )

        row = 0
        stat_count = 0
        if self.pitcher_ratings.iloc[0]['Fastball'] != 0:
            self.fastball_label = RatingLabel(
                self,
                'FB: '
            )
            self.fastball_label.grid(
                row=(row % 4) + 7,
                column=(stat_count // 4) * 2,
                sticky='nsew'
            )
            self.fastball_rating_label = RatingLabel(
                self,
                self.pitcher_ratings.iloc[0]['Fastball'],
            )
            self.fastball_rating_label.grid(
                row=(row % 4) + 7,
                column=(stat_count // 4) * 2 + 1,
                sticky='nsew'
            )
            row += 1
            stat_count += 1

        if self.pitcher_ratings.iloc[0]['Sinker'] != 0:
            self.sinker_label = RatingLabel(
                self,
                'SI: '
            )
            self.sinker_label.grid(
                row=(row % 4) + 7,
                column=(stat_count // 4) * 2,
                sticky='nsew'
            )
            self.sinker_rating_label = RatingLabel(
                self,
                self.pitcher_ratings.iloc[0]['Sinker'],
            )
            self.sinker_rating_label.grid(
                row=(row % 4) + 7,
                column=(stat_count // 4) * 2 + 1,
                sticky='nsew'
            )
            row += 1
            stat_count += 1

        if self.pitcher_ratings.iloc[0]['Slider'] != 0:
            self.slider_label = RatingLabel(
                self,
                'Slider: '
            )
            self.slider_label.grid(
                row=(row % 4) + 7,
                column=(stat_count // 4) * 2,
                sticky='nsew'
            )

            self.slider_rating_label = RatingLabel(
                self,
                self.pitcher_ratings.iloc[0]['Slider'],
            )
            self.slider_rating_label.grid(
                row=(row % 4) + 7,
                column=(stat_count // 4) * 2 + 1,
                sticky='nsew'
            )
            row += 1
            stat_count += 1

        if self.pitcher_ratings.iloc[0]['Curveball'] != 0:
            self.curveball_label = RatingLabel(
                self,
                'Curveball: '
            )
            self.curveball_label.grid(
                row=(row % 4) + 7,
                column=(stat_count // 4) * 2,
                sticky='nsew'
            )

            self.curveball_rating_label = RatingLabel(
                self,
                self.pitcher_ratings.iloc[0]['Curveball'],
            )
            self.curveball_rating_label.grid(
                row=(row % 4) + 7,
                column=(stat_count // 4) * 2 + 1,
                sticky='nsew'
            )
            row += 1
            stat_count += 1

        if self.pitcher_ratings.iloc[0]['Changeup'] != 0:
            self.changeup_label = RatingLabel(
                self,
                'Changeup: '
            )
            self.changeup_label.grid(
                row=(row % 4) + 7,
                column=(stat_count // 4) * 2,
                sticky='nsew'
            )

            self.changeup_rating_label = RatingLabel(
                self,
                self.pitcher_ratings.iloc[0]['Changeup'],
            )
            self.changeup_rating_label.grid(
                row=(row % 4) + 7,
                column=(stat_count // 4) * 2 + 1,
                sticky='nsew'
            )
            row += 1
            stat_count += 1

        if self.pitcher_ratings.iloc[0]['Cutter'] != 0:
            self.cutter_label = RatingLabel(
                self,
                'Cutter: '
            )
            self.cutter_label.grid(
                row=(row % 4) + 7,
                column=(stat_count // 4) * 2,
                sticky='nsew'
            )

            self.cutter_rating_label = RatingLabel(
                self,
                self.pitcher_ratings.iloc[0]['Cutter'],
            )
            self.cutter_rating_label.grid(
                row=(row % 4) + 7,
                column=(stat_count // 4) * 2 + 1,
                sticky='nsew'
            )
            row += 1
            stat_count += 1

        if self.pitcher_ratings.iloc[0]['Splitter'] != 0:
            self.splitter_label = RatingLabel(
                self,
                'Splitter: '
            )
            self.splitter_label.grid(
                row=(row % 4) + 7,
                column=(stat_count // 4) * 2,
                sticky='nsew'
            )

            self.splitter_rating_label = RatingLabel(
                self,
                self.pitcher_ratings.iloc[0]['Splitter'],
            )
            self.splitter_rating_label.grid(
                row=(row % 4) + 7,
                column=(stat_count // 4) * 2 + 1,
                sticky='nsew'
            )
            row += 1
            stat_count += 1

        if self.pitcher_ratings.iloc[0]['Forkball'] != 0:
            self.forkball_label = RatingLabel(
                self,
                'Forkball: '
            )
            self.forkball_label.grid(
                row=(row % 4) + 7,
                column=(stat_count // 4) * 2,
                sticky='nsew'
            )

            self.forkball_rating_label = RatingLabel(
                self,
                self.pitcher_ratings.iloc[0]['Forkball'],
            )
            self.forkball_rating_label.grid(
                row=(row % 4) + 7,
                column=(stat_count // 4) * 2 + 1,
                sticky='nsew'
            )
            row += 1
            stat_count += 1

        if self.pitcher_ratings.iloc[0]['Screwball'] != 0:
            self.screwball_label = RatingLabel(
                self,
                'Screwball: '
            )
            self.screwball_label.grid(
                row=(row % 4) + 7,
                column=(stat_count // 4) * 2,
                sticky='nsew'
            )

            self.screwball_rating_label = RatingLabel(
                self,
                self.pitcher_ratings.iloc[0]['Screwball'],
            )
            self.screwball_rating_label.grid(
                row=(row % 4) + 7,
                column=(stat_count // 4) * 2 + 1,
                sticky='nsew'
            )
            row += 1
            stat_count += 1

        if self.pitcher_ratings.iloc[0]['Circlechange'] != 0:
            self.circlechange_label = RatingLabel(
                self,
                'Circlechange: '
            )
            self.circlechange_label.grid(
                row=(row % 4) + 7,
                column=(stat_count // 4) * 2,
                sticky='nsew'
            )

            self.circlechange_rating_label = RatingLabel(
                self,
                self.pitcher_ratings.iloc[0]['Circlechange'],
            )
            self.circlechange_rating_label.grid(
                row=(row % 4) + 7,
                column=(stat_count // 4) * 2 + 1,
                sticky='nsew'
            )
            row += 1
            stat_count += 1

        if self.pitcher_ratings.iloc[0]['Knucklecurve'] != 0:
            self.knucklecurve_label = RatingLabel(
                self,
                'Knucklecurve: '
            )
            self.knucklecurve_label.grid(
                row=(row % 4) + 7,
                column=(stat_count // 4) * 2,
                sticky='nsew'
            )

            self.knucklecurve_rating_label = RatingLabel(
                self,
                self.pitcher_ratings.iloc[0]['Knucklecurve'],
            )
            self.knucklecurve_rating_label.grid(
                row=(row % 4) + 7,
                column=(stat_count // 4) * 2 + 1,
                sticky='nsew'
            )
            row += 1
            stat_count += 1

        if self.pitcher_ratings.iloc[0]['Knuckleball'] != 0:
            self.knuckleball_label = RatingLabel(
                self,
                'Knuckleball: '
            )
            self.knuckleball_label.grid(
                row=(row % 4) + 7,
                column=(stat_count // 4) * 2,
                sticky='nsew'
            )

            self.knuckleball_rating_label = RatingLabel(
                self,
                self.pitcher_ratings.iloc[0]['Knuckleball'],
            )
            self.knuckleball_rating_label.grid(
                row=(row % 4) + 7,
                column=(stat_count // 4) * 2 + 1,
                sticky='nsew'
            )
