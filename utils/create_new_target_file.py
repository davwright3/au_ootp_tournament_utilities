"""Script for adding a new file."""
import os
import shutil
import re


def sanitize_filename(filename):
    """Remove characters not allow in filenames."""
    return re.sub(r'[^\w\s-]', '', filename.strip())


def create_file_from_template(template_path, output_folder, new_name):
    """
    Copy template file to the output folder.

    For use in making new CSV files for data analysis.

    Args:
        template_path (str): Path to the template file.
        output_folder (str): Destination folder for new file.
        new_name (str): Name of new file.

    Returns:
         str: Full path to the created file, or raises an error.
    """
    sanitized_filename = sanitize_filename(new_name)
    if not sanitized_filename:
        raise ValueError("Invalid filename")

    destination_path = os.path.join(output_folder, f"{sanitized_filename}.csv")

    if os.path.exists(destination_path):
        raise FileExistsError(f"File {destination_path} already exists")

    shutil.copy(template_path, destination_path)
    return destination_path
