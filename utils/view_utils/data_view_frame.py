"""Create frame for viewing data."""
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import pandas as pd


class TreeviewTableFrame(ctk.CTkFrame):
    """Create frame for viewing data."""

    def __init__(self, master):
        """Initialize the frame view."""
        super().__init__(master)
        self.df = pd.DataFrame()
        self.sort_state = {"col": None, "reverse": False}
        self.tree = None

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

    def load_dataframe(self, df: pd.DataFrame, min_pa=1):
        """Load dataframe for Treeview."""
        print("Loading dataframe into table...")

        for widget in self.tree_frame.winfo_children():
            widget.destroy()

        self.df = df.copy()
        self.sort_state = {"col": None, "reverse": False}

        self.tree = ttk.Treeview(
            self.tree_frame,
            columns=list(df.columns),
            show="headings"
        )

        # Set column headers
        for col in df.columns:
            self.tree.heading(
                col,
                text=col,
                command=lambda c=col: self.sort_by_column(c)
            )

            if col == "Title":
                self.tree.column(
                    col,
                    anchor="w",
                    width=350,
                    minwidth=200,
                    stretch=True
                )
            else:
                self.tree.column(
                    col,
                    anchor='center',
                    width=80,
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

        for _, row in df.iterrows():
            self.tree.insert('', 'end', values=list(row))

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
