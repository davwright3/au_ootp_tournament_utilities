# <img src="assets/Unicorn_logo_nobg2.png" width="40" height="40" alt="Unicorn Logo"> Angered Unicorn's OOTP Tournament Utilities and Tools  <img src="assets/Unicorn_logo_nobg2.png" width="40" height="40" alt="Unicorn Logo"> 

Welcome to the home for my OOTP Tournament Tools.  

This is a desktop utility for processing and analyzing OOTP Baseball tournament data.

---

## Current Features (v 0.1.1 early alpha)

- 🗃️ (WIP) File Processing for OOTP CSV exports
- ⚙️ Editable settings with JSON-based configuration
- ✨ CustomTkinter GUI with consistent header/footer layout
- 📳 Modular app design using subprocess launching
- ➡️ Linted with flake8 with docstring support


---

## Getting Started

### Initial Startup

- Set window sizes (1920x1080 recommended)
- Set target folders and files for file processing

  - RECOMMENDED:  Have one main folder for your processed files and individual raw data folders for each tournament
  - Setting targets is not mandatory but is recommended for improving your workflow

### File Processing

- Export file as a CSV from your "Sortable Statistics" page

  - By default, this file will be automatically exported to your "\<user>\OOTP Developments\OOTP Baseball XX\online_data" folder

- Move this CSV to your raw data folder for the currently working program
- In the File Processing application, select the target (destination) file for your main tournament data and 
the folder you are importing data from
- Press the "Process Files" button and all CSV's in the folder that are not already in the file will be added
- NOTE: The application uses the name of the file to determine whether it is already in the target dataset (i.e. 24 May)
- NOTE: I expect the initial release of the statistic to use DateTime for sorting, with a future update being able to 
manage between DateTime and integers.  For now, I recommend labeling your raw data in DD MMM format.  I will advice when
this becomes obsolete.

![File Processing Image](assets/file_processing.png)


---

## Upcoming Features

- Tournament statistic application displaying player stats
- Team analysis
- Player comparison tool
- Player and tournament statistics over time

### Authored By
- David Wright
- Github: [David Wright](https://github.com/davwright3)
- LinkedIn: [David Wright](https://www.linkedin.com/in/davidwright79/)
- Twitch: [Angered_Unicorn](https://www.twitch.tv/angered_unicorn)
- Join me on Discord: [Angered_Unicorn](https://discord.gg/pfBPmFS)


- Bug reports: [FORM](https://docs.google.com/forms/d/e/1FAIpQLSdAmXv6rTwoBw9ipBdeSc7qvyV7IO83CpIVkEX5_aEbgwpy6w/viewform?usp=sharing&ouid=112838883589285917619)
- Feature requests: [FORM](https://docs.google.com/forms/d/e/1FAIpQLSftrpDw8ypLglDXteZAT0uo7H5NqkJf9UKdBCjX1OEvpKp66w/viewform?usp=sharing&ouid=112838883589285917619)



