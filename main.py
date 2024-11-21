from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from pyclip import copy
from datetime import datetime

# TODO: convert dates

# Variables
issue = ''

def extract_variables(input:str, w_name, issue, client, date, desc):
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
month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
month_completer = WordCompleter(month_list, ignore_case=True, match_middle=False)
def date_prompt(completer):
	result = prompt('Input date (use tab to auto-complete the month): ', completer=completer)
	return result
# for date input

# character_completer = WordCompleter(characters, ignore_case=True, match_middle=True)
#     print('\nPlease enter the characters in the chapter cover.\nNOTE: Press <tab> to use auto-complete function.')
#     cover_char = prompt('Cover character: ', completer=character_completer)
#     while True:
#         if cover_char == '':
#             cover_char = prompt('Invalid response. Cover character: ', completer=character_completer)
#         elif cover_char.lower() != 'done':
#             input_cover_chars.append(cover_char)
#             cover_char = prompt('Cover character: ', completer=character_completer)
#         else:
#             break

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
	
	while True:
		command = input("Enter command (show, extract, title, or desc): ")
		command = command.strip().split(' ')
		main_command = command[0]
		# parameter = ' '.join(command[1:])
		# print(parameter)
		if main_command == 'title':
			out_title = mk_title(data_list)
			copy(out_title)
			print('TITLE:', out_title)
			print('Copied to your clipboard.')
		elif main_command == 'extract':
			with open('input_data.txt', 'r') as infile:
				input_load = infile.read()
			
			data_list = extract_variables(input_load, w_name, issue, client, date, desc)
		elif main_command == 'desc':
			out_desc = mk_desc(data_list)
			copy(out_desc)
			print('DESC:', out_desc)
			print('Copied to your clipboard.')
		elif main_command == 'show':
			print(data_list)
		else:
			print('Command not recognized.')

if __name__ == "__main__":
	main()