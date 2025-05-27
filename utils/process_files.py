"""Process raw files into ready data file"""
import os
import pandas as pd
import glob

class ProcessFiles(object):
    """Process files into the ready CSV."""
    def process_files(self, target_csv, raw_dir):
        """Process files into the ready CSV."""
        target_csv = target_csv.replace('\\', '/')
        raw_dir = raw_dir.replace('\\', '/')

        print(f"Target CSV: {target_csv}")
        print(F"Raw CSV: {raw_dir}")