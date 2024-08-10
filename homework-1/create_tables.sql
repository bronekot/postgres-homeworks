-- SQL-команды для создания таблиц

-- Создание таблицы employees
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    title VARCHAR(100),
    birth_date DATE,
    notes TEXT
);

-- Создание таблицы customers
CREATE TABLE customers (
    customer_id VARCHAR(5) PRIMARY KEY,
    company_name VARCHAR(100),
    contact_name VARCHAR(100)
);

-- Создание таблицы orders
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id VARCHAR(5) REFERENCES customers(customer_id),
    employee_id INTEGER REFERENCES employees(employee_id),
    order_date DATE,
    ship_city VARCHAR(100)
);