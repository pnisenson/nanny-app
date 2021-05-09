from openpyxl import load_workbook
from datetime import date


returns = {'wakeUp': '07:00', 'firstNap': '09:00', 'lunch': 'blus', 'snack': 'red', 'reminder': 'sdsdadsa'}

# print(returns.values())


new_row_data = [date.today().strftime("%m/%d/%Y")]
for i in returns.values():
	new_row_data.append(i)
print(new_row_data)

wb = load_workbook("weeklyinput.xlsx")
# Select First Worksheet
ws = wb.worksheets[0]
ws.append(new_row_data)

wb.save("weeklyinput.xlsx")