import os
from utils.file_utils.file_selector import open_file

def handle_select_file(self, initial_dir="/", initial_target_dir=None, target_file_label=None):
    """Open select target file dialog."""
    path = self.initial_target_dir.strip().replace("\\", "/")
    if os.path.isdir(path):
        file = open_file(parent=self, initial_dir=self.initial_target_dir)
        if file:
            self.selected_target_file = file.name
            self.log_message(
                f"Target file: {self.selected_target_file} selected")
            if target_file_label:
                self.target_file_label.configure(
                    text=self.selected_target_file)
            return file.name
    else:
        print("Invalid start directory")
        self.log_message("Invalid start directory")