import openpyxl

file_name = "data.xlsx"

data = {}

wb = openpyxl.load_workbook(file_name)
ws = wb['Sheet1']

for row in ws.iter_rows(min_row=1):
    print(row)
    if row[0] not in data:
        data[row[0]] = {}
    if "Tier 1" not in data[row[0]]:
        data[row[0]]["Tier 1"] = row[1]
    if row[2] not in data[row[0]]:
        data[row[0]][row[2]] = []
    curr_obj = {
        "Tier 3": row[3],
        "English name": row[4],
        "Helps with": row[5],
        "Tier 4": row[6],
        "Tier 5": row[7],
        "Tier 6": row[8],
        "Tier 7": row[9]
    }
    data[row[0]][row[2]].append(curr_obj)

print(data)    