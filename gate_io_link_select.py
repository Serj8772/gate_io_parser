import requests
import csv

# получение списка пар на маркете gate.io
host = "https://api.gateio.ws"
prefix = "/api/v4"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

url = '/spot/tickers/'
r = requests.request('GET', host + prefix + url, headers=headers)
rows = r.json()

# создание таблицы
with open('list.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(rows[1].keys())   # заголовок
    for i in rows:
        writer.writerow(i.values()) # значения


# функция сортировки таблицы по столбцу
def sort_csv(csv_file, sorted_csv_file, sort_column):
    with open(csv_file, 'r', newline='') as f:
        reader = csv.DictReader(f)
        sorted_data = sorted(reader, key=lambda row: float(row[sort_column]), reverse=True)

    with open(sorted_csv_file, 'w', newline='') as f:
        headers = reader.fieldnames
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(sorted_data)

sort_csv('list.csv', 'sorted_list.csv', 'change_percentage')

# добавление ссылки на торговую пару в таблицу
def change_csv_cell(filename):
    with open(filename, 'r') as f:
        rows = list(csv.reader(f))

    for row in rows[1:]:
        row[0] = f'{link}{row[0]}'
    
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

link = 'https://www.gate.io/ru/trade/'
change_csv_cell('sorted_list.csv')


# выделяем первые 500 монет с объемом больше Х
def select_csv(in_filename, out_filename, volume, percent_limit):
    with open(in_filename, 'r') as f:
        rows = list(csv.reader(f))

    rows_500 = rows[1:500]





    with open(out_filename, 'w', newline='') as f:
        writer = csv.writer(f)
        for row in rows_500:            
            print(row[0])
            if float(row[8]) > volume and float(row[4]) > percent_limit:
                print(row)
                writer.writerow(row)
    

select_csv('sorted_list.csv', 'selected_list.csv', 100000, 10)