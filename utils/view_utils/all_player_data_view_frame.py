"""Create frame for viewing data."""
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import pandas as pd


def open_batter_view(cid, file_path):
    from apps.batter_info_view import BatterInfoView
    BatterInfoView(cid, file_path)

def open_pitcher_view(cid, file_path):
    from apps.pitcher_info_view import PitcherInfoView
    PitcherInfoView(cid, file_path)


class TreeviewTableFrame(ctk.CTkFrame):
    """Create frame for viewing data."""

    def __init__(self, master):
        """Initialize the frame view."""
        super().__init__(master)
        self.parent = master
        self.df = pd.DataFrame()
        self.sort_state = {"col": None, "reverse": False}
        self.tree = None
        self.team_to_highlight = None

        self.style = ttk.Style()
        self.style.configure(
            "Treeview",
            background="#ffffff",
            font=("Arial", 16),
            rowheight=32
        )

        self.style.configure(
            "Treeview.Heading",
            font=("Arial", 16, "bold")
        )

        self.tree_frame = tk.Frame(self, bg="red")
        self.tree_frame.pack(fill="both", expand=True)

        self.table = None

    def load_dataframe(self, df: pd.DataFrame, min_pa=1, passed_team=None):
        """Load dataframe for Treeview."""
        print("Loading dataframe into table...Passed team:")

        for widget in self.tree_frame.winfo_children():
            widget.destroy()

        self.df = df.copy()
        self.sort_state = {"col": None, "reverse": False}
        self.team_to_highlight = passed_team

        self.tree = ttk.Treeview(
            self.tree_frame,
            columns=list(df.columns),
            show="headings"
        )

        self.tree.tag_configure('evenrow', background="#ffffff")
        self.tree.tag_configure('oddrow', background="#f0f0f0")
        self.tree.tag_configure('highlightrow', background="#c7f2c7")

        self.tree.bind("<Double-1>", self.on_row_double_click)

        # Set column headers
        for col in df.columns:
            self.tree.heading(
                col,
                text=col,
                command=lambda c=col: self.sort_by_column(c)
            )

            if col == "Title" or col == "ORG":
                self.tree.column(
                    col,
                    anchor="w",
                    width=350,
                    minwidth=200,
                    stretch=True
                )
            elif col == 'PA' or col == 'IPC':
                self.tree.column(
                    col,
                    anchor="center",
                    width=5*26,
                    stretch=False
                )
            else:
                self.tree.column(
                    col,
                    anchor='center',
                    width=max(80, len(col)*26),
                    stretch=False
                )

        # Insert data
        self._insert_data(df)

        scrollbar = ctk.CTkScrollbar(
            self.tree_frame,
            orientation='vertical',
            command=self.tree.yview
        )
        scrollbar.grid(row=0, column=1, sticky='ns')
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree_frame.grid_rowconfigure(0, weight=1)
        self.tree_frame.grid_columnconfigure(0, weight=1)
        self.tree.grid(row=0, column=0, sticky='nsew')

    def _insert_data(self, df):
        """Insert data into Treeview."""
        for row in self.tree.get_children():
            self.tree.delete(row)

        for i, (_, row) in enumerate(df.iterrows()):
            org_value = str(row.get('ORG', '')).strip().lower()
            selected_value = str(self.team_to_highlight).strip().lower()

            if selected_value and org_value == selected_value:
                tag = 'highlightrow'
            else:
                tag = 'evenrow' if i % 2 == 0 else 'oddrow'
            self.tree.insert('', 'end', values=list(row), tags=(tag,))

    def sort_by_column(self, col):
        """Sort by column."""
        reverse = not \
            (self.sort_state["col"] == col and self.sort_state["reverse"])
        self.sort_state = {"col": col, "reverse": reverse}

        try:
            sorted_df = self.df.sort_values(
                by=col,
                ascending=not reverse,
                key=lambda x: pd.to_numeric(x, errors='coerce'))
        except: # noqa
            sorted_df = self.df.sort_values(by=col, ascending=not reverse)

        self._insert_data(sorted_df)

    def on_row_double_click(self, event):
        selected_item = self.tree.focus()
        try:
            file_path = self.parent.target_file
            print("File pah: ", file_path)
        except ValueError:
            print("No file path found")
            return

        try:
            role = self.parent.role
        except ValueError:
            role = "batter"

        values = self.tree.item(selected_item, 'values')
        columns = self.tree['columns']

        try:
            cid_index = columns.index("CID")
            cid_value = values[cid_index]
            print(cid_value)
        except ValueError:
            print("CID column not found")
            return
        if role == 'batter':
            open_batter_view(cid_value, file_path)
        elif role == 'pitcher':
            open_pitcher_view(cid_value, file_path)


