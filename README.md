# Trello Card Description Generator
This is a simple command-line application meant to help interns with their SS Audit callouts. It generates the Trello card description of a row from the SS Audit sheet, removing risks of human-error in copying and saving time.

## Requirements
You need the following set up on your laptop to run this script:
* Machine running on Windows 10/11 OS
* Installed Python 3.3 or later
* Python is in machine's PATH

## Usage
### Getting Ready
1. Download or clone this respository.
3. Go to the project folder (may be named "TrelloCardAutomation" or "TrelloCardAutomation-main").
4. Run the application by clicking on the Automate Card - Shortcut.
5. You may move "Automate Card - shortcut" anywhere you want on your machine. 

### How to use
1. Running the app will open two windows, a terminal window and a text file name input_text.txt (never rename this file).
2. On the SS Sheet, click on the row number of the row you would like to generate a description for to select it.
3. Press `Ctrl + C` to copy its contents.
4. Go to the input_text.txt, clear its contents and paste the content of the row with `Ctrl + V`.
5. Save input_text.txt.
6. Go to the terminal window.
7. Type `extract` and press `Enter`. This extracts the data from input_text.txt.
8. Type `desc` and press `Enter`. This generates a description and copies it into your clipboard.
9. You may now paste the generated description to your Trello card.
