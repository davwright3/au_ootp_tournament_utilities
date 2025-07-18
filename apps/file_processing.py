"""App for processing raw files."""
import os.path
import customtkinter as ctk
from utils.config_utils import settings as settings_module
from utils.view_utils.header_footer_frame import Header, Footer
from utils.file_utils.file_selector import open_file
from utils.file_utils.folder_selector import select_folder
from utils.file_utils.create_new_target_file import create_file_from_template
from utils.dialog_utils.input_dialog import CustomInputDialog
from utils.file_utils.process_files import process_files
from utils.config_utils.settings import settings
from utils.config_utils.get_resource_path import get_resource_path


class FileProcessor(ctk.CTkToplevel):
    """Load module for processing raw files."""

    def __init__(self):
        """Initialize the class."""
        super().__init__()

        page_settings = settings_module.settings
        # Initialize target folder and file variables
        self.selected_target_file = None
        self.selected_raw_dir = None

        # Set element heights from the settings
        self.height = int(page_settings['FileProcessor']['height'])
        self.width = int(page_settings['FileProcessor']['width'])
        self.frame_width = self.width * .9
        self.initial_target_dir = (
            page_settings['InitialFileDirs']['initial_target_folder']
        )
        self.initial_data_dir = (
            page_settings['InitialFileDirs']['initial_data_folder']
        )

        # Title and window size from the settings
        self.title(f"{settings['FileProcessor']['title']}")
        self.geometry(f"{self.width}x{self.height}")

        # Variables for grid Configurations
        self.grid_columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=0)

        header_footer_height = int(int(self.height) * .1)

        # Set up the frames
        # Header frame
        self.header_frame = Header(
            self,
            height=header_footer_height,
            width=int(self.frame_width),
            title="File Processing Tool"
        )
        self.header_frame.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

        # File/folder selection frame
        self.file_select_frame = ctk.CTkFrame(
            self, height=header_footer_height, width=int(self.frame_width)
        )
        self.file_select_frame.grid(
            column=0, row=1, padx=10, pady=10, sticky='new'
        )
        self.file_select_frame.columnconfigure(0, weight=0)
        self.file_select_frame.columnconfigure(1, weight=0)
        self.file_select_frame.columnconfigure(2, weight=1)
        self.file_select_frame.columnconfigure(3, weight=0)
        self.file_select_frame.rowconfigure(0, weight=1)
        self.file_select_frame.rowconfigure(1, weight=1)
        self.file_select_frame.rowconfigure(2, weight=1)

        # Main frame
        self.main_frame = ctk.CTkFrame(
            self, corner_radius=5, width=int(self.frame_width)
        )
        self.main_frame.grid(
            column=0, row=2, padx=10, pady=10, sticky='nsew'
        )

        # Footer frame
        self.footer_frame = Footer(
            self,
            height=header_footer_height,
            width=int(self.frame_width),
        )
        self.footer_frame.grid(
            column=0, row=3, padx=10, pady=10, sticky='ew')

        # Set up the data for the file/folder selection frame
        self.target_file_select_button = ctk.CTkButton(
            self.file_select_frame,
            text="Select target file",
            command=self.select_file
        )
        self.target_file_select_button.grid(column=0, row=0)

        self.target_file_label = ctk.CTkLabel(
            self.file_select_frame,
            text="No file selected"
        )
        self.target_file_label.grid(column=1, row=0, padx=2, pady=2)

        self.data_folder_select_button = ctk.CTkButton(
            self.file_select_frame,
            text="Select data folder",
            command=self.select_folder_handler
        )
        self.data_folder_select_button.grid(column=0, row=1, padx=2, pady=2)

        self.data_folder_select_label = ctk.CTkLabel(
            self.file_select_frame,
            text="No data folder selected"
        )
        self.data_folder_select_label.grid(column=1, row=1)

        self.data_folder_make_new_target_file_button = ctk.CTkButton(
            self.file_select_frame,
            text="New File",
            command=self.create_new_file
        )
        self.data_folder_make_new_target_file_button.grid(
            column=3,
            row=0,
            padx=2,
            pady=2)

        self.process_files_button = ctk.CTkButton(
            self.file_select_frame,
            text="Process files",
            command=self.process_files
        )
        self.process_files_button.grid(
            column=0,
            row=2,
            padx=2,
            pady=2)

        self.status_label = ctk.CTkLabel(
            self.file_select_frame,
            text="Select target file and raw folder"
        )
        self.status_label.grid(column=2, row=0)

        # Data for text box in main frame
        self.output_textbox = ctk.CTkTextbox(
            self.main_frame,
            height=300,
            width=int(self.frame_width * .95),
            wrap="word"
        )
        self.output_textbox.pack(padx=10, pady=10, fill="both", expand=True)

        self.lift()
        self.focus_force()
        self.attributes("-topmost", True)

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

    def select_file(self):
        """Open select target file dialog."""
        path = self.initial_target_dir.strip().replace("\\", "/")
        if os.path.isdir(path):
            file = open_file(parent=self, initial_dir=self.initial_target_dir)
            if file:
                self.selected_target_file = file.name
                self.log_message(
                    f"Target file: {self.selected_target_file} selected")
                self.target_file_label.configure(
                    text=self.selected_target_file)
        else:
            print("Invalid start directory")
            self.log_message("Invalid start directory")

    def log_message(self, message):
        """Log message to output textbox."""
        self.output_textbox.insert("end", message + "\n")
        self.output_textbox.see("end")

    def select_folder_handler(self):
        """Open select data folder dialog."""
        data_directory = select_folder(
            parent=self,
            initial_dir=self.initial_data_dir)
        if data_directory:
            self.selected_raw_dir = data_directory
            self.log_message(
                f"Selected raw data directory: {self.selected_raw_dir}")
            self.data_folder_select_label.configure(text=self.selected_raw_dir)

    def process_files(self):
        """Process files into the ready CSV."""
        # paths to the targets
        target_csv = self.selected_target_file
        raw_dir = self.selected_raw_dir
        if not target_csv or not raw_dir:
            self.status_label.configure(text="No file selected")
            return

        self.log_message(f"Processing {raw_dir} into {target_csv}")
        processed_files = process_files(target_csv, raw_dir)
        # for file_name, removed in processed_files:
        for file_name in processed_files:
            # self.log_message(f"Added {file_name} | Teams removed {removed}")
            self.log_message(f"Added {file_name}")

        self.log_message(f"Processed {len(processed_files)} files")

    def create_new_file(self):
        """Use template file to create a new file in the target directory."""
        root_window = self.winfo_toplevel()
        dialog = CustomInputDialog(
            root_window,
            title="Create New File",
            prompt="Enter new file name (without extension): ")
        user_input = dialog.get_input()

        if not user_input:
            return

        template_path = get_resource_path(os.path.join("assets", "empty.csv"))
        try:
            new_file = create_file_from_template(
                template_path=template_path,
                output_folder=self.initial_target_dir,
                new_name=user_input
            )
            self.target_file_label.configure(text=f"Created: {new_file}")
        except FileExistsError:
            self.target_file_label.configure(text="File already exists")
        except Exception as e:
            self.target_file_label.configure(text=str(e))
