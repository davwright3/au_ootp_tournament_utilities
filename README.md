# <img src="assets/Unicorn_logo_nobg2.png" width="40" height="40" alt="Unicorn Logo"> Angered Unicorn's OOTP Tournament Utilities and Tools  <img src="assets/Unicorn_logo_nobg2.png" width="40" height="40" alt="Unicorn Logo"> 

Welcome to the home for my OOTP Tournament Tools.  

This is a desktop utility for processing and analyzing OOTP Baseball tournament data.

- Bug reports: [FORM](https://docs.google.com/forms/d/e/1FAIpQLSdAmXv6rTwoBw9ipBdeSc7qvyV7IO83CpIVkEX5_aEbgwpy6w/viewform?usp=sharing&ouid=112838883589285917619)
- Feature requests: [FORM](https://docs.google.com/forms/d/e/1FAIpQLSftrpDw8ypLglDXteZAT0uo7H5NqkJf9UKdBCjX1OEvpKp66w/viewform?usp=sharing&ouid=112838883589285917619)

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
  - View should include the following stats, in this order:
     - Tag Controls, PT Card ID, Organization, PT Card Value, PT Is Variant, PT Variant Level, (Batter) G, GS, PA, AB, H, 1B, 2B, 3B, HR, RBI, R, BB, IBB,
       HP, SH, SF, SO, GIDP, EBH, TB, RC, RC/27, wOBA, WPA, WAR, SB, CS, wSB, UBR, BsR, (Pitcher) G, GS, W, L, SVO, SV, BS, HLD, SD, MD, IP, BF, AB, HA, 1B,
       2B, 3B, HR, TB, R, ER, BB, IBB, K, HP, SH, SF, WP, DP, IR, IRS, QS, CG, SHO, GB, FB, SB, CS, FIP, WAR, TC, A, PO, E, DP, TP, PCT, ZR, SBA, RTO

### Settings

- By default, your target folders and files will be set to C:\, you will need to use the Edit Settings menu to move them

- It is recommended that you set up a Raw Data and Ready Data folder (or similar names) and set your initial_target_folder and initial data folders to these

  - The initial_target_folder is where the template will be sent to when you use the "New File" command in the File Processing App

- MANDATORY: You MUST set the target_card_list_file to be linked with your card list export file from OOTP Baseball

  - By default, this file is exported to c:\<user>\Documents\OOTP Developments\OOTP Baseball 26\online_data\card_list.csv

- OPTIONAL: The target_collection_list_file is currently unused, but is designed to be linked to a file that exports your collection (hide duplicates to keep size down) with just the Card IDs in the file.  This is for future use.

### File Processing

- Export file as a CSV from your "Sortable Statistics" page

  - By default, this file will be automatically exported to your "\<user>\Documents\OOTP Developments\OOTP Baseball XX\online_data" folder

- Move this CSV to your raw data folder for the currently working program
- In the File Processing application, select the target (destination) file for your main tournament data and 
the folder you are importing data from
- Press the "Process Files" button and all CSV's in the folder that are not already in the file will be added
- NOTE: The application uses the name of the file to determine whether it is already in the target dataset (i.e. 24 May)
- NOTE: I expect the initial release of the statistic to use DateTime for sorting, with a future update being able to 
manage between DateTime and integers.  For now, I recommend labeling your raw data in DD MMM format.  I will advise when
this becomes obsolete.

![File Processing Image](assets/file_processing.png)

### Basic Batting and Pitching Stats

- Simply select the processed CSV you want to see the data for and process the file.  You can filter batters by position.  Starter/reliever filtering will be in the next update.
- All columns can be sorted by clicking on the header and will reverse (ascending/descending) when sorted again.

___
# Release Information

### v0.1.13

- Initial release
- File processing utility

### v0.1.16

- Fixed pathing issue for creation of new file from program template

### v0.1.17

- Minor UI adjustments

### v0.1.2.19

- Basic batting and pitching stat views
- initial release of macOS compatible ZIP build


---

## Upcoming Features and Improvements

- **(Priority)** Fix for resolution issues when changing between monitors
- **(Priority)** Relief/Starting Pitcher filtering
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



