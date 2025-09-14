from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit import print_formatted_text, HTML
from pyclip import copy
from datetime import datetime
from json import dumps

# Function to extract data from input_text.txt
def extract_variables(input:str, w_name, issue, client, date, desc) -> dict:
	dict_var = {}

	data = input.split('\t')
	w_name = data[4]
	issue = data[8] 
	client = data[5]
	desc = data[14].strip('"')

	# CONVERT DATE
	date_str = data[3]
	date_obj = datetime.strptime(date_str, "%m/%d/%Y")
	formatted_date = date_obj.strftime("%B %d, %Y")
	date = formatted_date
	
	dict_var['w_name'] = w_name
	dict_var['issue'] = issue
	dict_var['client'] = client
	dict_var['date'] = date
	dict_var['desc'] = desc
	return dict_var

# Functions
def mk_title(data_list) -> str:
	output = f"{data_list['w_name']} - {data_list['issue']}"
	return output

def mk_bulleted_desc(desc:str) -> str:
	output = desc.replace('\n', '\n\t- ')
	output = '- ' + output
	return output

def mk_desc(data_list:dict) -> str:
	bulleted_desc = mk_bulleted_desc(data_list['desc'])
	output = f'''Date: {data_list['date']}\n{bulleted_desc}\n----'''
	return output

	
# Auto-complete feature
command_list = ['extract', 'show', 'desc', 'title']
command_completer = WordCompleter(command_list, ignore_case=True, match_middle=False)
def command_prompt(completer):
	result = prompt('\n\nEnter command (Press tab to complete and toggle through choices): ', completer=completer)
	return result

def main():
	input_load = ""
	w_name = ""
	issue = "" 
	client = ""
	date = ""
	desc = ""
	input_load = ""

	with open('input_data.txt', 'r') as infile:
		input_load = infile.read()
	
	print('Please copy a row from the Mockup Google Sheet to the "input_text.txt" window and save it.\n'
	    + '''Commands:
	   extract => extract data from "input_data.txt". Must be done before other commands are available.
	   show => show the extracted data from the extract command in JSON string format.
	   title => creates a title from the extracted data and copies it to your clipboard.
	   desc => creates a description from the extracted data and copies it to your clipboard.''')
	data_list = None
	
	while True:
		command = command_prompt(completer=command_completer)
		# command = input("\nEnter command (extract, show, title, or desc): ")
		command = command.lower().strip().split(' ')
		main_command = command[0]

		# MAIN LOGIC
		if main_command == 'extract':
			try:
				with open('input_data.txt', 'r') as infile:
					input_load = infile.read()
				data_list = extract_variables(input_load, w_name, issue, client, date, desc)
				print_formatted_text(HTML('<lime>Data extracted!</lime>'))
			except Exception as e: # Catches any other unexpected exceptions
				print(f"An error has occurred, please ensure input-text.txt has valid data.\nError encountered: {e}")
		
		elif main_command == 'show':
			if data_list:
				print_formatted_text(HTML('<lightslategray>' + dumps(data_list, indent=4) + '</lightslategray>')) 
			else: 
				print_formatted_text(HTML("<red>Please extract data first!</red>"))
		
		elif main_command == 'title':
			if data_list:
				out_title = mk_title(data_list)
				copy(out_title)
				print_formatted_text(HTML('<white>TITLE:</white><lightslategray>' + out_title + '</lightslategray>'))
				print_formatted_text(HTML('<lime>Copied to your clipboard!</lime>'))
			else:
				print_formatted_text(HTML("<red>Please extract data first!</red>"))
		
		elif main_command == 'desc':
			if data_list:
				out_desc = mk_desc(data_list)
				copy(out_desc)
				print_formatted_text(HTML('<white>DESC:</white><lightslategray>' + out_desc + '</lightslategray>'))
				print_formatted_text(HTML('<lime>Copied to your clipboard!</lime>'))
			else:
				print_formatted_text(HTML("<red>Please extract data first!</red>"))
		
		else:
			print_formatted_text(HTML('<red>Command not recognized.</red>'))

if __name__ == "__main__":
	main()