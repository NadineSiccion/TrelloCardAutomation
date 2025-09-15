# Trello Card Description Generator
This is a simple **Command-Line Interface Automation** made to help interns in a specific task where we processed **over a hundred records per day**.


https://github.com/user-attachments/assets/d4c08c75-fb7d-4470-be3b-1a5eef9d7fb4

It generates the Trello card description of a row from the Audit sheet, it 
* **Removes the risk of human-error**,
* **Eliminates the need for human data validation**, and
* **Reduces wasted time**.

# Business Problem
Interns would inspect data on employee performance. Issues and Non-Issues would be tagged in the "Audit Sheet". Over a hundred of these entries as made. Managers are informed of Issues via Trello boards, which the interns would input manually and formatted according to business rules. 

This method is prone to:
* Critical data entry mistakes (wrong values referenced).
* Wasted time (manual copying and formatting of data via GUI).
* Inconsistent formatting and formatting errors.

# Solution
I made this script to reduce time in copying, so interns can spend more time ensuring data accuracy in the main sheet. 

Together, we did over a hundred of this data entry task per day, alongside other projects.

Let us assume the following:
* 150 entries needing description in Trello.
* Let's say each description takes 50 seconds to copy (likely longer with data validation).
* With this script, it takes only around 10 seconds for each entry, no need for data validation.
* **Time saved would be:** `((50 sec - 10 sec) X 150 entries) / 60 secs = 100 mins` thus, roughly **1 hour and 40 minutes per day** for the department of 2 interns working 6 hours a day. 


## Requirements
You need the following set up on your laptop to run this script:
* Machine running on Windows 10/11 OS
* Installed Python 3.3 or later
* Python is in machine's PATH

## Usage
### Getting Ready
1. Download or clone this respository.
3. Go to the project folder (may be named `TrelloCardAutomation` or `TrelloCardAutomation-main`).
4. Run the file `!MainScript.bat`.
5. Never rename `input_text.txt`.

### How to use
1. Running the app will open two windows, a terminal window and a text file name input_text.txt (never rename this file).
2. On the Audit Sheet, click on the row number of the row you would like to generate a description for to select it.
3. Press `Ctrl + C` to copy its contents.
4. Go to the input_text.txt, clear its contents and paste the content of the row with `Ctrl + V`.
5. Save input_text.txt.
6. Go to the terminal window.
7. Type `extract` and press `Enter`. This extracts the data from input_text.txt.
8. Type `desc` and press `Enter`. This generates a description and copies it into your clipboard.
9. You may now paste the generated description to your Trello card (which accepts Markdown formatted text).
