import csv
import json

# 讀取 CSV 檔案
csv_file_path = 'aqx_p_432.csv'
json_file_path = 'aqx_p_432.json'

data = []

with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data.append(row)

# 寫入 JSON 檔案
with open(json_file_path, mode='w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print(f"CSV 檔案已成功轉換為 JSON 檔案：{json_file_path}")