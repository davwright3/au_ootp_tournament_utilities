"""App for comparing player ratings across collection."""
import customtkinter as ctk
from utils.config_utils import settings as settings_module
from utils.view_utils.header_footer_frame import Header, Footer
from utils.view_utils.all_player_data_view_frame import TreeviewTableFrame
from utils.data_utils.card_list_store import card_store
from utils.view_utils.ratings_menu_frame import RatingsMenuFrame
from utils.stats_utils.calculate_return_rating_values import calculate_return_rating_values


class PlayerRatingToolView(ctk.CTkToplevel):
    """Base class for the view."""

    def __init__(self):
        """Initialize the class."""
        super().__init__()

        page_settings = settings_module.settings

        # Get the card list
        card_store.load_card_list()
        self.card_df = card_store.get_all_card_ratings()

        self.height = int(page_settings['FileProcessor']['height'])
        self.width = int(page_settings['FileProcessor']['width'])
        self.frame_width = int(int(self.width) * .9)
        self.initial_target_dir = (
            page_settings['InitialFileDirs']['initial_target_folder'])
        header_footer_height = int(int(self.height) * .1)

        self.title = 'Basic Stats View'
        self.geometry(f"{self.width}x{self.height}")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=0)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)

        # Set up the necessary frames
        self.header_frame = Header(
            self,
            height=header_footer_height,
            width=int(self.frame_width),
            title=self.title
        )
        self.header_frame.grid(
            row=0,
            column=0,
            columnspan=3,
            padx=10,
            pady=10,
            sticky='nsew'
        )

        self.data_view_frame = TreeviewTableFrame(self)
        self.data_view_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            padx=10,
            pady=10,
            sticky='nsew')

        self.menu_frame = ctk.CTkScrollableFrame(
            self,
            width=300,
            height=self.height,
        )
        self.menu_frame.grid(
            row=1,
            column=2,
            padx=5,
            pady=5,
            sticky='nsew'
        )

        self.menu_frame.columnconfigure(0, weight=1)
        self.menu_frame.columnconfigure(1, weight=0)


        self.footer_frame = Footer(
            self,
            height=header_footer_height,
            width=int(self.frame_width),
        )
        self.footer_frame.grid(
            row=2,
            column=0,
            columnspan=3,
            padx=10,
            pady=10,
            sticky='nsew'
        )

        # Put the required items in the frames

        self.ratings_menu = RatingsMenuFrame(
            self.menu_frame,
        )
        self.ratings_menu.grid(
            row=0,
            column=0,
            padx=0,
            pady=20,
            sticky='ns'
        )

        self.update_button = ctk.CTkButton(
            self.menu_frame,
            command=self.update_view,
        )
        self.update_button.grid(
            row=3,
            column=0,
            padx=10,
            pady=10,
        )

        self.update_view()

        def show_and_release_topmost():
            """Lift window, set topmost and then release safely."""
            if not self.winfo_exists():
                return

            try:
                self.lift()
                self.attributes("-topmost", True)
            except Exception():
                return

            def release():
                if self.winfo_exists():
                    try:
                        self.attributes("-topmost", False)
                    except Exception:
                        pass

            self.after(100, release)

        show_and_release_topmost()


    def update_view(self):
        """Update the view."""
        ratings_to_view = self.ratings_menu.get_active_ratings()
        batter_weights = self.ratings_menu.get_batting_weights()
        pitcher_weights = self.ratings_menu.get_pitching_weights()
        defense_weights = self.ratings_menu.get_defense_weights()
        min_value, max_value = self.ratings_menu.get_min_max_values()
        min_year, max_year = self.ratings_menu.get_min_max_year()
        selected_position = self.ratings_menu.get_selected_position()
        selected_card_type = self.ratings_menu.get_selected_card_type()
        ratings_df = calculate_return_rating_values(
            self.card_df,
            ratings_to_view=ratings_to_view,
            min_rating=min_value,
            max_rating=max_value,
            min_year=min_year,
            max_year=max_year,
            batting_weights=batter_weights,
            pitching_weights=pitcher_weights,
            defense_weights=defense_weights,
            position=selected_position,
            selected_card_types=selected_card_type,
        )
        self.data_view_frame.load_dataframe(ratings_df)
