from db import run_query_select, run_update_query

run_update_query("""CREATE TABLE IF NOT EXISTS company (
    id INT PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    age  NOT NULL,
    address CHAR(50),
    salary)""")

run_update_query("INSERT INTO company (id, name, age, address, salary) VALUES (?, ?, ?, ?, ?)", (1, 'Paul', 32, 'California', 20000.00))
run_update_query("INSERT INTO company (id, name, age, address, salary) VALUES (?, ?, ?, ?, ?)", (2, 'Allen', 25, 'Texas', 15000.00))
run_update_query("INSERT INTO company (id, name, age, address, salary) VALUES (?, ?, ?, ?, ?)", (3, 'Teddy', 23, 'Norway', 20000.00))
run_update_query("INSERT INTO company (id, name, age, address, salary) VALUES (?, ?, ?, ?, ?)", (4, 'Mark', 25, 'Rich-Mond', 65000.00))
run_update_query("INSERT INTO company (id, name, age, address, salary) VALUES (?, ?, ?, ?, ?)", (5, 'David', 27, 'Texas', 85000.00))
run_update_query("INSERT INTO company (id, name, age, address, salary) VALUES (?, ?, ?, ?, ?)", (6, 'Kim', 22, 'South-Hall', 45000.00))
company = run_query_select("SELECT * FROM company")
for c in company:
    print(c)

company = run_query_select('SELECT * FROM company WHERE salary > 30000.00')
print('over 30k')
for c in company:
    print(c)

company = run_query_select("SELECT * FROM company WHERE name like 'D%'")
print('start with d')
for c in company:
    print(c)

select_id = int(input('Enter ID: '))
new_name = input('Enter name: ')

run_update_query('UPDATE company SET name = ? WHERE id = ?', (new_name, select_id))
print('the new name')
company = run_query_select('SELECT * FROM company WHERE id = ?', (select_id,))
for c in company:
    print(c)


id_2 = int(input('Enter ID: '))
check = run_query_select('SELECT * FROM company WHERE id = ?', params=(id_2,))
if check:
    run_update_query('DELETE FROM company WHERE id = ?', (id_2,))
    print('user deleted')
else:
    print('user not exist')
company = run_query_select('SELECT * FROM company')
for c in company:
    print(c)

