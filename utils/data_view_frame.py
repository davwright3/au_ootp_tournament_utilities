"""Create frame for viewing data"""
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import pandas as pd

class TreeviewTableFrame(ctk.CTkFrame):
    """Create frame for viewing data"""
    def __init__(self, master):
        super().__init__(master)

        self.style = ttk.Style()
        self.style.configure(
            "Treeview",
            background="#ffffff",
            font=("Arial", 14)
        )

        self.style.configure(
            "Treeview.Heading",
            font=("Arial", 14)
        )

        self.tree_frame = tk.Frame(self, bg="red")
        self.tree_frame.pack(fill="both", expand=True)

        self.table = None


    def load_dataframe(self, df: pd.DataFrame):
        print("Loading dataframe into table...")
        print(df.head())

        for widget in self.tree_frame.winfo_children():
            widget.destroy()

        self.tree = ttk.Treeview(self.tree_frame, columns=list(df.columns), show="headings")

        # Set column headers
        for col in df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")

        # Insert data
        for _, row in df.iterrows():
            self.tree.insert('', 'end', values=list(row))

        self.tree.pack(fill="both", expand=True)
