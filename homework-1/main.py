import csv
from datetime import datetime
import psycopg2
import os

# Изменяем рабочий каталог. А то у нас репозиторий с несколькими уроками
#  и чтобы не переходить в каждый.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Параметры подключения к базе данных
db_params = {
    "dbname": "north",
    "user": "postgres",
    "password": "031995",
    "host": "localhost",
}


# Функция для вставки данных в таблицу
def insert_data(conn, table_name, data):
    cur = conn.cursor()
    columns = ", ".join(data[0].keys())
    values = ", ".join(["%s" for _ in data[0]])
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"

    for row in data:
        cur.execute(query, list(row.values()))

    conn.commit()
    cur.close()


# Функция для чтения CSV файла
def read_csv(filename):
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


# Преобразование строки даты в объект date
def parse_date(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d").date()


# Основная функция
def main():
    conn = psycopg2.connect(**db_params)

    # Путь к папке с CSV файлами
    data_folder = "north_data"

    # Загрузка и вставка данных для таблицы employees
    employees_data = read_csv(os.path.join(data_folder, "employees_data.csv"))
    for employee in employees_data:
        employee["birth_date"] = parse_date(employee["birth_date"])
    insert_data(conn, "employees", employees_data)

    # Загрузка и вставка данных для таблицы customers
    customers_data = read_csv(os.path.join(data_folder, "customers_data.csv"))
    insert_data(conn, "customers", customers_data)

    # Загрузка и вставка данных для таблицы orders
    orders_data = read_csv(os.path.join(data_folder, "orders_data.csv"))
    for order in orders_data:
        order["order_date"] = parse_date(order["order_date"])
    insert_data(conn, "orders", orders_data)

    conn.close()
    print("Вставка данных завершена успешно.")


if __name__ == "__main__":
    main()
